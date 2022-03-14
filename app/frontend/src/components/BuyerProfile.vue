<template>
  <div>
    <p>THIS SECTION IS TO DISPLAY BUYER INFORMATION</p>
    <div v-if="this.currentBuyer">
      <p>Name: {{ this.currentBuyer.name }}</p>
      <p>Surname: {{ this.currentBuyer.surname }}</p>
      <p>Addresses: {{ this.currentBuyer.addresses }}</p>
      <p>Buyer: {{ this.currentBuyer }}</p>
    </div>
    <div v-else>
      <button @click="this.$router.push('/signup')">
        FINISH REGISTERING AS BUYER
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BuyerProfile',
  computed: {
    currentBuyer() {
      return this.$store.state.auth.user.buyer;
    },
  },
};
</script>
