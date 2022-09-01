import ProductService from '@/services/product.service';

const searchedProducts =
  JSON.parse(localStorage.getItem('searchedProducts')) || [];
const sellerProducts = JSON.parse(localStorage.getItem('sellerProducts')) || [];
const currentPage = 1;
const productsPerPage = 2;
const substring = '';

function findProductIndex(list, productId) {
  return list.findIndex((product) => product.id == productId);
}

export const product = {
  namespaced: true,
  state: {
    searchedProducts,
    sellerProducts,
    substring,
    currentPage,
    productsPerPage,
  },
  mutations: {
    setSearchedProducts(state, value) {
      state.searchedProducts = value;
    },
    setSellerProducts(state, value) {
      state.sellerProducts = value;
    },
    setProduct(state, value) {
      state.product = value;
    },
    setSubstring(state, value) {
      if (state.substring != value) {
        state.currentPage = 1;
      }
      state.substring = value;
    },
    setTotalPages(state, totalProducts) {
      state.totalPages = Math.ceil(totalProducts / state.productsPerPage);
    },
    movePage(state, number) {
      let value = number + state.currentPage;
      if (value > state.totalPages) {
        value = state.totalPages;
      } else if (value < 1) {
        value = 1;
      }
      state.currentPage = value;
    },
    registerProduct(state, product) {
      product.available = false;
      state.sellerProducts.push(product);
    },
    editProduct(state, { product, productId }) {
      const sellerProductIndex = findProductIndex(
        state.sellerProducts,
        productId
      );
      state.sellerProducts[sellerProductIndex] = product;
      const searchedProductIndex = findProductIndex(
        state.searchedProducts,
        productId
      );
      state.searchedProducts[searchedProductIndex] = product;
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
      if (state.sellerProducts[productIndex].images.length == 0) {
        state.sellerProducts[productIndex].available = false;
      }
    },
    removeSellerProducts(state) {
      state.sellerProducts = null;
    },
  },
  actions: {
    getSearchedProducts({ commit, state }) {
      return ProductService.getSearchedProducts(
        state.substring,
        state.currentPage,
        state.productsPerPage
      ).then((response) => {
        commit('setSearchedProducts', response[0]);
        commit('setTotalPages', response[1]);
        return Promise.resolve(response[0]);
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
