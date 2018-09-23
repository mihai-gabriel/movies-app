<template>
  <div class="movie">
    <div class="container extra-margin-top extra-margin-bottom">
      <div class="columns">
        <div class="column">
          <h1 class="title" v-text="movie.title"></h1>
          <h2 class="subtitle" v-text="movie.author"></h2>
          <hr>
          <p v-text="movie.description"></p>
        </div>
      </div>
      <b-loading :is-full-page="true" :active.sync="isLoading"></b-loading>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'movie',
  data() {
    return {
      isLoading: false,
      id: this.$route.params.id,
      movie: {}
    }
  },
  methods: {
    fetchMovie() {
      const token = window.localStorage.getItem('authtoken');
      this.isLoading = true;
      return axios({
        method: 'get',
        url: 'http://localhost:8000/api/movies/' + this.id
      })
        .then(response => {
          this.movie = response.data;
          this.isLoading = false;
        })
        .catch(error => {
          if (error.response.status == 404) {
            this.$router.push({ name: '404' });
          }
          console.error(error);
        })
      ;
    }
  },
  mounted() {
    this.fetchMovie();
  }
}
</script>

<style>

</style>
