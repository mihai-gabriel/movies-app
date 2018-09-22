<template>
  <div class="profile">
    <Header
      :title="usernameCapitalized + '\'s profile'"
      subtitle="A dream profile page"
    />
    <div class="container">
      <div class="columns">
        <div class="column has-text-centered">
          Name: {{ user.username }} <br>
          Email: {{ user.email }} <br> 
          First Name: {{ user.first_name }} <br>
          Last Name: {{ user.last_name }} <br>
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
