<template>
  <div class="root">
    <button @click="toggleImages">Select Images To Delete</button>
    <div v-show="showImages" class="images">
      <div v-for="image in images" :key="image" class="thumbnail">
        <input
          type="checkbox"
          :value="image.id"
          @change="check($event, image.id)"
        />
        <Image :src="image.id" :alt="image.filename" class="thumbnail" />
      </div>
      <button :disabled="loading" @click="deleteImages">Delete Images</button>
    </div>
  </div>
</template>

<script>
import Image from '@/components/Image.vue';
export default {
  name: 'DeleteImages',
  components: {
    Image,
  },
  props: {
    productId: Number,
    images: Array,
  },
  data() {
    return {
      loading: false,
      showImages: false,
      checkedIds: {},
    };
  },
  mounted() {
    this.initializeCheckedIds();
  },
  methods: {
    initializeCheckedIds() {
      for (let image of this.$props.images) {
        this.checkedIds[image.id] = false;
      }
    },
    toggleImages() {
      this.showImages = !this.showImages;
    },
    check(e, id) {
      this.checkedIds[id] = e.target.checked;
    },
    deleteImages() {
      this.loading = true;
      let imageIds = [];
      for (let [id, checked] of Object.entries(this.checkedIds)) {
        if (checked) {
          imageIds.push(id);
        }
      }
      imageIds = imageIds.join(',');
      this.$store
        .dispatch('product/deleteImages', {
          productId: this.$props.productId,
          imageIds,
        })
        .then(() => {
          this.loading = false;
          this.initializeCheckedIds();
        })
        .catch((error) => {
          this.loading = false;
          this.$store.dispatch('alert/setMessage', error);
        });
    },
  },
};
</script>

<style lang="postcss" scoped>
.root {
  margin-bottom: 1rem;
}

.images {
  margin-top: 0.5rem;
}

.thumbnail :deep() .image {
  max-width: 3rem;
  max-height: 3rem;
  height: auto;
  width: auto;
}

.thumbnail {
  display: inline-block;
  margin: 0.3rem 0.2rem 0;
}
</style>
