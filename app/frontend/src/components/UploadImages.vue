<template>
  <div>
    <p>ID: {{ productId }}</p>
    <form onsubmit="return false;">
      <div class="imgContent">
        <input
          type="file"
          class="file_input"
          name="images"
          ref="images"
          @change="onFileChange"
          accept="image/*"
          multiple
        />
        <button @click="onUploadImage" :disabled="zeroImages">Upload Images</button>
      </div>
    </form>
  </div>
</template>

<script>
import ProductService from '@/services/product.service.js';
export default {
  name: 'UploadImages',
  props: {
    productId: Number,
  },
  data() {
    return {
      images: [],
    };
  },
  computed: {
    zeroImages() {
      return this.images.length === 0;
    }
  },
  methods: {
    onFileChange(e) {
      const files = e.target.files;
      this.images.push(...files);
    },
    onUploadImage() {
      const images = Object.assign([], this.images);
      ProductService.uploadImages(this.$props.productId, images)
        .then(() => {
          this.$refs.images.value = null;
          this.$store.dispatch('alert/setMessage', 'Image/s uploaded successfully');
        })
        .catch((error) => {
          this.$store.dispatch('alert/setMessage', error);
        });
    },
  },
};
</script>
