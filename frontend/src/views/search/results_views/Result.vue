<template>
  <b-col class="result ms-card">
    <div class="d-flex flex-column justify-content-center align-content-center combi-container" 
      v-if="item.isCombination">
        <h2 class="Angebots-Kombi">Angebots Combi</h2>
        <span class="Es-wurde-kein-Angebo">Es wurde kein Angebot für deinen Bedarf gefunden. Du kannst aber diese beiden Angebote kombinieren.</span>
    </div>
    <result-entity
      v-for="(result, index) in item.items"
      :key="result.giverId"
      :entity="result"
      :isAppend="item.items.length > 1 && index + 1 < item.items.length">
    </result-entity>
    <b-button 
      class="Rectangle w-100 ms-mt-46"
      :style="buttonStyle"
      @click="$emit('contactDonors', item.items)">{{ buttonText }}</b-button>
  </b-col>
</template>
<script>
import ResultEntity from './ResultEntity'

export default {
  name: "result",
  components: {
    'result-entity': ResultEntity
  },
  props: {
    item: {
      type: Object,
      required: true
    }
  },
  computed: {
    buttonText () {
      return this.item.isCombination ? 'Kontaktanfrage an alle Anbieter' : 'Kontaktanfrage stellen'
    },
    buttonStyle () {
      return this.$store.state.theme.activeStyle.buttons
    }
  }
};
</script>

<style scoped>
.giver-name {
  font-size: 14px;
  font-weight: 600;
  line-height: 1.5;
  color: var(--dark-grey);
}

.combi-container {
  margin-bottom: 43px;
}

.Angebots-Kombi {
  font-family: Montserrat;
  font-size: 18px;
  font-weight: 600;
  font-stretch: normal;
  font-style: normal;
  line-height: 1.33;
  letter-spacing: normal;
  text-align: center;
  color: var(--dark-grey);
}

.Es-wurde-kein-Angebo {
  font-family: Montserrat;
  font-size: 14px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: 1.5;
  letter-spacing: normal;
  text-align: center;
  color: var(--dark-grey);
  margin-top: 16px;
}

.-Stk {
  font-size: 18px;
  font-weight: 600;
  line-height: 1.33;
  color: var(--dark-grey);
}
</style>