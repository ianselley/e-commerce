<template>
  <div
    id="nav"
    class="px-10 py-6 mb-8 sticky top-0 z-40 flex flex-row justify-between bg-white bg-opacity-70 backdrop-filter backdrop-blur-md shadow"
  >
    <IanSelleyLogo />
    <div id="endpoints" class="flex flex-row content-center space-x-8">
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
      <router-link v-if="!loggedIn" to="/signup">Signup</router-link>
      <router-link v-if="!loggedIn" to="/login" class="button-a">
        <button>Login</button>
      </router-link>
      <router-link v-if="userIsSeller" to="/products">Products</router-link>
      <router-link v-if="loggedIn" to="/orders">Orders</router-link>
      <router-link v-if="userIsBuyer" to="/cart">
        <ShoppingCartLogo class="color" />
      </router-link>
      <router-link v-if="loggedIn" to="/profile">
        <ProfileLogo class="color" />
      </router-link>
      <button v-if="loggedIn" @click="logout">Logout</button>
    </div>
  </div>
</template>

<script>
import IanSelleyLogo from '@/components/IanSelleyLogo.vue';
import ShoppingCartLogo from '@/components/ShoppingCartLogo.vue';
import ProfileLogo from '@/components/ProfileLogo.vue';
export default {
  name: 'Navbar',
  components: {
    IanSelleyLogo,
    ShoppingCartLogo,
    ProfileLogo,
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.loggedIn;
    },
    currentUser() {
      return this.$store.state.auth.user;
    },
    userIsSeller() {
      return this.$store.state.auth.loggedInAs == 'seller';
    },
    currentSeller() {
      return this.$store.state.auth.seller;
    },
    userIsBuyer() {
      return this.$store.state.auth.loggedInAs == 'buyer';
    },
    currentBuyer() {
      return this.$store.state.auth.buyer;
    },
  },
  methods: {
    logout() {
      if (this.loggedIn) {
        this.$store.dispatch('auth/logout');
        this.$store.dispatch('product/removeSellerProducts');
      }
      if (!this.currentUser) {
        this.$router.push('/login');
      }
      this.$store.dispatch('auth/logout');
    },
  },
};
</script>

<style lang="postcss" scoped>
#nav * {
  @apply font-bold;
}

#nav a:not(.button-a) {
  @apply flex content-center items-center leading-10 text-violet-900;
}

#nav a.router-link-exact-active {
  @apply text-amber-500;
}

#nav a.router-link-exact-active button {
  @apply bg-amber-400 transition ease-in-out duration-300 hover:bg-amber-500;
}

#nav a.router-link-exact-active .color :deep(.color) {
  fill: #f59e0b;
  stroke: #f59e0b;
}

#endpoints > * {
  @apply transition font-semibold ease-in-out duration-300 transform hover:scale-110;
}

button {
  @apply bg-violet-500 hover:bg-violet-400;
}
</style>
