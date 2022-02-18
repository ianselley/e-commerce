<template>
  <!-- Check that the SDK client is not currently loading before accessing is methods -->
  <button @click="signup">Sign up</button>
  <div v-if="!isLoading">
    <!-- show login when not authenticated -->
    <button v-if="!isAuthenticated" @click="login">Log in</button>
    <!-- show logout when authenticated -->
    <button v-if="isAuthenticated" @click="logout">Log out</button>
  </div>
</template>

<script>
import { useAuth0 } from '@/services/auth0-plugin';
import { computed } from 'vue';

export default {
  name: 'Authentication',
  setup() {
    const auth0 = useAuth0();

    const isLoading = computed(() => auth0.isLoading.value);
    const isAuthenticated = computed(() => auth0.isAuthenticated.value);
    const signup = () => auth0.login({ screen_hint: 'signup' });
    const login = () => auth0.login();
    const logout = () => auth0.logout({ returnTo: window.location.origin });

    return { login, logout, isAuthenticated, isLoading, signup };
  },
};
</script>
