// The JavaScript port must reproduce the Python package exactly. The golden files are written by
// tools/build_js_golden.py from the Python reference; regenerate them after any change there.
import assert from "node:assert/strict";
import fs from "node:fs";
import { test } from "node:test";
import { gunzipSync } from "node:zlib";
import { Lexicon, candidates, entries, normalize, soundKey, toSinhala } from "../dist/index.js";

const GOLDEN = new URL("./golden/", import.meta.url);
const read = (name) => fs.readFileSync(new URL(name, GOLDEN));
const lines = (text) => text.split("\n").filter(Boolean).map((l) => JSON.parse(l));

const OPTIONS = {
  default: {},
  repayaZwj: { repayaZwj: true },
  classical: { classical: true },
  archaic: { archaic: true },
  rakaransayaU: { rakaransayaU: true },
};
const ZWJ = "‍";

/** Compare every row, then report the first few mismatches instead of stopping at the first. */
function check(rows, actual, label) {
  const bad = [];
  for (const row of rows) {
    const [got, want] = actual(row);
    if (got !== want) bad.push(`${label(row)}: got ${JSON.stringify(got)}, want ${JSON.stringify(want)}`);
  }
  assert.equal(bad.length, 0, `${bad.length} of ${rows.length} differ:\n${bad.slice(0, 15).join("\n")}`);
}

const romanization = lines(gunzipSync(read("romanization.jsonl.gz")).toString("utf-8"));

test("toSinhala matches the Python reference", () => {
  assert.ok(romanization.length > 50000);
  check(romanization, ([opts, src, out]) => [toSinhala(src, OPTIONS[opts]), out], ([opts, src]) => `${opts} ${JSON.stringify(src)}`);
});

test("soundKey matches the Python reference", () => {
  check(romanization, ([, , out, key]) => [soundKey(out), key], ([, src]) => JSON.stringify(src));
});

test("normalize restores ZWJ like the Python reference", () => {
  check(romanization, ([, , out, , norm]) => [normalize(out.replaceAll(ZWJ, "")), norm], ([, src]) => JSON.stringify(src));
});

test("candidates match the Python reference", () => {
  const lex = new Lexicon(read("lexicon.txt").toString("utf-8"));
  const rows = lines(read("candidates.jsonl").toString("utf-8"));
  assert.ok(rows.length > 1000);
  check(
    rows,
    ([q, partial, want]) => [JSON.stringify(candidates(lex, q, { limit: 8, partial })), JSON.stringify(want)],
    ([q, partial]) => `${JSON.stringify(q)}${partial ? " (partial)" : ""}`,
  );
});

test("Lexicon also accepts [word, count] pairs", () => {
  const text = read("lexicon.txt").toString("utf-8");
  const pairs = text.split("\n").filter(Boolean).map((l) => l.split("\t")).map(([w, n]) => [w, Number(n)]);
  const a = new Lexicon(text);
  const b = new Lexicon(pairs);
  assert.deepEqual([...b.count], [...a.count]);
  assert.deepEqual(b.keys, a.keys);
});

test("entries match the Python inventory", () => {
  assert.deepEqual(entries(), JSON.parse(read("entries.json").toString("utf-8")));
});
