<template>
  <div>
    <div v-if="!currentSeller">
      <button @click="this.$router.push('/signup')">
        FINISH REGISTERING AS SELLER
      </button>
    </div>
    <div v-else>
      <p>Products sold: {{ currentSeller.number_of_products_sold }}</p>
      <DisplayProduct
        v-for="product in sellerProducts"
        :key="product"
        :product="product"
      />
      <button @click="uploadProductFunction()">UPLOAD PRODUCT</button>
      <UploadProduct v-if="uploadProduct" />
      <div style="margin-top: 1.5rem"><strong>ORDERS:</strong></div>
      <DisplayOrders />
    </div>
  </div>
</template>

<script>
import UploadProduct from '@/components/UploadProduct.vue';
import DisplayProduct from '@/components/DisplayProduct.vue';
import DisplayOrders from '@/components/DisplayOrders.vue';
export default {
  name: 'SellerProfile',
  components: {
    UploadProduct,
    DisplayProduct,
    DisplayOrders,
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
