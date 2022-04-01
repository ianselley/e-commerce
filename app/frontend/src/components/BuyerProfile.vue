<template>
  <div>
    <p><strong>THIS SECTION DISPLAYS THE BUYER INFORMATION</strong></p>
    <div v-if="!currentBuyer">
      <button @click="this.$router.push('/signup')">
        FINISH REGISTERING AS BUYER
      </button>
    </div>
    <div v-else>
      <p>Name: {{ currentBuyer.name }}</p>
      <p>Surname: {{ currentBuyer.surname }}</p>
      <p>Buyer id: {{ currentBuyer.id }}</p>
      <DisplayAddress
        v-for="address in currentBuyer.addresses"
        :key="address"
        :address="address"
      />
      <button @click="addAddressFunction()">Add Address</button>
      <RegisterAddress v-if="addAddress && !$store.state.auth.addedAddress" />
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
    };
  },
  computed: {
    currentBuyer() {
      return this.$store.state.auth.buyer;
    },
  },
  methods: {
    addAddressFunction() {
      this.addAddress = !this.addAddress;
      this.$store.commit('auth/resetAddedAddress');
    },
  },
};
</script>
