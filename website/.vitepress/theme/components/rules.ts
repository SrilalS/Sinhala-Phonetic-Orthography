// The G-* rules, parsed from the tables in docs/00-rules.md.
import RULES_MD from "../../../../docs/00-rules.md?raw";

export type Rule = { id: string; text: string; kind: string; conf: string; section: string };

export const RULES: Record<string, Rule> = {};

let section = "";
let header: string[] = [];
for (const line of RULES_MD.split("\n")) {
  if (line.startsWith("## ")) { section = line.slice(3).trim(); header = []; continue; }
  if (!line.startsWith("|")) continue;
  const cells = line.slice(1, line.trimEnd().endsWith("|") ? line.trimEnd().length - 1 : undefined).split(" | ").map((c) => c.trim());
  if (cells[0] === "ID") { header = cells; continue; }
  if (!/^G-[A-Z]+-\d+$/.test(cells[0])) continue;
  const col = (name: string) => cells[header.indexOf(name)] ?? "";
  // Section 1 has no Kind column: its heading says the rules are HARD.
  const kind = col("Kind") || (/\((HARD|SOFT|STYLE)\)/.exec(section)?.[1] ?? "");
  RULES[cells[0]] = { id: cells[0], text: col("Rule"), kind, conf: col("Conf"), section: section.replace(/^\d+\.\s*/, "") };
}

/** Minimal inline Markdown (bold, code) → HTML, for rule text. */
export function inline(md: string) {
  return md
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>");
}
