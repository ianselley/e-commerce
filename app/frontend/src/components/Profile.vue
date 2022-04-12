<template>
  <div v-if="currentUser">
    <header>
      <h3>
        <strong>{{
          (currentSeller && currentSeller.brand) ||
          (currentBuyer && currentBuyer.name + ' ' + currentBuyer.surname)
        }}</strong>
        Profile
      </h3>
    </header>
    <p>
      <strong>Token:</strong>
      {{ currentUser.access_token }}
    </p>
    <p>
      <strong>User id:</strong>
      {{ currentUser.id }}
    </p>
    <p>
      <strong>Email:</strong>
      {{ currentUser.email }}
    </p>
    <p>
      <strong>Role:</strong>
      {{ currentUser.role }}
    </p>
    <BuyerProfile v-if="userIsBuyer" />
    <SellerProfile v-if="userIsSeller" />
  </div>
</template>

<script>
import BuyerProfile from '@/components/BuyerProfile.vue';
import SellerProfile from '@/components/SellerProfile.vue';

export default {
  name: 'Profile',
  components: {
    BuyerProfile,
    SellerProfile,
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
      this.$store.dispatch('alert/setMessage', 'You are not logged in!');
    } else {
      this.$store
        .dispatch('auth/getUser', this.currentUser.id)
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
