const colors = require('tailwindcss/colors');

module.exports = {
  content: ['./public/index.html', './src/**/*.{vue,js}'],
  theme: {
    maxWidth: {
      70: '70vw',
      50: '50vw',
    },
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
