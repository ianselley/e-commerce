<template>
  <div>
    <RegisterUser />
    <RegisterBuyer v-if="userIsBuyer" />
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
    userIsBuyer() {
      return (
        this.$store.state.auth.user &&
        this.$store.state.auth.user.role == 'buyer'
      );
    },
  },
};
</script>
