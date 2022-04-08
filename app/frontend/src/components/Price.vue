<template>
  <span
    ><span class="price">{{ price.toFixed(2) }}</span
    >€</span
  >
</template>

<script>
export default {
  name: 'Price',
  props: {
    price: Number,
  },
};
</script>

<style scoped>
.price {
  font-size: 30px;
  font-weight: 600;
  font-style: italic;
}
</style>
