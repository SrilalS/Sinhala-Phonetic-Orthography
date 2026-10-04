<script setup lang="ts">
import { computed, nextTick, onMounted, reactive, ref, watch } from "vue";
import { withBase } from "vitepress";
import { loadEngine, TABLES, type Explained, type Options } from "./engine";

const EXAMPLES: [string, string][] = [
  ["aayuboovan", "greeting"],
  ["shrii lankaava", "rakaransaya, n + velar → ං"],
  ["oyaata kohomada", "d is ද"],
  ["vidyaava", "yansaya"],
  ["karma kaarya", "plain repaya"],
  ["lait kauda", "glides, not ෛ / ෞ"],
  ["kruura mrudu", "C + ru → ෘ / ෲ"],
  ["kazda saha kanda", "sanyaka vs cluster"],
  ["akShara", "try the classical option"],
  ["siMhala", "explicit ං"],
];

const OPTIONS: { key: keyof Options; label: string; note: string; rule: string }[] = [
  { key: "repaya_zwj", label: "ZWJ repaya", note: "කර්‍ම instead of plain කර්ම", rule: "r-08" },
  { key: "classical", label: "Classical conjuncts", note: "ZWJ for the 13 bandi akuru pairs (ක්‍ෂ, න්‍ද …)", rule: "r-10" },
  { key: "rakaransaya_u", label: "Rakaransaya + u", note: "ක්‍රූර instead of the usual කෲර", rule: "r-06" },
  { key: "archaic", label: "Archaic letters", note: "ඏ ඐ ෟ ෳ ඎ ඁ ඦ and touching letters", rule: "r-14" },
];

const input = ref("shrii lankaava");
const opts = reactive<Options>({ archaic: false, repaya_zwj: false, classical: false, rakaransaya_u: false });
const state = ref<"idle" | "loading" | "ready" | "error">("idle");
const error = ref("");
const result = ref<Explained | null>(null);
const copied = ref(false);
const tab = ref<"consonants" | "vowels" | "signs">("consonants");
const textarea = ref<HTMLTextAreaElement | null>(null);
let convert: ((t: string, o: Options) => Explained) | null = null;

function run() {
  if (!convert) return;
  try {
    result.value = convert(input.value, { ...opts });
  } catch (e: any) {
    error.value = String(e?.message ?? e);
  }
  syncUrl();
}

let timer: ReturnType<typeof setTimeout> | undefined;
watch([input, () => ({ ...opts })], () => {
  clearTimeout(timer);
  timer = setTimeout(run, 80);
});

function syncUrl() {
  const p = new URLSearchParams();
  if (input.value) p.set("q", input.value);
  const on = (Object.keys(opts) as (keyof Options)[]).filter((k) => opts[k]);
  if (on.length) p.set("o", on.join(","));
  history.replaceState(history.state, "", `${location.pathname}${p.size ? "?" + p : ""}`);
}

async function start() {
  state.value = "loading";
  error.value = "";
  try {
    convert = await loadEngine();
    state.value = "ready";
    run();
  } catch (e: any) {
    state.value = "error";
    error.value = String(e?.message ?? e);
  }
}

onMounted(() => {
  const p = new URLSearchParams(location.search);
  if (p.has("q")) input.value = p.get("q")!;
  for (const k of (p.get("o") ?? "").split(",")) if (k in opts) opts[k as keyof Options] = true;
  start();
});

async function copy() {
  if (!result.value) return;
  await navigator.clipboard.writeText(result.value.output);
  copied.value = true;
  setTimeout(() => (copied.value = false), 1200);
}

async function insert(seq: string) {
  const el = textarea.value;
  if (!el) { input.value += seq; return; }
  const [a, b] = [el.selectionStart, el.selectionEnd];
  input.value = input.value.slice(0, a) + seq + input.value.slice(b);
  await nextTick();
  el.focus();
  el.setSelectionRange(a + seq.length, a + seq.length);
}

