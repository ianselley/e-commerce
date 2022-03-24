import { useCookies } from 'vue3-cookies';

import AuthService from '@/services/auth.service.js';
import AddressService from '@/services/address.service.js';
import ProductService from '@/services/product.service';

const { cookies } = useCookies();
const user = cookies.get('user');
let userRole;

if (user && user.buyer) {
  userRole = 'buyer';
} else if (user && user.seller) {
  userRole = 'seller';
} else {
  userRole = 'user';
}

const initialState = user
  ? { loggedIn: true, loggedInAs: userRole, user }
  : { loggedIn: false, loggedInAs: null, user: null };

export const auth = {
  namespaced: true,
  state: initialState,
  mutations: {
    registerSuccess(state) {
      state.loggedInAs = null;
      state.loggedIn = false;
    },
    registerFailure(state) {
      state.loggedInAs = null;
      state.loggedIn = false;
    },
    registerBuyer(state, buyer) {
      state.loggedInAs = 'buyer';
      state.user.buyer = buyer;
    },
    registerSeller(state, seller) {
      state.loggedInAs = 'seller';
      state.user.seller = seller;
    },
    registerAddress(state, address) {
      state.user.buyer.addresses.push(address);
      if (!state.user.buyer.main_address_id) {
        state.user.buyer.main_address_id = address.buyer.main_address_id;
      }
      state.addedAddress = true;
    },
    resetAddedAddress(state) {
      state.addedAddress = false;
    },
    registerProduct(state, product) {
      state.user.seller.products.push(product);
    },
    uploadImages(state, productId) {
      state.user.seller.products.forEach((product) => {
        if (product.id === productId) {
          product.hasImages = true;
        }
      });
    },
    loginSuccess(state, user) {
      if (user.seller) {
        state.loggedInAs = 'seller';
      } else if (user.buyer) {
        state.loggedInAs = 'buyer';
      } else {
        state.loggedInAs = 'user';
      }
      state.loggedIn = true;
      state.user = user;
    },
    loginFailure(state) {
      state.loggedInAs = null;
      state.loggedIn = false;
      state.user = null;
    },
    logout(state) {
      state.loggedInAs = null;
      state.loggedIn = false;
      state.user = null;
    },
  },

  actions: {
    login({ commit }, user) {
      return AuthService.login(user)
        .then((user) => {
          commit('loginSuccess', user);
          return Promise.resolve(user);
        })
        .catch((error) => {
          commit('loginFailure');
          return Promise.reject(error);
        });
    },

    logout({ commit }) {
      AuthService.logout();
      commit('logout');
    },

    register({ commit }, user) {
      return AuthService.register(user)
        .then((response) => {
          commit('registerSuccess');
          return Promise.resolve(response);
        })
        .catch((error) => {
          commit('registerFailure');
          return Promise.reject(error);
        });
    },

    registerBuyer({ commit }, buyer) {
      return AuthService.registerBuyer(buyer)
        .then((response) => {
          commit('registerBuyer', response);
          return Promise.resolve(response);
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },

    registerSeller({ commit }, info) {
      return AuthService.registerSeller(info)
        .then((response) => {
          commit('registerSeller', response);
          return Promise.resolve(response);
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },

    registerAddress({ commit }, address) {
      return AddressService.registerAddress(address)
        .then((response) => {
          commit('registerAddress', response);
          return Promise.resolve(response);
        })
        .catch((error) => {
          return Promise.reject(error);
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

    uploadImages({ commit }, productId, images) {
      return ProductService.uploadImages(productId, images)
        .then((response) => {
          commit('uploadImages', productId);
          return Promise.resolve(response);
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },
  },
};
