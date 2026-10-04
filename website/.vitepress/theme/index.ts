import DefaultTheme from "vitepress/theme";
import type { Theme } from "vitepress";
import Playground from "./components/Playground.vue";
import Explorer from "./components/Explorer.vue";
import "./custom.css";

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component("Playground", Playground);
    app.component("Explorer", Explorer);
  },
} satisfies Theme;
