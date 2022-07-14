<template>
  <div class="about">
    <h1>This is an about page</h1>
    <Modal
      modal_content="This message is a prop defined in the Modal component and initialized in the About view component"
    />
  </div>
</template>

<script>
import Modal from '@/components/Modal.vue';
export default {
  name: 'About',
  data() {
    return {};
  },
  components: {
    Modal,
  },
};
</script>

<style lang="postcss" scoped></style>
