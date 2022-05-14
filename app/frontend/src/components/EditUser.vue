<template>
  <div>
    <button ref="toggleEditUser" @click="toggleEdit">Edit User Info</button>
    <div v-if="edit">
      <EditName v-if="userIsBuyer" />
      <EditBrand v-if="userIsSeller" />
      <EditTelephone />
      <EditEmail />
      <EditPassword />
    </div>
  </div>
</template>

<script>
import EditTelephone from '@/components/EditTelephone.vue';
import EditEmail from '@/components/EditEmail.vue';
import EditPassword from '@/components/EditPassword.vue';
import EditName from '@/components/EditName.vue';
import EditBrand from '@/components/EditBrand.vue';
export default {
  name: 'EditUser',
  components: {
    EditTelephone,
    EditEmail,
    EditPassword,
    EditName,
    EditBrand,
  },
  data() {
    return {
      edit: false,
    };
  },
  computed: {
    userIsBuyer() {
      return this.$store.state.auth.user.buyer !== null;
    },
    userIsSeller() {
      return this.$store.state.auth.user.seller !== null;
    },
  },
  methods: {
    toggleEdit() {
      this.edit = !this.edit;
    },
  },
};
</script>

<style scoped></style>
