<template>
  <div class="flex flex-col justify-center">
    <DefaultImageProfile />
    <form @submit="handleLogin" onsubmit="return false;">
      <div class="form-content">
        <div class="form-title">LOGIN</div>
        <div>
          <p><label for="email">Email</label></p>
          <input
            id="email"
            name="email"
            v-model="values.email"
            type="text"
            class="focus:outline-none"
          />
        </div>
        <div>
          <p><label for="password">Password</label></p>
          <input
            id="password"
            name="password"
            v-model="values.password"
            type="password"
            autocomplete="on"
          />
        </div>
        <button type="submit" :disabled="loading" class="register-button">
          <img src="@/assets/loader.svg" alt="loading" v-show="loading" />
          <span v-show="!loading">LOGIN</span>
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import DefaultImageProfile from '@/components/DefaultImageProfile.vue';
export default {
  name: 'Login',
  components: {
    DefaultImageProfile,
  },
  data() {
    const values = {
      email: '',
      password: '',
    };
    return {
      loading: false,
      values,
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.loggedIn;
    },
  },
  created() {
    if (this.loggedIn) {
      this.$router.push('/profile');
      this.$store.commit(
        'alert/setMessage',
        'You are already logged in, you would have to log out to access this'
      );
    }
  },
  methods: {
    handleLogin() {
      this.loading = true;
      const user = Object.assign({}, this.values);
      this.$store
        .dispatch('auth/login', user)
        .then((response) => {
          if (response.seller) {
            const sellerId = response.seller.id;
            return this.$store.dispatch('product/getSellerProducts', sellerId);
          }
        })
        .then(() => {
          this.loading = false;
          this.$router.push('/profile');
        })
        .catch((error) => {
          this.$store.dispatch('alert/setMessage', error);
          this.loading = false;
        });
    },
  },
};
</script>

<style lang="postcss" scoped></style>
