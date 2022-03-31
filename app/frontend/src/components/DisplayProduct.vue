<template>
  <div v-if="productHasAttributes" class="base">
    <img v-if="productHasImages" :src="`${API_URL}/product/images/${product.images[0].id}`" style="width: auto; height: 200px">
    <div>
      <p @click="productPage"><strong>{{ product.title }}</strong> - {{ shortDescription }}</p>
      <p><span class="price">{{ product.price.toFixed(2) }}</span>€</p>
    </div>
    <UploadImages v-if="userIsOwner" :productId="product.id" />
  </div>
</template>

<script>
import UploadImages from '@/components/UploadImages.vue';
import { API_URL } from '@/config.json';
export default {
  name: 'DisplayProduct',
  components: {
    UploadImages,
  },
  data() {
    const maxLength = 30;
    const description = this.$props.product.description;
    return {
      API_URL,
      shortDescription: description.slice(0, maxLength) + (description.length > maxLength ? '...' : ''),
      productHasAttributes: this.product.title && this.product.price && this.product.stock,
      productHasImages: this.$props.product.images.length > 0,
    };
  },
  props: {
    product: Object,
  },
  computed: {
    owner() {
      return this.$store.state.auth.seller;
    },
    userIsOwner() {
      return (
        this.owner &&
        this.$store.state.auth.seller.id == this.$props.product.seller_id
      );
    },
  },
};
</script>

<style scoped>
.base {
  border: 1px solid black;
  border-radius: 1rem;
  background-color: #eee;
  max-width: 50%;
  margin: 3.5rem auto;
}

.base > img {
  margin-top: 2rem;
}

.price {
  font-size: 30px;
  font-weight: 600;
  font-style: italic;
}
</style>
