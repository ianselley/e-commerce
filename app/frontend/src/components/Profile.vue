<template>
  <div v-if="currentUser">
    <pre> {{ currentUser }} </pre>
    <header>
      <h3>
        <!-- <strong>{{
          (currentUser.seller && currentUser.seller.brand) || currentUser.buyer && (currentUser.buyer.name + ' ' + currentUser.buyer.surname)
        }}</strong> -->
        Profile
      </h3>
    </header>
    <p>
      <strong>Token:</strong>
      {{ currentUser.accessToken }}
    </p>
    <p>
      <strong>Id:</strong>
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
      return this.currentUser.role == 'buyer';
    },
    userIsSeller() {
      return this.currentUser.role == 'seller';
    },
  },
  created() {
    if (!this.currentUser) {
      this.$router.push('/login');
      this.$store.commit('alert/setMessage', 'You are not logged in!');
    }
  },
};
</script>
