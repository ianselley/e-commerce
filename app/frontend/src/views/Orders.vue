<template>
  <div>
    <div style="margin-top: 1.5rem"><strong>ORDERS:</strong></div>
    <DisplayOrders />
  </div>
</template>

<script>
import DisplayOrders from '@/components/DisplayOrders.vue';
export default {
  name: 'Orders',
  components: {
    DisplayOrders,
  },
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    },
  },
  created() {
    if (!this.currentUser) {
      this.$router.push('/login');
      this.$store.dispatch('alert/setMessage', 'You are not logged in');
    } else {
      this.$store
        .dispatch('auth/getUser')
        .then((response) => {
          if (response.seller) {
            const sellerId = response.seller.id;
            return this.$store.dispatch('product/getSellerProducts', sellerId);
          }
        })
        .catch((error) => {
          this.$store.dispatch('alert/setMessage', error);
        });
    }
  },
};
</script>

<style lang="postcss" scoped></style>
