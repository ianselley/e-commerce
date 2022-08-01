const colors = require('tailwindcss/colors');

module.exports = {
  content: ['./public/index.html', './src/**/*.{vue,js}'],
  theme: {
    maxWidth: {
      full: '100%',
      52: '13rem',
    },
    minWidth: {
      40: '10rem',
    },
    extend: {
      colors: {
        violet: colors.violet,
        sky: colors.sky,
        amber: colors.amber,
        lime: colors.lime,
      },
    },
  },
  plugins: [],
};
