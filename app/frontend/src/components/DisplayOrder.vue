<template>
  <div>
    <DisplayProduct :product="product" :edit="false" />
    <Countdown :deadline="deadline" />
  </div>
</template>

<script>
import Countdown from '@/components/Countdown.vue';
import DisplayProduct from '@/components/DisplayProduct.vue';
export default {
  name: 'DisplayOrder',
  components: {
    DisplayProduct,
    Countdown,
  },
  props: {
    order: Object,
  },
  mounted() {
    if (this.currentBuyer && this.afterDeadline && !this.productDelivered) {
      this.productArrives();
    }
  },
  computed: {
    currentBuyer() {
      return this.$store.state.auth.buyer;
    },
    product() {
      return this.$props.order.cart_product.product;
    },
    productDelivered() {
      return this.order.delivered;
    },
    afterDeadline() {
      const now = new Date();
      return now > this.deadline;
    },
    deadline() {
      const date = new Date(this.order.date);
      date.setDate(date.getDate() + 1);
      date.setTime(date.getTime() + 2 * 60 * 60 * 1000);
      console.log(date);
      return date;
    },
  },
  methods: {
    productArrives() {
      const orderId = this.order.id;
      this.$store.dispatch('order/productArrives', orderId).catch((error) => {
        this.$store.dispatch('alert/setMessage', error);
      });
    },
  },
};
</script>

<style scoped></style>
