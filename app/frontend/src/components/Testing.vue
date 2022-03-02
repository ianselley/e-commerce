<template>
  <!-- <div>This is the value of "loggedIn" (in data()) is: {{ loggedIn }}</div> -->
  <div>
    This is the value of "loggedIn" (in computed) is: {{ loggedIn_computed }}
  </div>
  <br />
  <!-- <button v-on:click="this.$store.commit('auth/loginSuccess')">
    Change "loggedIn" to true
  </button> -->
  <table>
    <tr>
      <th>Name</th>
      <th>Description</th>
    </tr>
    <tr>
      <td>A</td>
      <td>Description of A</td>
    </tr>
    <tr>
      <td>B</td>
      <td>Description of B</td>
    </tr>
    <tr>
      <td>C (larger)</td>
      <td>Description of B (larger)</td>
    </tr>
  </table>
</template>

<script>
export default {
  name: 'Testing',
  data() {
    return {
      loggedIn: this.$store.state.auth.loggedIn,
    };
  },
  computed: {
    loggedIn_computed() {
      return this.$store.state.auth.loggedIn;
    },
  },
};
</script>
