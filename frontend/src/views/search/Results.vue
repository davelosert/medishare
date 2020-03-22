<template>
  <b-row id="results" class="flex-column">
    <b-col class="Search-Query ms-card flex-shrink-1 flex-grow-0">
      <p class="Ihre-Suche">Ihre Suche:</p>
      <p 
        class="-OP-Masken-Sofort p-0 m-0"
        v-for="(item, index) in queryItems" 
        :key="index">{{ item }}</p>
    </b-col>
    <separator :delimiter="'Angebote'"></separator>
    <result
      class="ms-mt-15"
      v-for="result in results"
      :key="result.giverId"
      :item="result">
    </result>
    <div class="ms-mt-64 d-flex flex-column">
      <h2 class="Nichts-passendes-dab">Nichts passendes dabei?</h2>
      <span class="Erstellen-Sie-einfac">Erstellen Sie einfach ein Such-Inserat, wir benachrichtigen Sie sobald ein passendes Angebot eingestellt wurde.:</span>
      <b-button class="w-100 Rectangle Rectangle-CTA ms-mt-24">Inserat erstellen</b-button>
    </div>
  </b-row>
</template>
<script>
import { mapState } from 'vuex' 
import Result from './results_views/Result'
import Separator from './Separator'

export default {
  name: 'results',
  components: {
    Result, Separator
  },
  created () {
    this.$store.dispatch('searchResults/search')
  },
  computed: {
    ...mapState({
      results: state => state.searchResults.result,
      query: state => state.cart.query,
    }),
    queryItems() {
      const requestDate = new Date(this.query.date)
      const now = new Date()
      const isRequestedNow = requestDate.getDate() === now.getDate() && 
        requestDate.getMonth() === now.getMonth() &&
        requestDate.getFullYear() === now.getFullYear()
      return [
        `${this.query.count} ${this.query.category.name}`,
        isRequestedNow ? 'Sofort' : new Date(this.query.date).toLocaleDateString()
      ]
    }
  }
}
</script>

<style scoped>
#results {
  padding: 35px 15px 15px 15px;
}

/* ZEPLIN Styles */
.Erstellen-Sie-einfac {
  font-family: Montserrat;
  font-size: 14px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: 1.5;
  letter-spacing: normal;
  text-align: center;
  color: var(--dark-grey);
}

.Search-Query {
  color: var(--dark-grey);
  text-align: start;
}

.-OP-Masken-Sofort {
  font-weight: normal;
  color: var(--dark-grey);
}

.Nichts-passendes-dab {
  font-size: 18px;
  font-weight: 600;
  font-stretch: normal;
  font-style: normal;
  line-height: 1.33;
  letter-spacing: normal;
  text-align: center;
  color: var(--dark-grey);
}
</style>