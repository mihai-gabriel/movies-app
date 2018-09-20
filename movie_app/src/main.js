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
  const token = window.localStorage.getItem('authtoken');
  const user = window.localStorage.getItem('user');
  if (!(user && token)) {
    store.dispatch('setAuth', false);
  } else {
    axios
      .post('http://localhost:8000/api/api-token-verify/', {
        token: token
      })
      .then(response => {
        window.localStorage.setItem('user', JSON.stringify(response.data.user));
        store.dispatch('setUser', JSON.parse(window.localStorage.getItem('user')));
      })
      .catch(() => {
        window.localStorage.clear();
        store.dispatch('setAuth', false);
      })
    store.dispatch('setAuth', true);
    next()
  }
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!(store.state.isAuth)) {
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
