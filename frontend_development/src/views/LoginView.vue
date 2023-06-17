<template>
  <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
      <div class="main-left">
          <div class="p-12 bg-white border border-gray-200 rounded-lg">
              <h1 class="mb-6 text-2xl">Log in</h1>

              <p class="mb-6 text-gray-500">
                  Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ullam, architecto incidunt esse consectetur rem libero ducimus, 
                  ipsam illo aliquam dolorum nisi labore quidem? Soluta non, quaerat placeat ex magni mollitia!
              </p>

              <p class="font-bold">
                  Don't have an account? <RouterLink :to="{'name': 'signup'}" class="underline">Click here</RouterLink> to create one!
              </p>
          </div>
      </div>

      <div class="main-right">
          <div class="p-12 bg-white border border-gray-200 rounded-lg">
              <form class="space-y-6">
                  <div>
                      <label>Email</label>
                      <input type="email" placeholder="Your email address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                  </div>
                  <div>
                      <label>Password</label>
                      <input type="password" placeholder="Your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                  </div>
                  <div>
                      <button class="py-4 px-6 bg-green-600 text-white rounded-lg">Log in</button>
                  </div>
              </form>
          </div>
      </div>
  </div>


</template>

<script>

</script>

<style>

</style>