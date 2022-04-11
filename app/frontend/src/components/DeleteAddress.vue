<template>
  <div>
    <button :disabled="loading" @click="deleteAddress">Delete Address</button>
  </div>
</template>

<script>
export default {
  name: 'DeleteAddress',
  props: {
    addressId: Number,
  },
  data() {
    return {
      loading: false,
    };
  },
  methods: {
    deleteAddress() {
      this.loading = true;
      this.$store
        .dispatch('address/deleteAddress', this.$props.addressId)
        .then(() => {
          this.loading = false;
        })
        .catch((error) => {
          this.$store.dispatch('alert/setMessage', error);
          this.loading = false;
        });
    },
  },
};
</script>

<style scoped></style>
