import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Axios from 'axios'
import * as api from './api'
import jsCookie from 'js-cookie'

Vue.prototype.$jsCookie = jsCookie
Vue.prototype.$api = api
Vue.config.productionTip = false
// 将axios 注册进Vue 原型 ,以后在项目中可以在使用 this.$http
Vue.prototype.$http = Axios
// 导入vant
import Vant from 'vant';
import 'vant/lib/index.css';

Vue.use(Vant);
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
