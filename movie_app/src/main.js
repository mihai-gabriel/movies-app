import 'buefy/dist/buefy.css'

import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Buefy from 'buefy'
import axios from 'axios'

Vue.use(Buefy)

Vue.config.productionTip = false

router.beforeEach((to, from, next) => {
  // getting authentication proof
  const token = window.localStorage.getItem('authtoken');
  const user = window.localStorage.getItem('user');
  if (!(user && token)) { // check if authentication proof exists
    store.dispatch('setAuth', false);
  } else {
    // check if jwt token is still available for every request
    axios
      .post('http://localhost:8000/api/api-token-verify/', {
        token: token
      })
      .then(response => {
        // check user object state for every request then update vuex user object
        window.localStorage.setItem('user', JSON.stringify(response.data.user));
        store.dispatch('setUser', JSON.parse(window.localStorage.getItem('user')));
      })
      .catch(() => {
        // if jwt token expired, logout the user
        window.localStorage.clear();
        store.dispatch('setAuth', false);
      })
    // keep user authenticated if everything ran fine
    store.dispatch('setAuth', true);
    next()
  }
  // check for pages that requires authentication
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!(store.state.isAuth)) {
      // not authenticated, to go first page (temporary)
      next({
        path: '/',
      })
    } else {
      next()
    }
  } else {
    next()
  }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
