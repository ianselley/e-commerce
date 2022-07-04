<template>
  <div v-if="currentUser">
    <div class="main-title">PROFILE</div>
    <div class="md:flex flex-row items-start justify-center md:space-x-10">
      <div class="md:sticky md:top-48 z-50">
        <div class="form-content card">
          <div v-if="userIsBuyer" class="text-left">
            <strong>Name:</strong> {{ currentBuyer.name }}
          </div>
          <div v-if="userIsSeller" class="text-left">
            <strong>Brand:</strong> {{ currentSeller.brand }}
          </div>
          <div class="text-left">
            <strong>Email:</strong> {{ currentUser.email }}
          </div>
          <div class="text-left">
            <strong>Telephone:</strong> {{ currentUser.telephone }}
          </div>
          <div v-if="userIsSeller" class="text-left">
            Products sold: {{ currentSeller.number_of_products_sold }}
          </div>
          <EditUser />
        </div>
        <Modal v-if="userIsBuyer" :key="modalKey" button-text="Add Address">
          <RegisterAddress @submit="addAddress" />
        </Modal>
      </div>
      <div v-if="userIsBuyer" class="space-y-10 mt-10 md:mt-0">
        <DisplayAddress
          v-for="address in currentBuyer.addresses"
          :key="address"
          :address="address"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Modal from '@/components/Modal.vue';
import EditUser from '@/components/EditUser.vue';
import DisplayAddress from '@/components/DisplayAddress.vue';
import RegisterAddress from '@/components/RegisterAddress.vue';
export default {
  name: 'Profile',
  components: {
    Modal,
    EditUser,
    DisplayAddress,
    RegisterAddress,
  },
  data() {
    return {
      modalKey: 0,
    };
  },
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    },
    userIsBuyer() {
      return this.$store.state.auth.loggedInAs == 'buyer';
    },
    currentBuyer() {
      return this.$store.state.auth.buyer;
    },
    userIsSeller() {
      return this.$store.state.auth.loggedInAs == 'seller';
    },
    currentSeller() {
      return this.$store.state.auth.seller;
    },
  },
  created() {
    if (!this.currentUser) {
      this.$router.push('/login');
      this.$store.dispatch('alert/setMessage', 'You are not logged in');
    } else {
      this.$store
        .dispatch('auth/getUser')
        .then((response) => {
          if (response.seller) {
            const sellerId = response.seller.id;
            return this.$store.dispatch('product/getSellerProducts', sellerId);
          }
        })
        .catch((error) => {
          this.$store.dispatch('alert/setMessage', error);
        });
    }
  },
  methods: {
    addAddress() {
      this.modalKey++;
    },
  },
};
</script>

<style lang="postcss" scoped>
.card {
  max-width: 80vw;
  @apply mb-10 md:mx-0 p-10 space-y-3 break-words;
}

@screen md {
  .card {
    width: max-content;
    max-width: 35vw;
  }
}
</style>
