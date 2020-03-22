<template>
  <b-row id="search" class="flex-column justify-content-around">
    <b-col>
      <span class="Whlen-Sie-wann-und">
        Wählen Sie wann und wieviele {{ category.name }} Sie benötigen
      </span>
    </b-col>
    <b-col>
      <div class="center-container">
        <b-input type="number" min="1" max="1000" v-model="countValue"/>
        <b-form-datepicker
          no-flip
          dropup
          today-button
          v-model="dateValue"
          class="button-group"
        ></b-form-datepicker>
      </div>
    </b-col>
    <b-col class="d-flex flex-column justify-content-end">
      <b-button class="Rectangle-CTA w-100" @click="search">Suchen</b-button>
    </b-col>
  </b-row>
</template>

<script>
  export default {
    name: 'search',
    props: {
      categoryId: {
        required: true,
      }
    },
    data () {
      return {
        dateValue: new Date(),
        countValue: 10
      }
    },
    mounted () {
      const { date, count } = this.$store.state.cart.query
      this.dateValue = date
      this.countValue = count
    },
    computed: {
      category () {
        return this.$store.getters['categories/getCategory'](this.categoryId)
      },
      formattedDate () {
        return this.dateValue.toLocaleDateString()
      }
    },
    methods: {
      setDateToNow () {
        this.dateValue = new Date()
      },
      search () {
        this.$store.dispatch('cart/setQuery', {
          date: this.dateValue,
          count: this.countValue,
          category: this.category
        })
        this.$router.push({name: 'Results'})
      }
    }
  }
</script>

<style scoped>
#search {
  padding: 35px 0px 15px 0px;
  height: calc(100% - 56px);
}

.button-group {
  margin-top: 24px;
}

.Whlen-Sie-wann-und {
  font-size: 24px;
  line-height: 1.33;
  color: var(--dark-grey);
}
</style>