import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Results from '../views/search/Results.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/search/category',
    name: 'Categories',
    component: () => import('../views/search/Categories.vue')
  },
  {
    path: '/search/category/:categoryId',
    name: 'Search',
    component: () => import('../views/search/Search.vue'),
    props: true
  },
  {
    path: '/search/results',
    name: 'Results',
    component: Results,
  }
]

const router = new VueRouter({
  routes
})

export default router
