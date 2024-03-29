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
    editAddress(state, { address, addressId }) {
      delete address.buyer;
      const addressIndex = state.buyer.addresses.findIndex(
        (address) => address.id == addressId
      );
      state.buyer.addresses[addressIndex] = address;
    },
    makeItMainAddress(state, addressId) {
      state.buyer.main_address_id = addressId;
    },
    deleteAddress(state, addressId) {
      if (state.buyer.main_address_id == addressId) {
        state.buyer.main_address_id = null;
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
    changeCartProductQuantity(state, { cartProductId, quantity }) {
      const cartProductIndex = state.buyer.shopping_cart.findIndex(
        (cartProduct) => cartProduct.id == cartProductId
      );
      state.buyer.shopping_cart[cartProductIndex].quantity = quantity;
    },
    removeFromCart(state, cartProductId) {
      state.buyer.shopping_cart = state.buyer.shopping_cart.filter(
        (cartProduct) => cartProduct.id != cartProductId
      );
    },
    removeManyFromCart(state, cartProductIds) {
      let cartProductIdsList = cartProductIds.split(',');
      state.buyer.shopping_cart = state.buyer.shopping_cart.filter(
        (cartProduct) => !cartProductIdsList.includes(cartProduct.id.toString())
      );
    },
    addOrders(state, newOrders) {
      state.buyer.orders = state.buyer.orders.concat(newOrders);
    },
    productArrives(state, orderId) {
      const orderIndex = state.buyer.orders.findIndex(
        (order) => order.id == orderId
      );
      state.buyer.orders[orderIndex].delivered = true;
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

    getUser({ commit }) {
      return AuthService.getUser()
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

    editUser({ commit }, user) {
      return AuthService.editUser(user)
        .then((response) => {
          commit('loginSuccess', response);
          return Promise.resolve(response);
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },

    registerBuyer({ commit }, name) {
      return AuthService.registerBuyer(name)
        .then((response) => {
          commit('registerBuyer', response);
          return Promise.resolve(response);
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },

    editName({ commit }, name) {
      return AuthService.editName(name)
        .then((response) => {
          commit('registerBuyer', response);
          return Promise.resolve(response);
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },

    registerSeller({ commit }, brand) {
      return AuthService.registerSeller(brand)
        .then((response) => {
          commit('registerSeller', response);
          return Promise.resolve(response);
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },

    editBrand({ commit }, brand) {
      return AuthService.editBrand(brand)
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
