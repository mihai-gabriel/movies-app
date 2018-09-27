<template>
  <div class="movies">
    <Header
      title="Movies chapter"
      subtitle="I mean page"
    />
    <div class="container extra-margin-bottom">
      <div class="columns is-centered">
        <div class="column is-half">
          <ul>
            <li v-for="movie in movies" :key="movie.pk">
              <router-link
                tag="h1"
                class="title cursor-pointer"
                :to="{ name: 'movie', params: { id: movie.pk }}"
              >{{ movie.title }} </router-link>
              <h2 class="subtitle">{{ movie.author }}</h2> <br>
              <p>{{ movie.description }}</p>
              <hr>
            </li>
            <b-loading :is-full-page="true" :active.sync="isLoading"></b-loading>
          </ul>
           <b-pagination
            :total="total"
            :current.sync="current"
            :simple="false"
            :rounded="false"
            :per-page="perPage">
          </b-pagination>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Header from '@/components/Header'

export default {
  name: 'movies',
  data() {
    return {
      total: undefined,
      current: parseInt(this.$route.params.id),
      perPage: 5,
      isLoading: false,
      movies: []
    }
  },
  components: {
    Header
  },
  watch: {
    current(newValue, oldValue) {
      console.log(oldValue);
      this.$router.push({ name: 'movies', params: { id: newValue } });
    }
  },
  methods: {
    fetchMovies() {
      this.isLoading = true;
      return axios({
        method: 'get',
        url: 'http://localhost:8000/api/movies/?page=' + this.current
      })
        .then(response => {
          this.total = response.data.count;
          this.movies = response.data.results;
          this.isLoading = false;
        })
        .catch(error => {
          if (error.response.status == 404) {
            this.$router.push({ name: '404' });
          }
          this.isLoading = false;
          console.error(error);
        })
      ;
    }
  },
  beforeRouteUpdate(to, from, next) {
    this.fetchMovies();
    next();
  },
  mounted() {
    this.fetchMovies();
  }
}
</script>

<style scoped>
  .cursor-pointer {
    cursor: pointer;
  }
</style>
