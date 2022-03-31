import { createStore } from 'vuex';

import { auth } from './auth.module.js';
import { alert } from './alert.module.js';
import { product } from './product.module.js';

const store = createStore({
  modules: {
    auth,
    alert,
    product,
  },
});

export default store;
