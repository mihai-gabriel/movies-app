<template>
  <div class="home">
    <Header
      title="Movie app"
      subtitle="Don't really care about design"
    />
    <div class="container">
      <div class="columns is-centered extra-margin-top">
        <div class="column is-two-fifths">
          <Message title="Introducing..." subtitle="A Vue.js Project">
            This is my first project on which I've been working for some time. I hope you like it.
            It is not finished at the time I'm writing this, not even started, but I hope this will
            be a successful project for starters. Don't judge me on it.
            I'm using Buefy(Bulma.io) as CSS framework and Vue as JS framework.
            I will be using django as backend framework.
            So... Lorem, ipsum dolor sit amet
          </Message>
        </div>
        <div class="column is-one-quarter">
          <figure class="image">
            <img src="../assets/owl.jpg" class="owl-image" alt="">
          </figure>
        </div>
      </div>
      <div class="extra-margin-bottom"></div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Message from '@/components/Message'
import Header from '@/components/Header'

export default {
  name: 'home',
  components: {
    Message,
    Header
  }
}
</script>

<style scoped>
  .extra-margin-top {
    margin-top: 2em;
  }
  .extra-margin-bottom {
    margin-bottom: 6em;
  }
  .owl-image {
    opacity: 0.7;
  }
</style>
