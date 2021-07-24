<template>
  <div class="grid grid-cols-9 gap-10 ">
    <div class="col-start-2 col-end-4">
      <form class="bg-white shadow-md px-8 pt-6 pb-8 mb-4">
        <div class="mb-4">
          <label
            class="block text-gray-700 text-sm font-bold mb-2"
            for="username"
          >
            City Name
          </label>
          <input
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="username"
            type="text"
            placeholder="Username"
          />
        </div>
        <div class="mb-6">
          <label
            class="block text-gray-700 text-sm font-bold mb-2"
            for="password"
          >
            Place
          </label>
          <input
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="username"
            type="text"
            placeholder="Username"
          />
        </div>
      </form>
    </div>
    <div class="col-start-4 col-end-9 h-full">
      <div
        class=" container  max-w-md w-full bg-gray-900 shadow-lg rounded-xl p-6"
      >
        <div class="relative h-62 w-full mb-3">
          <img
            src="https://casco-media-prod.global.ssl.fastly.net/7b79bf78-62c4-5bc9-bfa3-df2adfd37e81/ea86a8907ddcc6f4af6445536e381ecf.jpg?width=600&auto=webp"
            alt="Just a flower"
            class="w-full object-fill rounded-2xl"
          />
        </div>
        <div class="flex-auto justify-evenly">
          <div class="flex flex-wrap">
            <div
              class="w-full flex-none text-sm flex items-center text-gray-600"
            >
              <span class="mr-2 text-gray-400">Amsterdam</span>
            </div>
            <div class="flex items-center w-full justify-between min-w-0">
              <h2
                class="
                    text-lg
                    mr-auto
                    cursor-pointer
                    text-gray-200
                    hover:text-purple-500
                    truncate
                  "
              >
                Apartment Bloemgracht 124 E
              </h2>
            </div>
          </div>
          <div class="text-xl text-white font-semibold mt-1">$240.00</div>
          <div class="flex space-x-2 text-sm font-medium justify-start">
            <button
              class="
                  transition
                  ease-in
                  duration-300
                  inline-flex
                  items-center
                  text-sm
                  font-medium
                  mb-2
                  md:mb-0
                  bg-purple-500
                  px-5
                  py-2
                  hover:shadow-lg
                  tracking-wider
                  text-white
                  rounded-full
                  hover:bg-purple-600
                "
            >
              <span>More</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
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
