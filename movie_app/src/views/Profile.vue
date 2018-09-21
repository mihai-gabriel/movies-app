<template>
  <div class="profile">
    <Header
      :title="usernameCapitalized + '\'s profile'"
    />
    <div class="container">
      Name: {{ user.username }} <br>
      Email: {{ user.email }} <br> 
      First Name: {{ user.first_name }} <br>
      Last Name: {{ user.last_name }} <br>
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
