<template>
  <div>
    <Modal button-text="UPLOAD PRODUCT">
      <UploadProduct />
    </Modal>
    <div
      class="p-8 grid grid-cols-3 2xl:grid-cols-4 max-w-screen-xl gap-x-4 gap-y-6"
    >
      <DisplayProduct
        v-for="product in sellerProducts"
        :key="product"
        :product="product"
        :edit="true"
      />
    </div>
  </div>
</template>

<script>
import Modal from '@/components/Modal.vue';
import UploadProduct from '@/components/UploadProduct.vue';
import DisplayProduct from '@/components/DisplayProduct.vue';
export default {
  name: 'Products',
  components: {
    Modal,
    UploadProduct,
    DisplayProduct,
  },
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    },
    userIsSeller() {
      return this.$store.state.auth.loggedInAs == 'seller';
    },
    sellerProducts() {
      return this.$store.state.product.sellerProducts;
    },
    currentSeller() {
      return this.$store.state.auth.seller;
    },
  },
  created() {
    if (!this.currentUser) {
      this.$router.push('/login');
      this.$store.dispatch('alert/setMessage', 'You are not logged in');
    } else if (!this.userIsSeller) {
      this.$router.push('/profile');
      this.$store.dispatch(
        'alert/setMessage',
        'Only sellers can view their uploaded products'
      );
    } else {
      this.$store
        .dispatch('auth/getUser')
        .then(() => {
          return this.$store.dispatch(
            'product/getSellerProducts',
            this.currentSeller.id
          );
        })
        .catch((error) => {
          this.$store.dispatch('alert/setMessage', error);
        });
    }
  },
};
</script>

<style lang="postcss" scoped></style>
