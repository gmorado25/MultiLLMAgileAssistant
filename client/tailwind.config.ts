import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
      colors: {
        Primary: "#01579B",
        Secondary: "#3050F8",
        Hover: "#ECF1FF",
        HighEmphasis: "#202020",
        MediumEmphasis: "#595959",
        LowEmphasis: "#D9D9D9",
        Disabled: "#909090",
        Success: "#7DB249",
        Warning: "#FAAA3A",
        Error: "#C62828",
      },
    },
  },
  plugins: [],
  corePlugins: {
    preflight: false,
  },
};
export default config;
