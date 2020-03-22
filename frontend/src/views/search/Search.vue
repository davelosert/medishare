<template>
  <b-row id="search" class="flex-column justify-content-around">
    <b-col>
      <span
        class="Whlen-Sie-wann-und"
      >Wählen Sie wann und wieviele {{ category.name }} Sie {{ text }}</span>
    </b-col>
    <b-col>
      <div class="center-container">
        <b-input type="number" min="1" max="1000" v-model="countValue" />
        <b-form-datepicker
          no-flip
          dropup
          today-button
          :min="new Date()"
          v-model="dateValue"
          class="button-group"
        ></b-form-datepicker>
      </div>
    </b-col>
    <b-col class="d-flex flex-column justify-content-end">
      <b-button :style="buttonStyle" class="Rectangle w-100" @click="search">{{ buttonText }}</b-button>
    </b-col>
    <b-modal id="modal" hide-header hide-footer centered>
      <h2 class="Anbieter-wurde-konta">Ihr Inserat wurde erstellt</h2>
      <p
        class="Wir-haben-den-Anbiet ms-mt-15"
      >Sollte jemand nach Ihren Materialien suchen, werden wir die Kontaktaufnahme herstellen</p>
      <b-button @click="back" class="Rectangle-O-CTA w-100 ms-mt-24">Weitere Materialien anbieten</b-button>
      <b-button @click="goHome" class="Rectangle-O w-100 ms-mt-15">Zurück zur Startseite</b-button>
    </b-modal>
  </b-row>
</template>

<script>
export default {
  name: "search",
  props: {
    categoryId: {
      required: true
    }
  },
  data() {
    return {
      dateValue: new Date(),
      countValue: 10
    };
  },
  mounted() {
    const { date, count } = this.$store.state.cart.query;
    this.dateValue = date;
    this.countValue = count;
  },
  computed: {
    category() {
      return this.$store.getters["categories/getCategory"](this.categoryId);
    },
    formattedDate() {
      return this.dateValue.toLocaleDateString();
    },
    buttonStyle() {
      return this.$store.state.theme.activeStyle.buttons;
    },
    activeIsDonor() {
      return this.$store.getters["theme/activeIsDonor"];
    },
    text() {
      return this.activeIsDonor ? "bereitstellen könnten" : "benötigen";
    },
    buttonText() {
      return this.activeIsDonor ? "Inserieren" : "Suchen";
    }
  },
  methods: {
    setDateToNow() {
      this.dateValue = new Date();
    },
    search() {
      if (this.activeIsDonor) {
        this.$bvModal.show("modal");
        return;
      }
      this.$store.dispatch("cart/setQuery", {
        date: this.dateValue,
        count: this.countValue,
        category: this.category
      });
      this.$router.push({ name: "Results" });
    },
    back() {
      this.$bvModal.hide("modal");
      this.$router.go(-1);
    },
    goHome() {
      this.$bvModal.hide("modal");
      this.$router.replace({ name: "Home" });
    }
  }
};
</script>

<style scoped>
#search {
  padding: 35px 0px 15px 0px;
  height: calc(100% - 56px);
}

.button-group {
  margin-top: 24px;
}

.Whlen-Sie-wann-und {
  font-size: 24px;
  line-height: 1.33;
  color: var(--dark-grey);
}
</style>