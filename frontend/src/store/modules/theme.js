const receiverStyles = {
  buttons: {
    border: 'solid 2px var(--ms-primary) !important',
    backgroundColor: 'var(--ms-primary) !important',
  }
}

const donorStyles = {
  buttons: {
    border: 'solid 2px var(--ms-orange) !important',
    backgroundColor: 'var(--ms-orange) !important',
  }
}

const getters = {
  activeBG: state => state.activeStyle.buttons.backgroundColor,
  activeIsDonor: state => state.activeStyle.buttons.backgroundColor === donorStyles.buttons.backgroundColor
}

// initial state
const state = {
  activeStyle: {
    buttons: receiverStyles.buttons
  },
  receiverStyle: receiverStyles,
  donorStyle: donorStyles
}

// actions
const actions = {
  setReceiverStyle ({ commit }) {
    commit('SET_STYLE', receiverStyles)
  },
  setDonorStyle ({ commit }) {
    commit('SET_STYLE', donorStyles)
  }
}

// mutations
const mutations = {
  SET_STYLE (state, activeStyle) {
    state.activeStyle = activeStyle
  },
}

export default {
  namespaced: true,
  state,
  actions,
  getters,
  mutations
}