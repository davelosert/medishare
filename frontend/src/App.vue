<template>
  <b-container fluid id="app" class="h-100">
    <b-navbar toggleable="lg" type="dark" class="pr-0 pl-0">
      <b-navbar-nav>
        <div @click="back" class="back-button" :class="{'hover': displayBack}">
          <img alt="Back" src="./assets/ic-24-back.svg" v-show="displayBack" />
        </div>
      </b-navbar-nav>
      <b-navbar-nav fill class="ml-auto mr-auto">
        <img alt="Brand" src="./assets/home/medi-share-logo.svg" />
      </b-navbar-nav>
      <b-navbar-nav>
        <b-nav-item-dropdown right no-caret>
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <img alt="three dots" src="./assets/home/ic-24-overflow.svg" />
          </template>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-navbar>
    <router-view />
  </b-container>
</template>
<script>
export default {
  data() {
    return {
      displayBack: false
    };
  },
  methods: {
    back() {
      if (!this.displayBack) {
        return;
      }

      this.$router.go(-1);
    }
  },
  watch: {
    $route(newVal) {
      this.displayBack = newVal.name !== "Home";
    }
  }
};
</script>

<style>
:root {
  --ms-orange: #fc5733 !important;
  --ms-primary: #17a48b !important;
  --green: #17a48b;
  --orange: #fc5733 !important;
  --off-white: #e8e8e8;
  --dark-grey: #4a5a68;
}

body,
html,
#app {
  height: 100%;
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-family: Montserrat;
  font-size: 14px;
  font-weight: 600;
  font-stretch: normal;
  font-style: normal;
  line-height: 1.5;
  letter-spacing: normal;
  text-align: center;
  color: var(--dark-grey);
}

.back-button {
  width: 24px;
  height: 24px;
  object-fit: contain;
  background-color: #fff !important;
  border: none !important;
}

.hover {
  cursor: pointer;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.ms-mt-64 {
  margin-top: 64px;
}

.ms-mb-15 {
  margin-bottom: 15px;
}

.ms-mt-15 {
  margin-top: 15px;
}

.ms-mt-24 {
  margin-top: 24px;
}

.ms-mt-46 {
  margin-top: 46px;
}

.ms-card {
  border-radius: 8px;
  border-color: unset;
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
  padding: 16px;
}

/* ZEPLIN CSS */

.Rectangle {
  width: 100%;
  max-width: 330px !important;
  height: 48px;
  border-radius: 8px !important;
  color: #fff !important;
}

.Rectangle-O {
  width: 100%;
  max-width: 330px !important;
  height: 48px;
  border-radius: 8px !important;
  color: var(--orange) !important;
  border: solid 2px var(--ms-orange) !important;
  background-color: white !important;
}

.Rectangle-O-CTA {
  height: 48px;
  width: 100%;
  max-width: 330px !important;
  border-radius: 8px !important;
  color: #fff !important;
  border: solid 2px var(--ms-orange) !important;
  background-color: var(--ms-orange) !important;
}

.Rectangle-Inactive {
  width: 100%;
  max-width: 330px !important;
  height: 48px;
  border-radius: 8px !important;
  border: 2px solid #6c757d !important;
}

.Anbieter-wurde-konta {
  font-size: 18px;
  font-weight: 600;
  font-stretch: normal;
  font-style: normal;
  line-height: 1.33;
  letter-spacing: normal;
  text-align: center;
  color: var(--dark-grey);
}

.Wir-haben-den-Anbiet {
  font-size: 14px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: 1.5;
  letter-spacing: normal;
  text-align: center;
  color: var(--dark-grey);
}
</style>
