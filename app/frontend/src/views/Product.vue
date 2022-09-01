<template>
  <div class="flex justify-center mx-6">
    <div v-if="productExists" class="flex">
      <DisplayImages :images="product.images" />
      <div class="width-text px-10 text-left">
        <div class="text-xl font-semibold">{{ product.seller.brand }}</div>
        {{ product.title }} - {{ product.description }}
      </div>
      <div
        class="bg-white w-48 p-6 border border-gray-300 rounded-lg cart-extra"
      >
        <div v-if="product.available && productHasStock">
          <p><Price :price="product.price" :available="product.available" /></p>
          <p v-if="productHasStock" class="font-bold text-lime-600 mt-1">
            In stock
          </p>
          <AddToCart :productId="parseInt(productId)" :stock="product.stock" />
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
    product() {
      return this.$store.state.product.product;
    },
    productExists() {
      return this.product != null;
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
  min-width: max-content;
}

.width-text {
  min-width: 16rem;
  max-width: 46rem;
}

@screen lg {
  .width-text {
    min-width: 22rem;
  }
}

@screen xl {
  .width-text {
    min-width: 34rem;
  }
}
</style>
