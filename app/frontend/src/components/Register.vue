<template>
  <div>
    <div>
      <img id="profile-img" src="//ssl.gstatic.com/accounts/ui/avatar_2x.png" />
      <form @submit="handleRegister" :validation-schema="registerSchema" onsubmit="return false;">
        <div v-if="!successful">
          <div>
            <input
              id="buyer"
              name="role"
              type="radio"
              value="buyer"
              v-model="values.role"
              checked
            />
            <label for="buyer" class="text-3xl">Buyer</label>

            <input
              id="seller"
              name="role"
              type="radio"
              value="seller"
              v-model="values.role"
            />
            <label for="seller">Seller</label>
          </div>
          <div>
            <label for="telephone">Telephone</label>
            <input
              id="telephone"
              name="telephone"
              v-model="values.telephone"
              type="text"
              @blur="validate('telephone')"
              @keyup="validate('telephone')"
              autofocus
            />
            <span>{{ errors.telephone }}</span>
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
      </form>
    </div>
  </div>
</template>

<script>
import * as yup from 'yup';
export default {
  name: 'Register',
  data() {
    const telphoneRegExp =
      /(\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$)|^$/;
    const registerSchema = yup.object({
      telephone: yup
        .string()
        .optional()
        .matches(telphoneRegExp, 'Thelphone number is invalid'),
      email: yup
        .string()
        .required('Email is required')
        .email('Email is invalid')
        .max(64, 'Must be maximum 64 characters'),
      password: yup
        .string()
        .required('Password is required')
        .min(8, 'Must be at least 8 characters')
        .max(64, 'Must be maximum 64 characters'),
      repeatPassword: yup
        .string()
        .required('Repeat password is required')
        .oneOf([yup.ref('password'), null], 'Passwords must match'),
    });
    const values = {
      telephone: '',
      email: '',
      password: '',
      repeatPassword: '',
      role: '',
    };
    const errors = {
      telephone: '',
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
        telephone: this.values.telephone,
        email: this.values.email,
        password: this.values.password,
        role: this.values.role,
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
        this.$store.dispatch('auth/login', user)
      } catch (err) {
        err.inner.forEach((error) => {
          this.errors[error.path] = error.message;
        });
      }
    },
  },
};
</script>

<style scoped>
</style>
