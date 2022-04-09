import ProductService from '@/services/product.service';

const allProducts = JSON.parse(localStorage.getItem('allProducts'));
const sellerProducts = JSON.parse(localStorage.getItem('sellerProducts')) || [];

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
      if (!state.sellerProducts) state.sellerProducts = [];
      state.sellerProducts.push(product);
    },
    uploadImages(state, { productId, images }) {
      const productListId = state.sellerProducts.findIndex(
        (product) => product.id == productId
      );
      state.sellerProducts[productListId].images = images;
    },
    deleteImages(state, { productId, imageIds }) {
      const productListId = state.sellerProducts.findIndex(
        (product) => product.id == productId
      );
      state.sellerProducts[productListId].images = state.sellerProducts[
        productListId
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

    getSellerProducts({ commit }, sellerId) {
      return ProductService.getSellerProducts(sellerId).then((response) => {
        commit('setSellerProducts', response);
      });
    },

    removeSellerProducts({ commit }) {
      commit('removeSellerProducts');
    },
  },
};
