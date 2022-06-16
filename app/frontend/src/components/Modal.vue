<template>
  <div>
    <button @click="open" class="modal-button">{{ buttonText }}</button>
    <div
      v-if="isOpen"
      @mousedown="closeDown"
      @mouseup="closeUp"
      class="z-50 fixed top-0 left-0 w-full h-full bg-black bg-opacity-50"
    >
      <div @mouseup.stop @mousedown.stop @mouseup="upInside" class="modal">
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Modal',
  props: {
    buttonText: {
      type: String,
      default: 'Open Modal',
    },
  },
  data() {
    return {
      isOpen: false,
      downOustide: false,
    };
  },
  methods: {
    closeDown() {
      this.downOutside = true;
    },
    closeUp() {
      if (this.downOutside) {
        this.isOpen = false;
      }
    },
    upInside() {
      this.downOutside = false;
    },
    open() {
      this.isOpen = true;
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
  @apply fixed bg-white rounded-xl shadow-lg;
  top: 50%;
  left: 50%;
  max-height: calc(100vh - 80px);
  max-width: 100vw;
  overflow: auto;
  transform: translate(-50%, -50%);
}
</style>
