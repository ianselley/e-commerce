<template>
  <div class="flex flex-col justify-center">
    <DefaultImageProfile />
    <RegisterUser v-if="!user" />
    <RegisterAddress v-if="loggedInAsBuyer" :doItLater="true" />
  </div>
</template>

<script>
import RegisterUser from '@/components/RegisterUser.vue';
import RegisterAddress from '@/components/RegisterAddress.vue';
import DefaultImageProfile from '@/components/DefaultImageProfile.vue';
export default {
  name: 'Signup',
  components: {
    RegisterUser,
    RegisterAddress,
    DefaultImageProfile,
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
  created() {
    if (
      this.user &&
      (this.$store.state.auth.seller ||
        (this.$store.state.auth.buyer &&
          this.$store.state.auth.buyer.main_address_id))
    ) {
      this.$router.push('/profile');
      this.$store.dispatch(
        'alert/setMessage',
        'You are already registered, you would have to log out to access the signup page'
      );
    }
  },
};
</script>
