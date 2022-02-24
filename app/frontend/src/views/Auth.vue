<template>
  <div>
    <Register />
    <br />
    <hr size="10" noshade="noshade" />
    <br />
    <Login />
  </div>
</template>

<script>
import Login from '@/components/Login.vue';
import Register from '@/components/Register.vue';

export default {
  name: 'Auth',
  components: {
    Login,
    Register,
  },
};
</script>
