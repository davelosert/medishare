<template>
  <div class="result-entity d-flex">
    <div class="image-container d-flex flex-column justify-content-center">
      <img src="../../../assets/material/illustration-op-mask.svg" alt="Op Mask" />
      <span>{{ entity.itemCount }}</span>
    </div>
    <div class="info-container d-flex flex-column justify-content-center align-items-center">
      <span class="giver-name">{{ entity.giverName }}</span>
      <span class="distance">{{ distance }}</span>
      <span :class="[{'giver-name': availability !== 0}]">{{ availability }}</span>
    </div>
    <separator v-if="isAppend" :delimiter="'+'"></separator>
  </div>
</template>

<script>
import Separator from '../Separator'
export default {
  name: "result-entity",
  components: {
    Separator
  },
  props: {
    entity: {
      type: Object,
      required: true
    },
    isAppend: {
      type: Boolean,
      required: true
    }
  },
  mounted () {
    // eslint-disable-next-line no-debugger
    debugger
    console.log(this.entity)
  },
  computed: {
    distance() {
      return this.entity.distance / 1000 + 'km entfernt';
    },
    availability() {
      return this.entity.availability === 0
        ? "Sofort"
        : new Date(this.entity.availability).toLocaleDateString();
    }
  }
};
</script>

<style>
</style>