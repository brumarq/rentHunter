<template>
  <div id="app">
    <Apartments />
  </div>
</template>

<script>
import Apartments from './components/Apartments'

export default {
  name: "App",
  components: {
    Apartments,
  },
};
</script>

<style src="./assets/tailwind.css"/>
<style>
body {
  background-image: url('https://images.unsplash.com/photo-1496163290419-406e5dd84a07?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1950&q=80');
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
