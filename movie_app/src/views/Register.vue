<template>
  <div class="register">
    <Header
      title="Register"
      subtitle="The place where everything begins"
    />
    <div class="container extra-margin-top">
      <div class="columns is-centered">
        <div class="column is-half">
          <form
            action=""
            @submit.prevent=""
            class="extra-margin-bottom extra-margin-top"
          >
            <section>
              <b-field label="Username">
                <b-input
                  maxlength="30"
                  v-model="username"
                ></b-input>
              </b-field>
              

              <b-field label="Email">
                <b-input
                  type="email"
                  maxlength="30"
                  v-model="email"
                >
                </b-input>
              </b-field>

              <b-field label="First Name">
                  <b-input v-model="first_name"></b-input>
              </b-field>

              <b-field label="Last Name">
                  <b-input v-model="last_name"></b-input>
              </b-field>

              <b-field label="Password">
                <b-input
                  v-model="password"
                  password-reveal
                  type="password"
                  maxlength="30"
                ></b-input>
              </b-field>

              <button class="button is-primary" @click="submit()">
                Submit
              </button>
            </section>
          </form>
        </div>
      </div>
    </div>
    <b-loading :is-full-page="true" :active.sync="isLoading"></b-loading>
  </div>
</template>

<script>
import axios from 'axios';
import Header from '@/components/Header'

export default {
  name: 'register',
  components: {
    Header
  },
  data() {
    return {
      username: '',
      password: '',
      first_name: '',
      last_name: '',
      email: '',
      isLoading: false,
    }
  },
  methods: {
    submit() {
      this.isLoading = true;
      return axios({
        method: 'post',
        url: `http://${this.$store.state.domain}/api/users/`,
        data: {
          username: this.username,
          first_name: this.first_name,
          last_name: this.last_name,
          password: this.password,
          email: this.email
        },
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then(response => {
          if (response.status == 201) {
            this.clearInputs();
            this.$toast.open({
              duration: 1500,
              type: 'is-success',
              message: 'You just got a new account just now',
              queue: false
            });
            this.$toast.open({
              type: 'is-success',
              message: 'Go ahead, log in!'
            });
            this.isLoading = false;
            window.setTimeout(() => {
              this.$store.dispatch('displayLoginModal', true);
            }, 1500);
          }
        })
        .catch(error => {
          this.isLoading = false;
          let message = error.response.data.username;
          if (!message) {
            message = "An unexpected error occured during proccesing."
          }
          this.$toast.open({
            type: 'is-danger',
            message: `${message}`,
            queue: false
          });
          console.error(error);
        })
      ;
    },
    clearInputs() {
      this.username = '';
      this.password = '';
      this.first_name = '';
      this.last_name = '';
      this.email = '';
    }
  }
}
</script>
