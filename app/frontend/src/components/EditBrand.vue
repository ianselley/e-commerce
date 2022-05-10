<template>
  <div>
    <div>
      <strong>Brand: </strong>
      <span v-if="!edit">{{ currentSeller().brand }}</span>
      <form
        v-else
        @submit="submitChange"
        :validation-schema="editBrandSchema"
        onsubmit="return false;"
      >
        <div>
          <input
            id="brand"
            name="brand"
            v-model="values.brand"
            @keyup="validate"
            @blur="validate"
            type="text"
          />
          <span>{{ errors.brand }}</span>
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
  brand: 'EditBrand',
  data() {
    const editBrandSchema = yup.object({
      brand: yup.string().required('Brand is required'),
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

<style scoped></style>
