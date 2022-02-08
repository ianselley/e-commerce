<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld />
    <Authentication />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue';
import Authentication from '@/components/Authentication.vue';

export default {
  name: 'Home',
  components: {
    HelloWorld,
    Authentication,
  },
};
</script>
