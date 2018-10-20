/* eslint-disable no-shadow */
// modules hold user information

const state = {
  userName: '',
  userEmail: '',
  userPhotoUrl: '',
};

const getters = {
  getUserName: state => state.userName,
  getUserEmail: state => state.userEmail,
  getUserPhotoUrl: state => state.userPhotoUrl,
};

const mutations = {
  setUserName: (state, payload) => {
    state.userName = payload;
  },
  setUserEmail: (state, payload) => {
    state.userEmail = payload;
  },
  setUserPhotoUrl: (state, payload) => {
    state.userPhotoUrl = payload;
  },
};

const actions = {
  actionUserName: ({ commit }, payload) => {
    commit('setUserName', payload);
  },
  actionUserEmail: ({ commit }, payload) => {
    commit('setUserEmail', payload);
  },
  actionUserPhotoUrl: ({ commit }, payload) => {
    commit('setUserPhotoUrl', payload);
  },
};

export default {
  state,
  mutations,
  actions,
  getters,
};
