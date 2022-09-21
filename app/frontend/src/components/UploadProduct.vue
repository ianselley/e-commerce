<template>
  <div>
    <form
      v-if="!submitted"
      @submit="handleUploadProduct"
      :validation-schema="uploadProductSchema"
      onsubmit="return false;"
    >
      <div class="form-content">
        <div class="form-title">
          <span v-if="edit">EDIT</span><span v-else>UPLOAD</span> PRODUCT
        </div>
        <div>
          <label
            for="title"
            class="tooltip"
            :class="{ 'tooltip-error': errors.title }"
            >Title *
            <span class="tooltip-text">{{ errors.title }}</span>
          </label>
          <input
            id="title"
            name="title"
            v-model="values.title"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
            autofocus
          />
        </div>
        <div>
          <label
            for="description"
            class="tooltip"
            :class="{ 'tooltip-error': errors.description }"
            >Description
            <span class="tooltip-text">{{ errors.description }}</span>
          </label>
          <input
            id="description"
            name="description"
            v-model="values.description"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
          />
        </div>
        <div>
          <label
            for="price"
            class="tooltip"
            :class="{ 'tooltip-error': errors.price }"
            >Price *
            <span class="tooltip-text">{{ errors.price }}</span>
          </label>
          <input
            id="price"
            name="price"
            v-model="values.price"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
          />
        </div>
        <div>
          <label
            for="stock"
            class="tooltip"
            :class="{ 'tooltip-error': errors.stock }"
            >Stock *
            <span class="tooltip-text">{{ errors.stock }}</span>
          </label>
          <input
            id="stock"
            name="stock"
            v-model="values.stock"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
          />
        </div>
        <div>
          <button type="submit" :disabled="loading || !isValid">
            <span v-if="loading">LOADING</span>
            <span v-else
              ><span v-if="edit">Save changes</span
              ><span v-else>Submit product and add images</span></span
            >
          </button>
        </div>
      </div>
    </form>
    <UploadImages v-if="productId" :productId="productId" class="m-6" />
  </div>
</template>

<script>
import * as yup from 'yup';
import UploadImages from './UploadImages.vue';
const emptyValues = {
  title: '',
  description: '',
  price: '',
  stock: '',
};
export default {
  name: 'UploadProduct',
  components: {
    UploadImages,
  },
  props: {
    product: {
      default: { ...emptyValues },
    },
    edit: {
      default: false,
    },
  },
  data() {
    const uploadProductSchema = yup.object({
      title: yup.string().required('Title is required'),
      description: yup.string().optional(),
      price: yup.string().required('Price is required'),
      stock: yup.string().required('Stock is required'),
    });
    const values = {
      title: this.product.title,
      description: this.product.description,
      price: this.product.price,
      stock: this.product.stock,
    };
    const errors = { ...emptyValues };
    return {
      loading: false,
      values,
      errors,
      uploadProductSchema,
      productId: undefined,
      submitted: false,
    };
  },
  mounted() {
    this.validateAll();
  },
  computed: {
    user() {
      return this.$store.state.auth.user;
    },
    isValid() {
      for (let [, value] of Object.entries(this.errors)) {
        if (value !== '') {
          return false;
        }
      }
      return true;
    },
  },
  methods: {
    validateAll() {
      this.uploadProductSchema
        .validate(this.values, { abortEarly: false })
        .then(() => {
          this.errors = {};
        })
        .catch((err) => {
          this.errors = {};
          err.inner.forEach((error) => {
            this.errors[error.path] = error.message;
          });
        });
    },
    handleUploadProduct() {
      this.validateAll();
      this.loading = true;
      const product = Object.assign({}, this.values);
      if (!this.$props.product.id) {
        this.$store
          .dispatch('product/registerProduct', product)
          .then((response) => {
            this.loading = false;
            this.productId = response.id;
            this.submitted = true;
          })
          .catch((error) => {
            this.loading = false;
            this.$store.dispatch('alert/setMessage', error);
          });
      } else {
        const productId = this.$props.product.id;
        this.$store
          .dispatch('product/editProduct', { product, productId })
          .then(() => {
            this.loading = false;
          })
          .catch((error) => {
            this.loading = false;
            this.$store.dispatch('alert/setMessage', error);
          });
      }
    },
  },
};
</script>

<style lang="postcss" scoped></style>
