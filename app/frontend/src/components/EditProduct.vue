<template>
  <div>
    <button @click="activateModal">Edit Product</button>
    <Modal>
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
  methods: {
    activateModal() {
      this.$store.commit('modal/activateModal');
    },
  },
};
</script>

<style lang="postcss" scoped></style>
