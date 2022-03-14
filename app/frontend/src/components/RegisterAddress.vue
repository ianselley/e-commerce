<template>
  <div>
    <form
      @submit="handleRegisterAddress"
      :validation-schema="registerAddressSchema"
      onsubmit="return false;"
    >
      <div>
        <div>
          <label for="name">Name</label>
          <input
            id="name"
            name="name"
            v-model="values.name"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
            autofocus
          />
          <span>{{ errors.name }}</span>
        </div>
        <div>
          <label for="street">Street</label>
          <input
            id="street"
            name="street"
            v-model="values.street"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
          />
          <span>{{ errors.street }}</span>
        </div>
        <div>
          <label for="number">Number</label>
          <input
            id="number"
            name="number"
            v-model="values.number"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
          />
          <span>{{ errors.number }}</span>
        </div>
        <div>
          <label for="city">City</label>
          <input
            id="city"
            name="city"
            v-model="values.city"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
          />
          <span>{{ errors.city }}</span>
        </div>
        <div>
          <label for="flat">Flat</label>
          <input
            id="flat"
            name="flat"
            v-model="values.flat"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
          />
          <span>{{ errors.flat }}</span>
        </div>
        <div>
          <label for="state">State</label>
          <input
            id="state"
            name="state"
            v-model="values.state"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
          />
          <span>{{ errors.state }}</span>
        </div>
        <div>
          <label for="zipCode">Zip Code</label>
          <input
            id="zipCode"
            name="zipCode"
            v-model="values.zipCode"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
          />
          <span>{{ errors.zipCode }}</span>
        </div>
        <div>
          <label for="country">Country</label>
          <input
            id="country"
            name="country"
            v-model="values.country"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
          />
          <span>{{ errors.country }}</span>
        </div>
        <div>
          <label for="details">Details</label>
          <input
            id="details"
            name="details"
            v-model="values.details"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
          />
          <span>{{ errors.details }}</span>
        </div>
        <div>
          <button type="submit" :disabled="loading || !isValid">
            <span v-show="loading">LOADING</span>
            Register address
          </button>
          <button type="button" @click="goToProfile">Do it later</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import * as yup from 'yup';
export default {
  name: 'RegisterAddress',
  data() {
    const registerAddressSchema = yup.object({
      name: yup.string().optional(),
      street: yup.string().required('Street is required'),
      number: yup.string().optional(),
      city: yup.string().required('City is required'),
      flat: yup.string().optional(),
      state: yup.string().required('State is required'),
      zipCode: yup.string().required('Zip Code is required'),
      country: yup.string().required('Country is required'),
      details: yup.string().optional(),
    });
    const values = {
      name: '',
      street: '',
      number: '',
      city: '',
      flat: '',
      state: '',
      zipCode: '',
      country: '',
      details: '',
    };
    const errors = {
      name: '',
      street: 'Street is required',
      number: '',
      city: 'City is required',
      flat: '',
      state: 'State is required',
      zipCode: 'Zip Code is required',
      country: 'Country is required',
      details: '',
    };
    return {
      loading: false,
      values,
      errors,
      registerAddressSchema,
    };
  },
  computed: {
    user() {
      return this.$store.state.auth.user;
    },
    isValid() {
      for (let [, value] of Object.entries(this.errors)) {
        if (value !== '') {
          return false;
        }
      }
      return true;
    },
  },
  methods: {
    goToProfile() {
      this.$router.push('/profile');
    },
    validateAll() {
      this.registerAddressSchema
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
    async handleRegisterAddress() {
      await this.validateAll();
      const address = Object.assign({}, this.values);
      this.loading = true;
      await this.$store
        .dispatch('auth/registerAddress', address)
        .then(() => {
          this.loading = false;
          this.$router.push('/profile');
        })
        .catch((error) => {
          this.loading = false;
          this.$store.dispatch('alert/setMessage', error);
        });
    },
  },
};
</script>

<style scoped></style>
