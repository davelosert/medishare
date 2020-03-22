<template>
  <b-row id="results" class="flex-column">
    <b-col class="Search-Query flex-shrink-1 flex-grow-0">
      <p class="Ihre-Suche">Ihre Suche:</p>
      <p 
        class="-OP-Masken-Sofort p-0 m-0"
        v-for="(item, index) in queryItems" 
        :key="index">{{ item }}</p>
    </b-col>
  </b-row>
</template>
<script>
import { mapState } from 'vuex' 
export default {
  name: 'results',
  computed: {
    ...mapState({
      response: state => state.searchResults.response,
      query: state => state.cart.query
    }),
    queryItems() {
      return [
        `${this.query.count} ${this.query.categoryName}`,
        new Date(this.query.date).toLocaleDateString()
      ]
    }
  }
}
</script>

<style scoped>
#results {
  padding: 35px 15px 15px 15px;
  height: calc(100% - 56px);
}
/* ZEPLIN Styles */
.Search-Query {
  border-radius: 8px;
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
  color: var(--dark-grey);
  text-align: start;
  padding: 16px; 
}

.-OP-Masken-Sofort {
  font-weight: normal;
  color: var(--dark-grey);
}
</style>