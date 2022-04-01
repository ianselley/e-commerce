<template>
  <div v-if="product">
    <DisplayImages :images="product.images" />
  </div>
</template>

<script>
import DisplayImages from '@/components/DisplayImages.vue';
export default {
  name: 'Product',
  components: {
    DisplayImages,
  },
  data() {
    return {
      loading: false,
      productId: this.$route.params.id,
    };
  },
  computed: {
    product() {
      return this.$store.state.product.product;
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
