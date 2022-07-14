<template>
  <div>
    <div v-if="!edit" class="edit-profile">
      <span><strong>Email:</strong> {{ currentUser().email }}</span>
      <button @click="toggleEdit" class="btn-edit-profile">Edit</button>
    </div>
    <div v-else>
      <form
        @submit="submitChange"
        :validation-schema="editEmailSchema"
        onsubmit="return false;"
      >
        <label
          class="tooltip font-bold"
          :class="{ 'tooltip-error': errors.email }"
          for="email"
          >Email *
          <span class="tooltip-text">{{ errors.email }}</span>
        </label>
        <div class="flex items-center">
          <input
            id="email"
            name="email"
            type="text"
            v-model="values.email"
            @keyup="validate"
            @blur="validate"
          />
          <button class="icon-button" :disabled="loading || !isValid">
            <img src="@/assets/check.svg" alt="apply changes" />
          </button>
          <button @click="toggleEdit" class="icon-button" :disabled="loading">
            <img src="@/assets/cross.svg" alt="cancel changes" />
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import * as yup from 'yup';
export default {
  name: 'EditEmail',
  data() {
    const emailRegex = /[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}/;
    const editEmailSchema = yup.object({
      email: yup
        .string()
        .max(64, 'Must be a maximum of 64 characters')
        .matches(emailRegex, 'Email is invalid')
        .required('Email is required'),
    });
    return {
      edit: false,
      loading: false,
      values: { email: this.currentUser().email },
      errors: { email: '' },
      editEmailSchema,
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
  },
  mounted() {
    this.validate();
  },
  methods: {
    validate() {
      this.editEmailSchema
        .validate(this.values)
        .then(() => {
          this.errors = {};
        })
        .catch((err) => {
          this.errors = { email: err.message };
        });
    },
    currentUser() {
      return this.$store.state.auth.user;
    },
    toggleEdit() {
      this.edit = !this.edit;
    },
    submitChange() {
      this.loading = true;
      const user = { email: this.values.email };
      this.$store
        .dispatch('auth/editUser', user)
        .then(() => {
          this.loading = false;
          this.edit = false;
        })
        .catch((error) => {
          this.$store.dispatch('alert/setMessage', error);
          this.loading = false;
        });
    },
  },
};
</script>

<style lang="postcss" scoped></style>
