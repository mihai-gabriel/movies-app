<template>
  <div id="app">
    <Navbar title="/Movie dir/" />
    <transition name="fade" mode="out-in">
      <router-view/>
    </transition>    
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

  .router-link-exact-active {
    border-bottom: 2px solid #fff;
  }
</style>
