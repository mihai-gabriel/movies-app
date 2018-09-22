<template>
  <div class="movies">
    <Header
      title="Movies chapter"
      subtitle="I mean page"
    />
  </div>
</template>

<script>
import axios from 'axios'
import Header from '@/components/Header'

export default {
  name: 'movies',
  data() {
    return {
      movies: []
    }
  },
  components: {
    Header
  },
  methods: {
    fetchMovies() {
      return axios({
        method: 'get',
        url: 'http://localhost:8000/api/movies/',
      })
        .then(response => {
          this.movies = response.data;
        })
      ;
    }
  },
  mounted() {
    this.fetchMovies();
  }
}
</script>

<style>

</style>
