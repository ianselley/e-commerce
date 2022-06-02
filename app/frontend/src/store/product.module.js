import ProductService from '@/services/product.service';

const allProducts = JSON.parse(localStorage.getItem('allProducts')) || [];
const sellerProducts = JSON.parse(localStorage.getItem('sellerProducts')) || [];

function findProductIndex(list, productId) {
  return list.findIndex((product) => product.id == productId);
}

export const product = {
  namespaced: true,
  state: { allProducts, sellerProducts },
  mutations: {
    setAllProducts(state, value) {
      state.allProducts = value;
    },
    setSellerProducts(state, value) {
      state.sellerProducts = value;
    },
    setProduct(state, value) {
      state.product = value;
    },
    registerProduct(state, product) {
      state.sellerProducts.push(product);
    },
    editProduct(state, { product, productId }) {
      const sellerProductIndex = findProductIndex(
        state.sellerProducts,
        productId
      );
      state.sellerProducts[sellerProductIndex] = product;
      const allProductIndex = findProductIndex(state.allProducts, productId);
      state.allProducts[allProductIndex] = product;
    },
    uploadImages(state, { productId, images }) {
      const productIndex = findProductIndex(state.sellerProducts, productId);
      state.sellerProducts[productIndex].images = images;
    },
    changeProductAvailability(state, productId) {
      const productIndex = findProductIndex(state.sellerProducts, productId);
      state.sellerProducts[productIndex].available =
        !state.sellerProducts[productIndex].available;
    },
    deleteImages(state, { productId, imageIds }) {
      const productIndex = findProductIndex(state.sellerProducts, productId);
      state.sellerProducts[productIndex].images = state.sellerProducts[
        productIndex
      ].images.filter((image) => !imageIds.includes(image.id));
    },
    removeSellerProducts(state) {
      state.sellerProducts = null;
    },
  },
  actions: {
    getAllProducts({ commit }) {
      return ProductService.getAllProducts().then((response) => {
        commit('setAllProducts', response);
        return Promise.resolve(response);
      });
    },

    getProduct({ commit }, productId) {
      return ProductService.getProduct(productId).then((response) => {
        commit('setProduct', response);
        return Promise.resolve(response);
      });
    },

    registerProduct({ commit }, product) {
      return ProductService.registerProduct(product)
        .then((response) => {
          commit('registerProduct', response);
          return Promise.resolve(response);
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },

    editProduct({ commit }, { product, productId }) {
      return ProductService.editProduct(product, productId)
        .then((response) => {
          commit('editProduct', { product: response, productId });
          return Promise.resolve(response);
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },

    uploadImages({ commit }, { productId, images }) {
      return ProductService.uploadImages(productId, images)
        .then((images) => {
          commit('uploadImages', { productId, images });
          return Promise.resolve(images);
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },

    changeProductAvailability({ commit }, productId) {
      return ProductService.changeProductAvailability(productId)
        .then((response) => {
          commit('changeProductAvailability', productId);
          return Promise.resolve(response);
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },

    deleteImages({ commit }, { productId, imageIds }) {
      return ProductService.deleteImages(productId, imageIds)
        .then(() => {
          commit('deleteImages', { productId, imageIds });
          return Promise.resolve();
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },

    getSellerProducts({ commit }) {
      return ProductService.getSellerProducts().then((response) => {
        commit('setSellerProducts', response);
      });
    },

    removeSellerProducts({ commit }) {
      commit('removeSellerProducts');
    },
  },
};
