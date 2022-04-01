<template>
  <div></div>
</template>

<script>
export default {
  name: 'Logout',
  computed: {
    loggedIn() {
      return this.$store.state.auth.loggedIn;
    },
    currentUser() {
      return this.$store.state.auth.user;
    },
  },
  created() {
    if (this.loggedIn) {
      this.$store.dispatch('auth/logout');
      this.$store.dispatch('product/removeSellerProducts');
    }
    if (!this.currentUser) {
      this.$router.push('/login');
    }
  },
};
</script>
