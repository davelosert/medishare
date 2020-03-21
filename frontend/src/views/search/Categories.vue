<template>
  <b-row id="categories" class="flex-column">
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
        id: 4,
        name: 'Kategorie 5'
      }]
    }
  }
}
</script>
<style scoped>
#materials {
  padding: 35px 15px 15px 15px;
}

/* ZEPLIN CSS */

.Welche-Materialien-s {
  font-size: 24px;
  font-weight: 600;
  line-height: 1.33;
  color: #4a5a68;
}
</style>