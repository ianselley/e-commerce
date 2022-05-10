<template>
  <div v-if="productHasAttributes" class="base">
    <div @click="productPage" class="link">
      <img
        v-if="productHasImages"
        :src="`${API_URL}/product/images/${product.images[0].id}`"
        style="width: auto; height: 200px"
      />
      <p>
        <strong>{{ product.title }}</strong>
        <span v-if="product.description"> - {{ shortDescription }}</span>
      </p>
    </div>
    <p>
      <Price :price="product.price" :available="product.available" />
    </p>
    <div v-if="userIsOwner && edit">
      <ChangeProductAvailability
        :productId="product.id"
        :available="product.available"
      />
      <EditProduct :product="product" />
      <UploadImages :productId="product.id" />
      <DeleteImages :productId="product.id" :images="product.images" />
    </div>
  </div>
</template>

<script>
import ChangeProductAvailability from '@/components/ChangeProductAvailability.vue';
import UploadImages from '@/components/UploadImages.vue';
import DeleteImages from '@/components/DeleteImages.vue';
import EditProduct from '@/components/EditProduct.vue';
import Price from '@/components/Price.vue';
import { API_URL } from '@/config.json';
export default {
  name: 'DisplayProduct',
  components: {
    ChangeProductAvailability,
    UploadImages,
    DeleteImages,
    EditProduct,
    Price,
  },
  props: {
    product: Object,
    edit: {
      default: true,
    },
  },
  data() {
    const maxLength = 30;
    const description = this.$props.product.description;
    return {
      API_URL,
      shortDescription:
        description.slice(0, maxLength) +
        (description.length > maxLength ? '...' : ''),
      productHasAttributes:
        this.product.title && this.product.price && this.product.stock,
    };
  },
  computed: {
    owner() {
      return this.$store.state.auth.seller;
    },
    userIsOwner() {
      return (
        this.owner &&
        this.$store.state.auth.seller.id == this.$props.product.seller_id
      );
    },
    productHasImages() {
      return this.$props.product.images.length > 0;
    },
  },
  methods: {
    productPage() {
      this.$router.push(`/product/${this.product.id}`);
    },
  },
};
</script>

<style scoped>
.base {
  border: 1px solid black;
  border-radius: 1rem;
  background-color: #eee;
  max-width: 50%;
  min-width: fit-content;
  margin: 3.5rem auto;
}

.base > img {
  margin: 2rem 2rem 0;
}

.link {
  margin: 2rem 2rem 0;
}

.link:hover {
  text-decoration: underline;
  color: rgb(46, 56, 122);
  cursor: pointer;
}
</style>
