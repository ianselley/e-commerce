<template>
  <div>
    <span v-if="available">
      <span class="price">{{ price.toFixed(2) }} </span>€
    </span>
    <span v-else class="not-available">Not available</span>
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
};
</script>

<style lang="postcss" scoped>
.price {
  font-size: 30px;
  font-weight: 600;
  font-style: italic;
}

.not-available {
  font-weight: 700;
  color: red;
}
</style>
