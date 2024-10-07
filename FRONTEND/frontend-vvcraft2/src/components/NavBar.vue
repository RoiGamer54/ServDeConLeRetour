<template>
  <div class="top">
    <nav class="navbar">
      <div class="logo">
        <router-link to="/">Logo</router-link> 
      </div>
      <ul class="nav-links">
        <li><router-link to="/">Accueil</router-link></li> 
        <li><router-link to="/serveurs">Serveurs</router-link></li> 
        <li><router-link to="/test">Images</router-link></li> 
        <li><router-link to="/contact">Contact</router-link></li> 
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
}
</script>