<template>
  <div>
    <button ref="activateEditUser" @click="activateModal">
      Edit User Info
    </button>
    <Modal>
      <EditName v-if="userIsBuyer" />
      <EditBrand v-if="userIsSeller" />
      <EditTelephone />
      <EditEmail />
      <EditPassword />
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
      return this.$store.state.auth.user.buyer !== null;
    },
    userIsSeller() {
      return this.$store.state.auth.user.seller !== null;
    },
    activeModal() {
      return this.$store.state.modal.active;
    },
  },
  methods: {
    activateModal() {
      this.$store.commit('modal/activateModal');
    },
  },
};
</script>

<style lang="postcss" scoped></style>
