<template>
  <div>
    <div>
      <img id="profile-img" src="//ssl.gstatic.com/accounts/ui/avatar_2x.png" />
      <form @submit="handleLogin" :validation-schema="loginSchema">
        <div>
          <div>
            <label for="email">Email</label>
            <input
              id="email"
              name="email"
              v-model="values.email"
              type="text"
              @blur="validate('email')"
              @keyup="validate('email')"
            />
            <span>{{ errors.email }}</span>
          </div>
          <div>
            <label for="password">Password</label>
            <input
              id="password"
              name="password"
              v-model="values.password"
              type="password"
              @blur="validate('password')"
              @keyup="validate('password')"
              autocomplete="on"
            />
            <span>{{ errors.password }}</span>
          </div>
          <button :disabled="loading">
            <span v-show="loading"></span>
            <span>Login</span>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import * as yup from 'yup';
export default {
  name: 'Login',
  data() {
    const loginSchema = yup.object({
      email: yup.string().email().required('Email is required'),
      password: yup.string().required('Password is required'),
    });
    const values = {
      email: '',
      password: '',
    };
    const errors = {
      email: '',
      password: '',
    };
    return {
      loading: false,
      message: '',
      loginSchema,
      values,
      errors,
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.loggedIn;
    },
  },
  created() {
    if (this.loggedIn) {
      this.$router.push('/profile');
      this.$store.commit(
        'alert/setMessage',
        'You are already logged in, you would have to log out to access this'
      );
    }
  },
  methods: {
    validate(field) {
      this.registerSchema
        .validateAt(field, this.values)
        .then(() => {
          this.errors[field] = '';
        })
        .catch((error) => {
          this.errors[field] = error.message;
        });
    },
    handleLogin() {
      this.loading = true;
      this.$store
        .dispatch('auth/login', this.values)
        .then(() => {
          this.$router.push('/profile');
        })
        .catch(() => {
          this.loading = false;
        });
    },
  },
};
</script>

<style scoped></style>
