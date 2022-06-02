<template>
  <div>
    <img :src="`${API_URL}/product/images/${src}`" class="image" :alt="alt" />
  </div>
</template>

<script>
import { API_URL } from '@/config.json';
export default {
  name: 'Image',
  props: {
    src: Number,
    alt: String,
    Class: String,
  },
  data() {
    return {
      API_URL,
    };
  },
};
</script>

<style lang="postcss" scoped>
.image {
  width: auto;
  height: 20rem;
}
</style>
