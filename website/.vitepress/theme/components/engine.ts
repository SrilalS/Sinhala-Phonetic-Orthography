// Runs the reference implementation (src/sinhala_orthography) in the browser with Pyodide,
// so the playground always behaves exactly like the Python package.
const PYODIDE = "https://cdn.jsdelivr.net/pyodide/v314.0.7/full/";

// The package source and its tables, bundled as text at build time.
const SOURCES = import.meta.glob("../../../../src/sinhala_orthography/**/*.{py,json}", {
  query: "?raw",
  import: "default",
  eager: true,
}) as Record<string, string>;

export const TABLES = {
  consonants: JSON.parse(source("data/consonants.json")) as [string, string, string, string][],
  vowels: JSON.parse(source("data/vowels.json")) as [string, string, string, string, string, string][],
  specials: JSON.parse(source("data/specials.json")) as [string, string, string, string][],
};

function source(rel: string) {
  const key = Object.keys(SOURCES).find((k) => k.endsWith(`sinhala_orthography/${rel}`));
  if (!key) throw new Error(`missing ${rel}`);
  return SOURCES[key];
}

// Display helper: the same longest-match scan as romanization.tokenize, but it keeps the
// matched Latin sequence of every token. The conversion itself is the real to_sinhala().
const HELPER = `
import json, unicodedata
from sinhala_orthography import romanization as R, to_sinhala

def _tokens(word, archaic):
    out, i = [], 0
    while i < len(word):
        for seq, tok in R._SEQUENCES[archaic]:
            if word.startswith(seq, i):
                kind = tok[0]
                if kind == "C":
                    out.append({"seq": seq, "kind": "consonant", "letter": tok[1]})
                elif kind == "V":
                    out.append({"seq": seq, "kind": "vowel", "letter": tok[2], "sign": tok[3], "vowel": tok[1]})
                else:
                    out.append({"seq": seq, "kind": "sign", "letter": tok[1]})
                i += len(seq)
                break
        else:
            out.append({"seq": word[i], "kind": "dropped" if word[i] == "z" else "literal", "letter": word[i]})
            i += 1
    return out

def _chars(text):
    return [{"ch": c, "cp": "U+%04X" % ord(c), "name": unicodedata.name(c, "?")} for c in text]

def explain(text, archaic, repaya_zwj, classical, rakaransaya_u):
    opts = dict(archaic=archaic, repaya_zwj=repaya_zwj, classical=classical, rakaransaya_u=rakaransaya_u)
    words = []
    for w in text.split():
        out = to_sinhala(w, **opts)
        words.append({"input": w, "output": out, "tokens": _tokens(w, archaic), "chars": _chars(out)})
    return json.dumps({"output": to_sinhala(text, **opts), "words": words}, ensure_ascii=False)
`;

export type Token = { seq: string; kind: string; letter: string; sign?: string; vowel?: string };
export type Explained = {
  output: string;
  words: { input: string; output: string; tokens: Token[]; chars: { ch: string; cp: string; name: string }[] }[];
};
export type Options = { archaic: boolean; repaya_zwj: boolean; classical: boolean; rakaransaya_u: boolean };

let ready: Promise<(text: string, o: Options) => Explained> | null = null;

function loadScript(src: string) {
  return new Promise<void>((resolve, reject) => {
    const s = document.createElement("script");
    s.src = src;
    s.onload = () => resolve();
    s.onerror = () => reject(new Error(`Could not load ${src}`));
    document.head.appendChild(s);
  });
}

export function loadEngine() {
  ready ??= (async () => {
    await loadScript(PYODIDE + "pyodide.js");
    const py = await (window as any).loadPyodide({ indexURL: PYODIDE });
    for (const [key, text] of Object.entries(SOURCES)) {
      const rel = key.slice(key.indexOf("sinhala_orthography/"));
      const dir = "/home/pyodide/" + rel.slice(0, rel.lastIndexOf("/"));
      py.FS.mkdirTree(dir);
      py.FS.writeFile("/home/pyodide/" + rel, text);
    }
    py.runPython(HELPER);
    const explain = py.globals.get("explain");
    return (text: string, o: Options) =>
      JSON.parse(explain(text, o.archaic, o.repaya_zwj, o.classical, o.rakaransaya_u)) as Explained;
  })();
  ready.catch(() => (ready = null));
  return ready;
}
