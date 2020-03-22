<template>
  <b-row id="categories" class="justify-content-center">
    <b-col cols="12">
      <p class="Welche-Materialien-s">Welche Materialien {{ text }}?</p>
    </b-col>
    <category v-for="category in categories" :key="category.id" :category="category"></category>
    <b-col cols="12" class="button-container">
      <b-button 
        :disabled="selectedItem === undefined"
        :style="buttonTheme"
        :class="buttonClass"
        @click="next"
      >Weiter</b-button>
    </b-col>
  </b-row>
</template>
<script>
import Category from "./material_views/Category";
import { mapState } from "vuex";

export default {
  name: "categories",
  components: {
    category: Category
  },
  created() {
    this.$store.dispatch("categories/fetchAll");
  },
  computed: {
    ...mapState({
      categories: state => state.categories.all,
      selectedItem: state => state.cart.selectedItem,
      buttonStyle: state => state.theme.activeStyle.buttons
    }),
    buttonTheme() {
      return this.selectedItem === undefined ? {} : this.buttonStyle;
    },
    buttonClass() {
      return this.selectedItem === undefined
        ? "Rectangle-Inactive"
        : "Rectangle";
    },
    text() {
      const activeIsDonor = this.$store.getters["theme/activeIsDonor"];
      if (activeIsDonor) {
        return " stellen Sie bereit";
      } else {
        return " suchen Sie";
      }
    }
  },
  methods: {
    next() {
      this.$router.push({
        name: "Search",
        params: { categoryId: this.selectedItem }
      });
    }
  }
};
</script>
<style scoped>
#categories {
  padding: 35px 0px 15px 0px;
  height: calc(100% - 56px);
}

.button-container {
  display: flex;
  margin-top: 16px !important;
  align-items: flex-end;
  justify-content: center;
}

/* ZEPLIN CSS */

.Welche-Materialien-s {
  font-size: 24px;
  font-weight: 600;
  line-height: 1.33;
  color: #4a5a68;
}
</style>