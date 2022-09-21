<template>
  <div class="flex flex-col items-center">
    <div
      class="p-8 grid grid-cols-3 lg:grid-cols-4 w-full max-w-screen-xl gap-x-4 gap-y-6"
    >
      <DisplayProduct
        v-for="product in searchedProducts"
        :key="product"
        :product="product"
      />
    </div>
    <FooterPages />
  </div>
</template>

<script>
import FooterPages from '@/components/FooterPages.vue';
import DisplayProduct from '@/components/DisplayProduct.vue';
export default {
  name: 'Home',
  components: {
    FooterPages,
    DisplayProduct,
  },
  computed: {
    searchedProducts() {
      return this.$store.state.product.searchedProducts;
    },
    productsPerPage() {
      return this.$store.state.product.productsPerPage;
    },
    currentPage() {
      return this.$store.state.product.currentPage;
    },
  },
  methods: {
    getAllProducts() {
      this.$store.dispatch('product/getSearchedProducts').catch((error) => {
        this.$store.dispatch('alert/setMessage', error);
      });
    },
  },
  created() {
    this.getAllProducts();
  },
};
</script>

<style lang="postcss" scoped></style>
