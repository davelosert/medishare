import categoriesApi from 'api/categories'

// initial state
const state = {
  all: []
}

const getters = {
  getCategory ({ state }, id) {
    return state.all.find(category => category.id === id)
  }
}

// actions
const actions = {
  fetchAll ({ commit }) {
    categoriesApi
      .fetchCategories()
      .then(categories => commit('SET_CATEGORIES', categories))
  },
  clear ({commit}) {
    commit('SET_CATEGORIES', [])
  }
}

// mutations
const mutations = {
  SET_CATEGORIES (state, items) {
    state.all = items
  }
}

export default {
  namespaced: true,
  getters,
  state,
  actions,
  mutations
}