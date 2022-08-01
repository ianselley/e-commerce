<template>
  <div>
    <div class="main-title">ORDERS</div>
    <div
      v-if="orders"
      class="w-full flex flex-col justify-center space-y-4 mt-6"
    >
      <DisplayOrder
        v-for="order in Array.from(orders).slice().reverse()"
        :key="order.id"
        :order="order"
        class="mx-auto"
      />
    </div>
  </div>
</template>

<script>
import DisplayOrder from '@/components/DisplayOrder.vue';
export default {
  name: 'Orders',
  components: {
    DisplayOrder,
  },
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    },
    currentBuyer() {
      return this.$store.state.auth.buyer;
    },
    currentSeller() {
      return this.$store.state.auth.seller;
    },
    orders() {
      if (this.currentBuyer) {
        return this.currentBuyer && this.currentBuyer.orders;
      }
      return this.currentSeller && this.currentSeller.orders;
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
