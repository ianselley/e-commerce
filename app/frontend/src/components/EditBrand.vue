<template>
  <div>
    <div v-if="!edit" class="edit-profile">
      <span><strong>Brand:</strong> {{ currentSeller().brand }}</span>
      <button @click="toggleEdit" class="btn-edit-profile">Edit</button>
    </div>
    <div v-else>
      <form
        @submit="submitChange"
        :validation-schema="editBrandSchema"
        onsubmit="return false;"
      >
        <label
          class="tooltip font-bold"
          :class="{ 'tooltip-error': errors.brand }"
          for="brand"
          >Brand *
          <span class="tooltip-text">{{ errors.brand }}</span>
        </label>
        <div class="flex items-center">
          <input
            id="brand"
            name="brand"
            type="text"
            v-model="values.brand"
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
  brand: 'EditBrand',
  data() {
    const editBrandSchema = yup.object({
      brand: yup
        .string()
        .max(64, 'Must be maximum 64 characters')
        .required('Brand is required'),
    });
    return {
      edit: false,
      loading: false,
      values: { brand: this.currentSeller().brand },
      errors: { brand: '' },
      editBrandSchema,
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
      this.editBrandSchema
        .validate(this.values)
        .then(() => {
          this.errors = {};
        })
        .catch((err) => {
          this.errors = { brand: err.message };
        });
    },
    currentSeller() {
      return this.$store.state.auth.seller;
    },
    toggleEdit() {
      this.edit = !this.edit;
    },
    submitChange() {
      this.loading = true;
      this.$store
        .dispatch('auth/editBrand', this.values.brand)
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
