<template>
  <App />
</template>

<script>
import App from './App.vue';
import { provideAuth0 } from './services/auth0-plugin';
export default {
  name: 'Auth0App',
  components: { App },
  setup() {
    provideAuth0();
  },
};
</script>
