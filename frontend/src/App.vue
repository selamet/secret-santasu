<template>
  <div>
    <router-view />
    <div class="select">
      <div class="select-wrapper">
        <select v-model="lang">
          <option value="tr">TR</option>
          <option value="en">EN</option>
        </select>
      </div>
    </div>
  </div>
</template>

<script>
import Home from "./components/Home";

export default {
  name: "app",
  data() {
    return {
      lang: localStorage.getItem('lang') ? localStorage.getItem('lang') : 'tr',
    };
  },
  watch: {
    lang(val) {
      localStorage.setItem('lang', val);
      window.location.reload();
    }
  },
  components: {
    Home: Home,
  },
};
</script>

<style>
.select {
  position: fixed;
  bottom: 10px;
  right: 10px;
}

.select-wrapper {
  position: relative;
}

.select-wrapper select {
  -webkit-appearance: none;
  appearance: none;
  padding: 5px 30px 5px 20px;
  border: none;
  border-radius: 4px;
  box-shadow: 0 1px 5px rgb(0 0 0 / 20%);
  appearance: none;
}

.select-wrapper::after {
  content: "▼";
  font-size: 1rem;
  top: 12px;
  right: 10px;
  position: absolute;
}

body {
  color: #666666;
  font-size: 15px;
  font-family: "Poppins", sans-serif;
  line-height: 1.80857;
}

input,
select,
textarea {
  outline: none !important;
}

a {
  color: #1f1f1f;
  text-decoration: none !important;
  outline: none !important;
  -webkit-transition: all 0.3s ease-in-out;
  -moz-transition: all 0.3s ease-in-out;
  -ms-transition: all 0.3s ease-in-out;
  -o-transition: all 0.3s ease-in-out;
  transition: all 0.3s ease-in-out;
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
  margin: 0;
}

h2 {
  font-size: 22px;
}

h1 a,
h2 a,
h3 a,
h4 a,
h5 a,
h6 a {
  color: #212121;
  text-decoration: none !important;
  opacity: 1;
}

h1 a:hover,
h2 a:hover,
h3 a:hover,
h4 a:hover,
h5 a:hover,
h6 a:hover {
  opacity: 0.8;
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
  -webkit-transition: all 0.3s ease-in-out;
  -moz-transition: all 0.3s ease-in-out;
  -ms-transition: all 0.3s ease-in-out;
  -o-transition: all 0.3s ease-in-out;
  transition: all 0.3s ease-in-out;
}
</style>
