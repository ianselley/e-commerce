import CartProductService from '@/services/cartProduct.service.js';

export const cartProduct = {
  namespaced: true,
  state: {},
  mutations: {},
  actions: {
    addToCart({ commit }, { quantity, productId }) {
      return CartProductService.addToCart(productId, quantity)
        .then((response) => {
          commit('auth/addToCart', response, { root: true });
          return Promise.resolve(response);
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },
    changeQuantity({ commit }, { cartProductId, quantity }) {
      return CartProductService.changeQuantity(cartProductId, quantity)
        .then((response) => {
          commit(
            'auth/changeCartProductQuantity',
            { cartProductId, quantity },
            { root: true }
          );
          return Promise.resolve(response);
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },
    removeFromCart({ commit }, cartProductId) {
      return CartProductService.removeFromCart(cartProductId)
        .then(() => {
          commit('auth/removeFromCart', cartProductId, { root: true });
          return Promise.resolve();
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },
  },
};
