import { defineConfig } from "vitepress";
import { REPO, ruleLinks, slugify } from "./rule-links";

const base = "/Sinhala-Phonetic-Orthography/";

export default defineConfig({
  title: "Sinhala Phonetic Orthography",
  description:
    "A sourced study of Sinhala orthography and romanization, with a rule set, letter-form data and a reference converter you can try in the browser.",
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
        href: "https://fonts.googleapis.com/css2?family=Noto+Sans+Sinhala:wght@400;600&family=Noto+Serif+Sinhala:wght@500&display=swap",
      },
    ],
  ],
  markdown: {
    anchor: { slugify },
    config: (md) => md.use(ruleLinks),
  },
  vite: {
    // The pages include docs/*.md and the components import src/ and data/ from the repo root.
    server: { fs: { allow: [".."] } },
  },
  themeConfig: {
    logo: "/logo.svg",
    nav: [
      { text: "Rules", link: "/rules", activeMatch: "^/rules" },
      { text: "Research", link: "/research/inventory", activeMatch: "^/research/" },
      { text: "Playground", link: "/playground" },
      { text: "Explorer", link: "/explorer" },
      { text: "Reference", link: "/reference/python", activeMatch: "^/reference/" },
    ],
    sidebar: {
      "/": [
        {
          text: "Start here",
          items: [
            { text: "Consolidated rule set", link: "/rules" },
            { text: "Playground", link: "/playground" },
            { text: "Letter explorer", link: "/explorer" },
          ],
        },
        {
          text: "Research",
          items: [
            { text: "01 · Letter inventory", link: "/research/inventory" },
            { text: "02 · Vowel signs", link: "/research/vowel-signs" },
            { text: "03 · Hal and conjuncts", link: "/research/hal-conjuncts" },
            { text: "04 · Nasals and spelling", link: "/research/nasals-and-spelling" },
            { text: "05 · Phonotactics, sandhi, spelling", link: "/research/phonotactics-sandhi-spelling" },
            { text: "06 · Romanization systems", link: "/research/romanization-systems" },
            { text: "07 · Phonetic romanization", link: "/research/phonetic-romanization" },
          ],
        },
        {
          text: "Reference",
          items: [
            { text: "Python package", link: "/reference/python" },
            { text: "Data files", link: "/reference/data" },
            { text: "Verification report", link: "/reference/verification" },
          ],
        },
      ],
    },
    outline: { level: [2, 3] },
    socialLinks: [{ icon: "github", link: REPO }],
    editLink: {
      // Research pages include a file from docs/; edit that file, not the wrapper page.
      // This function is serialized to the client, so it can't refer to REPO.
      pattern: ({ filePath, frontmatter }) =>
        "https://github.com/SrilalS/Sinhala-Phonetic-Orthography/edit/main/" +
        (frontmatter.source ?? "website/" + filePath),
      text: "Edit this page on GitHub",
    },
    search: { provider: "local" },
    footer: {
      message: "Text and code released under the MIT License.",
      copyright: "© Srilal Siriwardhana",
    },
  },
});
