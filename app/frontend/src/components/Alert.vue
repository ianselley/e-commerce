<template>
  <div>
    {{ message }}
    <button v-show="!messageIsEmpty" @click="removeMessage">OK</button>
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
      return this.message === '';
    },
  },
  methods: {
    removeMessage() {
      this.$store.commit('alert/removeMessage');
    },
  },
};
</script>
