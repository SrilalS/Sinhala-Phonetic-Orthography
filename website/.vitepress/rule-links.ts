// Turns rule IDs and repository paths in the research documents into links.
//
// Rule IDs are defined in docs/*.md in three ways: a heading ("### VS-007 — …"), a bold
// lead-in ("**INV-001 — …**") or the first cell of a table row ("| G-EN-01 | …").
// Every definition gets an anchor (the ID in lower case), and every mention of a defined ID
// ("G-HC-06", "02:VS-007", "R-11") links to it.
import fs from "node:fs";
import path from "node:path";
import type MarkdownIt from "markdown-it";

export const REPO = "https://github.com/SrilalS/Sinhala-Phonetic-Orthography";
const DOCS = path.resolve(__dirname, "../../docs");

// docs/<file> → site route. The two-digit prefix doubles as the "02:" in "02:VS-007".
export const PAGES: Record<string, string> = {
  "00-rules.md": "/rules",
  "01-inventory.md": "/research/inventory",
  "02-vowel-signs.md": "/research/vowel-signs",
  "03-hal-conjuncts.md": "/research/hal-conjuncts",
  "04-nasals-and-spelling-distinctions.md": "/research/nasals-and-spelling",
  "05-phonotactics-sandhi-spelling.md": "/research/phonotactics-sandhi-spelling",
  "06-romanization.md": "/research/romanization-systems",
  "07-phonetic-romanization.md": "/research/phonetic-romanization",
};
const BY_NUMBER = Object.fromEntries(Object.entries(PAGES).map(([f, r]) => [f.slice(0, 2), r]));

const ID = String.raw`(?:G-[A-Z]+-\d+|[A-Z][A-Z0-9]*-\d+[a-z]?)`;
const DEFINITION = [
  new RegExp(String.raw`^#{2,4} (${ID}) [—–]`, "gm"),
  new RegExp(String.raw`^\*\*(${ID}) [—–]`, "gm"),
  new RegExp(String.raw`^\| *(${ID}) *\|`, "gm"),
];
const MENTION = new RegExp(String.raw`(?:\b(0[0-7]):)?\b(${ID})(?![\w-])`, "g");
const HEADING_ID = new RegExp(String.raw`^(${ID}) [—–]`);
const CELL_ID = new RegExp(String.raw`^${ID}$`);
const LEAD_ID = new RegExp(String.raw`^\*\*(${ID}) [—–]`);

/** id → the routes that define it, for every rule in docs/. */
function scanDefinitions() {
  const defs = new Map<string, Set<string>>();
  for (const [file, route] of Object.entries(PAGES)) {
    const text = fs.readFileSync(path.join(DOCS, file), "utf-8").replace(/\r\n/g, "\n");
    for (const re of DEFINITION) {
      for (const m of text.matchAll(re)) {
        if (!defs.has(m[1])) defs.set(m[1], new Set());
        defs.get(m[1])!.add(route);
      }
    }
  }
  return defs;
}

const DEFS = scanDefinitions();

function routeOf(id: string, here: string, fileNumber?: string) {
  const routes = DEFS.get(id);
  if (!routes) return null;
  if (fileNumber) return routes.has(BY_NUMBER[fileNumber]) ? BY_NUMBER[fileNumber] : null;
  if (routes.has(here)) return here;
  return routes.size === 1 ? [...routes][0] : null;
}

// VitePress's default heading slug (from @mdit-vue/shared, which isn't a direct dependency).
const COMBINING = /[̀-ͯ]/g;
const CONTROL = /[\u0000-\u001f]/g;
const SPECIAL = /[\s~`!@#$%^&*()\-_+=[\]{}|\\;:"'“”‘’<>,.?/]+/g;
function defaultSlugify(s: string) {
  return s
    .normalize("NFKD")
    .replace(COMBINING, "")
    .replace(CONTROL, "")
    .replace(SPECIAL, "-")
    .replace(/-{2,}/g, "-")
    .replace(/^-+|-+$/g, "")
    .replace(/^(\d)/, "_$1")
    .toLowerCase();
}

/** Headings that start with a rule ID get the ID as their anchor. */
export function slugify(s: string) {
  const m = s.match(HEADING_ID);
  return m ? m[1].toLowerCase() : defaultSlugify(s);
}

function fileLink(code: string): string | null {
  const doc = code.replace(/^docs\//, "");
  if (PAGES[doc]) return PAGES[doc];
  if (/^(data|src|tools|reports|tests)\/[\w./-]+$/.test(code)) return `${REPO}/blob/main/${code}`;
  return null;
}

export function ruleLinks(md: MarkdownIt) {
  md.core.ruler.push("rule_links", (state) => {
    const rel: string = state.env.relativePath ?? "";
    const here = "/" + rel.replace(/(index)?\.md$/, "").replace(/\/$/, "");
    const tokens = state.tokens;
    const Token = state.Token;

    for (let i = 0; i < tokens.length; i++) {
      const t = tokens[i];
      // Anchors on table rows and bold lead-ins that define a rule.
      if (t.type === "tr_open" && tokens[i + 1]?.type === "td_open") {
        const cell = tokens[i + 2];
        if (cell?.type === "inline" && CELL_ID.test(cell.content.trim()) && !t.attrGet("id")) {
          t.attrSet("id", cell.content.trim().toLowerCase());
          t.attrJoin("class", "rule-row");
        }
      }
      if (t.type === "paragraph_open") {
        const m = tokens[i + 1]?.content.match(LEAD_ID);
        if (m) t.attrSet("id", m[1].toLowerCase());
      }
      if (t.type !== "inline" || !t.children) continue;
      if (tokens[i - 1]?.type === "heading_open") continue;

      const out: typeof t.children = [];
      let inLink = 0;
      for (const c of t.children) {
        if (c.type === "link_open") inLink++;
        if (c.type === "link_close") inLink--;
        if (inLink) { out.push(c); continue; }

        if (c.type === "code_inline") {
          const href = fileLink(c.content);
          if (href) {
            const open = new Token("link_open", "a", 1);
            open.attrSet("href", href);
            out.push(open, c, new Token("link_close", "a", -1));
            continue;
          }
        }
        if (c.type !== "text") { out.push(c); continue; }

        let last = 0;
        for (const m of c.content.matchAll(MENTION)) {
          const route = routeOf(m[2], here, m[1]);
          if (!route) continue;
          if (m.index! > last) {
            const pre = new Token("text", "", 0); pre.content = c.content.slice(last, m.index); out.push(pre);
          }
          const open = new Token("link_open", "a", 1);
          open.attrSet("href", (route === here ? "" : route) + "#" + m[2].toLowerCase());
          open.attrSet("class", "rule-ref");
          const txt = new Token("text", "", 0); txt.content = m[0];
          out.push(open, txt, new Token("link_close", "a", -1));
          last = m.index! + m[0].length;
        }
        if (last === 0) { out.push(c); continue; }
        if (last < c.content.length) {
          const post = new Token("text", "", 0); post.content = c.content.slice(last); out.push(post);
        }
      }
      t.children = out;
    }
  });
}
