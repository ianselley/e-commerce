import ProductService from '@/services/product.service';

const products = JSON.parse(localStorage.getItem('products'));

export const product = {
  namespaced: true,
  state: { products },
  mutations: {
    setProducts(state, value) {
      state.products = value;
    },
  },
  actions: {
    getProducts({ commit }) {
      return ProductService.getProducts().then((response) => {
        commit('setProducts', response);
        return Promise.resolve(response);
      });
    },
  },
};
