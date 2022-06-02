<template>
  <div
    v-if="activeModal"
    @click="this.$store.commit('modal/deactivateModal')"
    class="z-50 fixed top-0 left-0 w-full h-full bg-black bg-opacity-50"
  >
    <div @click.stop class="modal">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Modal',
  data() {
    return {
      isOpen: true,
    };
  },
  methods: {
    close() {
      this.isOpen = false;
    },
  },
  computed: {
    activeModal() {
      return this.$store.state.modal.active;
    },
  },
};
</script>

<style lang="postcss" scoped>
html,
body {
  height: 100%;
  overflow: hidden;
}

.modal {
  @apply fixed bg-white p-12 rounded-md shadow-lg;
  top: 50%;
  left: 50%;
  max-height: calc(100vh - 80px);
  overflow-y: auto;
  transform: translate(-50%, -50%);
}
</style>
