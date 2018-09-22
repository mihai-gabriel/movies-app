<template>
  <div>
    <nav class="navbar is-black">
      <div class="container">
        <div class="navbar-brand">
          <router-link
            class="navbar-item"
            :to="{ name: 'home' }"
            exact-active-class=""
          >
            <b-icon icon="settings"></b-icon>
            <h2 class="logo-title" v-text="title"></h2>
          </router-link>
          <div class="navbar-burger burger">
            <span></span>
            <span></span>
            <span></span>
          </div>
        </div>

        <div class="navbar-menu">
          <div class="navbar-start">
            <router-link class="navbar-item" :to="{ name: 'movies' }">
              <span class="icon-margin">Movies</span>
            </router-link>
          </div>
        </div>

        <div class="navbar-menu">
          <div class="navbar-end">
            <template v-if="isAuth">
              <router-link class="navbar-item user-profile" :to="{ name: 'profile' }">
                <span class="icon-margin" v-text="user.username"></span>
              </router-link>
              <a class="navbar-item" @click="logout()">
                <span class="icon-margin">Logout</span>
              </a>
            </template>
            <template v-else>
              <a class="navbar-item" @click="showLoginModal()" >
                <span class="icon-margin">Login</span>
              </a>
            </template>
          </div>
        </div>
      </div>
    </nav>
    <b-modal :active.sync="loginModal" has-modal-card>
      <login-form></login-form>
    </b-modal>
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm'

export default {
  name: 'Navbar',
  props: {
    title: String
  },
  components: {
    LoginForm
  },
  data() {
    return {
      isComponentModalActive: false
    }
  },
  computed: {
    user() {
      return this.$store.state.user;
    },
    isAuth() {
      return this.$store.state.isAuth;
    },
    loginModal: {
      get() {
        return this.$store.state.loginModalActive;
      },
      set(newValue) {
        this.$store.dispatch('displayLoginModal', newValue); // define the way the value should be
                                                             // changed
      }
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('logoutUser');
      this.$toast.open({
        duration: 950,
        message: 'Logged out successfully',
        type: 'is-info'
      });
      window.setTimeout(() => {
        if (this.$router.currentRoute.name != 'home') {
          this.$router.push({ name: 'home' }); // going to a page available as guest
        } else {
          this.$router.go();
        }
      }, 1100);
    },
    showLoginModal() {
      return this.$store.dispatch('displayLoginModal', true);
    }
  }
}
</script>

<style>
  .logo-title {
    font-family: 'Capriola', Verdana, Geneva, Tahoma, sans-serif;
    margin: 0 0.5em;
  }

  .navbar {
    font-family: 'Nanum Gothic', sans-serif !important;
  }
  
  .navbar::before {
    content: url('../assets/navbar-sub.svg');
    position: absolute;
    top: 100%;
    left: 30%;
  }

  .icon-margin {
    margin: 0 0.3em;
  }

</style>

