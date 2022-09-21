<template>
  <div class="mx-6">
    <div class="main-title">CART</div>
    <div class="flex flex-row">
      <div v-if="!cartIsEmpty" class="w-full space-y-4">
        <DisplayCartProduct
          v-for="cartProduct in shoppingCart"
          :key="cartProduct"
          :cartProduct="cartProduct"
          class="m-auto"
        />
      </div>
      <div v-else class="mx-auto my-20">Your cart is empty</div>
      <OrderProducts />
    </div>
  </div>
</template>

<script>
import OrderProducts from '@/components/OrderProducts.vue';
import DisplayCartProduct from '@/components/DisplayCartProduct.vue';
export default {
  name: 'Cart',
  components: {
    OrderProducts,
    DisplayCartProduct,
  },
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    },
    userIsBuyer() {
      return this.$store.state.auth.loggedInAs == 'buyer';
    },
    currentBuyer() {
      return this.$store.state.auth.buyer;
    },
    shoppingCart() {
      return (
        (this.currentBuyer &&
          this.currentBuyer.shopping_cart.slice().reverse()) ||
        []
      );
    },
    cartIsEmpty() {
      return this.shoppingCart.length == 0;
    },
  },
  created() {
    if (!this.currentUser) {
      this.$router.push('/login');
      this.$store.dispatch('alert/setMessage', 'You are not logged in');
    } else if (!this.userIsBuyer) {
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
};
</script>

<style lang="postcss" scoped></style>
