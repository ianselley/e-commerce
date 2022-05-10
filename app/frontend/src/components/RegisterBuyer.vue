<template>
  <div>
    <form
      v-if="!loggedInAsBuyer"
      @submit="handleRegisterBuyer"
      :validation-schema="registerBuyerSchema"
      onsubmit="return false;"
    >
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
      <button type="submit" :disabled="loading || !isValid">
        Sign up as Buyer
      </button>
    </form>
    <RegisterAddress v-if="loggedInAsBuyer" />
  </div>
</template>

<script>
import RegisterAddress from './RegisterAddress.vue';
import * as yup from 'yup';
const emptyValues = {
  name: '',
};
export default {
  name: 'RegisterBuyer',
  components: {
    RegisterAddress,
  },
  data() {
    const registerBuyerSchema = yup.object({
      name: yup.string().required('Name is required'),
    });
    const values = { ...emptyValues };
    const errors = { ...emptyValues };
    return {
      loading: false,
      values,
      errors,
      registerBuyerSchema,
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
    loggedInAsBuyer() {
      return this.$store.state.auth.loggedInAs === 'buyer' && this.buyer;
    },
    buyer() {
      return this.$store.state.auth.buyer;
    },
  },
  mounted() {
    this.validateAll();
  },
  methods: {
    validateAll() {
      this.registerBuyerSchema
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
    handleRegisterBuyer() {
      const buyer = Object.assign({}, this.values);
      this.loading = true;
      this.$store
        .dispatch('auth/registerBuyer', buyer)
        .then(() => {
          this.loading = false;
        })
        .catch((error) => {
          this.loading = false;
          this.$store.dispatch('alert/setMessage', error);
        });
    },
  },
};
</script>
