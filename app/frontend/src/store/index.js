import { createStore } from 'vuex';

import { auth } from './auth.module.js';
import { alert } from './alert.module.js';
import { product } from './product.module.js';
import { cartProduct } from './cartProduct.module.js';

const store = createStore({
  modules: {
    auth,
    alert,
    product,
    cartProduct,
  },
});

export default store;
