<template>
  <div class="flex justify-center w-full">
    <input
      @keyup.enter="search"
      ref="search"
      type="text"
      placeholder="Search products..."
    />
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  computed: {
    productsPerPage() {
      return this.$store.state.product.productsPerPage;
    },
    currentPage() {
      return this.$store.state.product.currentPage;
    },
  },
  methods: {
    search() {
      const search = this.$refs.search.value;
      this.$store.commit('product/setSubstring', search);
      this.$store.dispatch('product/getSearchedProducts').catch((error) => {
        this.$store.dispatch('alert/setMessage', error);
      });
    },
  },
};
</script>

<style lang="postcss" scoped>
input {
  width: 100%;
  max-width: 500px;
  padding: 10px 45px;
  background: white url('../assets/search-icon.svg') no-repeat 15px center;
  background-size: 15px 15px;
  font-size: 16px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
  @apply block mx-8 border-0 rounded-md;
}
</style>
