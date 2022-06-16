<template>
  <div>
    <div v-if="!edit" class="edit-profile">
      <span><strong>Password:</strong> ******</span>
      <button @click="toggleEdit" class="btn-edit-profile">Edit</button>
    </div>
    <div v-else>
      <form
        @submit="submitChange"
        :validation-schema="editPasswordSchema"
        onsubmit="return false;"
      >
        <label
          class="tooltip font-bold"
          :class="{ 'tooltip-error': errors.password }"
          for="password"
          >Password *
          <span class="tooltip-text">{{ errors.password }}</span>
        </label>
        <div class="flex items-center">
          <input
            id="password"
            name="password"
            type="password"
            v-model="values.password"
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
  name: 'EditPassword',
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

<style lang="postcss" scoped></style>
