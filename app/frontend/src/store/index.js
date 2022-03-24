import { createStore } from 'vuex';

import { auth } from './auth.module.js';
import { alert } from './alert.module.js';

const store = createStore({
  modules: {
    auth,
    alert,
  },
});

export default store;
