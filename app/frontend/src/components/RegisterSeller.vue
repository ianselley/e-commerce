<template>
  <div>
    <form
      @submit="handleRegisterSeller"
      :validation-schema="registerSellerSchema"
      onsubmit="return false;"
    >
      <div>
        <label for="brand">Brand</label>
        <input
          id="brand"
          name="brand"
          v-model="value.brand"
          @keyup="validate()"
          @blur="validate()"
          type="text"
          autofocus
        />
        <span>{{ brandError }}</span>
      </div>
      <button type="submit" :disabled="loading || !isValid">
        Sign up as Seller
      </button>
    </form>
  </div>
</template>

<script>
import * as yup from 'yup';
export default {
  name: 'RegisterSeller',
  data() {
    const registerSellerSchema = yup.object({
      brand: yup.string().required('Brand is required'),
    });
    const value = {
      brand: '',
    };
    return {
      loading: false,
      brandError: '',
      value,
      registerSellerSchema,
    };
  },
  computed: {
    isValid() {
      if (this.brandError === '') {
        return true;
      }
      return false;
    },
  },
  mounted() {
    this.validate();
  },
  methods: {
    validate() {
      this.registerSellerSchema
        .validateAt('brand', this.value)
        .then(() => {
          this.brandError = '';
        })
        .catch((err) => {
          this.brandError = err.message;
        });
    },
    handleRegisterSeller() {
      const brand = Object.assign({}, this.value);
      this.loading = true;
      this.$store
        .dispatch('auth/registerSeller', brand)
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
