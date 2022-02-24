<template>
  <div>
    <div>
      <img id="profile-img" src="//ssl.gstatic.com/accounts/ui/avatar_2x.png" />
      <form @submit="handleLogin" :validation-schema="loginSchema">
        <div>
          <label for="username">Username</label>
          <input name="username" type="text" />
          <span name="username" />
        </div>
        <div>
          <label for="password">Password</label>
          <input name="password" type="password" autocomplete="on" />
          <span name="password" />
        </div>
        <div>
          <button :disabled="loading">
            <span v-show="loading"></span>
            <span>Login</span>
          </button>
        </div>
        <div>
          <div v-if="message" role="alert">
            {{ message }}
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
// import { form, Field, ErrorMessage } from 'vee-validate';
import * as yup from 'yup';
export default {
  name: 'Login',
  // components: {
  //   form,
  //   Field,
  //   ErrorMessage,
  // },
  data() {
    const loginSchema = yup.object({
      username: yup.string().required('Username is required!'),
      password: yup.string().required('Password is required!'),
    });
    return {
      loading: false,
      message: '',
      loginSchema,
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },
  },
  created() {
    if (this.loggedIn) {
      this.$router.push('/profile');
    }
  },
  methods: {
    handleLogin(user) {
      this.loading = true;
      this.$store.dispatch('auth/login', user).then(
        () => {
          this.$router.push('/profile');
        },
        (error) => {
          this.loading = false;
          this.message =
            (error.response &&
              error.response.data &&
              error.response.data.message) ||
            error.message ||
            error.toString();
        }
      );
    },
  },
};
</script>

<style scoped></style>
