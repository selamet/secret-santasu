import Vue          from 'vue'
import App          from './App.vue'
import VModal       from 'vue-js-modal'
import { router }   from "./router"

Vue.use(VModal)

new Vue({
  el      : '#app',
  render  : h => h(App),
  router,
})


