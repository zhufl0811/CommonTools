<template>
  <div id="app">
    <div id="nav">
      <router-link to="/login">Login</router-link>
      <router-link to="/model">Model</router-link>
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>
