<template>
  <div>
    <div id="nav">
      <IanSelleyLogo />
      <router-link
        v-for="route in this.$router.options.routes"
        :key="route.name"
        :to="route.path"
      >
        <span v-if="route.name">{{ route.name }} |</span>
      </router-link>
    </div>
    <Alert />
    <router-view />
    <footer />
  </div>
</template>

<script>
import IanSelleyLogo from '@/components/IanSelleyLogo.vue';
import Alert from '@/components/Alert.vue';

export default {
  name: 'App',
  components: {
    IanSelleyLogo,
    Alert,
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

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

footer {
  margin-top: 10rem;
}
</style>
