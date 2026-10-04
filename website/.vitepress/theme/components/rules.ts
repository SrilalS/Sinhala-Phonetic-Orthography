// The G-* rules, parsed from the tables in docs/00-rules.md and its Sinhala translation.
import RULES_EN from "../../../../docs/00-rules.md?raw";
import RULES_SI from "../../../../docs/si/00-rules.md?raw";

export type Rule = { id: string; text: string; kind: string; conf: string; section: string };

// Column names in each language. "Finding" is the rule column of the informal-romanization table.
const COLUMNS = {
  root: { rule: ["Rule", "Finding"], kind: "Kind", conf: "Conf", kinds: ["HARD", "SOFT", "STYLE"] },
  si: { rule: ["නීතිය", "සොයාගැනීම"], kind: "වර්ගය", conf: "විශ්වාසය", kinds: ["අනිවාර්ය", "නැඹුරුව", "විකල්ප"] },
};

function parse(md: string, cols: (typeof COLUMNS)["root"]) {
  const rules: Record<string, Rule> = {};
  const sectionKind = new RegExp(`\\((${cols.kinds.join("|")})\\)`);
  let section = "";
  let header: string[] = [];
  for (const line of md.replace(/\r\n/g, "\n").split("\n")) {
    if (line.startsWith("## ")) { section = line.slice(3).trim(); header = []; continue; }
    if (!line.startsWith("|")) continue;
    const cells = line.slice(1, line.trimEnd().endsWith("|") ? line.trimEnd().length - 1 : undefined).split(" | ").map((c) => c.trim());
    if (cells[0] === "ID") { header = cells; continue; }
    if (!/^G-[A-Z]+-\d+$/.test(cells[0])) continue;
    const col = (...names: string[]) => cells[header.findIndex((h) => names.includes(h))] ?? "";
    // Section 1 has no Kind column: its heading says the rules are HARD.
    const kind = col(cols.kind) || (sectionKind.exec(section)?.[1] ?? "");
    rules[cells[0]] = { id: cells[0], text: col(...cols.rule), kind, conf: col(cols.conf), section: section.replace(/^\d+\.\s*/, "") };
  }
  return rules;
}

/** Rules by locale ("root" is English). */
export const RULES: Record<string, Record<string, Rule>> = {
  root: parse(RULES_EN, COLUMNS.root),
  si: parse(RULES_SI, COLUMNS.si),
};

/** Minimal inline Markdown (bold, code) → HTML, for rule text. */
export function inline(md: string) {
  return md
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>");
}
