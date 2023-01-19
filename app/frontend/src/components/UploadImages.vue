<template>
  <div>
    <form onsubmit="return false;">
      <div class="flex flex-col space-y-2">
        <div class="font-bold mb-2 text-lg">SELECT OR DRAG IMAGES</div>
        <input
          type="file"
          name="images"
          ref="images"
          @change="onFileChange"
          accept="image/*"
          multiple
        />
        <button @click="onUploadImage" :disabled="zeroImages || loading">
          <span v-show="!loading">Upload images</span>
          <span v-show="loading">UPLOADING</span>
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
      if (images.length == 0) {
        this.dispatch('alert/setMessage', 'No images selected');
        return;
      }
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
          this.$refs.images.value = null;
          this.images = [];
          this.$store.dispatch('alert/setMessage', error);
        });
    },
  },
};
</script>

<style lang="postcss" scoped></style>
