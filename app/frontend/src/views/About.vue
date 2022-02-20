<template>
  <div class="about">
    <h1>This is an about page</h1>
    <Modal modal_content="this message has been hard coded" />
  </div>
</template>

<script>
import Modal from '../components/Modal.vue';
export default {
  name: 'About',
  components: {
    Modal,
  },
};
</script>

<style scoped></style>
