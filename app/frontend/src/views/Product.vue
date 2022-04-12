<template>
  <div v-if="product" class="image-info-cart">
    <DisplayImages :images="product.images" />
    <div class="cart">
      <div v-if="product.available && productHasStock">
        <p><Price :price="product.price" /></p>
        <p v-if="productHasStock" class="available">In stock</p>
        <AddToCart v-if="buyer" :productId="parseInt(productId)" />
      </div>
      <p v-else class="not-available">Currently not available</p>
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
