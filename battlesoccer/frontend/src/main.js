import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import Vuelidate from 'vuelidate'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
import { VLazyImagePlugin } from "v-lazy-image";
Vue.use(Vuelidate)

Vue.directive('$model', {
  bind: function (el, binding, vnode) {
      el.oninput = () => (vnode.context[binding.expression] = el.value)
  }
})
Vue.use(VLazyImagePlugin);
// using CommonJS modules
import vueScrollBehavior from 'vue-scroll-behavior'

Vue.use(vueScrollBehavior, {
  router: router,    // The router instance
  maxLength: 100,    // Saved history List max length
  ignore: [/\/boo/, /\/zoo/]    // ignore some routes, they will directly scroll to the top
})

Vue.filter('capitalize', function (value) {
  if (!value) return ''
  value = value.toString()
  return value.charAt(0).toUpperCase() + value.slice(1)
})

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
