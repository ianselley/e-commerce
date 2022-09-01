<template>
  <div
    id="nav"
    class="px-10 py-6 mb-8 sticky top-0 z-30 flex flex-row justify-between bg-white bg-opacity-70 backdrop-filter backdrop-blur-md shadow"
  >
    <IanSelleyLogo />
    <SearchBar v-if="home" />
    <div id="endpoints" class="flex flex-row content-center space-x-8">
      <router-link to="/">
        <HomeLogo class="color-fill" />
      </router-link>
      <router-link to="/about">About</router-link>
      <router-link v-if="!loggedIn" to="/signup">Signup</router-link>
      <router-link v-if="!loggedIn" to="/login" class="button-a">
        <button>Login</button>
      </router-link>
      <router-link v-if="userIsSeller" to="/products">Products</router-link>
      <router-link v-if="loggedIn" to="/orders">Orders</router-link>
      <router-link v-if="userIsBuyer" to="/cart">
        <ShoppingCartLogo class="color-fill" />
      </router-link>
      <router-link v-if="loggedIn" to="/profile">
        <ProfileLogo class="color-stroke" />
      </router-link>
      <button v-if="loggedIn" @click="logout">Logout</button>
    </div>
  </div>
</template>

<script>
import HomeLogo from '@/components/HomeLogo.vue';
import SearchBar from '@/components/SearchBar.vue';
import ProfileLogo from '@/components/ProfileLogo.vue';
import IanSelleyLogo from '@/components/IanSelleyLogo.vue';
import ShoppingCartLogo from '@/components/ShoppingCartLogo.vue';
export default {
  name: 'Navbar',
  components: {
    HomeLogo,
    SearchBar,
    ProfileLogo,
    IanSelleyLogo,
    ShoppingCartLogo,
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
    home() {
      return this.$route.path == '/';
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

a.router-link-exact-active .color-fill :deep(.color) {
  fill: #f59e0b;
}

a.router-link-exact-active .color-stroke :deep(.color) {
  stroke: #f59e0b;
}

#endpoints > * {
  @apply transition font-semibold ease-in-out duration-300 transform hover:scale-110;
}

button {
  @apply bg-violet-500 hover:bg-amber-500;
}
</style>
