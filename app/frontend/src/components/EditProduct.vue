<template>
  <div>
    <button @click="toggleEdit">Edit Product</button>
    <UploadProduct v-if="edit" :product="product" />
  </div>
</template>

<script>
import UploadProduct from './UploadProduct.vue';
export default {
  name: 'EditProduct',
  components: { UploadProduct },
  props: {
    product: Object,
  },
  data() {
    return {
      edit: false,
    };
  },
  methods: {
    toggleEdit() {
      this.edit = !this.edit;
    },
  },
};
</script>

<style scoped></style>
