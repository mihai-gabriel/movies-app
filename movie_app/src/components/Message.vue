<template>
  <div class="custom-message">
    <h1 class="title" v-text="title"></h1>
    <h2 class="subtitle" v-text="subtitle"></h2>
    <p><slot /></p>
  </div>
</template>

<script>
export default {
  name: 'Message',
  props: {
    title: String,
    subtitle: String
  }
}
</script>
