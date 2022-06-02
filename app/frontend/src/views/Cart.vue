<template>
  <div class="flex flex-row-reverse">
    <OrderProducts />
    <p><strong>CART:</strong></p>
    <div class="cart" v-if="!cartIsEmpty">
      <DisplayCartProduct
        v-for="cartProduct in shopping_cart"
        :key="cartProduct"
        :cartProduct="cartProduct"
      />
    </div>
    <div v-else>Your cart is empty</div>
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
    currentBuyer() {
      return this.$store.state.auth.buyer;
    },
    shopping_cart() {
      return (this.currentBuyer && this.currentBuyer.shopping_cart) || [];
    },
    cartIsEmpty() {
      return this.shopping_cart.length == 0;
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
};
</script>

<style lang="postcss" scoped>
.cart {
  border: 1px solid rgb(106, 90, 205);
  border-radius: 0.4rem;
  background: rgba(192, 192, 192, 0.6);
  display: inline-block;
}
</style>
