<template>
  <div>
    <button @click="uploadProductFunction()">UPLOAD PRODUCT</button>
    <UploadProduct v-if="uploadProduct" />
    <DisplayProduct
      v-for="product in sellerProducts"
      :key="product"
      :product="product"
      :edit="true"
    />
  </div>
</template>

<script>
import UploadProduct from '@/components/UploadProduct.vue';
import DisplayProduct from '@/components/DisplayProduct.vue';
export default {
  name: 'Products',
  components: {
    UploadProduct,
    DisplayProduct,
  },
  data() {
    return {
      uploadProduct: false,
    };
  },
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
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
    } else if (!this.currentSeller) {
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
  methods: {
    uploadProductFunction() {
      this.uploadProduct = !this.uploadProduct;
    },
  },
};
</script>

<style lang="postcss" scoped></style>
