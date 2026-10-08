import { createHash } from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { defineConfig, type DefaultTheme } from "vitepress";
import { REPO, ruleLinks, slugify } from "./rule-links";

const base = "/Sinhala-Phonetic-Orthography/";
const ROOT = path.resolve(__dirname, "../..");

/** A translated research page: its English original, and whether that changed since (tools/check_translations.py). */
function translationOf(source: string, relativePath: string) {
  if (!/^docs\/[a-z]+\//.test(source) || !fs.existsSync(path.join(ROOT, source))) return undefined;
  const stamp = fs.readFileSync(path.join(ROOT, source), "utf-8").match(/^<!-- translated from (\S+) sha256:([0-9a-f]{12}) -->/);
  if (!stamp) return undefined;
  const english = fs.readFileSync(path.join(ROOT, stamp[1]), "utf-8").replace(/\r\n/g, "\n");
  const hash = createHash("sha256").update(english, "utf-8").digest("hex").slice(0, 12);
  const original = "/" + relativePath.replace(/^[a-z]+\//, "").replace(/\.md$/, "");
  return { original, stale: hash !== stamp[2] };
}

// Labels for the nav bar and the sidebar, per language. Pages under /si/ mirror the English ones.
type Labels = {
  rules: string; research: string; playground: string; explorer: string; reference: string;
  startHere: string; ruleSet: string; letterExplorer: string;
  docs: [string, string][]; python: string; data: string; verification: string;
};

function nav(p: string, l: Labels): DefaultTheme.NavItem[] {
  return [
    { text: l.rules, link: `${p}/rules`, activeMatch: `^${p}/rules` },
    { text: l.research, link: `${p}/research/inventory`, activeMatch: `^${p}/research/` },
    { text: l.playground, link: `${p}/playground` },
    { text: l.explorer, link: `${p}/explorer` },
    { text: l.reference, link: `${p}/reference/python`, activeMatch: `^${p}/reference/` },
  ];
}

function sidebar(p: string, l: Labels): DefaultTheme.SidebarItem[] {
  return [
    {
      text: l.startHere,
      items: [
        { text: l.ruleSet, link: `${p}/rules` },
        { text: l.playground, link: `${p}/playground` },
        { text: l.letterExplorer, link: `${p}/explorer` },
      ],
    },
    { text: l.research, items: l.docs.map(([text, page]) => ({ text, link: `${p}/research/${page}` })) },
    {
      text: l.reference,
      items: [
        { text: l.python, link: `${p}/reference/python` },
        { text: l.data, link: `${p}/reference/data` },
        { text: l.verification, link: `${p}/reference/verification` },
      ],
    },
  ];
}

const en: Labels = {
  rules: "Rules", research: "Research", playground: "Playground", explorer: "Explorer", reference: "Reference",
  startHere: "Start here", ruleSet: "Consolidated rule set", letterExplorer: "Letter explorer",
  docs: [
    ["01 · Letter inventory", "inventory"],
    ["02 · Vowel signs", "vowel-signs"],
    ["03 · Hal and conjuncts", "hal-conjuncts"],
    ["04 · Nasals and spelling", "nasals-and-spelling"],
    ["05 · Phonotactics, sandhi, spelling", "phonotactics-sandhi-spelling"],
    ["06 · Romanization systems", "romanization-systems"],
    ["07 · Phonetic romanization", "phonetic-romanization"],
  ],
  python: "Python & JS packages", data: "Data files", verification: "Verification report",
};

const si: Labels = {
  rules: "නීති", research: "පර්යේෂණ", playground: "අත්හදා බැලීම", explorer: "අකුරු ගවේෂකය", reference: "යොමු",
  startHere: "මෙතැනින් අරඹන්න", ruleSet: "ඒකාබද්ධ නීති මාලාව", letterExplorer: "අකුරු ගවේෂකය",
  docs: [
    ["01 · අක්ෂර මාලාව", "inventory"],
    ["02 · පිලි (ස්වර ලකුණු)", "vowel-signs"],
    ["03 · හල් ලකුණ සහ සංයුක්ත අකුරු", "hal-conjuncts"],
    ["04 · නාසික සහ අක්ෂර වින්‍යාසය", "nasals-and-spelling"],
    ["05 · ශබ්ද සංයෝජනය, සන්ධි, අක්ෂර වින්‍යාසය", "phonotactics-sandhi-spelling"],
    ["06 · රෝමානුකරණ ක්‍රම", "romanization-systems"],
    ["07 · ශබ්දානුසාරී රෝමානුකරණය", "phonetic-romanization"],
  ],
  python: "Python සහ JS පැකේජ", data: "දත්ත ගොනු", verification: "සත්‍යාපන වාර්තාව",
};

export default defineConfig({
  // Served from GitHub Pages at https://srilals.github.io/Sinhala-Phonetic-Orthography/
  base,
  cleanUrls: true,
  head: [
    ["link", { rel: "icon", type: "image/svg+xml", href: `${base}logo.svg` }],
    ["meta", { name: "theme-color", content: "#9b1c42" }],
    ["link", { rel: "preconnect", href: "https://fonts.googleapis.com" }],
    ["link", { rel: "preconnect", href: "https://fonts.gstatic.com", crossorigin: "" }],
    [
      "link",
      {
        rel: "stylesheet",
        href: "https://fonts.googleapis.com/css2?family=Noto+Sans+Sinhala:wght@400;600;700&family=Noto+Serif+Sinhala:wght@500&display=swap",
      },
    ],
  ],
  transformPageData(page) {
    const translation = translationOf(page.frontmatter.source ?? "", page.relativePath);
    if (translation) page.frontmatter.translation = translation;
  },
  markdown: {
    anchor: { slugify },
    config: (md) => md.use(ruleLinks),
  },
  vite: {
    // The pages include docs/*.md and the components import src/ and data/ from the repo root.
    server: { fs: { allow: [".."] } },
  },

  locales: {
    root: {
      label: "English",
      lang: "en-US",
      title: "Sinhala Phonetic Orthography",
      description:
        "A sourced study of Sinhala orthography and romanization, with a rule set, letter-form data and a reference converter you can try in the browser.",
      themeConfig: {
        nav: nav("", en),
        sidebar: { "/": sidebar("", en) },
        editLink: {
          // Research pages include a file from docs/; edit that file, not the wrapper page.
          // This function is serialized to the client, so it can't refer to REPO.
          pattern: ({ filePath, frontmatter }) =>
            "https://github.com/SrilalS/Sinhala-Phonetic-Orthography/edit/main/" +
            (frontmatter.source ?? "website/" + filePath),
          text: "Edit this page on GitHub",
        },
        footer: {
          message: 'Text and code released under the MIT License. Cite as <a href="https://doi.org/10.5281/zenodo.23244126">doi:10.5281/zenodo.23244126</a>.',
          copyright: "© Srilal Siriwardhana",
        },
      },
    },
    si: {
      label: "සිංහල",
      lang: "si-LK",
      link: "/si/",
      title: "සිංහල ශබ්දානුසාරී අක්ෂර වින්‍යාසය",
      description:
        "සිංහල අක්ෂර වින්‍යාසය සහ රෝමානුකරණය පිළිබඳ මූලාශ්‍ර සහිත අධ්‍යයනයක්: නීති මාලාවක්, අකුරු රූප දත්ත සහ බ්‍රවුසරයෙන්ම අත්හදා බැලිය හැකි යොමු පරිවර්තකයක්.",
      themeConfig: {
        nav: nav("/si", si),
        sidebar: { "/si/": sidebar("/si", si) },
        editLink: {
          pattern: ({ filePath, frontmatter }) =>
            "https://github.com/SrilalS/Sinhala-Phonetic-Orthography/edit/main/" +
            (frontmatter.source ?? "website/" + filePath),
          text: "මෙම පිටුව GitHub හි සංස්කරණය කරන්න",
        },
        footer: {
          message: 'පෙළ සහ කේතය MIT බලපත්‍රය යටතේ නිකුත් කර ඇත. උපුටා දක්වන්න: <a href="https://doi.org/10.5281/zenodo.23244126">doi:10.5281/zenodo.23244126</a>.',
          copyright: "© Srilal Siriwardhana",
        },
        outline: { level: [2, 3], label: "මෙම පිටුවේ" },
        docFooter: { prev: "පෙර පිටුව", next: "ඊළඟ පිටුව" },
        darkModeSwitchLabel: "පෙනුම",
        lightModeSwitchTitle: "ආලෝක පෙනුමට මාරු වන්න",
        darkModeSwitchTitle: "අඳුරු පෙනුමට මාරු වන්න",
        sidebarMenuLabel: "මෙනුව",
        returnToTopLabel: "ඉහළට යන්න",
        langMenuLabel: "භාෂාව වෙනස් කරන්න",
        skipToContentLabel: "අන්තර්ගතයට යන්න",
        notFound: {
          title: "පිටුව හමු නොවීය",
          quote: "ඔබ සොයන පිටුව මෙහි නැත. සබැඳිය වැරදි හෝ පිටුව ඉවත් කර තිබිය හැක.",
          linkLabel: "මුල් පිටුවට යන්න",
          linkText: "මුල් පිටුවට",
        },
      },
    },
  },

  themeConfig: {
    logo: "/logo.svg",
    outline: { level: [2, 3] },
    socialLinks: [{ icon: "github", link: REPO }],
    search: {
      provider: "local",
      options: {
        locales: {
          si: {
            translations: {
              button: { buttonText: "සොයන්න", buttonAriaLabel: "සොයන්න" },
              modal: {
                displayDetails: "විස්තර පෙන්වන්න",
                resetButtonTitle: "සෙවුම මකන්න",
                backButtonTitle: "සෙවුම වසන්න",
                noResultsText: "ප්‍රතිඵල හමු නොවීය",
                footer: {
                  selectText: "තෝරන්න",
                  selectKeyAriaLabel: "Enter",
                  navigateText: "ගමන් කරන්න",
                  navigateUpKeyAriaLabel: "ඉහළට",
                  navigateDownKeyAriaLabel: "පහළට",
                  closeText: "වසන්න",
                  closeKeyAriaLabel: "Escape",
                },
              },
            },
          },
        },
      },
    },
  },
});
