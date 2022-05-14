<template>
  <div>
    <img
      id="profile-img"
      src="https://ssl.gstatic.com/accounts/ui/avatar_2x.png"
    />
    <RegisterUser v-if="!user" />
    <RegisterAddress v-if="loggedInAsBuyer" :doItLater="true" />
  </div>
</template>

<script>
import RegisterUser from '@/components/RegisterUser.vue';
import RegisterAddress from '@/components/RegisterAddress.vue';
export default {
  name: 'Register',
  components: {
    RegisterUser,
    RegisterAddress,
  },
  computed: {
    user() {
      return this.$store.state.auth.user;
    },
    buyer() {
      return this.$store.state.auth.buyer;
    },
    loggedInAsBuyer() {
      return this.$store.state.auth.loggedInAs === 'buyer' && this.buyer;
    },
  },
  mounted() {
    if (
      this.user &&
      (this.$store.state.auth.seller ||
        (this.$store.state.auth.buyer &&
          this.$store.state.auth.buyer.main_address_id))
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
