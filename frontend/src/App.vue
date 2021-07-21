<template>
  <div id="app">
    <table>
      <thead>
        <th>Title</th>
        <th>Price</th>
      </thead>
      <tbody>
        <tr v-for="apartment in apartments" :key="apartment.id">
          <td>{{ apartment.title }}</td>
          <td>{{ apartment.price }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      apartments: [],
    };
  },
  async created(){
    var response = await fetch('http://127.0.0.1:8000/api/apartments/');
    this.apartments = await response.json();
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
