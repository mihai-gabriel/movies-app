<template>
  <div class="forbidden">
    <Header
      title="403"
      subtitle="Forbidden"
    />
    <div class="container extra-margin-top extra-margin-bottom">
      <div class="columns is-centered">
        <div class="column is-half">
          <section class="has-text-centered" >
            <b-icon class="icon-large" icon="security-lock" size="is-large"></b-icon>
            <h1 class="title">Please log in first</h1>
            <h2 class="subtitle">You are not authorized to access {{ path }}</h2>
          </section>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from '@/components/Header'

export default {
  name: 'Forbidden',
  components: {
    Header
  },
  computed: {
    path() {
      if(!this.$route.params.path_to) {
        return "this page";
      }
      return this.$route.params.path_to;
    }
  }
}
</script>

<style>
  .icon-large .mdi-security-lock::before {
    font-size: 140px !important
  }

  .icon-large {
    margin-bottom: 4em !important;
  }
</style>
