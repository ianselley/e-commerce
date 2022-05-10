<template>
  <div>
    <div>
      <img
        id="profile-img"
        src="https://ssl.gstatic.com/accounts/ui/avatar_2x.png"
      />
      <form @submit="handleLogin" onsubmit="return false;">
        <div>
          <div>
            <label for="email">Email</label>
            <input id="email" name="email" v-model="values.email" type="text" />
          </div>
          <div>
            <label for="password">Password</label>
            <input
              id="password"
              name="password"
              v-model="values.password"
              type="password"
              autocomplete="on"
            />
          </div>
          <button type="submit" :disabled="loading">
            <span v-show="loading">LOADING</span>
            <span v-show="!loading">Login</span>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
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

<style scoped></style>
