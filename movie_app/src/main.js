import 'buefy/dist/buefy.css'

import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Buefy from 'buefy'
import axios from 'axios'

Vue.use(Buefy)

Vue.config.productionTip = false

axios.defaults.headers.post['X-CSRFToken'] = window.localStorage.getItem('csrf_token');
// axios.defaults.headers.get['Authorization'] = `JWT ${window.localStorage.getItem('token')}`;


// Middleware
router.beforeEach((to, from, next) => {
  // check if the server is available
  axios
    .get('http://localhost:8000/')
    .catch(error => {
      console.log(error);
      Vue.prototype.$toast.open({
        duration: 2000 * 1000,
        message: "Unable to fetch data from the server",
        type: 'is-danger',
      });
    })
  // getting authentication proof
  const token = window.localStorage.getItem('authtoken');
  const user = window.localStorage.getItem('user');


  if (!(user && token)) { // check if authentication proof exists
    store.dispatch('setAuth', false);
    const check_first_time = window.localStorage.getItem('notFirstTime');
    if (!to.meta.requiresAuth && !check_first_time) { // if someones click an unauthorized link, 
      Vue.prototype.$snackbar.open({ // it will stack snackbars without this condition
        duration: 6000,
        message: 'To gain full access, please log in',
        type: 'is-info',
        actionText: 'OK',
        position: 'is-bottom-right',
      });
      window.localStorage.setItem('notFirstTime', true); // prevent snackbar showing again
    }
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
        store.dispatch('logoutUser');
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
      Vue.prototype.$toast.open({
        duration: 2000,
        message: "Not authorized. Please, log in",
        type: 'is-danger',
        queue: false,
      });
      window.setTimeout(() => {
        store.dispatch('setNextURL', to.fullPath);
        store.dispatch('displayLoginModal', true);
      }, 500);
      next({
        name: 'home'
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
