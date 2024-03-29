import { createStore } from 'vuex';

import { auth } from './auth.module.js';
import { alert } from './alert.module.js';
import { order } from './order.module.js';
import { address } from './address.module.js';
import { product } from './product.module.js';
import { cartProduct } from './cartProduct.module.js';

const store = createStore({
  modules: {
    auth,
    alert,
    order,
    address,
    product,
    cartProduct,
  },
});

export default store;
