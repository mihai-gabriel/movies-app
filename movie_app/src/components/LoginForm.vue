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
          window.localStorage.setItem('authtoken', response.data.token);
          window.localStorage.setItem('user', JSON.stringify(response.data.user));
          this.$parent.close();
          this.$router.go();
        })
        .catch(error => {
          alert(error.response.data.non_field_errors);
          console.error(error);
          this.isLoading = false;
        });
    }
  }
}
</script>

<style scoped>
</style>
