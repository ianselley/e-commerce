<template>
  <div v-if="currentUser">
    <header>
      <div class="text-2xl">
        <strong
          >{{
            (currentSeller && currentSeller.brand) ||
            (currentBuyer && currentBuyer.name)
          }}, PROFILE</strong
        >
      </div>
    </header>
    <p v-if="currentBuyer"><strong>Name:</strong> {{ currentBuyer.name }}</p>
    <p v-if="currentSeller">
      <strong>Brand:</strong> {{ currentSeller.brand }}
    </p>
    <p><strong>Email:</strong> {{ currentUser.email }}</p>
    <p><strong>Telephone:</strong> {{ currentUser.telephone }}</p>
    <p v-if="userIsSeller">
      Products sold: {{ currentSeller.number_of_products_sold }}
    </p>
    <EditUser />
    <BuyerProfile v-if="userIsBuyer" />
  </div>
</template>

<script>
import EditUser from '@/components/EditUser.vue';
import BuyerProfile from '@/components/BuyerProfile.vue';
export default {
  name: 'Profile',
  components: {
    EditUser,
    BuyerProfile,
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
};
</script>
