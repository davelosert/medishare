<template>
  <b-row id="search" class="flex-column">
    <b-col>
      <span class="Whlen-Sie-wann-und">
        Wählen Sie wann und wieviele {{ category }} Sie benötigen
      </span>
    </b-col>
    <b-col>
      <div class="center-container">
        <b-input type="number"/>
        <b-button-group>
          <b-button class="Rectangle-CTA" @click="setDateToNow()">Sofort</b-button>
          <b-form-datepicker id="datepicker" v-model="dateValue"></b-form-datepicker>
        </b-button-group>
      </div>
    </b-col>
    <b-col>
      <b-button class="Rectangle-CTA w-100">Suchen</b-button>
    </b-col>
  </b-row>
</template>

<script>
  export default {
    name: 'search',
    props: {
      categoryId: {
        type: Number,
        required: true,
      }
    },
    data () {
      return {
        dateValue: Date.now()
      }
    },
    computed: {
      category () {
        return this.$store.getters['categories/getCategory'](this.categoryId)
      }
    },
    methods: {
      setDateToNow () {
        this.dateValue = Date.now()
      }
    }
  }
</script>

<style scoped>
#search {
  padding: 35px 0px 15px 0px;
  height: calc(100% - 56px);
}

.Whlen-Sie-wann-und {
  font-size: 24px;
  line-height: 1.33;
  color: var(--dark-grey);
}
</style>