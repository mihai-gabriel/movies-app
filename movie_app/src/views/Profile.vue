<template>
  <div class="profile">
    <Header
      :title="usernameCapitalized + '\'s profile'"
      subtitle="A dream profile page"
    />
    <div class="container extra-margin-bottom">
      <div class="columns is-centered">
        <div class="column is-half">
          <h1 class="title">
            <b-icon icon="account-circle" size="is-medium"></b-icon>
            {{ user.username }}
          </h1> 
          <hr>
          <p>Email: {{ user.email }}</p>  
          <p>First Name: {{ user.first_name }}</p> 
          <p>Last Name: {{ user.last_name }}</p> 
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import Header from '@/components/Header'

export default {
  name: 'Profile',
  components: {
    Header
  },
  computed: {
    user() {
      return this.$store.state.user;
    },
    usernameCapitalized() {
      return this.capitalize(this.user.username);
    }
  },
  methods: {
    capitalize(value) {
      if (!value) return ''
      value = value.toString()
      return value.charAt(0).toUpperCase() + value.slice(1)
    }
  },
}
</script>
