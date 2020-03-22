<template>
  <b-col 
      class="d-flex justify-content-around align-items-center w-100 separator-container p-0 flex-grow-0">
      <div class="separator flex-grow-1"></div>
      <span class="delimiter">{{ delimiter }}</span>
      <div class="separator flex-grow-1"></div>
    </b-col>
</template>

<script>
export default {
  name: 'separator',
  props: {
    delimiter: {
      type: String,
      required: true
    }
  }
}
</script>

<style scoped>
.separator {
  height: 1px;
  background-color: #dddddd;
}

.separator-container {
  margin: 15px 0px;
}

.delimiter {
  line-height: 1.5;
  text-align: center;
  color: #dddddd;
  margin: 0 8px;
}
</style>