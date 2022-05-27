<template>
  <div class="relative w-0 h-0">
    <div v-show="!messageIsEmpty" class="alert">
      <div class="blend"></div>
      <span class="text-violet-900 mr-8">{{ message }}</span>
      <button @click="removeMessage">OK</button>
      <div class="blend"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Alert',
  computed: {
    message() {
      return this.$store.state.alert.message;
    },
    messageIsEmpty() {
      return this.message == undefined;
    },
  },
  methods: {
    removeMessage() {
      this.$store.commit('alert/removeMessage');
    },
  },
};
</script>

<style scoped>
.alert {
  @apply bg-amber-100 w-full fixed top-28 z-40;
}
.blend {
  @apply w-full bg-amber-100 h-0;
  box-shadow: 0 0 20px 20px #fef3c7;
}
</style>
