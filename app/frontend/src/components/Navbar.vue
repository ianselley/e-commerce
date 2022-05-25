<template>
  <div
    id="nav"
    class="px-10 py-6 sticky top-0 z-50 flex flex-row justify-between bg-white bg-opacity-50 backdrop-filter backdrop-blur-md shadow"
  >
    <IanSelleyLogo />
    <div id="endpoints" class="flex flex-row content-center space-x-8">
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
      <router-link to="/signup">Register</router-link>
      <router-link to="/login">Login</router-link>
      <router-link to="/profile">Profile</router-link>
      <button @click="logout">Logout</button>
    </div>
  </div>
</template>

<script>
import IanSelleyLogo from '@/components/IanSelleyLogo.vue';
export default {
  name: 'Navbar',
  components: {
    IanSelleyLogo,
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.loggedIn;
    },
    currentUser() {
      return this.$store.state.auth.user;
    },
  },
  methods: {
    logout() {
      if (this.loggedIn) {
        this.$store.dispatch('auth/logout');
        this.$store.dispatch('product/removeSellerProducts');
      }
      if (!this.currentUser) {
        this.$router.push('/login');
      }
      this.$store.dispatch('auth/logout');
    },
  },
};
</script>

<style scoped>
#nav * {
  @apply font-medium;
}
#nav a {
  @apply flex content-center leading-10 text-violet-900;
}

#nav a.router-link-exact-active {
  @apply text-amber-500;
}

#endpoints > * {
  @apply transition font-semibold ease-in-out duration-300 transform hover:scale-110;
}
</style>
