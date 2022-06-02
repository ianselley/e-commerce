export const modal = {
  namespaced: true,
  state: {
    active: false,
  },
  mutations: {
    activateModal(state) {
      state.active = true;
    },
    deactivateModal(state) {
      state.active = false;
    },
  },
  actions: {},
};
