<template>
  <div>
    <p>THIS SECTION IS TO DISPLAY BUYER INFORMATION</p>
    <div v-if="this.currentBuyer">
      <p>Name: {{ this.currentBuyer.name }}</p>
      <p>Surname: {{ this.currentBuyer.surname }}</p>
      <p>Buyer: {{ this.currentBuyer }}</p>
      <DisplayAddress v-for="address in this.currentBuyer.addresses" v-bind:key="address" :address="address" />
      <button @click="addAddressFunction()">Add Address</button>
      <RegisterAddress v-if="addAddress && !this.$store.state.auth.addedAddress"/>
    </div>
    <div v-else>
      <button @click="this.$router.push('/signup')">
        FINISH REGISTERING AS BUYER
      </button>
    </div>
  </div>
</template>

<script>
import DisplayAddress from '@/components/DisplayAddress.vue';
import RegisterAddress from '@/components/RegisterAddress.vue';
export default {
  name: 'BuyerProfile',
  components: { RegisterAddress, DisplayAddress },
  data() {
    return {
      addAddress: false,
      addressesLength: this.$store.state.auth.user.buyer.addresses.length,
    }
  },
  computed: {
    currentBuyer() {
      return this.$store.state.auth.user.buyer;
    },
  },
  methods: {
    addAddressFunction() {
      this.addAddress = true;
      this.$store.commit('auth/resetAddedAddress');
    }
  },
};
</script>
