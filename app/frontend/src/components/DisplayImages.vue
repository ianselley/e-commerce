<template>
  <div>
    <div class="total-images">
      <div class="group-images">
        <Image
          v-for="image in images"
          :key="image"
          :src="image.id"
          :alt="image.filename"
          class="left-images"
          @click="changeSelectedImage(image.id)"
        />
      </div>
      <Image
        :src="selectedImage.id"
        :alt="selectedImage.filename"
        class="big-image"
      />
    </div>
  </div>
</template>

<script>
import Image from '@/components/Image.vue';
export default {
  name: 'DisplayImages',
  components: {
    Image,
  },
  props: {
    images: Array,
  },
  data() {
    return {
      imageId: undefined,
    };
  },
  computed: {
    selectedImage() {
      return (
        this.images.find((image) => image.id == this.imageId) || this.images[0]
      );
    },
  },
  methods: {
    changeSelectedImage(imageId) {
      this.imageId = imageId;
    },
  },
};
</script>

<style lang="postcss" scoped>
.total-images {
  display: flex;
  flex-direction: row;
}
.left-images {
  margin-right: 2rem;
}
.left-images :deep() .image {
  max-width: 3.5rem;
  max-height: 3.5rem;
  @apply h-auto w-auto;
}
.big-image :deep() .image {
  max-height: 42rem;
  @apply max-w-2xl h-auto w-auto;
}
</style>
