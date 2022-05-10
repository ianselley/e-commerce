<template>
  <div>
    <div>
      <strong>Telephone: </strong>
      <span v-if="!edit">{{ currentUser().telephone }}</span>
      <form
        v-else
        @submit="submitChange"
        :validation-schema="editTelephoneSchema"
        onsubmit="return false;"
      >
        <div>
          <input
            id="telephone"
            name="telephone"
            v-model="values.telephone"
            @keyup="validate"
            @blur="validate"
            type="text"
          />
          <span>{{ errors.telephone }}</span>
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
  telephone: 'EditTelephone',
  data() {
    const telphoneRegex =
      /(\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$)|^$/;
    const editTelephoneSchema = yup.object({
      telephone: yup
        .string()
        .matches(telphoneRegex, 'Telphone number is invalid')
        .optional(),
    });
    return {
      edit: false,
      loading: false,
      values: { telephone: this.currentUser().telephone },
      errors: { telephone: '' },
      editTelephoneSchema,
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
      this.editTelephoneSchema
        .validate(this.values)
        .then(() => {
          this.errors = {};
        })
        .catch((err) => {
          this.errors = { telephone: err.message };
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
      const user = { telephone: this.values.telephone };
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

<style scoped></style>
