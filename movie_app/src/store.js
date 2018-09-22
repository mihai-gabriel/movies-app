import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isAuth: false,
    user: {},
    loginModalActive: false,
    nextURL: ''
  },
  mutations: {
    changeAuth(state, val) {
      state.isAuth = val;
    },
    updateUser(state, val) {
      state.user = val
    },
    showLoginModal(state, val) {
      state.loginModalActive = val;
    },
    setNextUrl(state, value) {
      state.nextURL = value;
    }
  },
  actions: {
    setAuth(context, value) {
      context.commit('changeAuth', value);
    },
    setUser(context, value) {
      context.commit('updateUser', value);
    },
    displayLoginModal(context, value) {
      context.commit('showLoginModal', value);
    },
    setNextURL(context, value) {
      context.commit('setNextUrl', value);
    },
    logoutUser() {
      window.localStorage.removeItem('authtoken');
      window.localStorage.removeItem('user');
      window.localStorage.removeItem('csrf_token');
    }
  }
})
