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
      <p>CART:</p>
      <div class="cart" v-if="currentBuyer.shopping_cart.length > 0">
        <DisplayCartProduct
          v-for="cartProduct in currentBuyer.shopping_cart"
          :key="cartProduct"
          :cartProduct="cartProduct"
        />
      </div>
      <div v-else>Your cart is empty</div>
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
import DisplayCartProduct from '@/components/DisplayCartProduct.vue';
export default {
  name: 'BuyerProfile',
  components: {
    RegisterAddress,
    DisplayAddress,
    DisplayCartProduct,
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

<style scoped>
.cart {
  border: 1px solid rgb(106, 90, 205);
  border-radius: 0.4rem;
  background: rgba(192, 192, 192, 0.6);
  display: inline-block;
}
</style>
