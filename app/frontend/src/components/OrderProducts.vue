<template>
  <div>
    <div class="process-order">
      <strong>TOTAL:</strong> {{ cartTotal }} €
      <button
        :disabled="!buyerHasAddresses || emptyCart"
        @click="activateModal"
      >
        Process order
      </button>
      <div v-if="emptyCart">
        To be able to order some products you need to have some products in your
        cart
        <button @click="goToHome">Search for products</button>
      </div>
      <div v-else-if="!buyerHasAddresses">
        To be able to order some products you need to provide us at least one
        address
        <button @click="toggleAddAddress">Add Address</button>
        <RegisterAddress v-if="addAddress" />
      </div>
    </div>
    <Modal>
      <p>
        <strong>1. Selected address </strong
        ><button @click="toggleChangeSelectedAddress">Change address</button>
      </p>
      <DisplayAddress
        v-show="!changeSelectedAddress"
        :address="selectedAddress"
        :edit="false"
      />
      <div v-show="changeSelectedAddress">
        <div v-for="address in addresses" :key="address">
          <input
            type="radio"
            name="selectAddress"
            :value="address.id"
            @change="temporarySave(address.id)"
          />
          <DisplayAddress :address="address" :edit="false" />
        </div>
        <button
          :disabled="loading"
          @click="saveSelectedAddress(temporaryAddressId)"
        >
          Send to this address
        </button>
      </div>
      <p><strong>2. Payment method</strong></p>
      As this website doesn't actually work with real products or sellers, this
      field isn't needed
      <p><strong>3. Select products</strong></p>
      <div v-for="cartProduct in shopping_cart" :key="cartProduct">
        <input
          type="checkbox"
          :value="cartProduct.id"
          checked
          @change="check($event, cartProduct.id)"
        />
        <DisplayProduct :product="cartProduct.product" />
      </div>
      <button :disabled="allCheckedIdsFalse" @click="orderProducts">
        Order Products
      </button>
    </Modal>
  </div>
</template>

<script>
import Modal from '@/components/Modal.vue';
import RegisterAddress from '@/components/RegisterAddress.vue';
import DisplayAddress from '@/components/DisplayAddress.vue';
import DisplayProduct from '@/components/DisplayProduct.vue';
export default {
  name: 'OrderProducts',
  components: {
    Modal,
    RegisterAddress,
    DisplayAddress,
    DisplayProduct,
  },
  data() {
    return {
      loading: false,
      addAddress: false,
      processOrder: false,
      checkedIds: {},
      selectedAddressId: undefined,
      changeSelectedAddress: false,
      temporarySelectedAddressId: undefined,
    };
  },
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    },
    currentBuyer() {
      return this.$store.state.auth.buyer;
    },
    shopping_cart() {
      return (this.currentBuyer && this.currentBuyer.shopping_cart) || [];
    },
    emptyCart() {
      return this.shopping_cart.length == 0;
    },
    cartTotal() {
      if (this.emptyCart) {
        return 0;
      }
      return this.currentBuyer.shopping_cart.reduce((prev, curr) => {
        return prev + curr.quantity * curr.product.price;
      }, 0);
    },
    buyerHasAddresses() {
      return this.currentBuyer && this.currentBuyer.addresses.length > 0;
    },
    mainAddress() {
      const main_address_id = this.currentBuyer.main_address_id;
      return this.addresses.find((address) => address.id == main_address_id);
    },
    addresses() {
      return this.currentBuyer.addresses;
    },
    selectedAddress() {
      if (this.selectedAddressId == null) {
        return this.mainAddress;
      }
      return this.addresses.find(
        (address) => address.id == this.selectedAddressId
      );
    },
    allCheckedIdsFalse() {
      if (Object.keys(this.checkedIds).length === 0) return true;
      for (let [, value] of Object.entries(this.checkedIds)) {
        if (value == true) return false;
      }
      return true;
    },
  },
  created() {
    if (!this.currentUser) {
      this.$router.push('/login');
      this.$store.dispatch('alert/setMessage', 'You are not logged in');
    } else if (!this.currentBuyer) {
      this.$router.push('/profile');
      this.$store.dispatch(
        'alert/setMessage',
        'Only buyers can view their shopping cart'
      );
    } else {
      this.$store.dispatch('auth/getUser').catch((error) => {
        this.$store.dispatch('alert/setMessage', error);
      });
    }
  },
  methods: {
    goToHome() {
      this.$router.push('/');
    },
    activateModal() {
      this.initializeChechedIds();
      this.$store.commit('modal/activateModal');
    },
    toggleAddAddress() {
      this.addAddress = !this.addAddress;
    },
    toggleChangeSelectedAddress() {
      this.changeSelectedAddress = !this.changeSelectedAddress;
    },
    temporarySave(id) {
      this.temporarySelectedAddressId = id;
    },
    saveSelectedAddress() {
      this.selectedAddressId = this.temporarySelectedAddressId;
      this.toggleChangeSelectedAddress();
    },
    initializeChechedIds() {
      this.checkedIds = {};
      for (let cartProduct of this.shopping_cart) {
        this.checkedIds[cartProduct.id] = true;
      }
    },
    check(e, id) {
      this.checkedIds[id] = e.target.checked;
    },
    orderProducts() {
      if (this.allCheckedIdsFalse) {
        this.$store.dispatch(
          'alert/setMessage',
          'You need to select at least one product'
        );
        return;
      }
      this.loading = true;
      const cartProductIdsList = [];
      for (let [id, checked] of Object.entries(this.checkedIds)) {
        if (checked) {
          cartProductIdsList.push(id);
        }
      }
      const cartProductIds = cartProductIdsList.join(',');
      const addressId = this.selectedAddressId || this.mainAddress.id;
      this.$store
        .dispatch('order/orderProducts', { addressId, cartProductIds })
        .then(() => {
          this.$store.commit('modal/activateModal');
          this.loading = false;
        })
        .catch((error) => {
          this.$store.dispatch('alert/setMessage', error);
          this.loading = false;
        });
    },
  },
};
</script>

<style lang="postcss" scoped>
.process-order {
  background-color: azure;
  border: 1px solid black;
  border-radius: 4px;
  margin: 0.5rem 0;
  padding: 0.6rem;
  display: inline-block;
}
</style>
