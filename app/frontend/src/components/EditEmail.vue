<template>
  <div>
    <div>
      <strong>Email: </strong>
      <span v-if="!edit">{{ currentUser().email }}</span>
      <form
        v-else
        @submit="submitChange"
        :validation-schema="editEmailSchema"
        onsubmit="return false;"
      >
        <div>
          <input
            id="email"
            name="email"
            v-model="values.email"
            @keyup="validate"
            @blur="validate"
            type="text"
          />
          <span>{{ errors.email }}</span>
        </div>
        <button type="submit" :disabled="loading || !isValid">
          Apply Change
        </button>
      </form>
    </div>
    <button @click="toggleEdit">
      <span v-if="edit">Cancel</span><span v-else>Edit</span>
    </button>
  </div>
</template>

<script>
import * as yup from 'yup';
export default {
  email: 'EditEmail',
  data() {
    const emailRegex = /[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}/;
    const editEmailSchema = yup.object({
      email: yup
        .string()
        .max(64, 'Must be maximum 64 characters')
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
