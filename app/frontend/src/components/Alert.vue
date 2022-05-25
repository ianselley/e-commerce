<template>
  <div v-show="!messageIsEmpty" class="bg-amber-100 w-full p-4">
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

<style scoped></style>
