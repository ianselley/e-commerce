import AddressService from '@/services/address.service.js';

export const address = {
  namespaced: true,
  state: {},
  mutations: {},
  actions: {
    registerAddress({ commit }, address) {
      return AddressService.registerAddress(address)
        .then((response) => {
          commit('auth/registerAddress', response, { root: true });
          return Promise.resolve(response);
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },

    editAddress({ commit }, { address, addressId }) {
      return AddressService.editAddress(address, addressId)
        .then((response) => {
          commit(
            'auth/editAddress',
            { address: response, addressId },
            { root: true }
          );
          return Promise.resolve(response);
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },

    deleteAddress({ commit }, addressId) {
      return AddressService.deleteAddress(addressId)
        .then((response) => {
          commit('auth/deleteAddress', addressId, { root: true });
          return Promise.resolve(response);
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },

    makeItMainAddress({ commit }, addressId) {
      return AddressService.makeItMainAddress(addressId)
        .then((response) => {
          commit('auth/makeItMainAddress', addressId, { root: true });
          return Promise.resolve(response);
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },
  },
};
