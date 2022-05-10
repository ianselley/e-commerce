<template>
  <div>
    <DisplayProduct
      v-for="order in Array.from(orders).slice().reverse()"
      :key="order"
      :product="order.cart_product.product"
      :edit="false"
    />
  </div>
</template>

<script>
import DisplayProduct from '@/components/DisplayProduct.vue';
export default {
  name: 'DisplayOrders',
  components: {
    DisplayProduct,
  },
  computed: {
    currentBuyer() {
      return this.$store.state.auth.buyer;
    },
    orders() {
      if (this.currentBuyer) return this.$store.state.auth.buyer.orders;
      return this.$store.state.auth.seller.orders;
    },
  },
};
</script>

<style scoped></style>
