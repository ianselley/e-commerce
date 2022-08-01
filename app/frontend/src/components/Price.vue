<template>
  <div>
    <span v-if="available">
      <span class="text-3xl italic font-semibold">{{ commafy(price) }} </span>
      €
    </span>
    <span v-else class="text-red-600 font-bold">Not available</span>
  </div>
</template>

<script>
export default {
  name: 'Price',
  props: {
    price: Number,
    available: {
      type: Boolean,
      default: true,
    },
  },
  methods: {
    commafy(x) {
      return x
        .toFixed(2)
        .toString()
        .replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    },
  },
};
</script>

<style lang="postcss" scoped></style>
