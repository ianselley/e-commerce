<template>
  <div
    class="p-8 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 max-w-screen-xl gap-x-4 gap-y-6"
  >
    <DisplayProduct
      v-for="product in allProducts"
      :key="product"
      :product="product"
    />
  </div>
</template>

<script>
import DisplayProduct from '@/components/DisplayProduct.vue';
export default {
  name: 'Home',
  components: {
    DisplayProduct,
  },
  data() {
    return {
      allProducts: [],
    };
  },
  methods: {
    getAllProducts() {
      this.$store
        .dispatch('product/getAllProducts')
        .then((response) => {
          this.allProducts = response;
        })
        .catch((error) => {
          this.$store.commit('alert/setMessage', error);
        });
    },
  },
  created() {
    this.getAllProducts();
  },
};
</script>

<style lang="postcss" scoped>
.max-w-screen-xl {
  max-width: 1280px;
  @apply mx-auto;
}
</style>
