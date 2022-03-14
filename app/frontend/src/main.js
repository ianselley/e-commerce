import { createApp } from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import VueCookies from 'vue3-cookies';

import App from './App.vue';
import router from './router';
import store from './store';
import { BASE_URL } from './config.json';

axios.defaults.withCredentials = true;
axios.defaults.baseURL = BASE_URL;

const cookiesConfig = {
  expireTimes: '30d',
  path: '/',
  domain: '',
  secure: false,
  sameSite: 'strict',
  httpOnly: true,
};

createApp(App)
  .use(store)
  .use(router)
  .use(VueAxios, axios)
  .use(VueCookies, cookiesConfig)
  .mount('#app');
