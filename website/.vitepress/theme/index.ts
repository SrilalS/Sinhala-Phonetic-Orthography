import { h } from "vue";
import DefaultTheme from "vitepress/theme";
import type { Theme } from "vitepress";
import Playground from "./components/Playground.vue";
import Explorer from "./components/Explorer.vue";
import TranslationNotice from "./components/TranslationNotice.vue";
import "./custom.css";

export default {
  extends: DefaultTheme,
  Layout: () => h(DefaultTheme.Layout, null, { "doc-before": () => h(TranslationNotice) }),
  enhanceApp({ app }) {
    app.component("Playground", Playground);
    app.component("Explorer", Explorer);
  },
} satisfies Theme;
