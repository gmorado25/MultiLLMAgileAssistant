import { defineConfig } from "cypress";

export default defineConfig({
  e2e: {
    baseUrl: "http://127.0.0.1:8000/",
    viewportHeight: 1280,
    viewportWidth: 800,
  },

  component: {
    devServer: {
      framework: "next",
      bundler: "webpack",
    },
  },
});
