<template>
  <div>
    <button @click="changeProductAvailability">Make product <span v-if="available">not</span> available</button>
  </div>
</template>

<script>
export default {
  name: 'ChangeProductAvailablility',
  props: {
    productId: Number,
    available: Boolean,
  },
  data() {
    return {
      loading: false,
    };
  },
  methods: {
    changeProductAvailability() {
      this.loading = true;
      this.$store
        .dispatch('product/changeProductAvailability', this.$props.productId)
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
