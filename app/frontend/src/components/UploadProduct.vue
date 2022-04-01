<template>
  <div>
    <form
      v-if="!submitted"
      @submit="handleUploadProduct"
      :validation-schema="uploadProductSchema"
      onsubmit="return false;"
    >
      <div>
        <div>
          <label for="title">Title</label>
          <input
            id="title"
            name="title"
            v-model="values.title"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
            autofocus
          />
          <span>{{ errors.title }}</span>
        </div>
        <div>
          <label for="description">Description</label>
          <input
            id="description"
            name="description"
            v-model="values.description"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
          />
          <span>{{ errors.description }}</span>
        </div>
        <div>
          <label for="price">Price</label>
          <input
            id="price"
            name="price"
            v-model="values.price"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
          />
          <span>{{ errors.price }}</span>
        </div>
        <div>
          <label for="stock">Stock</label>
          <input
            id="stock"
            name="stock"
            v-model="values.stock"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
          />
          <span>{{ errors.stock }}</span>
        </div>
        <div>
          <label for="specifications">Specifications</label>
          <input
            id="specifications"
            name="specifications"
            v-model="values.specifications"
            @keyup="validateAll"
            @blur="validateAll"
            type="text"
          />
          <span>{{ errors.specifications }}</span>
        </div>
        <div>
          <button type="submit" :disabled="loading || !isValid">
            <span v-show="loading">LOADING</span>
            <span v-show="!loading">Submit product and add images</span>
          </button>
        </div>
      </div>
    </form>
    <UploadImages v-if="productId" :productId="productId" />
  </div>
</template>

<script>
import * as yup from 'yup';
import UploadImages from './UploadImages.vue';
export default {
  components: {
    UploadImages,
  },
  name: 'UploadProduct',
  data() {
    const uploadProductSchema = yup.object({
      title: yup.string().required('Title is required'),
      description: yup.string().optional(),
      price: yup.string().required('Price is required'),
      stock: yup.string().required('Stock is required'),
      specifications: yup.string().optional(),
    });
    const values = {
      title: '',
      description: '',
      price: '',
      stock: '',
      specifications: '',
    };
    const errors = {
      title: 'Title is required',
      description: '',
      price: 'Price is required',
      stock: 'Stock is required',
      specifications: '',
    };
    return {
      loading: false,
      values,
      errors,
      uploadProductSchema,
      productId: undefined,
      submitted: false,
    };
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
    },
  },
};
</script>

<style scoped></style>
