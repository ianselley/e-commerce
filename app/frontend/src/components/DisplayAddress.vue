<template>
  <div
    v-if="hasAttributes"
    class="base break-words"
    :class="[addressIsMainId ? 'main-address' : 'not-main-address']"
  >
    <p>
      <strong>{{ address.name }}</strong>
    </p>
    <p>{{ address.street }} {{ address.number }} {{ address.flat }}</p>
    <p>{{ address.zip_code }} {{ address.city }} {{ address.state }}</p>
    <p>{{ address.country }}</p>
    <p>{{ address.details }}</p>
    <div
      v-if="edit"
      class="flex flex-col md:flex-row justify-center md:items-center space-y-2 md:space-y-0 md:space-x-2 mt-4"
    >
      <Modal button-text="Edit Address" class="edit-address">
        <RegisterAddress v-if="edit" :address="address" />
      </Modal>
      <MakeItMainAddress v-if="!addressIsMainId" :addressId="address.id" />
      <DeleteAddress :addressId="address.id" />
    </div>
  </div>
</template>

<script>
import Modal from '@/components/Modal.vue';
import RegisterAddress from '@/components/RegisterAddress.vue';
import DeleteAddress from '@/components/DeleteAddress.vue';
import MakeItMainAddress from '@/components/MakeItMainAddress.vue';
export default {
  name: 'DisplayAddress',
  components: {
    Modal,
    RegisterAddress,
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
  @apply rounded-md mx-auto p-6;
  max-width: 80vw;
}

@screen md {
  .base {
    max-width: 50vw;
  }
}

.main-address {
  @apply border-2 border-amber-400 bg-amber-100;
}

.not-main-address {
  @apply border border-gray-300 bg-gray-100;
}

.edit-address :deep() .form-content {
  @apply shadow-none;
}
</style>
