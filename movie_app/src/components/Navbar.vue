<template>
  <div>
    <nav class="navbar is-black">
      <div class="container">
        <div class="navbar-brand">
          <router-link class="navbar-item" :to="{ name: 'home' }">
            <b-icon icon="folder-open" ></b-icon>
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
              <b-icon icon="filmstrip"></b-icon>
              <span class="icon-margin">Movies</span>
            </router-link>
          </div>
        </div>

        <div class="navbar-menu">
          <div class="navbar-end">
            <template v-if="isAuth">
              <router-link class="navbar-item" :to="{name: 'profile'}">
                <b-icon icon="account-outline"></b-icon>
                <span class="icon-margin" v-text="user.username"></span>
              </router-link>
              <a class="navbar-item" @click="logout()">
                <b-icon icon="account-outline"></b-icon>
                <span class="icon-margin">Logout</span>
              </a>
            </template>
            <template v-else>
              <a class="navbar-item" @click="isComponentModalActive = true" >
                <b-icon icon="account-outline"></b-icon>
                <span class="icon-margin">Login</span>
              </a>
            </template>
          </div>
        </div>
      </div>
    </nav>
    <b-modal :active.sync="isComponentModalActive" has-modal-card>
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
    }
  },
  methods: {
    logout() {
      window.localStorage.clear();
      this.$router.go();
    }
  }
}
</script>

<style>
  .logo-title {
    font-family: 'Capriola', Verdana, Geneva, Tahoma, sans-serif;
    margin: 0 0.5em;
  }

  .icon-margin {
    margin: 0 0.3em;
  }
</style>

