<script setup lang="ts">
import { computed, onMounted, onUnmounted, reactive, ref, shallowRef, watch } from "vue";
import { RULES, inline } from "./rules";
import { useI18n } from "./i18n";

const { t, link, locale } = useI18n();
const rules = computed(() => RULES[locale.value] ?? RULES.root);

type Form = {
  id: string; text: string; status: Status; shape: string | null; rules: string[];
  roman: Record<OptionSet, string[]>;
};
type Status = "valid" | "loan" | "rare" | "unattested" | "never";
type OptionSet = "default" | "repaya_zwj" | "classical" | "archaic" | "rakaransaya_u";

const STATUSES: Status[] = ["valid", "loan", "rare", "unattested", "never"];
const OPTION_SETS: { key: OptionSet; param: string }[] = [
  { key: "default", param: "" },
  { key: "repaya_zwj", param: "repaya_zwj" },
  { key: "classical", param: "classical" },
  { key: "archaic", param: "archaic" },
  { key: "rakaransaya_u", param: "rakaransaya_u" },
];
const VOWEL_COLS = ["hal", "a", "aa", "ae", "aee", "i", "ii", "u", "uu", "ru", "ruu", "ilu", "iluu", "e", "ee", "ai", "o", "oo", "au"];
const CONJ_COLS = ["yansaya", "rakaransaya", "repaya"];

const forms = shallowRef<Map<string, Form>>(new Map());
const consonants = shallowRef<string[]>([]);
const loading = ref(true);
const selected = ref("ka.a");
const query = ref("");
const shown = reactive<Record<Status, boolean>>({ valid: true, loan: true, rare: true, unattested: true, never: true });

// The selected form lives in the URL hash, so links like /explorer#ka.u work, also from this page.
function fromHash() {
  const id = decodeURIComponent(location.hash.slice(1));
  if (forms.value.has(id)) selected.value = id;
}
onUnmounted(() => window.removeEventListener("hashchange", fromHash));

onMounted(async () => {
  const [validity, coverage] = await Promise.all([
    import("../../../../data/validity.json").then((m) => m.default as any[]),
    import("../../../../data/romanization-coverage.json").then((m) => m.default as any[]),
  ]);
  const roman = new Map(coverage.map((c) => [c.id, c]));
  const map = new Map<string, Form>();
  const cons: string[] = [];
  for (const v of validity) {
    const c = roman.get(v.id);
    map.set(v.id, { ...v, roman: { default: c.default, repaya_zwj: c.repaya_zwj, classical: c.classical, archaic: c.archaic, rakaransaya_u: c.rakaransaya_u } });
    const [head, tail] = v.id.split(".");
    if (tail === "hal") cons.push(head);
  }
  forms.value = map;
  consonants.value = cons;
  fromHash();
  window.addEventListener("hashchange", fromHash);
  loading.value = false;
});

watch(selected, (id) => history.replaceState(history.state, "", `#${id}`));

const counts = computed(() => {
  const n: Record<string, number> = {};
  for (const f of forms.value.values()) n[f.status] = (n[f.status] ?? 0) + 1;
  return n;
});
const vowelRow = computed(() => [...forms.value.values()].filter((f) => f.id.startsWith("vowel.") || f.id.startsWith("sign.")));
const colHeads = computed(() =>
  VOWEL_COLS.map((v) => {
    if (v === "a") return { id: v, glyph: "–" };
    const ka = forms.value.get(`ka.${v}`)?.text ?? "";
    return { id: v, glyph: "◌" + ka.slice(1) };
  }),
);
const conjHeads = [
  { id: "yansaya", glyph: "◌්‍ය" },
  { id: "rakaransaya", glyph: "◌්‍ර" },
  { id: "repaya", glyph: "ර්‍◌" },
];

const SINHALA = /[඀-෿]/;
const matches = computed(() => {
  const q = query.value.trim();
  if (!q) return null;
  const hit = new Set<string>();
  const noZwj = (s: string) => s.replace(/‍/g, "");
  for (const f of forms.value.values()) {
    const ok = SINHALA.test(q)
      ? noZwj(f.text) === noZwj(q)
      : OPTION_SETS.some((o) => f.roman[o.key].includes(q));
    if (ok) hit.add(f.id);
  }
  return hit;
});
watch(matches, (m) => { if (m?.size) selected.value = [...m][0]; });

function dim(f?: Form) {
  if (!f) return true;
  return !shown[f.status] || (matches.value !== null && !matches.value.has(f.id));
}

