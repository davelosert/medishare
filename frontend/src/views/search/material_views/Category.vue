<template>
  <b-col
    class="Material hover"
    :class="{'active': isActive}"
    :style="borderColor"
    cols="6"
    @click="onClick"
  >
    <b-row class="flex-column" no-gutters>
      <b-col class="category-container d-flex flex-column align-items-center">
        <img :src="require(`@/assets/material/${this.category.image}`)" class="Mask" alt="Maske" />
        <span class="Masken">{{ category.name }}</span>
      </b-col>
    </b-row>
    <b-icon-check :style="backgroundColor" class="Oval checkmark-container" v-show="isActive"></b-icon-check>
  </b-col>
</template>

<script>
export default {
  name: "category",
  props: {
    category: {
      required: true,
      type: Object
    }
  },
  computed: {
    isActive() {
      return this.$store.state.cart.selectedItem === this.category.id;
    },
    borderColor() {
      return !this.isActive
        ? {}
        : { borderColor: this.$store.getters["theme/activeBG"] };
    },
    backgroundColor() {
      return !this.isActive
        ? {}
        : { backgroundColor: this.$store.getters["theme/activeBG"] };
    }
  },
  methods: {
    onClick() {
      this.$store.dispatch("cart/set", this.category.id);
    }
  }
};
</script>

<style scoped>
.category-container {
  padding: 26px 21px;
}

.checkmark-container {
  position: absolute;
  z-index: 2;
  bottom: -12px;
  left: calc(50% - 12px);
  color: #fff;
}

.active {
  border-radius: 8px;
  border: solid 3px;
}

/* zeplin styles */

.Material {
  width: 160px;
  height: 160px;
  max-width: 160px;
  max-height: 160px;
  border-radius: 8px;
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
  margin-top: 10px;
  margin-left: 10px;
}

.Mask {
  width: 118px;
  height: 79px;
  object-fit: contain;
}

.Masken {
  color: #4a5a68;
}

.Oval {
  width: 24px;
  height: 24px;
  border-radius: 50%;
}

.Path-4 {
  width: 12px;
  height: 9px;
  background-color: #ffffff;
}
</style>