<template>
  <div class="bg-white rounded-sm w-3/4 p-4 flex flex-row">
    <div
      @click.stop
      @click="productPage"
      class="min-w-40 w-40 h-40 flex justify-center items-center image-link"
    >
      <Image
        v-if="productHasImages"
        :src="image.id"
        :alt="image.filename"
        class="max-w-full max-h-full w-auto h-auto"
      />
    </div>
    <div class="flex flex-col justify-between ml-6 left-content">
      <div @click.stop @click="productPage" class="two-lines text-left link">
        {{ product.title }} - {{ product.description }}
      </div>
      <div class="flex items-center">
        <div v-if="productAvailable" class="pr-1">Price:</div>
        <Price
          :price="product.price"
          :available="productAvailable"
          class="inline-block"
        />
        <span
          v-if="multipleProducts && productAvailable"
          class="ml-4 text-xxs text-amber-900"
        >
          ({{ product.price }}€ x {{ cartProduct.quantity }} =
          {{ commafy(product.price * cartProduct.quantity) }}€)
        </span>
      </div>
      <div class="flex justify-between items-center">
        <div class="w-max">
          Quantity:
          <select
            v-if="product.stock > 0"
            ref="quantity"
            @click.stop
            @change="changeQuantity"
            :disabled="loading"
            class="text-center"
          >
            <option
              v-for="quantity in maxProducts"
              :key="quantity"
              :selected="quantity == cartProduct.quantity"
              :value="quantity"
            >
              {{ quantity }}
            </option>
          </select>
          <span v-else>0</span>
        </div>
        <button
          class="ml-12"
          @click.stop
          @click="removeFromCart"
          :disabled="loading"
        >
          Remove
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import Image from '@/components/Image.vue';
import Price from '@/components/Price.vue';
export default {
  name: 'DisplayCartProduct',
  components: {
    Image,
    Price,
  },
  props: {
    cartProduct: Object,
  },
  data() {
    return {
      loading: false,
    };
  },
  computed: {
    product() {
      return this.$props.cartProduct.product;
    },
    image() {
      return this.product.images[0];
    },
    productHasImages() {
      return this.product.images.length > 0;
    },
    multipleProducts() {
      return this.$props.cartProduct.quantity > 1;
    },
    maxProducts() {
      return Math.min(this.product.stock, 30);
    },
    productAvailable() {
      return this.product.available && this.product.stock > 0;
    },
  },
  methods: {
    commafy(x) {
      return x
        .toFixed(2)
        .toString()
        .replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    },
    removeFromCart() {
      const cartProductId = this.$props.cartProduct.id;
      this.loading = true;
      this.$store
        .dispatch('cartProduct/removeFromCart', cartProductId)
        .then(() => {
          this.loading = false;
        })
        .catch((error) => {
          this.loading = false;
          this.$store.dispatch('alert/setMessage', error);
        });
    },
    changeQuantity() {
      this.loading = true;
      const cartProductId = this.$props.cartProduct.id;
      const quantity = parseInt(this.$refs.quantity.value);
      this.$store
        .dispatch('cartProduct/changeQuantity', { cartProductId, quantity })
        .then(() => {
          this.loading = false;
        })
        .catch((error) => {
          this.$store.dispatch('alert/setMessage', error);
          this.loading = false;
        });
    },
    productPage() {
      this.$router.push(`/product/${this.product.id}`);
    },
  },
};
</script>

<style lang="postcss" scoped>
.left-content * {
  @apply mr-auto;
}

* {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.two-lines {
  max-height: 3.5rem;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  @apply overflow-hidden;
}

button {
  @apply text-base;
}

.text-xxs {
  font-size: 0.7rem;
  line-height: 0.85rem;
}

.max-w-full {
  max-width: 100%;
}
</style>
