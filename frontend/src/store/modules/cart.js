// initial state
const state = {
  items: [],
  query: {
    count: 1,
    date: new Date()
  }
}

// actions
const actions = {
  set ({ commit }, items) {
    commit('SET_ITEMS', items)
  },
  setQuery ({ commit }, query) {
    commit('SET_QUERY', query)
  },
  clear ({commit}) {
    commit('SET_ITEMS', [])
    commit('SET_QUERY', {})
  }
}

// mutations
const mutations = {
  SET_ITEMS (state, { items }) {
    state.items = items
  },
  SET_QUERY (state, query) {
    state.query = query
  }
}

export default {
  namespaced: true,
  state,
  actions,
  mutations
}