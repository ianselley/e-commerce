<template>
  <div>
    <form
      @submit="handleRegisterAddress"
      :validation-schema="registerAddressSchema"
      onsubmit="return false;"
    >
      <div class="form-content">
        <div class="form-title">
          <span v-if="address.id">EDIT</span
          ><span v-else>REGISTER</span> ADDRESS
        </div>
        <div>
          <label
            for="name"
            class="tooltip"
            :class="{ 'tooltip-error': errors.name }"
            >Name
            <span class="tooltip-text">{{ errors.name }}</span>
          </label>
          <input
            id="name"
            name="name"
            type="text"
            placeholder="John Smith"
            v-model="values.name"
            @keyup="validateAll"
            @blur="validateAll"
          />
        </div>
        <div>
          <label
            for="street"
            class="tooltip"
            :class="{ 'tooltip-error': errors.street }"
            >Street *
            <span class="tooltip-text">{{ errors.street }}</span>
          </label>
          <input
            id="street"
            name="street"
            type="text"
            placeholder="Calle de la Plata"
            v-model="values.street"
            @keyup="validateAll"
            @blur="validateAll"
          />
        </div>
        <div>
          <label
            for="number"
            class="tooltip"
            :class="{ 'tooltip-error': errors.number }"
          >
            Number
            <span class="tooltip-text">{{ errors.number }}</span>
          </label>
          <input
            id="number"
            name="number"
            type="text"
            placeholder="110"
            v-model="values.number"
            @keyup="validateAll"
            @blur="validateAll"
          />
        </div>
        <div>
          <label
            for="city"
            class="tooltip"
            :class="{ 'tooltip-error': errors.city }"
            >City/Town *
            <span class="tooltip-text">{{ errors.city }}</span>
          </label>
          <input
            id="city"
            name="city"
            type="text"
            placeholder="Alcobendas"
            v-model="values.city"
            @keyup="validateAll"
            @blur="validateAll"
          />
        </div>
        <div>
          <label
            for="flat"
            class="tooltip"
            :class="{ 'tooltip-error': errors.flat }"
            >Flat
            <span class="tooltip-text">{{ errors.flat }}</span>
          </label>
          <input
            id="flat"
            name="flat"
            type="text"
            placeholder="3º D"
            v-model="values.flat"
            @keyup="validateAll"
            @blur="validateAll"
          />
        </div>
        <div>
          <label
            for="state"
            class="tooltip"
            :class="{ 'tooltip-error': errors.state }"
            >State/Province/Region *
            <span class="tooltip-text">{{ errors.state }}</span>
          </label>
          <input
            id="state"
            name="state"
            type="text"
            placeholder="Madrid"
            v-model="values.state"
            @keyup="validateAll"
            @blur="validateAll"
          />
        </div>
        <div>
          <label
            for="zipCode"
            class="tooltip"
            :class="{ 'tooltip-error': errors.zipCode }"
            >Zip Code *
            <span class="tooltip-text">{{ errors.zipCode }}</span>
          </label>
          <input
            id="zipCode"
            name="zipCode"
            type="text"
            placeholder="36070"
            v-model="values.zipCode"
            @keyup="validateAll"
            @blur="validateAll"
          />
        </div>
        <div>
          <label
            for="country"
            class="tooltip"
            :class="{ 'tooltip-error': errors.country }"
            >Country *
            <span class="tooltip-text">{{ errors.country }}</span>
          </label>
          <input
            id="country"
            name="country"
            type="text"
            placeholder="Spain"
            v-model="values.country"
            @keyup="validateAll"
            @blur="validateAll"
          />
        </div>
        <div>
          <label for="details">Details</label>
          <input
            id="details"
            name="details"
            type="text"
            placeholder="Write here any additional information"
            v-model="values.details"
            @keyup="validateAll"
            @blur="validateAll"
          />
        </div>
        <div class="flex flex-row justify-between items-center">
          <button
            type="submit"
            class="register-button m-0"
            :disabled="loading || !isValid"
          >
            <img src="@/assets/loader.svg" alt="loading" v-show="loading" />
            <span v-show="!loading">Submit</span>
          </button>
          <button
            v-if="doItLater"
            class="text-xs font-light px-3 py-1"
            title="CAREFUL! It won't save the current values"
            @click="goToProfile"
          >
            Do it later
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import * as yup from 'yup';
const emptyValues = {
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
export default {
  name: 'RegisterAddress',
  props: {
    address: {
      default: { ...emptyValues },
    },
    doItLater: {
      default: false,
    },
  },
  data() {
    const registerAddressSchema = yup.object({
      name: yup.string().max(64, 'Must be a maximum of 64 characters'),
      street: yup
        .string()
        .required('Street is required')
        .max(128, 'Must be a maximum of 128 characters'),
      number: yup.string().max(64, 'Must be a maximum of 64 characters'),
      city: yup
        .string()
        .required('City is required')
        .max(64, 'Must be a maximum of 64 characters'),
      flat: yup.string().max(64, 'Must be a maximum of 64 characters'),
      state: yup.string().required('State is required'),
      zipCode: yup
        .string()
        .required('Zip Code is required')
        .max(64, 'Must be a maximum of 64 characters'),
      country: yup
        .string()
        .required('Country is required')
        .max(64, 'Must be a maximum of 64 characters'),
    });
    const { zip_code, ...values } = { ...this.address };
    values.zipCode = zip_code;
    const errors = { ...emptyValues };
    return {
      loading: false,
      values,
      errors,
      registerAddressSchema,
    };
  },
  mounted() {
    this.validateAll();
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
    handleRegisterAddress() {
      this.validateAll();
      const address = Object.assign({}, this.values);
      this.loading = true;
      if (!this.$props.address.id) {
        this.$store
          .dispatch('address/registerAddress', address)
          .then(() => {
            this.loading = false;
            this.$router.push('/profile');
          })
          .catch((error) => {
            this.loading = false;
            this.$store.dispatch('alert/setMessage', error);
          });
      } else {
        const addressId = this.$props.address.id;
        this.$store
          .dispatch('address/editAddress', { address, addressId })
          .then(() => {
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

<style lang="postcss" scoped></style>
