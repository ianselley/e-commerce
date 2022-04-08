<template>
  <div>
    <div class="quantity">Quantity:</div>
    <select ref="quantity">
      <option v-for="quantity in 30" :key="quantity" :value="quantity">
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
  },
  methods: {
    addToCart() {
      const quantity = parseInt(this.$refs.quantity.value);
      this.loading = true;
      this.$store
        .dispatch('cartProduct/addToCart', {
          productId: this.productId,
          quantity,
        })
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
.quantity {
  display: inline-block;
  margin-right: 0.7rem;
}
</style>
