import { createApp } from 'vue'
import axios from 'axios'

import App from './App.vue'
import router from './router'
import store from './store'
import './index.css'
import { BASE_URL } from './config.json'

axios.defaults.withCredentials = true
axios.defaults.baseURL = BASE_URL

const app = createApp(App)

app.use(store)
app.use(router)

app.mount('#app')
