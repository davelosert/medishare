// initial state
const state = {
  items: []
}

// actions
const actions = {
  set ({ commit }, items) {
    commit('SET_ITEMS', items)
  },
  clear ({commit}) {
    commit('SET_ITEMS', [])
  }
}

// mutations
const mutations = {
  SET_ITEMS (state, { items }) {
    state.items = items
  }
}

export default {
  namespaced: true,
  state,
  actions,
  mutations
}