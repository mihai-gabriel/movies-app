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
      <div class="columns is-centered">
        <div class="column is-three-fifths">

          <!-- Displaying Movie Data -->
          <a class="is-size-5 extra-padding-bottom" @click="$router.go(-1)">
            Back
          </a>
          <h1 class="title" v-text="movie.title"></h1>
          <h2 class="subtitle" v-text="movie.author"></h2>
          <hr>
          <p v-text="movie.description"></p>
        </div>
      </div>
      <hr>
      <h1 class="title has-text-centered">Reviews</h1>
      <div class="columns is-centered">
        <div class="column is-three-fifths">

          <!-- Listing reviews -->
          <div
            class="review extra-margin-bottom"
            v-for="review in movie.reviews"
            :key="review.pk"
          >
            <h1 class="title is-size-5" v-text="review.title"></h1>
            <router-link
              tag="h2" class="subtitle is-size-6 user_review"
              v-text="review.user_username"
              :to="{ name: 'profile', params: { id: review.user }}"
            ></router-link>
            <p v-text="review.review_text"></p>
          </div>
          <hr>

          <!-- Review Form -->
          <form
            action=""
            @submit.prevent=""
          >
            <section>
              <h2 class="subtitle">Add your review</h2>
              <b-field horizontal label="Title">
                  <b-input v-model="review_title" name="title" expanded required></b-input>
              </b-field>


              <b-field horizontal label="Message">
                  <b-input v-model="review_text" type="textarea" required></b-input>
              </b-field>

              <b-field horizontal><!-- Label left empty for spacing -->
                  <p class="control">
                      <button class="button is-primary" @click="submit">
                        Send review
                      </button>
                  </p>
              </b-field>
            </section>
          </form>
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
      movie: {},
      // review data
      review_title: '',
      review_text: '',
      newData: 0,
    }
  },
  computed: {
    user() {
      return this.$store.state.user;
    }
  },
  watch: {
    newData(newValue, oldValue) {
      console.log(oldValue);
      this.fetchMovie();
    }
  },
  methods: {
    fetchMovie() {
      this.isLoading = true;
      return axios({
        method: 'get',
        url: `http://${this.$store.state.domain}/api/movies/` + this.id + '/'
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
    },

    submit() {
      this.isLoading = true;
      const token = window.localStorage.getItem('authtoken');
      return axios({
        method: 'post',
        url: `http://${this.$store.state.domain}/api/reviews/`,
        data: {
          title: this.review_title,
          movie: this.id,
          review_text: this.review_text,
          user: this.user.pk
        },
        headers: {
          'Content-Type': 'application/json',
          Authorization: `JWT ${token}`
        }
      })
        .then(response => {
          this.isLoading = false;
          this.newData++;
          this.review_title = '';
          this.review_text = '';
          console.log(response);
          
          this.$toast.open({
            duration: 2000,
            message: "Your reviews has been posted successfully!",
            type: 'is-success',
            queue: false,
          });
        })
        .catch(error => {
          this.$toast.open({
            duration: 2000,
            message: "An error occured during your review submission!",
            type: 'is-danger',
            queue: false,
          });
          this.isLoading = false;
          console.error(error.response);
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

  .user_review {
    color: #0074D9;
    cursor: pointer;
  }
</style>
