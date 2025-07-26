/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        brown: '#a47b67',
        'dark-blue': '#6790a4',
        'dark-blue-2': '#486472',
        beige: '#efddd5',
        'light-blue': '#c2d8f4',
        yellow: '#d6a24f',
      },
    },
    fontFamily: {
      serif: ['Noto Serif', 'serif'],
    },
  },
  plugins: [],
}

