<template>
  <div>
    <div class="sticky top-48 z-50 w-56 rounded-sm bg-white p-4">
      <div class="mb-4">
        <strong>Total: </strong
        ><Price :price="cartTotal" class="inline-block" />
      </div>
      <Modal
        :key="modalKey"
        button-text="Process order"
        @click="initializeChechedIds"
        :disabled="!buyerHasAddresses || emptyCart"
        modal-class="p-12"
      >
        <div class="space-y-4">
          <div>
            <p class="mb-2">
              <strong>1. Selected address </strong>
              <button @click="toggleChangeSelectedAddress" class="ml-4">
                Change address
              </button>
            </p>
            <DisplayAddress
              v-show="!changeSelectedAddress"
              :address="selectedAddress"
              :edit="false"
            />
            <div v-show="changeSelectedAddress" class="space-y-4">
              <div
                v-for="address in addresses"
                :key="address.id"
                class="flex space-x-4"
              >
                <input
                  :id="address.id"
                  type="radio"
                  name="selectAddress"
                  :value="address.id"
                  @change="temporarySave(address.id)"
                />
                <label :for="address.id">
                  <DisplayAddress
                    :address="address"
                    :edit="false"
                    class="w-full"
                  />
                </label>
              </div>
              <button
                :disabled="loading"
                @click="saveSelectedAddress()"
                class="mt-2"
              >
                Send to selected address
              </button>
            </div>
          </div>
          <div>
            <p><strong>2. Payment method</strong></p>
            As this website doesn't actually work with real products or sellers,
            this field isn't needed. It is here just to show where it would be.
          </div>
          <div>
            <p><strong>3. Select products</strong></p>
            <div>
              Unselected products will remain in the cart and won't be delivered
            </div>
            <div
              v-for="cartProduct in shopping_cart"
              :key="cartProduct.id"
              class="flex"
            >
              <input
                v-if="
                  cartProduct.product.available &&
                  cartProduct.product.stock >= cartProduct.quantity
                "
                :id="cartProduct.id"
                type="checkbox"
                :value="cartProduct.id"
                checked
                @change="check($event, cartProduct.id)"
              />
              <label :for="cartProduct.id">
                <DisplayCartProduct
                  :cart-product="cartProduct"
                  class="w-full"
                />
              </label>
            </div>
          </div>
          <div>
            <strong>Total: </strong>
            <Price :price="selectedTotal" class="inline-block" />
          </div>
          <button :disabled="allCheckedIdsFalse" @click="orderProducts">
            Order Products
          </button>
        </div>
      </Modal>
      <div class="mt-4 text-red-800">
        <div v-if="!buyerHasAddresses">
          To be able to order some products you need to provide us at least one
          address
          <button @click="toggleAddAddress" class="mt-2">Add Address</button>
          <RegisterAddress v-if="addAddress" />
        </div>
        <div v-else-if="emptyCart">
          To be able to order some products you need to have some products in
          your cart
          <button @click="goToHome" class="mt-2">Search for products</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Modal from '@/components/Modal.vue';
import Price from '@/components/Price.vue';
import DisplayAddress from '@/components/DisplayAddress.vue';
import RegisterAddress from '@/components/RegisterAddress.vue';
import DisplayCartProduct from '@/components/DisplayCartProduct.vue';
export default {
  name: 'OrderProducts',
  components: {
    Modal,
    Price,
    DisplayAddress,
    RegisterAddress,
    DisplayCartProduct,
  },
  data() {
    return {
      loading: false,
      addAddress: false,
      modalKey: 0,
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
      return (
        (this.currentBuyer &&
          this.currentBuyer.shopping_cart.slice().reverse()) ||
        []
      );
    },
    emptyCart() {
      return this.shopping_cart.length == 0;
    },
    cartTotal() {
      if (this.emptyCart) {
        return 0;
      }
      return this.shopping_cart.reduce((prev, curr) => {
        return (
          prev +
          curr.quantity *
            curr.product.price *
            (curr.product.available && curr.product.stock >= curr.quantity
              ? 1
              : 0)
        );
      }, 0);
    },
    selectedTotal() {
      return this.shopping_cart.reduce((prev, curr) => {
        return (
          prev +
          curr.quantity *
            curr.product.price *
            (this.checkedIds[curr.id] && curr.product.available ? 1 : 0)
        );
      }, 0);
    },
    buyerHasAddresses() {
      return this.currentBuyer && this.currentBuyer.addresses.length > 0;
    },
    mainAddress() {
      const main_address_id = this.currentBuyer.main_address_id;
      if (!main_address_id) {
        return this.addresses[0];
      }
      return this.addresses.find((address) => address.id == main_address_id);
    },
    addresses() {
      return this.currentBuyer.addresses;
    },
    selectedAddress() {
      if (this.selectedAddressId == undefined) {
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
        if (
          cartProduct.product.available &&
          cartProduct.product.stock >= cartProduct.quantity
        ) {
          this.checkedIds[cartProduct.id] = true;
        }
      }
    },
    check(e, id) {
      this.checkedIds[id] = e.target.checked;
    },
    orderProducts() {
      this.modalKey++;
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
label {
  @apply text-black;
}
</style>
