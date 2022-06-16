<template>
  <div>
    <div v-if="!edit" class="edit-profile">
      <span><strong>Telephone:</strong> {{ currentUser().telephone }}</span>
      <button @click="toggleEdit" class="btn-edit-profile">Edit</button>
    </div>
    <div v-else>
      <form
        @submit="submitChange"
        :validation-schema="editTelephoneSchema"
        onsubmit="return false;"
      >
        <label
          class="tooltip font-bold"
          :class="{ 'tooltip-error': errors.telephone }"
          for="telephone"
          >Telephone
          <span class="tooltip-text">{{ errors.telephone }}</span>
        </label>
        <div class="flex items-center">
          <input
            id="telephone"
            name="telephone"
            type="text"
            v-model="values.telephone"
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
  telephone: 'EditTelephone',
  data() {
    const telphoneRegex =
      /(\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$)|^$/;
    const editTelephoneSchema = yup.object({
      telephone: yup
        .string()
        .matches(
          telphoneRegex,
          'Telphone number is invalid (no spaces and must have a prefix)'
        )
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

<style lang="postcss" scoped></style>
