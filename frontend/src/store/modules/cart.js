// initial state
const state = {
  selectedItem: undefined,
  query: {
    count: 1,
    date: new Date()
  }
}

// actions
const actions = {
  set ({ commit }, selectedItem) {
    commit('SET_ITEM', selectedItem)
  },
  setQuery ({ commit }, query) {
    commit('SET_QUERY', query)
  },
  clear ({commit}) {
    commit('SET_ITEM', undefined)
    commit('SET_QUERY', {})
  }
}

// mutations
const mutations = {
  SET_ITEM (state, selectedItem) {
    if (state.selectedItem === selectedItem) {
      state.selectedItem = undefined
    } else {
      state.selectedItem = selectedItem
    }
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