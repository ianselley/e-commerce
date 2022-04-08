<template>
  <div v-if="product" class="image-info-cart">
    <DisplayImages :images="product.images" />
    <div class="cart">
      <p><Price :price="product.price" /></p>
      <p v-if="productHasStock" class="has-stock">In stock</p>
      <p v-else class="no-stock">Currently not available</p>
      <AddToCart v-if="buyer" :productId="parseInt(productId)" />
    </div>
  </div>
</template>

<script>
import DisplayImages from '@/components/DisplayImages.vue';
import Price from '@/components/Price.vue';
import AddToCart from '@/components/AddToCart.vue';
export default {
  name: 'Product',
  components: {
    DisplayImages,
    AddToCart,
    Price,
  },
  data() {
    return {
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
        this.loading = false;
      })
      .catch((error) => {
        this.$store.dispatch('alert/setMessage', error);
      });
  },
};
</script>

<style scoped>
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

.has-stock,
.no-stock {
  font-weight: 700;
}

.has-stock {
  color: rgb(120, 171, 61);
}

.no-stock {
  color: red;
}
</style>
