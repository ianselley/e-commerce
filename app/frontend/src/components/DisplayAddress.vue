<template>
  <div
    v-if="hasAttributes"
    class="base"
    :class="[addressIsMainId ? 'main-address' : 'not-main-address']"
  >
    <p>
      <strong>{{ address.name }}</strong>
    </p>
    <p>{{ address.street }} {{ address.number }} {{ address.flat }}</p>
    <p>{{ address.zip_code }} {{ address.city }} {{ address.state }}</p>
    <p>{{ address.country }}</p>
    <p>{{ address.details }}</p>
    <div v-if="edit">
      <EditAddress :address="address" />
      <MakeItMainAddress v-if="!addressIsMainId" :addressId="address.id" />
      <DeleteAddress :addressId="address.id" />
    </div>
  </div>
</template>

<script>
import EditAddress from '@/components/EditAddress.vue';
import DeleteAddress from '@/components/DeleteAddress.vue';
import MakeItMainAddress from '@/components/MakeItMainAddress.vue';
export default {
  name: 'DisplayAddress',
  components: {
    EditAddress,
    DeleteAddress,
    MakeItMainAddress,
  },
  props: {
    address: Object,
    edit: {
      default: true,
    },
  },
  computed: {
    hasAttributes() {
      return (
        this.address.city &&
        this.address.street &&
        this.address.state &&
        this.address.zip_code &&
        this.address.country
      );
    },
    addressIsMainId() {
      return this.address.id === this.$store.state.auth.buyer.main_address_id;
    },
  },
};
</script>

<style lang="postcss" scoped>
.base {
  border-radius: 1rem;
  max-width: 50%;
  margin: 1.5rem auto;
}

.main-address {
  border: 2px solid hsl(44, 81%, 49%);
  background-color: bisque;
}

.not-main-address {
  border: 1px solid black;
  background-color: #eee;
}
</style>
