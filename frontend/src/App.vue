<template>
<b-container fluid id="app">
  <b-navbar toggleable="lg" type="dark" class="pr-0 pl-0">
    <b-navbar-nav fill class="ml-auto mr-auto">
      <img alt="Brand" src="./assets/home/medi-share-logo.svg">
    </b-navbar-nav>
    <b-navbar-nav>
      <b-nav-item-dropdown right no-caret>
        <!-- Using 'button-content' slot -->
        <template v-slot:button-content>
          <img alt="three dots" src="./assets/home/ic-24-overflow.svg">
        </template>
      </b-nav-item-dropdown>
    </b-navbar-nav>
  </b-navbar>
  <router-view/>
</b-container>
</template>

<style>
body, html, #app {
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
  color: #2c3e50;
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

/* ZEPLIN CSS */

.Rectangle {
  border-radius: 8px !important;
  border: solid 2px #17a48b !important;
}

.Rectangle-CTA {
  background-color: #17a48b !important;
  color: #fff !important;
}

.Rectangle-Default {
  color: #17a48b !important;
  background-color: #fff !important;
}

</style>
