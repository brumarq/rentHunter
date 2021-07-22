<template>
  <div id="app">
    <Header />
    <Apartments />
  </div>
</template>

<script>
import Apartments from './components/Apartments'
import Header from './components/Header.vue';

export default {
  name: "App",
  components: {
    Header,
    Apartments
  },
};
</script>

<style src="./assets/tailwind.css"/>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
