<template>
  <div v-if="currentUser">
    <header>
      <h3>
        <strong>{{ currentUser.username }}</strong> Profile
      </h3>
    </header>
    <p>
      <strong>Token:</strong>
      {{ currentUser.accessToken }}
    </p>
    <p>
      <strong>Id:</strong>
      {{ currentUser.user.id }}
    </p>
    <p>
      <strong>Email:</strong>
      {{ currentUser.user.email }}
    </p>
    <p>
      <strong>Role:</strong>
      {{ currentUser.user.role }}
    </p>
  </div>
</template>

<script>
export default {
  name: 'Profile',
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    },
  },
  created() {
    if (!this.currentUser) {
      this.$router.push('/login');
      this.$store.commit('alert/setMessage', 'You are not logged in!');
    }
  },
};
</script>
