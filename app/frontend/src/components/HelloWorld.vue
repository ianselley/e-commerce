<template>
  <div>
    <h1>{{ message }}</h1>
    <h4>{{ extra }}</h4>
    <h6>{{ extra2 }}</h6>
    <p>This is the home page</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: 'First message',
      extra: 'Default extra data',
    };
  },
  methods: {
    getMessage() {
      this.axios
        .get('/')
        .then((response) => {
          this.message = response.data;
          this.extra = JSON.stringify(response.data);
        })
        .catch((error) => {
          this.message = error;
          this.extra = 'environment variables: ' + JSON.stringify(process.env);
        });
    },
  },
  created() {
    this.getMessage();
    this.message = 'Second message';
  },
};
</script>

<style scoped></style>
