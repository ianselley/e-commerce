<template>
  <div>
    <Modal button-text="Edit Product">
      <UploadProduct :product="product" />
    </Modal>
  </div>
</template>

<script>
import Modal from '@/components/Modal.vue';
import UploadProduct from '@/components/UploadProduct.vue';
export default {
  name: 'EditProduct',
  components: {
    Modal,
    UploadProduct,
  },
  props: {
    product: Object,
  },
};
</script>

<style lang="postcss" scoped></style>
