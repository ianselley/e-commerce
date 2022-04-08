<template>
  <div class="cart-product">
    <div class="quantity">QUANTITY: {{ cartProduct.quantity }}</div>
    <button class="remove" @click="removeFromCart" :disabled="loading">
      Remove
    </button>
    <DisplayProduct :product="cartProduct.product" />
  </div>
</template>

<script>
import DisplayProduct from '@/components/DisplayProduct.vue';
export default {
  name: 'DisplayCartProduct',
  components: {
    DisplayProduct,
  },
  props: {
    cartProduct: Object,
  },
  data() {
    return {
      loading: false,
    };
  },
  methods: {
    removeFromCart() {
      const cartProductId = this.$props.cartProduct.id;
      this.loading = true;
      this.$store
        .dispatch('cartProduct/removeFromCart', cartProductId)
        .then(() => {
          this.loading = false;
        })
        .catch((error) => {
          this.loading = false;
          this.$store.dispatch('alert/setMessage', error);
        });
    },
  },
};
</script>

<style scoped>
.cart-product {
  margin: 0 3rem;
}

.quantity {
  display: inline-block;
}
</style>
