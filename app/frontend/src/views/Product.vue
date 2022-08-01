<template>
  <div>
    <div v-if="product" class="flex justify-between">
      <DisplayImages :images="product.images" />
      <div class="cart-extra w-40 pb-8 border border-black rounded-lg">
        <div v-if="product.available && productHasStock">
          <p><Price :price="product.price" :available="product.available" /></p>
          <p v-if="productHasStock" class="font-bold text-lime-600">In stock</p>
          <AddToCart
            v-if="buyer"
            :productId="parseInt(productId)"
            :stock="product.stock"
          />
        </div>
        <p v-else class="font-bold text-red-500">Currently not available</p>
      </div>
    </div>
    <NotFound v-else />
  </div>
</template>

<script>
import Price from '@/components/Price.vue';
import NotFound from '@/components/NotFound.vue';
import AddToCart from '@/components/AddToCart.vue';
import DisplayImages from '@/components/DisplayImages.vue';
export default {
  name: 'Product',
  components: {
    Price,
    NotFound,
    AddToCart,
    DisplayImages,
  },
  data() {
    return {
      productId: this.$route.params.id,
    };
  },
  computed: {
    buyer() {
      return this.$store.state.auth.buyer;
    },
    product() {
      return this.$store.state.product.product;
    },
    productHasStock() {
      return this.product.stock > 0;
    },
  },
  created() {
    this.$store
      .dispatch('product/getProduct', this.productId)
      .catch((error) => {
        this.$store.dispatch('alert/setMessage', error);
      });
  },
};
</script>

<style lang="postcss" scoped>
.cart-extra {
  height: fit-content;
}
</style>
