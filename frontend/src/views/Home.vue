<template>
  <b-row class="home flex-column justify-content-between" no-gutters>
    <b-col>
      <img src="../assets/home/group-4.svg" class="Group-4">
    </b-col>
    <b-col class="welcome-text-container">
      <span class="Willkommen-Dr-Meie">Willkommen, {{ username }}</span>
      <p class="Fehlt-es-Ihnen-an-Ar ms-mt-16">
        Fehlt es Ihnen an Arbeitsmaterialien, oder haben Sie etwas auf Vorrat,
        dass Sie gerne zur Verfügung stellen möchten?
      </p>
    </b-col>
    <b-col class="ms-mt-16 d-flex justify-content-end">
      <b-row 
        class="flex-column w-100 h-100 align-items-stretch justify-content-end"
        no-gutters>
        <b-col class="flex-grow-0">
          <b-button class="w-100 Rectangle Rectangle-CTA" @click="navToMaterialSearch">Ich suche Materialien</b-button>
        </b-col>
        <b-col class="ms-mt-16 flex-grow-0">
          <b-button class="w-100 Rectangle Rectangle-Default">Ich kann Materialien teilen</b-button>
        </b-col>
      </b-row>
    </b-col>
  </b-row>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      username: 'Dr. Meier'
    }
  },
  methods: {
    navToMaterialSearch () {
      this.$router.push({name: 'SearchMaterial'})
    }
  }
}
</script>

<style scoped>
.home {
  padding-top: 40px;
  padding-bottom: 24px;
  /* Subtract top and bottom padding */
  height: calc(100% - 64px);
}

.welcome-text-container {
  margin-top: 46px;
}

.ms-mt-16 {
  margin-top: 16px;
}

/* ZEPLIN STYLES */

.Willkommen-Dr-Meie {
  font-size: 18px;
  font-weight: 600;
  font-stretch: normal;
  font-style: normal;
  line-height: 1.33;
  letter-spacing: normal;
  text-align: center;
  color: #4a5a68;
}

.Group-4 {
  width: 268px;
  height: 198px;
  object-fit: contain;
}

.Fehlt-es-Ihnen-an-Ar {
  font-family: Montserrat;
  font-size: 14px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: 1.5;
  letter-spacing: normal;
  text-align: center;
  color: #4a5a68;
}
</style>
