<template>
  <b-row id="categories" class="flex-column justify-content-between">
    <b-col>
      <p class="Welche-Materialien-s">
        Welche Materialien suchen Sie?
      </p>
    </b-col>
    <b-col>
      <b-row class="justify-content-between" no-gutters>
        <category v-for="category in categories"
          :key="category.id"
          sm="6"
          :category="category"
          @selected="onSelection($event)">
        </category>
      </b-row>
    </b-col>
    <b-col class="d-flex flex-column justify-content-end">
      <b-button class="w-100" 
      :disabled="selectedItems.length === 0"
      :class="nextButtonClass" 
      @click="next">Weiter</b-button>
    </b-col>
  </b-row>
</template>
<script>
import Category from './material_views/Category'

export default {
  name: 'categories',
  components: {
    'category': Category
  },
  data () {
    return {
      selectedItems: [],
      categories: [{
        id: 1,
        name: 'Masken'
      },{
        id: 2,
        name: 'Kategorie 2'
      },{
        id: 3,
        name: 'Kategorie 3'
      },{
        id: 4,
        name: 'Kategorie 4'
      },{
        id: 5,
        name: 'Kategorie 5'
      }]
    }
  },
  computed: {
    nextButtonClass () {     
      return this.selectedItems.length > 0 ? ['Rectangle', 'Rectangle-CTA'] : 'Rectangle-Inactive'
    }
  },
  methods: {
    onSelection(categoryId) {
      const idx = this.selectedItems.indexOf(categoryId)
      
      if (idx > -1) {
        this.selectedItems.splice(idx, 1)
      } else {
        this.selectedItems.push(categoryId)
      }
    },
    next () {
      this.$store.dispatch('categories/set', this.selectedItems)
    }
  }
}
</script>
<style scoped>
#categories {
  padding: 35px 0px 15px 0px;
  height: calc(100% - 56px);
}

/* ZEPLIN CSS */

.Welche-Materialien-s {
  font-size: 24px;
  font-weight: 600;
  line-height: 1.33;
  color: #4a5a68;
}
</style>