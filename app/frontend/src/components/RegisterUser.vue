<template>
  <div>
    <form
      @submit="handleRegisterUser"
      :validation-schema="registerUserSchema"
      onsubmit="return false;"
    >
      <div class="form-content">
        <div class="form-title">SIGN UP</div>
        <div
          @change="validateAll"
          class="flex justify-center mx-auto w-min items-center bg-gradient-to-br from-indigo-50 to-violet-50 rounded-lg"
        >
          <div class="inline-flex rounded-lg">
            <input
              id="buyer"
              name="role"
              type="radio"
              value="buyer"
              v-model="values.role"
              checked
              hidden
            />
            <label for="buyer" class="radio">Buyer</label>
          </div>
          <div class="inline-flex rounded-lg">
            <input
              id="seller"
              name="role"
              type="radio"
              value="seller"
              v-model="values.role"
              hidden
            />
            <label for="seller" class="radio">Seller</label>
          </div>
        </div>
        <div>
          <label
            class="tooltip"
            :class="{ 'tooltip-error': errors.alias }"
            for="alias"
          >
            <span v-if="registerBuyer">Name *</span>
            <span v-else>Brand *</span>
            <span class="tooltip-text">{{ errors.alias }}</span>
          </label>
          <input
            id="alias"
            name="alias"
            type="text"
            :placeholder="registerBuyer ? 'John Smith' : 'Apple'"
            v-model="values.alias"
            @keyup="validateAll"
            @blur="validateAll"
            autofocus
          />
        </div>
        <div>
          <label
            class="tooltip"
            :class="{ 'tooltip-error': telephone.error }"
            for="telephone"
            >Telephone
            <span class="tooltip-text">{{ telephone.error }}</span>
          </label>
          <input
            id="telephone"
            name="telephone"
            type="tel"
            v-model="telephone.value"
            @keyup="validateAll"
            @blur="validateAll"
          />
        </div>
        <div>
          <label
            class="tooltip"
            :class="{ 'tooltip-error': errors.email }"
            for="email"
            >Email *
            <span class="tooltip-text">{{ errors.email }}</span>
          </label>
          <input
            id="email"
            name="email"
            type="text"
            :placeholder="
              registerBuyer ? 'johnsmith@example.com' : 'apple@contact.com'
            "
            v-model="values.email"
            @keyup="validateAll"
            @blur="validateAll"
          />
        </div>
        <div>
          <label
            class="tooltip"
            :class="{ 'tooltip-error': errors.password }"
            for="password"
            >Password *
            <span class="tooltip-text">{{ errors.password }}</span>
          </label>
          <input
            id="password"
            name="password"
            type="password"
            v-model="values.password"
            @keyup="validateAll"
            @blur="validateAll"
            autocomplete="on"
          />
        </div>
        <div>
          <label
            class="tooltip"
            :class="{ 'tooltip-error': errors.repeatPassword }"
            for="repeatPassword"
            >Repeat password *
            <span class="tooltip-text">{{ errors.repeatPassword }}</span>
          </label>
          <input
            id="repeatPassword"
            name="repeatPassword"
            type="password"
            v-model="values.repeatPassword"
            @keyup="validateAll"
            @blur="validateAll"
            autocomplete="on"
          />
        </div>
        <button
          type="submit"
          :disabled="loading || !isValid"
          class="register-button"
        >
          <img src="@/assets/loader.svg" alt="loading" v-show="loading" />
          <span v-show="!loading">
            <span v-if="registerSeller">SIGN UP AS A SELLER</span>
            <span v-else>NEXT</span>
          </span>
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import * as yup from 'yup';
const emptyValues = {
  alias: '',
  email: '',
  password: '',
  repeatPassword: '',
};
export default {
  name: 'RegisterUser',
  data() {
    const emailRegex = /[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}/;
    const values = { role: 'buyer', ...emptyValues };
    const errors = { ...emptyValues };
    const telephone = { value: '', error: '' };
    const registerUserSchema = yup.object({
      alias: yup.string().required('Name is required'),
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
      telephone,
      registerUserSchema,
      phoneInput: undefined,
    };
  },
  computed: {
    isValid() {
      if (this.telephone.error !== '') {
        return false;
      }
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
    const phoneInputField = document.querySelector('#telephone');
    this.phoneInput = window.intlTelInput(phoneInputField, {
      initialCountry: 'auto',
      geoIpLookup: this.getIp,
      utilsScript:
        'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.15/js/utils.js',
    });
    this.validateAll();
  },
  methods: {
    getIp(callback) {
      fetch('https://ipinfo.io/json?token=0e078cf2613cc6', {
        headers: { Accept: 'application/json' },
      })
        .then((resp) => resp.json())
        .catch(() => {
          return {
            country: 'us',
          };
        })
        .then((resp) => callback(resp.country));
    },
    handleAliasError() {
      if (this.errors.alias) {
        if (this.registerBuyer) {
          this.errors.alias = 'Name is required';
        } else {
          this.errors.alias = 'Brand is required';
        }
      }
    },
    validateTelephone() {
      if (this.phoneInput.isValidNumber() || this.telephone.value == '') {
        this.telephone.error = '';
      } else {
        this.telephone.error = 'Telephone number is invalid';
      }
      console.log(this.phoneInput.getNumber());
    },
    validateAll() {
      this.validateTelephone();
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
      user.telephone = this.phoneInput.getNumber();
      delete user.repeatPassword;
      delete user.alias;
      this.validateAll();
      const userLogin = Object.assign({}, user);
      delete userLogin.telephone;
      delete userLogin.role;
      try {
        await this.$store.dispatch('auth/register', user);
        await this.$store.dispatch('auth/login', userLogin);
        if (this.registerBuyer) {
          await this.$store.dispatch('auth/registerBuyer', alias);
        } else {
          await this.$store.dispatch('auth/registerSeller', alias);
          this.$router.push('/profile');
        }
        this.loading = false;
      } catch (error) {
        this.$store.dispatch('alert/setMessage', error);
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.radio {
  @apply m-0 w-min inline text-center self-center py-2 px-4 rounded-lg cursor-pointer;
}

:not(input:checked) ~ .radio {
  @apply transition ease-in-out duration-200 hover:bg-amber-50;
}

input:checked ~ .radio {
  @apply text-amber-50 font-bold bg-amber-400;
}

.tooltip-error {
  @apply text-red-700;
}

.tooltip {
  @apply relative;
}

.tooltip .tooltip-text {
  @apply bg-red-400 w-max rounded-md text-white text-center px-3 absolute z-10;
  @apply opacity-0 invisible transition duration-300 left-0;
}

.tooltip:hover .tooltip-text {
  @apply visible opacity-100 transition duration-300;
}
</style>
