<template>
  <div>
    <button :disabled="loading" @click="makeItMainAddress">
      Make it main address
    </button>
  </div>
</template>

<script>
export default {
  name: 'MakeItMainAddress',
  props: {
    addressId: Number,
  },
  data() {
    return {
      loading: false,
    };
  },
  methods: {
    makeItMainAddress() {
      this.loading = true;
      this.$store
        .dispatch('address/makeItMainAddress', this.$props.addressId)
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

<style lang="postcss" scoped></style>
