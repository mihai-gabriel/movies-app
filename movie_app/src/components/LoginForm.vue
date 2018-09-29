<template>
  <form action="">
    <div class="modal-card" style="width: auto">
      <header class="modal-card-head">
        <p class="modal-card-title">Login</p>
      </header>
      <section class="modal-card-body">
        <b-field label="Name">
          <b-input
              type="text"
              v-model="name"
              placeholder="Your name"
              required>
          </b-input>
        </b-field>

        <b-field label="Password">
          <b-input
              type="password"
              v-model="password"
              password-reveal
              placeholder="Your password"
              required>
          </b-input>
        </b-field>

        <b-checkbox v-model="rememberMe">Remember me</b-checkbox>
      </section>
      <footer class="modal-card-foot">
        <button
          class="button"
          type="button"
          @click="$store.dispatch('displayLoginModal', false)"
        >Close</button>
        <button class="button is-primary" @click.prevent="login()">Login</button>
      </footer>
      <b-loading :is-full-page="false" :active.sync="isLoading"></b-loading>
    </div>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginForm',
  data () {
    return {
      name: '',
      password: '',
      isLoading: false,
      rememberMe: false
    }
  },
  methods: {
    login() {
      if (this.name == '' || this.password == '') {
        this.$toast.open({
          message: 'No input provided',
          type: 'is-danger'
        });
        return null;
      }
      this.isLoading = true;
      return axios({
        method: 'post',
        url: `http://${this.$store.state.domain}/api/api-token-auth/`,
        data: {
          username: this.name,
          password: this.password
        },
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then(response => {
          // setting up the authentication variables
          window.localStorage.setItem('authtoken', response.data.token);
          window.localStorage.setItem('user', JSON.stringify(response.data.user));
          window.localStorage.setItem('csrf_token', response.data.csrf_token);
          this.$toast.open({
            duration: 950,
            message: 'Logged in successfully',
            type: 'is-success',
            queue: false,
          });
          window.setTimeout(() => {
            this.$store.dispatch('displayLoginModal', false); // closing login form modal
            const nextRoute = this.$store.state.nextURL;
            if (nextRoute != '') {
              this.$router.push({ path: nextRoute})
            }
            this.$router.go(); // refreshing the page to update the state
          }, 1100);
        })
        .catch(error => {
          // usually username or password wrong, display the error
          const error_message = error.response.data.non_field_errors[0];
          this.$toast.open({
            message: error_message,
            type: 'is-danger'
          });
          console.error(error);
          this.isLoading = false; // allow the user to refill the form
        });
    }
  }
}
</script>

<style scoped>
</style>
