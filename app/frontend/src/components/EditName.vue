<template>
  <div>
    <div v-if="!edit" class="edit-profile">
      <span><strong>Name:</strong> {{ currentBuyer().name }}</span>
      <button @click="toggleEdit" class="btn-edit-profile">Edit</button>
    </div>
    <div v-else>
      <form
        @submit="submitChange"
        :validation-schema="editNameSchema"
        onsubmit="return false;"
      >
        <label
          class="tooltip font-bold"
          :class="{ 'tooltip-error': errors.name }"
          for="name"
          >Name *
          <span class="tooltip-text">{{ errors.name }}</span>
        </label>
        <div class="flex items-center">
          <input
            id="name"
            name="name"
            type="text"
            v-model="values.name"
            @keyup="validate"
            @blur="validate"
            autofocus
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
  name: 'EditName',
  data() {
    const editNameSchema = yup.object({
      name: yup
        .string()
        .max(64, 'Must be maximum 64 characters')
        .required('Name is required'),
    });
    return {
      edit: false,
      loading: false,
      values: { name: this.currentBuyer().name },
      errors: { name: '' },
      editNameSchema,
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
      this.editNameSchema
        .validate(this.values)
        .then(() => {
          this.errors = {};
        })
        .catch((err) => {
          this.errors = { name: err.message };
        });
    },
    currentBuyer() {
      return this.$store.state.auth.buyer;
    },
    toggleEdit() {
      this.edit = !this.edit;
    },
    submitChange() {
      this.loading = true;
      this.$store
        .dispatch('auth/editName', this.values.name)
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
