<template>
  <div>
    <form
      v-if="!loggedInAsBuyer"
      @submit="handleRegisterUser"
      :validation-schema="registerUserSchema"
      onsubmit="return false;"
    >
      <div>
        <div @change="validateAll">
          <input
            id="buyer"
            name="role"
            type="radio"
            value="buyer"
            v-model="values.role"
          />
          <label for="buyer">Buyer</label>
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
          <label for="alias">
            <span v-if="registerBuyer">Name</span>
            <span v-else>Brand</span>
          </label>
          <input
            id="alias"
            name="alias"
            v-model="values.alias"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
            autofocus
          />
          <span>{{ errors.alias }}</span>
        </div>
        <div>
          <label for="telephone">Telephone</label>
          <input
            id="telephone"
            name="telephone"
            v-model="values.telephone"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
          />
          <span>{{ errors.telephone }}</span>
        </div>
        <div>
          <label for="email">Email</label>
          <input
            id="email"
            name="email"
            v-model="values.email"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
          />
          <span>{{ errors.email }}</span>
        </div>
        <div>
          <label for="password">Password</label>
          <input
            id="password"
            name="password"
            v-model="values.password"
            @keyup="validateAll"
            @blur="validateAll"
            type="password"
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
            @keyup="validateAll"
            @blur="validateAll"
            type="password"
            autocomplete="on"
          />
          <span>{{ errors.repeatPassword }}</span>
        </div>
        <div>
          <button type="submit" :disabled="loading || !isValid">
            <span v-show="loading">LOADING</span>
            <span v-show="!loading">
              <span v-if="registerSeller">SIGN UP AS A SELLER</span>
              <span v-else>NEXT</span>
            </span>
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import * as yup from 'yup';
const emptyValues = {
  alias: '',
  telephone: '',
  email: '',
  password: '',
  repeatPassword: '',
};
export default {
  name: 'RegisterUser',
  data() {
    const telephoneRegex =
      /(\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$)|^$/;
    const emailRegex = /[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}/;
    const values = { role: 'buyer', ...emptyValues };
    const errors = { ...emptyValues };
    const registerUserSchema = yup.object({
      alias: yup.string().required('Name is required'),
      telephone: yup
        .string()
        .matches(telephoneRegex, 'Telphone number is invalid')
        .optional(),
      email: yup
        .string()
        .max(64, 'Must be maximum 64 characters')
        .matches(emailRegex, 'Email is invalid')
        .required('Email is required'),
      password: yup
        .string()
        .min(8, 'Must be at least 8 characters')
        .max(64, 'Must be maximum 64 characters')
        .required('Password is required'),
      repeatPassword: yup
        .string()
        .oneOf([yup.ref('password'), null], 'Passwords must match')
        .required('Repeat password is required'),
    });
    return {
      loading: false,
      values,
      errors,
      registerUserSchema,
    };
  },
  computed: {
    isValid() {
      for (let [, value] of Object.entries(this.errors)) {
        if (value !== '') {
          return false;
        }
      }
      return true;
    },
    registerBuyer() {
      return this.values.role == 'buyer';
    },
    registerSeller() {
      return this.values.role == 'seller';
    },
  },
  mounted() {
    this.validateAll();
  },
  methods: {
    handleAliasError() {
      if (this.errors.alias) {
        if (this.registerBuyer) {
          this.errors.alias = 'Name is required';
        } else {
          this.errors.alias = 'Brand is required';
        }
      }
    },
    validateAll() {
      this.registerUserSchema
        .validate(this.values, { abortEarly: false })
        .then(() => {
          this.errors = {};
        })
        .catch((err) => {
          this.errors = {};
          err.inner.forEach((error) => {
            this.errors[error.path] = error.message;
          });
          this.handleAliasError();
        });
    },
    async handleRegisterUser() {
      this.loading = true;
      const user = Object.assign({}, this.values);
      const alias = this.values.alias;
      user.repeat_password = user.repeatPassword;
      delete user.repeatPassword;
      delete user.alias;
      this.validateAll();
      const userLogin = Object.assign({}, user);
      delete userLogin.telephone;
      delete userLogin.role;
      try {
        await this.$store.dispatch('auth/register', user)
        await this.$store.dispatch('auth/login', userLogin)
        if (this.registerBuyer) {
          await this.$store.dispatch('auth/registerBuyer', alias);
        } else {
          await this.$store.dispatch('auth/registerSeller', alias);
          this.$router.push('/profile');
        }
        this.loading = false;
      } catch(error) {
          this.$store.dispatch('alert/setMessage', error);
          this.loading = false;
      }
    },
  },
};
</script>

<style scoped></style>
