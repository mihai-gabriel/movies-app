<template>
  <div class="profile">
    <div class="container">
      Name: {{ user.username }} <br>
      Email: {{ user.email }} <br> 
      First Name: {{ user.first_name }} <br>
      Last Name: {{ user.last_name }} <br>
    </div>
  </div>
</template>


<script>
export default {
  name: 'Profile',
  computed: {
    user() {
      return this.$store.state.user;
    }
  }
}
</script>