// Cheat sheet: one cell per letter, every sequence that produces it.
type Cell = { glyph: string; sub?: string; seqs: { seq: string; alias: boolean }[]; archaic: boolean; note: string };
function group<T>(rows: T[], keyOf: (r: T) => string, make: (r: T) => Omit<Cell, "seqs">, seqOf: (r: T) => [string, boolean]) {
  const cells = new Map<string, Cell>();
  for (const r of rows) {
    const k = keyOf(r);
    if (!cells.has(k)) cells.set(k, { ...make(r), seqs: [] });
    const [seq, alias] = seqOf(r);
    cells.get(k)!.seqs.push({ seq, alias });
  }
  return [...cells.values()];
}
const sheet = computed(() => ({
  consonants: group(TABLES.consonants, (r) => r[1] + r[2],
    (r) => ({ glyph: r[1], archaic: r[2] === "archaic", note: r[3].startsWith("alias") ? "" : r[3] }),
    (r) => [r[0], r[3] === "alias"]),
  vowels: group(TABLES.vowels, (r) => r[1] + r[4],
    (r) => ({ glyph: r[2], sub: r[3] ? "ක" + r[3] : "ක", archaic: r[4] === "archaic", note: r[5] }),
    (r) => [r[0], false]),
  signs: group(TABLES.specials, (r) => r[1] + r[2],
    (r) => ({ glyph: r[1] === "touch" ? "ක‍්ක" : "ක" + r[1], archaic: r[2] === "archaic", note: r[3] }),
    (r) => [r[0], false]),
}));

function isSpecial(name: string) {
  return /VIRAMA|ZERO WIDTH/.test(name);
}
function shortName(name: string) {
  return name.replace(/^SINHALA (LETTER |VOWEL SIGN |SIGN )?/, "").toLowerCase();
}
</script>

<template>
  <div class="pg">
    <section class="pg-io">
      <div class="pg-pane">
        <label class="pg-label" for="pg-input">Romanized</label>
        <textarea id="pg-input" ref="textarea" v-model="input" spellcheck="false" autocapitalize="off"
          autocomplete="off" rows="3" placeholder="Type a romanization, e.g. shrii lankaava" />
      </div>
      <div class="pg-pane pg-out">
        <div class="pg-label">
          Sinhala
          <button class="pg-copy" :disabled="!result?.output" @click="copy">{{ copied ? "Copied" : "Copy" }}</button>
        </div>
        <div class="pg-result si" lang="si" aria-live="polite">
          <template v-if="state === 'ready'">{{ result?.output }}</template>
          <span v-else-if="state === 'loading'" class="pg-status">
            <span class="pg-spinner" /> Loading the Python reference implementation…
          </span>
          <span v-else-if="state === 'error'" class="pg-status pg-err">
            Couldn't start the converter: {{ error }}
            <button class="pg-copy" @click="start">Retry</button>
          </span>
        </div>
      </div>
    </section>

    <section class="pg-opts">
      <label v-for="o in OPTIONS" :key="o.key" class="pg-opt">
        <input v-model="opts[o.key]" type="checkbox" />
        <span><b>{{ o.label }}</b> <span class="pg-muted">{{ o.note }}</span>
          <a :href="withBase('/research/phonetic-romanization#' + o.rule)" class="pg-rule">{{ o.rule.toUpperCase() }}</a></span>
      </label>
    </section>

    <section class="pg-examples">
      <span class="pg-muted">Examples</span>
      <button v-for="[ex, why] in EXAMPLES" :key="ex" class="pg-chip" :title="why" @click="input = ex">{{ ex }}</button>
    </section>

    <section v-if="result?.words.length" class="pg-words">
      <h2>Step by step</h2>
      <p class="pg-muted">
        Each word is split into the longest matching sequences, then one left-to-right pass decides
        vowel signs, hal, ZWJ joins, glides and nasals (<a :href="withBase('/research/phonetic-romanization#_3-conversion-rules')">conversion rules C-1 … C-12</a>).
      </p>
      <div v-for="(w, i) in result.words.slice(0, 12)" :key="i" class="pg-word">
        <div class="pg-word-head">
          <code>{{ w.input }}</code><span class="pg-arrow">→</span><span class="si pg-word-out" lang="si">{{ w.output }}</span>
        </div>
        <div class="pg-tokens">
          <div v-for="(t, j) in w.tokens" :key="j" class="pg-tok" :class="'k-' + t.kind" :title="t.kind">
            <code>{{ t.seq }}</code>
            <span class="si">{{ t.kind === "dropped" ? "∅" : t.letter }}<template v-if="t.kind === 'vowel'"> · ◌{{ t.sign }}</template></span>
          </div>
        </div>
        <div class="pg-chars">
          <span v-for="(c, j) in w.chars" :key="j" class="pg-char" :class="{ special: isSpecial(c.name) }" :title="c.name">
            <span class="si">{{ isSpecial(c.name) ? (c.cp === "U+200D" ? "ZWJ" : "◌්") : c.ch }}</span>
            <small>{{ c.cp }}</small>
            <small class="pg-name">{{ shortName(c.name) }}</small>
          </span>
        </div>
      </div>
      <p v-if="result.words.length > 12" class="pg-muted">Showing the first 12 words.</p>
    </section>

    <section class="pg-sheet">
      <h2>Sequences</h2>
      <p class="pg-muted">Click a sequence to insert it. Case matters: capitals mark retroflex, aspirate and a few vowels.</p>
      <div class="pg-tabs" role="tablist">
        <button v-for="t in (['consonants', 'vowels', 'signs'] as const)" :key="t" role="tab"
          :aria-selected="tab === t" :class="{ on: tab === t }" @click="tab = t">{{ t }}</button>
      </div>
      <div class="pg-grid">
        <div v-for="(c, i) in sheet[tab]" :key="i" class="pg-cell" :class="{ archaic: c.archaic && !opts.archaic }"
          :title="c.note">
          <div class="pg-glyph si" lang="si">{{ c.glyph }}<small v-if="c.sub">{{ c.sub }}</small></div>
          <div class="pg-seqs">
            <button v-for="s in c.seqs" :key="s.seq" :class="{ alias: s.alias }" @click="insert(s.seq)">{{ s.seq }}</button>
          </div>
          <div v-if="c.archaic" class="pg-tag">archaic</div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.pg h2 { font-size: 20px; font-weight: 700; margin: 40px 0 6px; letter-spacing: -0.01em; }
