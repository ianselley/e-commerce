const colors = require('tailwindcss/colors');

module.exports = {
  content: ['./public/index.html', './src/**/*.{vue,js}'],
  theme: {
    fontFamily: {
      publicSans: ['Public Sans', 'Sans-serif'],
    },
    maxWidth: {
      full: '100%',
      52: '13rem',
      48: '12rem',
      'screen-xl': '1280px',
      '10xl': '104rem',
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
      width: {
        96: '24rem',
      },
    },
  },
  plugins: [],
};
