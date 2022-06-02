<template>
  <div v-if="orders">
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
};
</script>

<style lang="postcss" scoped></style>
