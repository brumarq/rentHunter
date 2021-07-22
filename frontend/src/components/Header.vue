<template>
  <nav class="inset-x-0 top-0 bg-white shadow-lg">
    <div class="md:flex items-center justify-between py-2 px-8 md:px-12">
      <div class="flex justify-between items-center">
        <div class="text-2xl font-bold text-gray-800 md:text-3xl">
          <a href="#">RentHunter</a>
        </div>
        <div>
            <a
          href="#"
          class="text-gray-800 rounded hover:bg-gray-900 hover:text-gray-100 hover:font-medium py-2 px-2 md:mx-2"
          >Apartments</a
        >
        <a
          href="#"
          class="text-gray-800 rounded hover:bg-gray-900 hover:text-gray-100 hover:font-medium py-2 px-2 md:mx-2"
          >Houses</a
        >
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Apartments",
  props: {
    msg: String,
  },

  data() {
    return {
      apartments: [],
    };
  },
  async created() {
    var response = await fetch("http://127.0.0.1:8000/api/apartments/");
    this.apartments = await response.json();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
