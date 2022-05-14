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
          commit('auth/addOrders', response, { root: true });
          return Promise.resolve(response);
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },
    productArrives({ commit }, orderId) {
      return OrderService.productArrives(orderId)
        .then(() => {
          commit('auth/productArrives', orderId, { root: true });
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },
  },
};
