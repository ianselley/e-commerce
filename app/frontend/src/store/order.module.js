import OrderService from '@/services/order.service.js';

export const order = {
  namespaced: true,
  state: {},
  mutations: {},
  actions: {
    orderProducts({ commit }, { addressId, cartProductIds }) {
      return OrderService.orderProducts({ addressId, cartProductIds })
        .then((response) => {
          commit('auth/removeManyFromCart', cartProductIds, { root: true });
          // for (let cartProductId of cartProductIds.split(',')) {
          //   commit('auth/removeFromCart', cartProductId, { root: true });
          // }
          commit('auth/addOrders', response, { root: true });
          return Promise.resolve(response);
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },
  },
};
