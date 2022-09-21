<template>
  <div>
    <Modal button-text="Edit product" :button-class="'w-full'">
      <UploadProduct :product="product" :edit="true" />
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
