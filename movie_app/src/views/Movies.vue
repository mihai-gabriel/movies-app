<template>
  <div class="movies" v-cloak>
    <Header
      title="Movies chapter"
      subtitle="I mean page"
    />
    <div class="container">
      <div class="columns is-centered">
        <div class="column is-half">
          <ul>
            <li v-for="movie in movies" :key="movie.id">
              <h1 class="title">{{ movie.title }}</h1>
              <h2 class="subtitle">{{ movie.author }}</h2> <br>
              <p>{{ movie.description }}</p>
              <hr>
            </li>
            <b-loading :is-full-page="true" :active.sync="isLoading"></b-loading>
          </ul>
          <nav
            v-if="(nextPage || previousPage)"
            class="pagination extra-margin-bottom"
            role="navigation"
            aria-label="pagination"
          >
            <a
              class="pagination-previous"
              v-if="previousPage"
              @click="getPage(previousPage)"
            >Previous</a>
            <a
              class="pagination-next"
              v-if="nextPage"
              @click="getPage(nextPage)"
            >Next</a>
            <!-- <ul class="pagination-list">
              <li>
                <a class="pagination-link is-current" aria-label="Page 1" aria-current="page">1</a>
              </li>
              <li>
                <a class="pagination-link" aria-label="Page 2" aria-current="page">2</a>
              </li>
            </ul> -->
          </nav>
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
      total: 2,
      current: 1,
      perPage: 5,
      previousPage: null,
      nextPage: null,
      isLoading: false,
      movies: []
    }
  },
  components: {
    Header
  },
  methods: {
    fetchMovies() {
      const token = window.localStorage.getItem('authtoken');
      this.isLoading = true;
      return axios({
        method: 'get',
        url: 'http://localhost:8000/api/movies/',
        headers: {
          Authorization: `JWT ${token}`,
        }
      })
        .then(response => {
          this.movies = response.data.results;
          this.total = response.data.count;
          this.nextPage = response.data.next;
          this.isLoading = false;
        })
        .catch(error => {
          console.error(error);
        })
      ;
    },
    getPage(URL) {
      const token = window.localStorage.getItem('authtoken');
      this.isLoading = true;
      return axios({
        method: 'get',
        url: URL,
        headers: {
          Authorization: `JWT ${token}`,
        }
      })
        .then(response => {
          this.movies = response.data.results;
          this.nextPage = response.data.next;
          this.previousPage = response.data.previous;
          this.isLoading = false
        })
        .catch(error => {
          console.error(error);
        });
    }
  },
  mounted() {
    this.fetchMovies();
  }
}
</script>

<style>

</style>
