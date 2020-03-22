import Vue from 'vue'
import Vuex from 'vuex'
import categories from './modules/categories'
import cart from './modules/cart'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    categories,
    cart
  }
})
