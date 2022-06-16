<template>
  <div v-if="productHasAttributes" class="base">
    <div
      @click="productPage"
      class="mt-3 mx-3 text-violet-900 hover:text-amber-600 hover:cursor-pointer"
    >
      <div class="h-0 w-full pb-full relative mb-6">
        <div class="flex items-center justify-center">
          <img
            v-if="productHasImages"
            :src="`${API_URL}/product/images/${product.images[0].id}`"
            class="max-w-full max-h-full w-auto h-auto absolute"
          />
        </div>
      </div>
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
      default: false,
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

<style lang="postcss" scoped>
.base {
  @apply bg-white border rounded;
  @apply transition duration-500 ease-in-out hover:shadow;
}

img {
  margin-top: 100%;
}
</style>
