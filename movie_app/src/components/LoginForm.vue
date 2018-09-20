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

        <b-checkbox>Remember me</b-checkbox>
      </section>
      <footer class="modal-card-foot">
        <button class="button" type="button" @click="$parent.close()">Close</button>
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
      isLoading: false
    }
  },
  methods: {
    login() {
      this.isLoading = true;
      return axios({
        method: 'post',
        url: 'http://localhost:8000/api/api-token-auth/',
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
          this.$parent.close(); // closing login form modal
          this.$router.go(); // refreshing the page to update the state
        })
        .catch(error => {
          // usually username or password wrong, display the error
          alert(error.response.data.non_field_errors); // lazy method to display the error (temporary)
          console.error(error);
          this.isLoading = false; // allow the user to refill the form
        });
    }
  }
}
</script>

<style scoped>
</style>
