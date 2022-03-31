<template>
  <div>
    <p>HERE ARE ALL THE PRODUCTS DISPLAYED</p>
    <DisplayProduct
      v-for="product in products"
      :key="product"
      :product="product"
    />
  </div>
</template>

<script>
import DisplayProduct from '@/components/DisplayProduct.vue';
export default {
  name: 'HelloWorld',
  components: {
    DisplayProduct,
  },
  data() {
    return {
      products: [],
    };
  },
  methods: {
    getProducts() {
      this.$store
        .dispatch('product/getProducts')
        .then((response) => {
          this.products = response;
        })
        .catch((error) => {
          this.$store.commit('alert/setMessage', error);
        });
    },
  },

  created() {
    this.getProducts();
  },
};
</script>

<style scoped></style>
