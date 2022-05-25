const colors = require('tailwindcss/colors');

module.exports = {
  content: ['./public/index.html', './src/**/*.{vue,js}'],
  theme: {
    extend: {
      colors: {
        violet: colors.violet,
        sky: colors.sky,
        amber: colors.amber,
      },
    },
  },
  plugins: [],
};
