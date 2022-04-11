import { useCookies } from 'vue3-cookies';

import AuthService from '@/services/auth.service.js';

const { cookies } = useCookies();
const user = cookies.get('user');
let buyer, seller;
try {
  buyer = JSON.parse(localStorage.getItem('buyer'));
  seller = JSON.parse(localStorage.getItem('seller'));
} catch {
  buyer = undefined;
  seller = undefined;
}
let userRole;

if (user && user.role == 'buyer') {
  userRole = 'buyer';
} else if (user && user.role == 'seller') {
  userRole = 'seller';
} else {
  userRole = 'user';
}

const initialState = user
  ? { loggedIn: true, loggedInAs: userRole, user, buyer, seller }
  : { loggedIn: false, loggedInAs: null, user: null, buyer, seller };

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
      state.buyer = buyer;
    },
    registerSeller(state, seller) {
      state.loggedInAs = 'seller';
      state.seller = seller;
    },
    registerAddress(state, address) {
      state.buyer.main_address_id = address.buyer.main_address_id;
      delete address.buyer;
      state.buyer.addresses.push(address);
      state.addedAddress = true;
    },
    makeItMainAddress(state, addressId) {
      state.buyer.main_address_id = addressId;
    },
    deleteAddress(state, addressId) {
      if (state.buyer.main_address_id == addressId) {
        this.commit('makeItMainAddress', null);
      }
      state.buyer.addresses = state.buyer.addresses.filter(
        (address) => address.id != addressId
      );
    },
    resetAddedAddress(state) {
      state.addedAddress = false;
    },
    loginSuccess(state, user) {
      if (user.role == 'seller') {
        state.loggedInAs = 'seller';
        if (user.seller) {
          delete user.seller.products;
        }
        state.seller = user.seller;
      } else if (user.role == 'buyer') {
        state.loggedInAs = 'buyer';
        state.buyer = user.buyer;
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
      state.buyer = null;
      state.seller = null;
    },
    logout(state) {
      state.loggedInAs = null;
      state.loggedIn = false;
      state.user = null;
      state.buyer = null;
      state.seller = null;
    },
    addToCart(state, cartProduct) {
      state.buyer.shopping_cart.push(cartProduct);
    },
    removeFromCart(state, cartProductId) {
      state.buyer.shopping_cart = state.buyer.shopping_cart.filter(
        (cartProduct) => cartProduct.id != cartProductId
      );
    },
  },

  actions: {
    login({ commit }, user) {
      return AuthService.login(user)
        .then((response) => {
          commit('loginSuccess', response);
          return Promise.resolve(response);
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
  },
};
