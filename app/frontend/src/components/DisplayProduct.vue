<template>
  <div v-if="productHasAttributes" class="base">
    <div @click="productPage" class="mt-3 mx-3 text-violet-900 link">
      <div class="h-0 w-full pb-full relative mb-6">
        <div class="flex items-center justify-center">
          <Image
            v-if="productHasImages"
            :src="product.images[0].id"
            class="image"
          />
        </div>
      </div>
      <p class="two-lines overflow-hidden">
        <strong>{{ product.title }}</strong>
        <span v-if="product.description"> - {{ product.description }}</span>
      </p>
    </div>
    <div class="mt-4 flex justify-around items-center">
      <Price :price="product.price" :available="product.available" />
      <span v-if="userIsOwner && edit">
        Stock: <strong>{{ product.stock }}</strong>
      </span>
    </div>
    <div
      v-if="userIsOwner && edit"
      class="mt-3 flex justify-around items-center"
    >
      <div>
        Money made:
        <strong>{{ commafy(product.money_made.toFixed(2)) }}</strong> €
      </div>
      <div>
        Items sold: <strong>{{ commafy(product.items_sold) }}</strong>
      </div>
    </div>
    <div
      v-if="userIsOwner && edit"
      class="mt-6 flex flex-col justify-items-stretch space-y-3"
    >
      <ChangeProductAvailability
        :productId="product.id"
        :available="product.available"
      />
      <EditProduct :product="product" />
      <DeleteImages :productId="product.id" :images="product.images" />
      <UploadImages :productId="product.id" />
    </div>
  </div>
</template>

<script>
import Image from '@/components/Image.vue';
import Price from '@/components/Price.vue';
import EditProduct from '@/components/EditProduct.vue';
import UploadImages from '@/components/UploadImages.vue';
import DeleteImages from '@/components/DeleteImages.vue';
import ChangeProductAvailability from '@/components/ChangeProductAvailability.vue';
export default {
  name: 'DisplayProduct',
  components: {
    Image,
    Price,
    EditProduct,
    UploadImages,
    DeleteImages,
    ChangeProductAvailability,
  },
  props: {
    product: Object,
    edit: {
      default: false,
    },
  },
  data() {
    return {
      productHasAttributes:
        this.product.title && this.product.price && this.product.stock,
    };
  },
  computed: {
    owner() {
      return this.$store.state.auth.seller;
    },
    userIsOwner() {
      return this.owner && this.owner.id == this.$props.product.seller_id;
    },
    productHasImages() {
      return this.$props.product.images.length > 0;
    },
  },
  methods: {
    productPage() {
      this.$router.push(`/product/${this.product.id}`);
    },
    commafy(x) {
      return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    },
  },
};
</script>

<style lang="postcss" scoped>
.base {
  @apply bg-white border rounded p-6;
  @apply transition duration-500 ease-in-out hover:shadow;
}

.image {
  margin-top: 100%;
  max-width: 100%;
  @apply absolute max-h-full w-auto h-auto;
}

.two-lines {
  height: 3rem;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}
</style>
