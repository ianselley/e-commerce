import { createApp } from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';

import Auth0App from './Auth0App.vue';
import router from './router';
import store from './store';
import { BASE_URL } from './config.json';

axios.defaults.withCredentials = true;
axios.defaults.baseURL = BASE_URL;

const app = createApp(Auth0App);

app.use(store);
app.use(router);
app.use(VueAxios, axios);

app.mount('#app');
