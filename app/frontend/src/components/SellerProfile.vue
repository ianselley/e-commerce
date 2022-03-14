<template>
  <div>
    <p>THIS SECTION IS TO DISPLAY SELLER INFORMATION</p>
    <div v-if="this.currentSeller">
      <p>Brand: {{ this.currentSeller.brand }}</p>
      <p>Items sold: {{ this.currentSeller.numberOfItemsSold }}</p>
      <p>Seller id: {{ this.currentSeller.id }}</p>
    </div>
    <div v-else>
      <button @click="this.$router.push('/signup')">
        FINISH REGISTERING AS SELLER
      </button>
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
};
</script>
