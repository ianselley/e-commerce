<template>
  <div class="flex justify-center items-center space-x-2">
    <button @click="movePage(-5)">&lsaquo;&lsaquo;5</button>
    <button @click="movePage(-1)">&lsaquo;1</button>
    <div>{{ currentPage }} / {{ totalPages }}</div>
    <button @click="movePage(1)">1&rsaquo;</button>
    <button @click="movePage(5)">5&rsaquo;&rsaquo;</button>
  </div>
</template>

<script>
export default {
  name: 'FooterPages',
  computed: {
    currentPage() {
      return this.$store.state.product.currentPage;
    },
    totalPages() {
      return this.$store.state.product.totalPages;
    },
  },
  methods: {
    movePage(number) {
      this.$store.commit('product/movePage', number);
      this.$store.dispatch('product/getSearchedProducts').catch((error) => {
        this.$store.dispatch('alert/setMessage', error);
      });
    },
  },
};
</script>

<style lang="postcss" scoped></style>
