<template>
  <div>
    <form
      @submit="handleRegisterUser"
      :validation-schema="registerUserSchema"
      onsubmit="return false;"
    >
      <div>
        <div v-if="!editingUser">
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
          <label for="telephone">Telephone</label>
          <input
            id="telephone"
            name="telephone"
            v-model="values.telephone"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
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
              <span v-if="editingUser">Submit Changes</span>
              <span v-else>Next</span>
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
  telephone: '',
  email: '',
  password: '',
  repeatPassword: '',
};
export default {
  name: 'RegisterUser',
  props: {
    user: {
      default: { ...emptyValues },
    },
  },
  data() {
    const telphoneRegex =
      /(\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$)|^$/;
    const emailRegex = /[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}/;
    const registerUserSchema = yup.object({
      telephone: yup
        .string()
        .matches(telphoneRegex, 'Thelphone number is invalid')
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
    const values = {
      role: 'buyer',
      telephone: this.user.telephone,
      email: this.user.email,
      password: this.user.password,
      repeatPassword: this.user.repeatPassword,
    };
    const errors = { ...emptyValues };
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
    editingUser() {
      return this.$props.user.id;
    },
  },
  mounted() {
    this.validateAll();
  },
  methods: {
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
        });
    },
    handleRegisterUser() {
      const user = Object.assign({}, this.values);
      delete user.repeatPassword;
      this.validateAll();
      this.loading = true;
      if (!this.$props.user.id) {
        const userLogin = Object.assign({}, user);
        delete userLogin.telephone;
        delete userLogin.role;
        this.$store
          .dispatch('auth/register', user)
          .then(() => {
            this.loading = false;
            this.$store.dispatch('auth/login', userLogin);
          })
          .catch((error) => {
            this.loading = false;
            this.$store.dispatch('alert/setMessage', error);
          });
      } else {
        delete user.role;
        this.$store
          .dispatch('auth/editUser', user)
          .then(() => {
            this.$parent.toggleEdit();
            this.loading = false;
          })
          .catch((error) => {
            this.$store.dispatch('alert/setMessage', error);
            this.loading = false;
          });
      }
    },
  },
};
</script>

<style scoped></style>
