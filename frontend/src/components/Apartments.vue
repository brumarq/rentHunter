<template>
  <div class="grid grid-cols-9 gap-10 grid-flow-col">
    <div class="col-start-2 col-end-9 mt-6">
      <h1 class="text-5xl">Apartments</h1>
    </div>
    <div class="grid col-start-2 col-end-4 row-span-3">
      <form class="bg-white shadow-lg px-8 pt-6 pb-8 mb-4 ">
        <div class="mb-4">
          <label
            class="block text-gray-700 text-sm font-bold mb-2"
            for="username"
          >
            City Name
          </label>
          <input
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="city_name"
            type="text"
            placeholder="Text"
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
            id="place"
            type="text"
            placeholder="Text"
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
            id="place"
            type="text"
            placeholder="Text"
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
            id="place"
            type="text"
            placeholder="Text"
          />
        </div>
      </form>
    </div>
    <div class="col-start-4 col-end-9 h-full">
      <div class="max-w-sm h-full w-full lg:max-w-full lg:flex shadow-lg">
        <div
          class="h-full lg:h-auto lg:w-2/6 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden"
          style="background-image: url('https://casco-media-prod.global.ssl.fastly.net/7b79bf78-62c4-5bc9-bfa3-df2adfd37e81/ea86a8907ddcc6f4af6445536e381ecf.jpg?width=600&auto=webp')"
          title="Woman holding a mug"
        ></div>
        <div
          class="border-r border-b border-l lg:border-l-0 lg:border-t  bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal"
        >
          <div class="mb-8">
            <div class="text-gray-900 font-bold text-xl mb-2">
              Can coffee make you a better developer?
            </div>
            <p class="text-gray-700 text-base">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit.
              Voluptatibus quia, nulla! Maiores et perferendis eaque,
              exercitationem praesentium nihil.
            </p>
          </div>
          <div class="flex items-center">
            <div class="text-sm">
              <p class="text-gray-900 leading-none">Jonathan Reinink</p>
              <p class="text-gray-600">Aug 18</p>
            </div>
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
