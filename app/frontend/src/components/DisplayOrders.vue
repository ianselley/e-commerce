<template>
  <div>
    <DisplayOrder
      v-for="order in Array.from(orders).slice().reverse()"
      :key="order"
      :order="order"
    />
  </div>
</template>

<script>
import DisplayOrder from '@/components/DisplayOrder.vue';
export default {
  name: 'DisplayOrders',
  components: {
    DisplayOrder,
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
