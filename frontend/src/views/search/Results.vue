<template>
  <b-row id="results" class="flex-column">
    <b-col class="Search-Query ms-card flex-shrink-1 flex-grow-0">
      <p class="Ihre-Suche">Ihre Suche:</p>
      <p
        class="-OP-Masken-Sofort p-0 m-0"
        v-for="(item, index) in queryItems"
        :key="index"
      >{{ item }}</p>
    </b-col>
    <separator :delimiter="'Angebote'" v-if="results.length > 0"></separator>
    <result
      class="ms-mt-15"
      v-for="result in results"
      :key="result.giverId"
      :item="result"
      @contactDonors="contactDonors($event)"
    ></result>
    <div class="ms-mt-64 d-flex flex-column" v-if="results.length > 0">
      <h2 class="Nichts-passendes-dab">Nichts passendes dabei?</h2>
      <span
        class="Erstellen-Sie-einfac"
      >Erstellen Sie einfach ein Such-Inserat, wir benachrichtigen Sie sobald ein passendes Angebot eingestellt wurde.:</span>
      <b-button 
        class="w-100 Rectangle ms-mt-24"
        :style="buttonStyle"
        @click="createAdvertisement">Inserat erstellen</b-button>
    </div>
    <b-modal id="modal" hide-header hide-footer centered>
      <h2 class="Anbieter-wurde-konta">{{ modalProps.title }}</h2>
      <p
        class="Wir-haben-den-Anbiet ms-mt-15"
      >{{ modalProps.description }}</p>
      <b-button @click="onModalCTAClick" class="Rectangle-O-CTA w-100 ms-mt-24">{{ modalProps.ctaText }}</b-button>
      <b-button @click="onModalDefaulClick" class="Rectangle-O w-100 ms-mt-15">{{ modalProps.btnText }}</b-button>
    </b-modal>
  </b-row>
</template>
<script>
import { mapState } from 'vuex';
import Result from './results_views/Result';
import Separator from './Separator';

const modalType = {
  CONTACT_DONORS: 'CONTACT_DONORS',
  NO_ITEMS_FOUND: 'NO_ITEMS_FOUND'
}

let timeoutId

export default {
  name: 'results',
  components: {
    Result,
    Separator
  },
  created() {
    this.$store.dispatch('searchResults/search');
  },
  data () {
    return {
      modalType: undefined
    }
  },
  mounted () {
    timeoutId = setTimeout(() => {
      if (this.$store.state.cart.query.category.id === 5) {
        this.modalType = modalType.NO_ITEMS_FOUND
        this.$bvModal.show('modal');
      }
    }, 200)
  },
  beforeDestroy () {
    clearTimeout(timeoutId)
  },
  computed: {
    ...mapState({
      results: state => state.searchResults.result,
      query: state => state.cart.query,
      buttonStyle: state => state.theme.activeStyle.buttons
    }),
    modalProps() {
      if (this.modalType === modalType.CONTACT_DONORS) {
        return {
          title: 'Anbieter wurden kontaktiert',
          description: 'Wir haben den Anbieter benachrichtigt, dass bei ihnen Bedarf besteht. Sie erhalten in Kürze Feedback mit weiteren Informationen.',
          ctaText: 'Schließen',
          btnText: 'Weitere Materialien suchen'
        }
      } else if (this.modalType === modalType.NO_ITEMS_FOUND) {
        return {
          title: 'Es wurde leider kein passendes Angebot gefunden',
          description: 'Erstellen Sie stattdessen ein Suchinserat mit Ihrem Bedarf. Sobald wir einen passenden Anbieter finden, werden Sie sofort benachrichtigt.',
          ctaText: 'Such-Inserat erstellen',
          btnText: 'Bearbeiten'
        }
      }

      return 'Hello'
    },
    queryItems() {
      const requestDate = new Date(this.query.date);
      const now = new Date();
      const isRequestedNow =
        requestDate.getDate() === now.getDate() &&
        requestDate.getMonth() === now.getMonth() &&
        requestDate.getFullYear() === now.getFullYear();
      return [
        `${this.query.count} ${this.query.category.name}`,
        isRequestedNow
          ? 'Sofort'
          : new Date(this.query.date).toLocaleDateString()
      ];
    },
  },
  methods: {
    onModalCTAClick() {
      this.$bvModal.hide('modal')
      if (this.modalType === modalType.CONTACT_DONORS) {
        this.onModalClose()
      } else if (this.modalType === modalType.NO_ITEMS_FOUND) {
        const selectedItem = this.$store.state.cart.selectedItem
        this.$router.push({name: 'Search', params: { categoryId: selectedItem, create: true }})
      }
    },
    onModalDefaulClick() {
      if (this.modalType === modalType.CONTACT_DONORS) {
        this.onLookForMore()
      } else if (this.modalType === modalType.NO_ITEMS_FOUND) {
        this.$router.go(-2)
      }
    },
    contactDonors(donorIds) {
      this.modalType = modalType.CONTACT_DONORS
      console.log('Will contact ' + JSON.stringify(donorIds));
      this.$bvModal.show('modal');
    },
    onModalClose() {
      this.$router.replace({name: 'Home'})
    },
    onLookForMore() {
      this.$router.go(-2)
    },
    createAdvertisement() {
      const selectedItem = this.$store.state.cart.selectedItem
      this.$router.push({name: 'Search', params: { categoryId: selectedItem, create: true }})
    }
  }
};
</script>

<style scoped>
#results {
  padding: 35px 15px 15px 15px;
}

/* ZEPLIN Styles */
.Erstellen-Sie-einfac {
  font-family: Montserrat;
  font-size: 14px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: 1.5;
  letter-spacing: normal;
  text-align: center;
  color: var(--dark-grey);
}

.Search-Query {
  color: var(--dark-grey);
  text-align: start;
}

.-OP-Masken-Sofort {
  font-weight: normal;
  color: var(--dark-grey);
}

.Nichts-passendes-dab {
  font-size: 18px;
  font-weight: 600;
  font-stretch: normal;
  font-style: normal;
  line-height: 1.33;
  letter-spacing: normal;
  text-align: center;
  color: var(--dark-grey);
}
</style>