const current = computed(() => forms.value.get(selected.value));
const codepoints = computed(() =>
  [...(current.value?.text ?? "")].map((ch) => {
    const cp = "U+" + ch.codePointAt(0)!.toString(16).toUpperCase().padStart(4, "0");
    const label = ch === "‍" ? "ZWJ" : ch === "්" ? "hal ◌්" : ch;
    return { cp, label, special: ch === "‍" || ch === "්" };
  }),
);
function describe(id: string) {
  const [head, tail] = id.split(".");
  const d = t.value.describe;
  if (head === "vowel") return d.vowel(tail);
  if (head === "sign") return t.value.signNames[tail] ?? tail;
  const base = forms.value.get(`${head}.a`)?.text ?? head;
  if (CONJ_COLS.includes(tail)) return d.conjunct(base, t.value.conjuncts[tail]);
  if (tail === "hal") return d.hal(base);
  if (tail === "a") return d.inherent(base);
  return d.sign2(base, tail);
}
// Option sets that type this form the same way are shown together; most forms have one group.
const typing = computed(() => {
  const f = current.value;
  if (!f) return [];
  const groups = new Map<string, { seqs: string[]; sets: typeof OPTION_SETS }>();
  for (const o of OPTION_SETS) {
    const key = JSON.stringify(f.roman[o.key]);
    if (!groups.has(key)) groups.set(key, { seqs: f.roman[o.key], sets: [] });
    groups.get(key)!.sets.push(o);
  }
  return [...groups.values()].map((g) => ({
    ...g,
    label: g.sets.length === OPTION_SETS.length ? t.value.anyOptions
      : capitalize(g.sets.map((o) => (o.key === "default" ? t.value.optionSets.default : t.value.withOption(t.value.optionSets[o.key]))).join(", ")),
    param: g.sets[0].param,
  }));
});
function capitalize(s: string) {
  return s.charAt(0).toUpperCase() + s.slice(1);
}
function tryHref(seq: string, param: string) {
  const p = new URLSearchParams({ q: seq });
  if (param) p.set("o", param);
  return link(`/playground?${p}`);
}
</script>

<template>
  <div class="ex">
    <div class="ex-controls">
      <div class="ex-legend" role="group" :aria-label="t.filterByStatus">
        <button v-for="s in STATUSES" :key="s" class="ex-status" :class="['st-' + s, { off: !shown[s] }]"
          :aria-pressed="shown[s]" :title="t.statuses[s][1]" @click="shown[s] = !shown[s]">
          <span class="ex-swatch" />{{ t.statuses[s][0] }} <b>{{ counts[s] ?? 0 }}</b>
        </button>
      </div>
      <div class="ex-find">
        <input v-model="query" type="search" :placeholder="t.findPlaceholder" :aria-label="t.findLabel" />
        <span v-if="matches" class="ex-muted">{{ t.matches(matches.size) }}</span>
      </div>
    </div>

    <p v-if="loading" class="ex-muted">{{ t.loadingForms }}</p>

    <div v-else class="ex-layout">
      <div class="ex-main">
        <h2>{{ t.vowelsAndSigns }}</h2>
        <div class="ex-vowels">
          <button v-for="f in vowelRow" :key="f.id" class="ex-cell si" :class="['st-' + f.status, { dim: dim(f), sel: f.id === selected }]"
            :title="f.id" @click="selected = f.id">{{ f.text }}</button>
        </div>

        <h2>{{ t.grid }}</h2>
        <div class="ex-scroll">
          <table class="ex-grid">
            <thead>
              <tr>
                <th class="ex-corner" />
                <th v-for="h in colHeads" :key="h.id" :title="h.id"><span class="si">{{ h.glyph }}</span><small>{{ h.id }}</small></th>
                <th v-for="h in conjHeads" :key="h.id" class="ex-conj" :title="h.id"><span class="si">{{ h.glyph }}</span><small>{{ h.id.slice(0, 5) }}</small></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="c in consonants" :key="c">
                <th class="ex-rowhead"><span class="si">{{ forms.get(c + '.a')?.text }}</span><small>{{ c }}</small></th>
                <td v-for="v in [...VOWEL_COLS, ...CONJ_COLS]" :key="v" :class="{ 'ex-conj': CONJ_COLS.includes(v) }">
                  <button class="ex-cell si" :class="['st-' + forms.get(c + '.' + v)?.status, { dim: dim(forms.get(c + '.' + v)), sel: selected === c + '.' + v }]"
                    :title="c + '.' + v" @click="selected = c + '.' + v">{{ forms.get(c + '.' + v)?.text }}</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <aside v-if="current" class="ex-detail" aria-live="polite">
        <div class="ex-big si" lang="si">{{ current.text }}</div>
        <div class="ex-id"><code>{{ current.id }}</code> · {{ describe(current.id) }}</div>
        <div class="ex-badge" :class="'st-' + current.status">{{ t.statuses[current.status][0] }}</div>
        <p class="ex-note">{{ t.statuses[current.status][1] }}</p>
        <p v-if="current.shape" class="ex-note"><b>{{ t.glyph }}</b> {{ t.shapes[current.shape] }}</p>

        <h3>{{ t.codePoints }}</h3>
        <div class="ex-cps">
          <span v-for="(c, i) in codepoints" :key="i" :class="{ special: c.special }"><span class="si">{{ c.label }}</span><small>{{ c.cp }}</small></span>
        </div>

        <h3>{{ t.rules }}</h3>
        <div v-for="r in current.rules" :key="r" class="ex-rule">
          <a :href="link('/rules#' + r.toLowerCase())">{{ r }}</a>
          <span v-if="rules[r]" class="ex-kind">{{ rules[r].kind }}</span>
          <div v-if="rules[r]" class="ex-rule-text" v-html="inline(rules[r].text)" />
        </div>

        <h3>{{ t.howToType }}</h3>
        <div v-for="g in typing" :key="g.label" class="ex-type">
          <div class="ex-type-label">{{ g.label }}</div>
          <div v-if="g.seqs.length" class="ex-romans">
            <a v-for="s in g.seqs" :key="s" :href="tryHref(s, g.param)" :title="t.openInPlayground"><code>{{ s }}</code></a>
          </div>
          <p v-else class="ex-muted">
            <template v-if="current.status === 'never'">{{ t.cantType }}</template>
            <template v-else>{{ t.notProduced }}</template>
          </p>
        </div>
        <p v-if="typing.length > 1" class="ex-hint">
          {{ t.optionsHint[0] }}<a :href="link('/playground')">{{ t.optionsHint[1] }}</a>{{ t.optionsHint[2] }}
        </p>
      </aside>
    </div>
  </div>
