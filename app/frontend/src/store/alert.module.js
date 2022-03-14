export const alert = {
  namespaced: true,
  state: {
    message: '',
  },
  mutations: {
    removeMessage(state) {
      state.message = '';
    },
    setMessage(state, value) {
      state.message = value;
    },
  },
  actions: {
    setMessage({ commit }, value) {
      if (value.toString() == 'Error: Network Error') {
        value = 'Server Error. Try again in a couple of seconds';
      }
      commit('setMessage', value);
    },
  },
};
