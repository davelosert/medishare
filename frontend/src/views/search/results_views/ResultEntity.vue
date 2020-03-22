<template>
  <div class="result-entity d-flex flex-column">
    <div class="d-flex justify-content-start">
      <div class="image-container d-flex flex-column justify-content-center">
        <img :src="require(`@/assets/material/${this.category.image}`)" alt="Op Mask" />
        <span>{{ entity.itemCount }}</span>
      </div>
      <div class="info-container d-flex flex-column justify-content-center align-items-center">
        <span class="giver-name">{{ entity.giverName }}</span>
        <span class="distance -km-entfernt">{{ distance }}</span>
        <span class="Sofort-verfgbar" :class="[{'green': availability !== 0}]">{{ availability }}</span>
      </div>
    </div>
    <separator v-if="isAppend" :delimiter="'+'"></separator>
  </div>
</template>

<script>
import Separator from "../Separator";
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
  computed: {
    distance () {
      return this.entity.distance / 1000 + " km entfernt";
    },
    availability () {
      return this.entity.availability === 0
        ? "Sofort"
        : new Date(this.entity.availability).toLocaleDateString();
    },
    category () {
      return this.$store.state.cart.query.category
    }
  }
};
</script>

<style scoped>
.info-container {
  margin-left: 24px;
}

.-km-entfernt {
  font-family: Montserrat;
  font-size: 14px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: 1.5;
  letter-spacing: normal;
  color: var(--dark-grey);
}

.Sofort-verfgbar {
  font-family: Montserrat;
  font-size: 14px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: 1.5;
  letter-spacing: normal;
}

.green {
  color: var(--green);
}
</style>