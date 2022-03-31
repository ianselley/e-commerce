<template>
  <div>
    <img
      id="profile-img"
      src="https://ssl.gstatic.com/accounts/ui/avatar_2x.png"
    />
    <RegisterUser v-if="!user" />
    <RegisterBuyer v-else-if="userIsBuyer" />
    <RegisterSeller v-else />
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
      return this.user && this.user.role == 'buyer';
    },
    loggedIn() {
      return this.$store.state.auth.loggedIn;
    },
  },
  mounted() {
    if (
      this.user &&
      (this.$store.state.auth.seller ||
        (this.$store.state.auth.buyer &&
          this.$storelstate.auth.buyer.main_address_id))
    ) {
      this.$router.push('/profile');
      this.$store.commit(
        'alert/setMessage',
        'You are already logged in, you would have to log out to access this'
      );
    }
  },
};
</script>
