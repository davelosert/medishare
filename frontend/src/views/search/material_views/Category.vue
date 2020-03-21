<template>
  <b-col class="Material hover" :class="{'active': isActive}" sm="6" @click="onClick">
    <b-row class="flex-column">
      <b-col class="category-container">
        <img src="../../../assets/material/mask.svg" class="Mask" alt="Maske" />
        <span class="Masken">{{ category.name }}</span>
      </b-col>
    </b-row>
    <b-icon-check class="Oval checkmark-container" v-show="isActive">
    </b-icon-check>
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
  data() {
    return {
      isActive: false
    };
  },
  methods: {
    onClick() {
      this.isActive = !this.isActive;
    }
  },
  watch: {
    isActive() {
      this.$emit("selected", this.category.id);
    }
  }
};
</script>

<style scoped>
.category-container {
  padding: 26px 21px;
}

.checkmark-container {
  position: relative;
  z-index: 2;
  top: -9px;
  color: #fff;
}

.active {
  border-radius: 8px;
  border: solid 3px #17a48b;
}

/* zeplin styles */

.Material {
  width: 160px;
  height: 160px;
  border-radius: 8px;
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
  margin-top: 10px;
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
  background-color: #17a48b;
}

.Path-4 {
  width: 12px;
  height: 9px;
  background-color: #ffffff;
}
</style>