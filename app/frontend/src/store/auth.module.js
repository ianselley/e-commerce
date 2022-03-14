import AuthService from '@/services/auth.service';
import { useCookies } from 'vue3-cookies';

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
      if (!state.user.buyer.mainAddressId) {
        state.user.buyer.mainAddressId = address.buyer.mainAddressId;
      }
      state.addedAddress = true;
    },
    resetAddedAddress(state) {
      state.addedAddress = false;
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
      return AuthService.registerAddress(address)
        .then((response) => {
          commit('registerAddress', response);
          return Promise.resolve(response);
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },
  },
};
