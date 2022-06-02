<template>
  <div>
    <div v-if="product" class="image-info-cart">
      <DisplayImages :images="product.images" />
      <div class="cart">
        <div v-if="product.available && productHasStock">
          <p><Price :price="product.price" :available="product.available" /></p>
          <p v-if="productHasStock" class="available">In stock</p>
          <AddToCart
            v-if="buyer"
            :productId="parseInt(productId)"
            :stock="product.stock"
          />
        </div>
        <p v-else class="not-available">Currently not available</p>
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
      found: undefined,
      loading: false,
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
  mounted() {
    this.loading = true;
    this.$store
      .dispatch('product/getProduct', this.productId)
      .then(() => {
        this.found = true;
        this.loading = false;
      })
      .catch(() => {
        this.found = false;
      });
  },
};
</script>

<style lang="postcss" scoped>
.image-info-cart {
  display: flex;
  justify-content: space-between;
}

.cart {
  width: 10rem;
  height: fit-content;
  padding-bottom: 2rem;
  border: 1px solid black;
  border-radius: 1.5rem;
}

.available,
.not-available {
  font-weight: 700;
}

.available {
  color: rgb(120, 171, 61);
}

.not-available {
  color: red;
}
</style>
