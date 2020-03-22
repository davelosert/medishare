import Vue from 'vue'
import Vuex from 'vuex'
import categories from './modules/categories'
import cart from './modules/cart'
import searchResults from './modules/searchResults'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    categories,
    cart,
    searchResults
  }
})
