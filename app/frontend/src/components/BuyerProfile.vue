<template>
  <div>
    <DisplayAddress
      v-for="address in currentBuyer.addresses"
      :key="address"
      :address="address"
    />
    <br />
    <button @click="addAddressFunction">Add Address</button>
    <RegisterAddress v-if="addAddress && !$store.state.auth.addedAddress" />
  </div>
</template>

<script>
import DisplayAddress from '@/components/DisplayAddress.vue';
import RegisterAddress from '@/components/RegisterAddress.vue';
export default {
  name: 'BuyerProfile',
  components: {
    DisplayAddress,
    RegisterAddress,
  },
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

<style lang="postcss" scoped></style>
