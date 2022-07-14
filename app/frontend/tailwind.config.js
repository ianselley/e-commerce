const colors = require('tailwindcss/colors');

module.exports = {
  content: ['./public/index.html', './src/**/*.{vue,js}'],
  theme: {
    maxWidth: {
      64: '13rem',
    },
    minWidth: {
      40: '10rem',
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
