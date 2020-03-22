import searchApi from 'api/search'

// initial state
const state = {
  result: []
}

const getters = {
  getDetail: (state) => (id) => {
    return state.response.results.find(searchItem => searchItem.id === id)
  }
}

// actions
const actions = {
  search ({ commit, rootState }) {
    searchApi
      .search(rootState.cart.query)
      .then(resp => commit('SET_RESPONSE', resp.data))
  },
  clear ({commit}) {
    commit('SET_RESPONSE', {})
  }
}

// mutations
const mutations = {
  SET_RESPONSE (state, result) {
    state.result = result
  }
}

export default {
  namespaced: true,
  getters,
  state,
  actions,
  mutations
}