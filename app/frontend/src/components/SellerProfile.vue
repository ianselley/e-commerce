<template>
  <div>
    <p><strong>THIS SECTION DISPLAYS THE SELLER INFORMATION</strong></p>
    <div v-if="!currentSeller">
      <button @click="this.$router.push('/signup')">
        FINISH REGISTERING AS SELLER
      </button>
    </div>
    <div v-else>
      <p>Brand: {{ currentSeller.brand }}</p>
      <p>Products sold: {{ currentSeller.number_of_products_sold }}</p>
      <p>Seller id: {{ currentSeller.id }}</p>
      <DisplayProduct
        v-for="product in sellerProducts"
        :key="product"
        :product="product"
      />
      <button @click="uploadProductFunction()">UPLOAD PRODUCT</button>
      <UploadProduct v-if="uploadProduct" />
    </div>
  </div>
</template>

<script>
import UploadProduct from '@/components/UploadProduct.vue';
import DisplayProduct from '@/components/DisplayProduct.vue';
export default {
  name: 'SellerProfile',
  components: {
    UploadProduct,
    DisplayProduct,
  },
  data() {
    return {
      uploadProduct: false,
    };
  },
  computed: {
    currentSeller() {
      return this.$store.state.auth.seller;
    },
    sellerProducts() {
      return this.$store.state.product.sellerProducts;
    },
  },
  methods: {
    uploadProductFunction() {
      this.uploadProduct = !this.uploadProduct;
    },
  },
};
</script>
