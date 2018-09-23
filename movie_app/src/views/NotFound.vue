<template>
  <div class="notfound">
    <Header
      title="404"
      subtitle="Not Found"
    />
    <div class="container extra-margin-bottom">
      <div class="columns is-centerd">
        <div class="column has-text-centered">
          <b-icon icon="magnify" class="magnify-class" size="is-large"></b-icon>
          <h1 class="title">The page you are looking <br> for is not longer here</h1>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from '@/components/Header';

export default {
  name: 'NotFound',
  components: {
    Header
  }
}
</script>

<style>
  .magnify-class .mdi-magnify::before {
    font-size: 140px !important
  }
</style>

