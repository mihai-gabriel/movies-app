<template>
  <div id="app">
    <div v-cloak>
      <Navbar title="PROJECT TITLE" />
      <transition name="fade" mode="out-in">
        <router-view/>
      </transition>    
      <footer class="footer">
        <div class="content has-text-centered">
          <a href="https://bulma.io/" target="_blank">
            <img
              src="https://bulma.io/images/made-with-bulma--white.png"
              width="304"
              height="57"
            />
          </a>

        </div>
      </footer>
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar'

export default {
  components: {
    Navbar,
  }
}
</script>

<style>
  html {
    overflow-y: auto !important;
  }

  [v-cloak] {
    display: none;
  }

  body {
    font-family: 'Karla', BlinkMacSystemFont, -apple-system,
    "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell",
    "Fira Sans", "Droid Sans", "Helvetica Neue", "Helvetica",
    "Arial", sans-serif;
  }

  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.2s
  }

  .fade-enter, .fade-leave-active {
    opacity: 0
  }

  .toast.is-info {
    background-color: #1f7da8 !important;
  }

  .footer {
    background-color: #0c0c0c;
  }

  .extra-margin-top {
    margin-top: 2em;
  }
  .extra-margin-bottom {
    margin-bottom: 6em;
  }

  /* .router-link-exact-active {
    border-bottom: 2px solid #fff;
  } */
</style>
