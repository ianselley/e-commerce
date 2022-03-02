<template>
  <div>
    <img id="profile-img" src="//ssl.gstatic.com/accounts/ui/avatar_2x.png" />
    <!-- <RegisterUser v-if="!user" />
    <RegisterBuyer v-else-if="userIsBuyer" />
    <RegisterSeller v-else /> -->
    <RegisterUser v-if="false" />
    <RegisterBuyer v-if="true" />
    <RegisterSeller v-if="false" />
  </div>
</template>

<script>
import RegisterUser from '@/components/RegisterUser.vue';
import RegisterBuyer from '@/components/RegisterBuyer.vue';
import RegisterSeller from '@/components/RegisterSeller.vue';
export default {
  name: 'Register',
  components: {
    RegisterUser,
    RegisterBuyer,
    RegisterSeller,
  },
  computed: {
    user() {
      return this.$store.state.auth.user;
    },
    userIsBuyer() {
      return this.user && this.$store.state.auth.user.role == 'buyer';
    },
    loggedIn() {
      return this.$store.state.auth.loggedIn;
    },
  },
  mounted() {
    if (this.user && (this.user.seller || this.user.buyer)) {
      this.$router.push('/profile');
      this.$store.commit(
        'alert/setMessage',
        'You are already logged in, you would have to log out to access this'
      );
    }
  },
};
</script>
