<template>
  <div id="app">
    <NavBar />
    <router-view />
  </div>
</template>

<script>
import './css/styles.css';
import NavBar from './components/NavBar.vue';

export default {
  name: 'App',
  components: {
    NavBar,
  }
}
</script>

