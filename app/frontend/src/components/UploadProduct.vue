<template>
  <div>
    <form
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
          <input
            id="file-input"
            type="file"
            accept="image/*"
            multiple
            @change="selectImages"
          />
        </div>
        <div>
          <button type="submit" :disabled="loading || !isValid">
            <span v-show="loading">LOADING</span>
            <span v-show="!loading">Submit product</span>
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import * as yup from 'yup';
export default {
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
      images: undefined,
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
    selectImages() {
      this.images = Array.from(event.target.files);
      console.log(this.images);
    },
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
        .dispatch('auth/registerProduct', product)
        .then((response) => {
          if (!this.images) return;
          return this.$store.dispatch(
            'auth/uploadImages',
            response.id,
            this.images
          );
        })
        .then(() => {
          this.loading = false;
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
