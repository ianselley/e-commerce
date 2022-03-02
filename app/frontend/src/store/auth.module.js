import AuthService from '@/services/auth.service';
import { useCookies } from 'vue3-cookies';

const { cookies } = useCookies();
const user = cookies.get('user');

const initialState = user
  ? { loggedIn: true, user }
  : { loggedIn: false, user: null };

export const auth = {
  namespaced: true,
  state: initialState,
  mutations: {
    registerSuccess(state) {
      state.loggedIn = false;
    },
    registerFailure(state) {
      state.loggedIn = false;
    },
    registerBuyer(state, buyer) {
      state.user.buyer = buyer;
    },
    registerSeller(state, seller) {
      state.user.seller = seller;
    },
    loginSuccess(state, user) {
      state.loggedIn = true;
      state.user = user;
    },
    loginFailure(state) {
      state.loggedIn = false;
      state.user = null;
    },
    logout(state) {
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

    registerSeller({ commit }, info) {
      return AuthService.registerSeller(info)
        .then((response) => {
          console.log(response);
          commit('registerSeller', response);
          return Promise.resolve(response);
        })
        .catch((error) => {
          return Promise.reject(error);
        });
    },
  },
};