</template>

<style scoped>
.ex h2 { font-size: 16px; font-weight: 700; margin: 24px 0 10px; }
.ex h3 { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: var(--vp-c-text-2); margin: 20px 0 8px; }
.ex-muted { color: var(--vp-c-text-2); font-size: 14px; }

.ex-controls { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 12px; }
.ex-legend { display: flex; flex-wrap: wrap; gap: 6px; }
.ex-status { display: inline-flex; align-items: center; gap: 6px; font-size: 13px; padding: 4px 10px; border-radius: 999px; border: 1px solid var(--vp-c-divider); background: var(--vp-c-bg-soft); color: var(--vp-c-text-1); }
.ex-status b { color: var(--vp-c-text-2); font-weight: 600; }
.ex-status.off { opacity: 0.45; text-decoration: line-through; }
.ex-swatch { width: 10px; height: 10px; border-radius: 3px; background: var(--c); }
.ex-find { display: flex; align-items: center; gap: 10px; }
.ex-find input { width: 220px; max-width: 60vw; padding: 6px 12px; border-radius: 8px; border: 1px solid var(--vp-c-divider); background: var(--vp-c-bg-soft); font-size: 14px; font-family: var(--vp-font-family-mono), var(--si-font); }
.ex-find input:focus { border-color: var(--vp-c-brand-1); outline: none; }

.st-valid { --c: var(--st-valid); --b: var(--st-valid-bg); }
.st-loan { --c: var(--st-loan); --b: var(--st-loan-bg); }
.st-rare { --c: var(--st-rare); --b: var(--st-rare-bg); }
.st-unattested { --c: var(--st-unattested); --b: var(--st-unattested-bg); }
.st-never { --c: var(--st-never); --b: var(--st-never-bg); }

.ex-layout { display: grid; grid-template-columns: minmax(0, 1fr) 320px; gap: 24px; align-items: start; }
@media (max-width: 1100px) { .ex-layout { grid-template-columns: minmax(0, 1fr); } }

