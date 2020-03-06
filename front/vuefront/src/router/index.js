import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Category from '../views/Category.vue'
import Login from '../views/Login.vue'
import Usercenter from '../views/Usercenter.vue'
import Regist from '../views/Regist.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/regist/',
    name: 'Regist',
    component: Regist
  },
  {
    path: '/usercenter/',
    name: 'Usercenter',
    component: Usercenter
  },
  
  {
    path: '/categorys/:id/',
    name: 'Category',
    component: Category
  },
  {
    path: '/login/',
    name: 'Login',
    component: Login
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
