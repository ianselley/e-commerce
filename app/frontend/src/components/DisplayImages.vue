<template>
  <div>
    <div class="flex">
      <div class="flex flex-col space-y-2">
        <div v-for="image in images" :key="image.id">
          <Image
            v-if="image"
            :src="image.id"
            :alt="image.filename"
            class="left-images"
            :class="{
              'border-2 border-amber-400 p-0.5 opacity-75':
                image.id == selectedImage.id,
            }"
            @click="changeSelectedImage(image.id)"
          />
        </div>
      </div>
      <div class="h-96 w-96">
        <Image
          v-if="selectedImage"
          :src="selectedImage.id"
          :alt="selectedImage.filename"
          class="big-image"
        />
      </div>
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
.left-images {
  max-width: 3rem;
  @apply mr-4 h-auto w-auto max-h-14;
}

.big-image {
  max-width: 100%;
  @apply mr-auto mb-auto block max-h-full;
}
</style>
