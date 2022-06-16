<template>
  <div class="mb-5">
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
        <button @click="onUploadImage" :disabled="zeroImages || loading">
          Upload Images
        </button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'UploadImages',
  props: {
    productId: Number,
  },
  data() {
    return {
      images: [],
      loading: false,
    };
  },
  computed: {
    zeroImages() {
      return this.images.length === 0;
    },
  },
  methods: {
    onFileChange(e) {
      const files = e.target.files;
      this.images.push(...files);
    },
    onUploadImage() {
      this.loading = true;
      const images = Object.assign([], this.images);
      const productId = this.$props.productId;
      this.$store
        .dispatch('product/uploadImages', { productId, images })
        .then(() => {
          this.loading = false;
          this.$refs.images.value = null;
          this.images = [];
          this.$store.dispatch(
            'alert/setMessage',
            'Image/s uploaded successfully'
          );
        })
        .catch((error) => {
          this.loading = false;
          this.$store.dispatch('alert/setMessage', error);
        });
    },
  },
};
</script>
