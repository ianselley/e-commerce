import { createApp } from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';

import App from './App.vue';
import router from './router';
import store from './store';
import { BASE_URL } from './config.json';
// import { domain, clientId } from './config.json';
// import { Auth0Plugin } from './auth';

axios.defaults.withCredentials = true;
axios.defaults.baseURL = BASE_URL;

const app = createApp(App);

app.use(store);
app.use(router);
app.use(VueAxios, axios);
// app.use(Auth0Plugin, {
//   domain,
//   clientId,
//   onRedirectCallback: (appState) => {
//     router.push(
//       appState && appState.targetUrl
//         ? appState.targetUrl
//         : window.location.pathname
//     );
//   },
// });

app.mount('#app');
