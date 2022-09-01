<template>
  <div class="font-publicSans">
    <Navbar />
    <Alert v-if="!messageIsEmpty" />
    <router-view />
    <footer />
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import Alert from '@/components/Alert.vue';

export default {
  name: 'App',
  components: {
    Navbar,
    Alert,
  },
  computed: {
    message() {
      return this.$store.state.alert.message;
    },
    messageIsEmpty() {
      return this.message == undefined;
    },
  },
};
</script>

<style>
html {
  overflow-y: scroll;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

footer {
  margin-top: 10rem;
}
</style>
