<template>
  <div class="profile">
    <Header
      :title="usernameCapitalized"
      subtitle="A dream profile page"
    />
    <div class="container extra-margin-bottom">
      <div class="columns is-centered">
        <div class="column is-half">
          <h1 class="title">
            <b-icon icon="account-circle" size="is-medium"></b-icon>
            {{ user_data.username }}
          </h1> 
          <hr>
          <p>Email: {{ user_data.email }}</p>  
          <p>First Name: {{ user_data.first_name }}</p> 
          <p>Last Name: {{ user_data.last_name }}</p> 
        </div>
      </div>
    </div>
    <b-loading :is-full-page="true" :active.sync="isLoading"></b-loading>
  </div>
</template>


<script>
import axios from 'axios'
import Header from '@/components/Header'

export default {
  name: 'Profile',
  components: {
    Header
  },
  data() {
    return {
      isLoading: false,
      id: this.$route.params.id,
      user_data: {}
    }
  },
  computed: {
    user() {
      return this.$store.state.user;
    },
    usernameCapitalized() {
      if (!(this.user.username == this.user_data.username)) {
        return this.capitalize(this.user_data.username) + '\'s profile';
      } else {
        return "Your profile";
      }
    }
  },
  methods: {
    capitalize(value) {
      if (!value) return ''
      value = value.toString()
      return value.charAt(0).toUpperCase() + value.slice(1)
    },
    fetchUser() {
      this.isLoading = true;
      const token = window.localStorage.getItem('authtoken');
      return axios({
        method: 'get',
        url: `http://${this.$store.state.domain}/api/users/` + this.id + '/',
        headers: {
          Authorization: `JWT ${token}`
        }
      })
        .then(response => {
          console.log(response.data);
          this.user_data = response.data;
          this.isLoading = false;
        })
        .catch(error => {
          if (error.response.status == 404) {
            this.$router.push({ name: '404' });
          }
        })
      ;
    }
  },
  beforeRouteUpdate(to, from, next) {
    this.id = to.params.id;
    this.fetchUser();
    next();
  },
  mounted() {
    this.fetchUser();
  }
}
</script>
