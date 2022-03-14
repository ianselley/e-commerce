<template>
  <div>
    <p>THIS SECTION IS TO DISPLAY BUYER INFORMATION</p>
    <div v-if="!currentBuyer">
      <button @click="this.$router.push('/signup')">
        FINISH REGISTERING AS BUYER
      </button>
    </div>
    <div v-else>
      <p>Name: {{ currentBuyer.name }}</p>
      <p>Surname: {{ currentBuyer.surname }}</p>
      <p>Buyer: {{ currentBuyer }}</p>
      <DisplayAddress v-for="address in currentBuyer.addresses" :key="address" :address="address" />
      <button @click="addAddressFunction()">Add Address</button>
      <RegisterAddress v-if="addAddress && !$store.state.auth.addedAddress"/>
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
