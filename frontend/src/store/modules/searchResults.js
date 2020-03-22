import searchApi from 'api/search'

// initial state
const state = {
  response: {}
}

const getters = {
  getDetail: (state) => (id) => {
    return state.response.results.find(searchItem => searchItem.id === id)
  }
}

// actions
const actions = {
  search ({ commit }, options) {
    searchApi
      .search(options)
      .then(resp => commit('SET_RESPONSE', resp.data))
  },
  clear ({commit}) {
    commit('SET_RESPONSE', {})
  }
}

// mutations
const mutations = {
  SET_RESPONSE (state, items) {
    state.result = items
  }
}

export default {
  namespaced: true,
  getters,
  state,
  actions,
  mutations
}