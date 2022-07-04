<template>
  <div
    class="bg-white rounded-sm w-full p-4 flex flex-row sm:max-w-70 md:max-w-50"
  >
    <div class="w-40 h-40 flex justify-center items-center">
      <Image
        :src="image.id"
        :alt="image.filename"
        class="max-w-full max-h-full w-auto h-auto"
      />
    </div>
    <div class="flex flex-col justify-between ml-6 left-content">
      <div class="two-lines">
        {{ product.title }} - {{ product.description }}
      </div>
      <div class="flex items-center">
        Price: <Price :price="product.price" class="inline-block ml-4" />
        <span v-if="multipleProducts" class="ml-4 text-xxs text-amber-900">
          ({{ product.price }}€ x {{ cartProduct.quantity }} =
          {{ product.price * cartProduct.quantity }}€)
        </span>
      </div>
      <div class="flex justify-between items-center">
        <div class="w-max">
          Quantity
          <select
            ref="quantity"
            @change="changeQuantity"
            :disabled="loading"
            class="rounded-md bg-amber-50 border border-amber-300"
          >
            <option
              v-for="quantity in 30"
              :key="quantity"
              :selected="quantity == cartProduct.quantity"
              :value="quantity"
              class="bg-white text-center"
            >
              {{ quantity }}
            </option>
          </select>
        </div>
        <button class="ml-12" @click="removeFromCart" :disabled="loading">
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
    multipleProducts() {
      return this.$props.cartProduct.quantity > 1;
    },
  },
  methods: {
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
  },
};
</script>

<style lang="postcss" scoped>
:root {
  --h: 1.75rem;
}

.left-content * {
  @apply mr-auto;
}

* {
  font-size: 1.125rem;
  line-height: var(--h);
}

.two-lines {
  /* height: calc(var(--h) * 2); It doesn't work :( */
  height: 3.5rem;
}

button {
  @apply text-base;
}

.text-xxs {
  font-size: 0.7rem;
  line-height: 0.85rem;
}
</style>
