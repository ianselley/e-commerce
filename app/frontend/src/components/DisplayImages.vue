<template>
  <div>
    <div class="total-images">
      <div v-for="image in images" :key="image" class="group-images">
        <Image
          v-if="image"
          :src="image.id"
          :alt="image.filename"
          class="left-images"
          @click="changeSelectedImage(image.id)"
        />
      </div>
      <Image
        v-if="selectedImage"
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
  max-width: 3.5rem;
  @apply mr-8 h-auto w-auto max-h-14;
}
.big-image {
  max-height: 42rem;
  max-width: 42rem;
  @apply h-auto w-auto;
}
</style>
