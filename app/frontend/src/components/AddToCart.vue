<template>
  <div class="mt-2">
    <div v-if="userIsBuyer" class="flex flex-col">
      <div>
        <div class="inline-block mr-1">Quantity</div>
        <select ref="quantity" class="text-center">
          <option
            v-for="quantity in maxProducts"
            :key="quantity"
            :value="quantity"
          >
            {{ quantity }}
          </option>
        </select>
      </div>
      <button @click="addToCart" :disabled="loading" class="mt-3">
        ADD TO CART
      </button>
    </div>
    <div v-else class="max-w-48">
      To be able to add this product to your cart you have to log in as a buyer
    </div>
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
    userIsBuyer() {
      return this.$store.state.auth.loggedInAs == 'buyer';
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
