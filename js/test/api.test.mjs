// A few readable examples of the public API (the golden tests cover the behaviour in bulk).
import assert from "node:assert/strict";
import { test } from "node:test";
import { CONSONANTS, Lexicon, SIGNS, TABLES, VOWELS, candidates, entries, soundKey, toSinhala, tokenize } from "../dist/index.js";

const Z = "‍";

test("toSinhala", () => {
  assert.equal(toSinhala("lankaava"), "ලංකාව");
  assert.equal(toSinhala("kruura"), "කෲර");
  assert.equal(toSinhala("kruura", { rakaransayaU: true }), "ක්" + Z + "රූර");
  assert.equal(toSinhala("lait"), "ලයිට්");
  assert.equal(toSinhala("akShara", { classical: true }), "අක්" + Z + "ෂර");
  assert.equal(toSinhala("karma", { repayaZwj: true }), "කර්" + Z + "ම");
  assert.equal(toSinhala("shrii lankaava!"), "ශ්" + Z + "රී ලංකාව!");
  assert.equal(toSinhala(""), "");
});

test("tokenize keeps the matched sequences", () => {
  assert.deepEqual(tokenize("kaa").map((t) => t.seq), ["k", "aa"]);
  assert.deepEqual(tokenize("zq").map((t) => t.kind), ["C"]); // "zq" is not a sequence: z is dropped, q is ද
});

test("candidates rank a word list", () => {
  const lex = new Lexicon("හොඳ\t900\nහොන්ද\t5\nකන්ද\t300\nකඳ\t200\n");
  assert.deepEqual(candidates(lex, "honda"), ["හොඳ", "හොන්ද"]);
  assert.deepEqual(candidates(lex, "kazda"), ["කඳ", "කන්ද"]); // explicit z marker beats frequency
  assert.deepEqual(candidates(lex, "ho", { partial: true }), ["හොඳ", "හොන්ද"]);
  assert.equal(soundKey("හොඳ"), "හොන්ද");
});

test("inventory", () => {
  assert.equal(entries().length, 923);
  assert.equal(VOWELS.length, 19);
  assert.equal(CONSONANTS.length, 41);
  assert.equal(SIGNS.length, 3);
  assert.ok(TABLES.consonants.length > 0);
});
