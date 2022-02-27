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
};
