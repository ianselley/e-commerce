<template>
  <div>
    <p>HERE ARE ALL THE PRODUCTS DISPLAYED</p>
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
  name: 'DisplayAllProducts',
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

<style scoped></style>
