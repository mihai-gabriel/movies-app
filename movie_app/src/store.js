import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isAuth: false,
    user: {}
  },
  mutations: {
    changeAuth(state, val) {
      state.isAuth = val;
    },
    updateUser(state, val) {
      state.user = val
    }
  },
  actions: {
    setAuth(context, value) {
      context.commit('changeAuth', value);
    },
    setUser(context, value) {
      context.commit('updateUser', value);
    }
  }
})
