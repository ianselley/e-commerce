<template>
  <div>
    <div class="inline-block mr-3">Quantity:</div>
    <select ref="quantity">
      <option v-for="quantity in maxProducts" :key="quantity" :value="quantity">
        {{ quantity }}
      </option>
    </select>
    <button @click="addToCart">ADD TO CART</button>
  </div>
</template>

<script>
export default {
  name: 'AddToCart',
  props: {
    productId: Number,
    stock: Number,
  },
  data() {
    return {
      loading: false,
    };
  },
  computed: {
    buyerId() {
      return this.$store.state.auth.buyer.id;
    },
    maxProducts() {
      return Math.min(this.$props.stock, 30);
    },
  },
  methods: {
    addToCart() {
      const quantity = this.$refs.quantity.value;
      this.loading = true;
      this.$store
        .dispatch('cartProduct/addToCart', {
          productId: this.productId,
          quantity,
        })
        .then(() => {
          this.$store.dispatch('alert/setMessage', 'PRODUCT ADDED TO CART!');
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

<style lang="postcss" scoped></style>
