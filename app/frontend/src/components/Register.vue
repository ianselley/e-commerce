<template>
  <div>
    <div>
      <img id="profile-img" src="//ssl.gstatic.com/accounts/ui/avatar_2x.png" />
      <Form @submit="handleRegister" :validation-schema="registerSchema">
        <div v-if="!successful">
          <div>
            <label for="username">Username</label>
            <input
              id="username"
              name="username"
              v-model="values.username"
              type="text"
              @blur="validate('username')"
              @keyup="validate('username')"
              :onkeydown="disableEnterKey"
              autofocus
            />
            <span>{{ errors.username }}</span>
          </div>
          <div>
            <label for="email">Email</label>
            <input
              id="email"
              name="email"
              v-model="values.email"
              type="text"
              @blur="validate('email')"
              @keyup="validate('email')"
              :onkeydown="disableEnterKey"
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
              :onkeydown="disableEnterKey"
            />
            <span>{{ errors.password }}</span>
          </div>
          <div>
            <label for="repeatPassword">Repeat password</label>
            <input
              id="repeatPassword"
              name="repeatPassword"
              v-model="values.repeatPassword"
              type="password"
              @blur="validate('repeatPassword')"
              @keyup="validate('repeatPassword')"
              autocomplete="on"
            />
            <span>{{ errors.repeatPassword }}</span>
          </div>
          <div>
            <button type="submit" :disabled="loading">
              <span v-show="loading">Wait a second, it's loading</span>
              Sign Up
            </button>
          </div>
        </div>
      </Form>
      <div
        v-if="message"
        :class="successful ? 'alert-success' : 'alert-danger'"
      >
        {{ message }}
      </div>
    </div>
  </div>
</template>

<script>
import * as yup from 'yup';
import { Form } from 'vee-validate';
export default {
  name: 'Register',
  data() {
    const registerSchema = yup.object({
      username: yup
        .string()
        .required('Username is required!')
        .max(32, 'Must be maximum 32 characters!'),
      email: yup
        .string()
        .required('Email is required!')
        .email('Email is invalid!')
        .max(64, 'Must be maximum 64 characters!'),
      password: yup
        .string()
        .required('Password is required!')
        .min(8, 'Must be at least 8 characters!')
        .max(64, 'Must be maximum 64 characters!'),
      repeatPassword: yup
        .string()
        .required('Repeat password is required!')
        .oneOf([yup.ref('password'), null], 'Passwords must match!'),
    });
    const values = {
      username: '',
      email: '',
      password: '',
      repeatPassword: '',
    };
    const errors = {
      username: '',
      email: '',
      password: '',
      repeatPassword: '',
    };
    return {
      successful: false,
      loading: false,
      message: '',
      values,
      errors,
      registerSchema,
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },
  },
  mounted() {
    if (this.loggedIn) {
      this.$router.push('/profile');
    }
  },
  methods: {
    disableEnterKey(event) {
      if (event.key === 'Enter') {
        event.preventDefault();
      }
    },
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
    async handleRegister() {
      const user = {
        username: this.values.username,
        email: this.values.email,
        password: this.values.password,
      };
      try {
        await this.registerSchema.validate(this.values, { abortEarly: false });
        this.errors = {};
        this.message = '';
        this.successful = false;
        this.loading = true;
        this.$store.dispatch('auth/register', user).then(
          (data) => {
            this.message = data.message;
            this.successful = true;
            this.loading = false;
          },
          (error) => {
            this.message =
              (error.response &&
                error.response.data &&
                error.response.data.message) ||
              error.message ||
              error.toString();
            this.successful = false;
            this.loading = false;
          }
        );
      } catch (err) {
        err.inner.forEach((error) => {
          this.errors[error.path] = error.message;
        });
      }
    },
  },
};
</script>

<style scoped></style>
