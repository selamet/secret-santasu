<template>

  <router-view/>

</template>

<script>
import Home from "./components/Home"

export default {
  name: 'app',
  data() {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  components: {
    Home: Home
  }
}
</script>

<style>

body {
    color: #666666;
    font-size: 15px;
    font-family: 'Poppins', sans-serif;
    line-height: 1.80857;
}


a {
    color: #1f1f1f;
    text-decoration: none !important;
    outline: none !important;
    -webkit-transition: all .3s ease-in-out;
    -moz-transition: all .3s ease-in-out;
    -ms-transition: all .3s ease-in-out;
    -o-transition: all .3s ease-in-out;
    transition: all .3s ease-in-out;
}

h2,

h6 {
    letter-spacing: 0;
    font-weight: normal;
    position: relative;
    padding: 0 0 10px 0;
    font-weight: normal;
    line-height: 120% !important;
    color: #1f1f1f;
    margin: 0
}



h2 {
    font-size: 22px
}



h1 a,
h2 a,
h3 a,
h4 a,
h5 a,
h6 a {
    color: #212121;
    text-decoration: none!important;
    opacity: 1
}

h1 a:hover,
h2 a:hover,
h3 a:hover,
h4 a:hover,
h5 a:hover,
h6 a:hover {
    opacity: .8
}

a {
    color: #1f1f1f;
    text-decoration: none;
    outline: none;
}

a,
.btn {
    text-decoration: none !important;
    outline: none !important;
    -webkit-transition: all .3s ease-in-out;
    -moz-transition: all .3s ease-in-out;
    -ms-transition: all .3s ease-in-out;
    -o-transition: all .3s ease-in-out;
    transition: all .3s ease-in-out;
}
</style>
