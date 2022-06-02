<template>
  <div class="cart-product">
    <div class="quantity">QUANTITY:</div>
    <select ref="quantity" @change="changeQuantity" :disabled="loading">
      <option
        v-for="quantity in 30"
        :key="quantity"
        :selected="quantity == cartProduct.quantity"
        :value="quantity"
      >
        {{ quantity }}
      </option>
    </select>
    <br />
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
    changeQuantity() {
      this.loading = true;
      const cartProductId = this.$props.cartProduct.id;
      const quantity = parseInt(this.$refs.quantity.value);
      this.$store
        .dispatch('cartProduct/changeQuantity', { cartProductId, quantity })
        .then(() => {
          this.loading = false;
        })
        .catch((error) => {
          this.$store.dispatch('alert/setMessage', error);
          this.loading = false;
        });
    },
  },
};
</script>

<style lang="postcss" scoped>
.cart-product {
  margin: 0 3rem;
}

.quantity {
  display: inline-block;
}
</style>
