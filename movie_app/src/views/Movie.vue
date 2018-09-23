<template>
  <div class="movie">
    <section class="hero is-black">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered">
            <div class="column has-text-centered">
             <b-icon icon="video" class="icon-large" size="is-large"></b-icon>
             <h1 class="title">Movie Details</h1>
            </div>
          </div>
        </div>
      </div>
    </section>
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
  .icon-large .mdi-video::before {
    font-size: 100px !important;
  }

  .extra-left-padding {
    padding-left: 80px;
  }
</style>
