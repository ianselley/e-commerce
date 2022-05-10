<template>
  <div>
    <button v-if="!currentBuyer" @click="this.$router.push('/signup')">
      FINISH REGISTERING AS BUYER
    </button>
    <div v-else>
      <p><strong>Name:</strong> {{ currentBuyer.name }}</p>
      <OrderProducts />
      <p><strong>CART:</strong></p>
      <div class="cart" v-if="!cartIsEmpty">
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
      <br />
      <button @click="addAddressFunction">Add Address</button>
      <RegisterAddress v-if="addAddress && !$store.state.auth.addedAddress" />
      <div style="margin-top: 1.5rem"><strong>ORDERS:</strong></div>
      <DisplayOrders />
    </div>
  </div>
</template>

<script>
import OrderProducts from '@/components/OrderProducts.vue';
import DisplayOrders from '@/components/DisplayOrders.vue';
import DisplayAddress from '@/components/DisplayAddress.vue';
import RegisterAddress from '@/components/RegisterAddress.vue';
import DisplayCartProduct from '@/components/DisplayCartProduct.vue';
export default {
  name: 'BuyerProfile',
  components: {
    OrderProducts,
    DisplayOrders,
    DisplayAddress,
    RegisterAddress,
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
    cartIsEmpty() {
      return this.currentBuyer.shopping_cart.length == 0;
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
