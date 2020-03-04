import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Axios from 'axios'
Vue.config.productionTip = false
// 将axios 注册进Vue 原型 ,以后在项目中可以在使用 this.$http
Vue.prototype.$http = Axios
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
