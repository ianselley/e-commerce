<template>
  <img :src="`${API_URL}/product/images/${src}`" :alt="alt" />
</template>

<script>
import { API_URL } from '@/config.json';
export default {
  name: 'Image',
  props: {
    src: Number,
    alt: String,
  },
  data() {
    return {
      API_URL,
    };
  },
};
</script>

<style lang="postcss" scoped></style>
