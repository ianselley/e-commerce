<template>
  <div class="w-3/4 relative">
    <div class="bg-amber-50 rounded-t-lg p-4 flex justify-around">
      <div>Order placed on {{ orderDate }}</div>
      <div>Quantity: {{ order.quantity }}</div>
      <div>TOTAL: {{ order.price * order.quantity }}€</div>
      <div class="max-w-52 truncate tooltip-address">
        Address: {{ order.address.name }}
      </div>
      <DisplayAddress
        class="scale-75 transform origin-top-right float-address top-12 right-8 z-20"
        :address="order.address"
        :edit="false"
      />
    </div>
    <div class="bg-white rounded-b-sm flex flex-row p-4">
      <div
        @click="productPage"
        class="min-w-40 w-40 h-40 flex justify-center items-center image-link"
      >
        <Image
          :src="image.id"
          :alt="image.filename"
          class="max-w-full max-h-full w-auto h-auto"
        />
      </div>
      <div class="flex flex-col justify-between ml-6 left-content">
        <div class="font-semibold text-2xl text-left">
          Product<span v-if="order.quantity > 1">s</span>
          <span v-if="afterDeadline">delivered</span
          ><span v-else> will be delivered</span> on {{ deliveryDate }}
        </div>
        <div @click="productPage" class="two-lines text-left link">
          {{ product.title }} - {{ product.description }}
        </div>
        <div class="flex items-center">
          Price: <Price :price="order.price" class="inline-block ml-4" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Image from '@/components/Image.vue';
import Price from '@/components/Price.vue';
import DisplayAddress from '@/components/DisplayAddress.vue';
export default {
  name: 'DisplayOrder',
  components: {
    Image,
    Price,
    DisplayAddress,
  },
  props: {
    order: Object,
  },
  mounted() {
    if (this.currentBuyer && this.afterDeadline && !this.productDelivered) {
      this.productArrives();
    }
  },
  computed: {
    currentBuyer() {
      return this.$store.state.auth.buyer;
    },
    product() {
      return this.order.product;
    },
    productDelivered() {
      return this.order.delivered;
    },
    orderDate() {
      return new Date(this.order.date).toISOString().slice(0, 10);
    },
    deadline() {
      const date = new Date(this.order.date);
      date.setDate(date.getDate() + 1);
      date.setTime(date.getTime() + 2 * 60 * 60 * 1000);
      return date;
    },
    deliveryDate() {
      return new Date(this.deadline).toISOString().slice(0, 10);
    },
    afterDeadline() {
      const now = new Date();
      return now > this.deadline;
    },
    image() {
      return this.product.images[0];
    },
  },
  methods: {
    productArrives() {
      const orderId = this.order.id;
      this.$store.dispatch('order/productArrives', orderId).catch((error) => {
        this.$store.dispatch('alert/setMessage', error);
      });
    },
    productPage() {
      this.$router.push(`/product/${this.product.id}`);
    },
  },
};
</script>

<style lang="postcss" scoped>
* {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.tooltip-address:hover {
  cursor: default;
}

.float-address {
  max-width: 20rem;
}

.two-lines {
  max-height: 3.5rem;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  @apply overflow-hidden;
}
</style>
