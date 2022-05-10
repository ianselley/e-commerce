<template>
  <div>
    <div>
      <strong>Password: </strong>
      <span v-if="!edit">******</span>
      <form
        v-else
        @submit="submitChange"
        :validation-schema="editPasswordSchema"
        onsubmit="return false;"
      >
        <div>
          <input
            id="password"
            name="password"
            ref="password"
            v-model="values.password"
            @keyup="validate"
            @blur="validate"
            type="password"
            autocomplete="off"
          />
          <span>{{ errors.password }}</span>
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
  password: 'EditPassword',
  data() {
    const editPasswordSchema = yup.object({
      password: yup
        .string()
        .min(8, 'Must be at least 8 characters')
        .max(64, 'Must be maximum 64 characters')
        .required('Password is required'),
    });
    return {
      edit: false,
      loading: false,
      values: { password: '' },
      errors: { password: '' },
      editPasswordSchema,
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
      this.editPasswordSchema
        .validate(this.values)
        .then(() => {
          this.errors = {};
        })
        .catch((err) => {
          this.errors = { password: err.message };
        });
    },
    toggleEdit() {
      this.edit = !this.edit;
    },
    submitChange() {
      this.loading = true;
      const user = { password: this.values.password };
      this.$store
        .dispatch('auth/editUser', user)
        .then(() => {
          this.edit = false;
          this.values.password = '';
          this.loading = false;
        })
        .catch((error) => {
          this.$store.dispatch('alert/setMessage', error);
          this.loading = false;
        });
    },
  },
};
</script>

<style scoped></style>
