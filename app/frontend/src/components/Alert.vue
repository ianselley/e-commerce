<template>
  <div class="alert">
    <span class="text-violet-900 mr-8">{{ message }}</span>
    <button @click="removeMessage">OK</button>
  </div>
</template>

<script>
export default {
  name: 'Alert',
  computed: {
    message() {
      return this.$store.state.alert.message;
    },
  },
  methods: {
    removeMessage() {
      this.$store.commit('alert/removeMessage');
    },
  },
};
</script>

<style lang="postcss" scoped>
.alert {
  @apply py-4 bg-amber-100 w-full fixed z-40 border-violet-300;
  top: 5.5rem;
  border-top-width: 1px;
  border-bottom-width: 1px;
}
</style>
