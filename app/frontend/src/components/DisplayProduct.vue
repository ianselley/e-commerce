<template>
  <div v-if="hasAttributes" class="base">
    <div>
      <p>TITLE: {{ product.title }}</p>
      <p>DESCRIPTION: {{ product.description }}</p>
      <p>PRICE: {{ product.price }}</p>
      <p>STOCK: {{ product.stock }}</p>
      <p>SPECIFICATIONS: {{ product.specifications }}</p>
    </div>
    <UploadImages :productId="product.id" />
  </div>
</template>

<script>
import UploadImages from '@/components/UploadImages.vue';
export default {
  name: 'DisplayProduct',
  components: { 
    UploadImages,
  },
  props: {
    product: Object,
  },
  computed: {
    hasAttributes() {
      return this.product.title && this.product.price && this.product.stock;
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
</style>