.pg-muted { color: var(--vp-c-text-2); font-size: 14px; }
.pg-muted a { color: var(--vp-c-brand-1); }

.pg-io { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
@media (max-width: 760px) { .pg-io { grid-template-columns: 1fr; } }
.pg-pane { background: var(--vp-c-bg-soft); border: 1px solid var(--vp-c-divider); border-radius: 12px; padding: 12px 16px 16px; display: flex; flex-direction: column; min-width: 0; }
.pg-label { display: flex; align-items: center; justify-content: space-between; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.06em; color: var(--vp-c-text-2); margin-bottom: 8px; min-height: 26px; }
textarea { width: 100%; flex: 1; min-height: 120px; resize: vertical; font: 20px/1.5 var(--vp-font-family-mono); background: transparent; color: var(--vp-c-text-1); border: none; outline: none; }
.pg-result { font-size: 34px; line-height: 1.6; min-height: 120px; word-break: break-word; white-space: pre-wrap; }
.pg-status { font: 14px/1.5 var(--vp-font-family-base); color: var(--vp-c-text-2); display: inline-flex; align-items: center; gap: 10px; flex-wrap: wrap; }
.pg-err { color: var(--st-never); }
.pg-spinner { width: 14px; height: 14px; border: 2px solid var(--vp-c-divider); border-top-color: var(--vp-c-brand-1); border-radius: 50%; animation: spin 0.8s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
.pg-copy { font-size: 12px; font-weight: 600; text-transform: none; letter-spacing: 0; padding: 3px 10px; border-radius: 6px; border: 1px solid var(--vp-c-divider); background: var(--vp-c-bg); color: var(--vp-c-text-1); }
.pg-copy:hover:not(:disabled) { border-color: var(--vp-c-brand-1); color: var(--vp-c-brand-1); }
.pg-copy:disabled { opacity: 0.5; }

.pg-opts { display: flex; flex-wrap: wrap; gap: 8px 24px; margin: 16px 0 12px; font-size: 14px; }
.pg-opt { display: flex; gap: 8px; align-items: baseline; cursor: pointer; }
.pg-opt input { accent-color: var(--vp-c-brand-1); }
.pg-rule { font-size: 12px; color: var(--vp-c-brand-1); margin-left: 4px; }

.pg-examples { display: flex; flex-wrap: wrap; align-items: center; gap: 8px; }
.pg-chip { font: 13px var(--vp-font-family-mono); padding: 4px 10px; border-radius: 999px; border: 1px solid var(--vp-c-divider); background: var(--vp-c-bg-soft); color: var(--vp-c-text-1); }
.pg-chip:hover { border-color: var(--vp-c-brand-1); color: var(--vp-c-brand-1); }

.pg-word { border: 1px solid var(--vp-c-divider); border-radius: 12px; padding: 14px 16px; margin-top: 12px; }
.pg-word-head { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; margin-bottom: 10px; }
.pg-word-head code { font-size: 15px; }
.pg-word-out { font-size: 24px; }
.pg-arrow { color: var(--vp-c-text-3); }
.pg-tokens, .pg-chars { display: flex; flex-wrap: wrap; gap: 6px; }
.pg-tokens { margin-bottom: 10px; }
.pg-tok { display: flex; flex-direction: column; align-items: center; gap: 2px; padding: 4px 8px; border-radius: 8px; background: var(--vp-c-bg-soft); border-bottom: 3px solid var(--vp-c-divider); min-width: 34px; }
.pg-tok code { background: none; padding: 0; font-size: 13px; }
.pg-tok .si { font-size: 18px; }
.k-consonant { border-bottom-color: var(--vp-c-brand-1); }
.k-vowel { border-bottom-color: var(--st-rare); }
.k-sign { border-bottom-color: var(--st-loan); }
.k-dropped .si { color: var(--vp-c-text-3); }
.pg-char { display: flex; flex-direction: column; align-items: center; padding: 4px 8px; border-radius: 8px; border: 1px dashed var(--vp-c-divider); min-width: 52px; }
.pg-char .si { font-size: 20px; line-height: 1.4; }
.pg-char small { font: 11px var(--vp-font-family-mono); color: var(--vp-c-text-2); }
.pg-char .pg-name { font-family: var(--vp-font-family-base); color: var(--vp-c-text-3); max-width: 110px; text-align: center; line-height: 1.2; }
.pg-char.special { border-style: solid; border-color: var(--vp-c-brand-1); background: var(--vp-c-brand-soft); }
.pg-char.special .si { font-size: 14px; font-weight: 700; color: var(--vp-c-brand-1); line-height: 1.9; }

.pg-tabs { display: flex; gap: 4px; margin: 12px 0; border-bottom: 1px solid var(--vp-c-divider); }
.pg-tabs button { padding: 6px 14px; font-size: 14px; font-weight: 600; text-transform: capitalize; color: var(--vp-c-text-2); border-bottom: 2px solid transparent; margin-bottom: -1px; }
.pg-tabs button.on { color: var(--vp-c-brand-1); border-bottom-color: var(--vp-c-brand-1); }
.pg-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(104px, 1fr)); gap: 8px; }
.pg-cell { border: 1px solid var(--vp-c-divider); border-radius: 10px; padding: 8px; text-align: center; background: var(--vp-c-bg-soft); }
.pg-cell.archaic { opacity: 0.45; }
.pg-glyph { font-size: 26px; line-height: 1.5; }
.pg-glyph small { font-size: 16px; color: var(--vp-c-text-2); margin-left: 6px; }
.pg-seqs { display: flex; flex-wrap: wrap; justify-content: center; gap: 4px; }
.pg-seqs button { font: 13px var(--vp-font-family-mono); padding: 1px 6px; border-radius: 5px; background: var(--vp-c-bg); border: 1px solid var(--vp-c-divider); color: var(--vp-c-text-1); }
.pg-seqs button:hover { border-color: var(--vp-c-brand-1); color: var(--vp-c-brand-1); }
.pg-seqs button.alias { color: var(--vp-c-text-3); }
.pg-tag { margin-top: 4px; font-size: 10px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--vp-c-text-3); }
</style>
