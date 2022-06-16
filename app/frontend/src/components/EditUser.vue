<template>
  <div>
    <Modal class="modal-class" button-text="Edit User Info">
      <div class="min-w-max flex flex-col space-y-4">
        <EditName v-if="userIsBuyer" />
        <EditBrand v-if="userIsSeller" />
        <EditTelephone />
        <EditEmail />
        <EditPassword />
      </div>
    </Modal>
  </div>
</template>

<script>
import Modal from '@/components/Modal.vue';
import EditName from '@/components/EditName.vue';
import EditBrand from '@/components/EditBrand.vue';
import EditEmail from '@/components/EditEmail.vue';
import EditPassword from '@/components/EditPassword.vue';
import EditTelephone from '@/components/EditTelephone.vue';
export default {
  name: 'EditUser',
  components: {
    Modal,
    EditName,
    EditBrand,
    EditEmail,
    EditPassword,
    EditTelephone,
  },
  computed: {
    userIsBuyer() {
      return this.$store.state.auth.loggedInAs == 'buyer';
    },
    userIsSeller() {
      return this.$store.state.auth.loggedInAs == 'seller';
    },
  },
};
</script>

<style lang="postcss" scoped>
.modal-class :deep() .modal-button {
}
</style>
