<template>
  <div>
    <button @click="toggleEdit">Edit Address</button>
    <RegisterAddress v-if="edit" :address="address" />
  </div>
</template>

<script>
import RegisterAddress from './RegisterAddress.vue';
export default {
  name: 'EditAddress',
  components: { RegisterAddress },
  props: {
    address: Object,
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
