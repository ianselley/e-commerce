<template>
  <div>
    <p>THIS SECTION IS TO DISPLAY SELLER INFORMATION</p>
    <div v-if="!currentSeller">
      <button @click="this.$router.push('/signup')">
        FINISH REGISTERING AS SELLER
      </button>
    </div>
    <div v-else>
      <p>Brand: {{ currentSeller.brand }}</p>
      <p>Products sold: {{ currentSeller.numberOfProductsSold }}</p>
      <p>Seller id: {{ currentSeller.id }}</p>
      <button @click="uploadProduct()">UPLOAD PRODUCT</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SellerProfile',
  computed: {
    currentSeller() {
      return this.$store.state.auth.user.seller;
    },
  },
  methods: {
    uploadProduct() {

    }
  },
};
</script>
