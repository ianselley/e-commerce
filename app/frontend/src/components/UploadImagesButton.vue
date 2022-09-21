<template>
  <div>
    <Modal button-text="Upload images" button-class="w-full" modal-class="p-6">
      <UploadImages :product-id="productId" />
    </Modal>
  </div>
</template>

<script>
import Modal from '@/components/Modal.vue';
import UploadImages from '@/components/UploadImages.vue';
export default {
  name: 'UploadImagesButton',
  components: {
    Modal,
    UploadImages,
  },
  props: {
    productId: Number,
  },
};
</script>

<style lang="postcss" scoped></style>
