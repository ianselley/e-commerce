import CartProductService from '@/services/cartProduct.service.js';

export const cartProduct = {
  namespaced: true,
  state: {},
  mutations: {},
  actions: {
    addToCart({ commit }, { quantity, productId }) {
      return CartProductService.addToCart(productId, quantity).then(
        (response) => {
          commit('auth/addToCart', response, { root: true });
        }
      );
    },
    removeFromCart({ commit }, cartProductId) {
      return CartProductService.removeFromCart(cartProductId).then(() => {
        commit('auth/removeFromCart', cartProductId, { root: true });
      });
    },
  },
};
