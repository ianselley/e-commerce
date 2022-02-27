import { createStore } from 'vuex';

import { auth } from './auth.module';
import { alert } from './alert.module';

const store = createStore({
  modules: {
    auth,
    alert,
  },
});

export default store;