.ex-vowels { display: flex; flex-wrap: wrap; gap: 4px; }
.ex-scroll { overflow-x: auto; border: 1px solid var(--vp-c-divider); border-radius: 12px; max-height: 72vh; overflow-y: auto; }
.ex-grid { border-collapse: separate; border-spacing: 2px; margin: 0; display: table; }
.ex-grid th, .ex-grid td { border: none; padding: 0; background: none; }
.ex-grid thead th { position: sticky; top: 0; z-index: 2; background: var(--vp-c-bg); padding: 4px 0; text-align: center; font-weight: 500; }
.ex-grid th span, .ex-rowhead span { display: block; font-size: 16px; line-height: 1.5; }
.ex-grid small, .ex-rowhead small { display: block; font: 10px var(--vp-font-family-mono); color: var(--vp-c-text-3); }
/* Sticky row labels: ".ex-grid" in the selector so it outranks the ".ex-grid th" reset above. The
   shadow covers the 2px border-spacing gap and draws the edge that cells scroll under. */
.ex-grid .ex-rowhead { position: sticky; left: 0; z-index: 1; background: var(--vp-c-bg); padding: 0 8px; text-align: center; min-width: 52px; box-shadow: 2px 0 0 var(--vp-c-bg), 3px 0 0 var(--vp-c-divider); }
.ex-grid thead .ex-corner { left: 0; z-index: 3; box-shadow: 2px 0 0 var(--vp-c-bg), 3px 0 0 var(--vp-c-divider); }
td.ex-conj, th.ex-conj { padding-left: 6px !important; }

.ex-cell { min-width: 44px; height: 44px; padding: 0 4px; white-space: nowrap; border-radius: 8px; font-size: 19px; line-height: 1; background: var(--b); border: 1px solid transparent; color: var(--vp-c-text-1); transition: opacity 0.15s, transform 0.1s; }
.ex-cell.st-never { color: var(--c); background: repeating-linear-gradient(135deg, var(--b) 0 6px, transparent 6px 10px); }
.ex-cell:hover { border-color: var(--c); }
.ex-cell.sel { border: 2px solid var(--vp-c-brand-1); box-shadow: 0 0 0 3px var(--vp-c-brand-soft); }
.ex-cell.dim { opacity: 0.12; }

.ex-detail { position: sticky; top: calc(var(--vp-nav-height) + 16px); border: 1px solid var(--vp-c-divider); border-radius: 14px; padding: 20px; background: var(--vp-c-bg-soft); margin-top: 24px; }
@media (max-width: 1100px) { .ex-detail { position: static; } }
.ex-big { font-family: var(--si-font-display); font-size: 72px; line-height: 1.4; text-align: center; }
.ex-id { text-align: center; font-size: 13px; color: var(--vp-c-text-2); }
.ex-badge { display: block; width: fit-content; margin: 10px auto 0; padding: 2px 12px; border-radius: 999px; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: var(--c); background: var(--b); border: 1px solid var(--c); }
.ex-note { font-size: 14px; color: var(--vp-c-text-2); margin: 10px 0 0; line-height: 1.55; }
.ex-cps { display: flex; flex-wrap: wrap; gap: 6px; }
.ex-cps > span { display: flex; flex-direction: column; align-items: center; padding: 4px 8px; border: 1px dashed var(--vp-c-divider); border-radius: 8px; }
.ex-cps > span.special { border-style: solid; border-color: var(--vp-c-brand-1); color: var(--vp-c-brand-1); }
.ex-cps .si { font-size: 18px; }
.ex-cps small { font: 11px var(--vp-font-family-mono); color: var(--vp-c-text-2); }
.ex-rule { font-size: 14px; margin-bottom: 10px; }
.ex-rule a { font-weight: 700; color: var(--vp-c-brand-1); }
.ex-kind { font-size: 11px; font-weight: 700; margin-left: 6px; color: var(--vp-c-text-2); }
.ex-rule-text { color: var(--vp-c-text-2); line-height: 1.55; margin-top: 2px; }
.ex-rule-text :deep(code) { font-size: 12px; }
.ex-type { margin-bottom: 10px; }
.ex-type-label { font-size: 12px; color: var(--vp-c-text-2); margin-bottom: 4px; }
.ex-hint { font-size: 12px; line-height: 1.5; color: var(--vp-c-text-3); margin: 8px 0 0; }
.ex-hint a { color: var(--vp-c-brand-1); }
.ex-romans { display: flex; flex-wrap: wrap; gap: 6px; }
.ex-romans a code { font-size: 14px; }
.ex-romans a:hover code { color: var(--vp-c-brand-1); }
</style>
