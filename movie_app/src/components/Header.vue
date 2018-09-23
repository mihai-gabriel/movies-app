<template>
  <section class="hero is-info">
    <div class="hero-body">
      <div class="container">
        <h1 class="title" v-text="title"></h1>
        <h2 class="subtitle" v-text="subtitle"></h2>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Header',
  props: {
    title: String,
    subtitle: String
  }
}
</script>

<style scoped>
  h1 {
    font-family: 'Proza Libre', Verdana, Geneva, Tahoma, sans-serif;
  }

  /* .oblique-hero {
    background-color: #34ADFF;
    background-image: -webkit-linear-gradient(150deg, #34ADFF 35%, #4CBFFF 35%);
  } */

  .hero {
    background: transparent;
  }

  .hero::before {
    content: url('../assets/header-vector.svg');
    position: absolute;
    top: 0;
    left: 0;
  }

  .hero-body {
    opacity: 0.95;
  }
</style>

