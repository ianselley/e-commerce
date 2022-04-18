<template>
  <div>
    <button ref="toggleEditUser" @click="toggleEdit">Edit User</button>
    <RegisterUser v-if="edit" :user="user" />
  </div>
</template>

<script>
import RegisterUser from '@/components/RegisterUser.vue';
export default {
  name: 'EditUser',
  components: { RegisterUser },
  props: {
    user: Object,
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
