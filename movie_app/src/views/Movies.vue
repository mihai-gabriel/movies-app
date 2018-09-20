<template>
  <div class="movies">
    <Header
      title="You can see movies only if you are logged in"
      subtitle="Yeah, movies, man"
    />
  </div>
</template>

<script>
import Header from '@/components/Header'

export default {
  name: 'movies',
  components: {
    Header
  }
}
</script>

<style>

</style>
