<template>
  <b-col class="result ms-card">
    <div class="d-flex flex-column justify-content-center align-content-center" 
      v-if="item.isCombination">
        <span class="Angebots-Kombi">Angebots Combi</span>
        <span class="Es-wurde-kein-Angebo">Es wurde kein Angebot für deinen Bedarf gefunden. Du kannst aber diese beiden Angebote kombinieren.</span>
    </div>
    <result-entity
      v-for="(result, index) in item.items"
      :key="result.giverId"
      :entity="result"
      :isAppend="item.items.length > 1 && index + 1 < item.items.length">
    </result-entity>
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

.Angebots-Kombi {
  font-size: 18px;
  font-weight: 600;
  line-height: 1.33;
  color: var(--dark-grey);
}

.Es-wurde-kein-Angebo {
  font-size: 14px;
  font-weight: normal;
  line-height: 1.5;
  color: var(--dark-grey);
}

.-Stk {
  font-size: 18px;
  font-weight: 600;
  line-height: 1.33;
  color: var(--dark-grey);
}
</style>