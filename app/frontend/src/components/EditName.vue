<template>
  <div>
    <div>
      <strong>Name: </strong>
      <span v-if="!edit">{{ currentBuyer().name }}</span>
      <form
        v-else
        @submit="submitChange"
        :validation-schema="editNameSchema"
        onsubmit="return false;"
      >
        <div>
          <input
            id="name"
            name="name"
            v-model="values.name"
            @keyup="validate"
            @blur="validate"
            type="text"
          />
          <span>{{ errors.name }}</span>
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
  name: 'EditName',
  data() {
    const editNameSchema = yup.object({
      name: yup.string().required('Name is required'),
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

<style scoped></style>
