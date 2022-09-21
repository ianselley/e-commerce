<template>
  <div v-if="productHasAttributes" class="base">
    <div @click="productPage" class="mt-3 mx-3 text-violet-900 link">
      <div class="h-0 w-full pb-full relative mb-6">
        <div class="flex items-center justify-center">
          <Image
            v-if="productHasImages"
            :src="product.images[0].id"
            :alt="product.images[0].filename"
            class="image"
          />
        </div>
      </div>
      <p class="one-line overflow-hidden mb-4">
        <strong>{{ product.title }}</strong>
      </p>
    </div>
    <div class="mt-4 flex justify-around items-center">
      <Price :price="product.price" :available="product.available" />
      <span v-if="userIsOwner && edit" class="text-xs">
        Stock: <strong>{{ product.stock }}</strong>
      </span>
    </div>
    <div
      v-if="userIsOwner && edit"
      class="mt-3 flex justify-around items-center text-xs"
    >
      <div>
        Money made:
        <strong>{{ commafy(product.money_made.toFixed(2)) }}</strong
        >€
      </div>
      <div>
        Items sold: <strong>{{ commafy(product.items_sold) }}</strong>
      </div>
    </div>
    <div
      v-if="userIsOwner && edit"
      class="mt-6 flex flex-col justify-items-stretch space-y-3"
    >
      <button
        :disabled="loadingAvailability || !productHasImages"
        @click="changeProductAvailability"
        class="w-full paddingx-4px"
        :title="
          !productHasImages
            ? 'To be able to change the availability of the product, you need to upload at least one image'
            : ''
        "
      >
        Make product <span v-if="available">un</span>available
      </button>
      <EditProduct :product="product" />
      <DeleteImages :productId="product.id" :images="product.images" />
      <UploadImagesButton :productId="product.id" />
    </div>
  </div>
</template>

<script>
import Image from '@/components/Image.vue';
import Price from '@/components/Price.vue';
import EditProduct from '@/components/EditProduct.vue';
import DeleteImages from '@/components/DeleteImages.vue';
import UploadImagesButton from './UploadImagesButton.vue';
export default {
  name: 'DisplayProduct',
  components: {
    Image,
    Price,
    EditProduct,
    DeleteImages,
    UploadImagesButton,
  },
  props: {
    product: Object,
    edit: {
      default: false,
    },
    available: Boolean,
  },
  data() {
    return {
      loadingAvailability: false,
      productHasAttributes:
        this.product.title &&
        this.product.price !== null &&
        this.product.stock !== null,
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
    changeProductAvailability() {
      if (!this.productHasImages) {
        this.$store.dispatch('alert/setMessage', 'You need at least one image');
        return;
      }
      this.loadingAvailability = true;
      this.$store
        .dispatch('product/changeProductAvailability', this.$props.product.id)
        .then(() => {
          this.loadingAvailability = false;
        })
        .catch((error) => {
          this.$store.dispatch('alert/setMessage', error);
          this.loadingAvailability = false;
        });
    },
  },
};
</script>

<style lang="postcss" scoped>
.base {
  @apply bg-white border rounded p-3 pb-6;
  @apply transition duration-500 ease-in-out hover:shadow;
}

.image {
  margin-top: 100%;
  max-width: 100%;
  @apply absolute max-h-full w-auto h-auto;
}

.paddingx-4px {
  padding-left: 4px;
  padding-right: 4px;
}

.one-line {
  height: 1.5rem;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
}
</style>
