<template>
  <div>
    <button
      @click="open"
      :disabled="disabled"
      class="button"
      :class="buttonClass"
    >
      {{ buttonText }}
    </button>
    <div
      v-if="isOpen"
      @click.stop
      @mousedown="closeDown"
      @mouseup="closeUp"
      class="z-50 fixed top-0 left-0 w-full h-full bg-black bg-opacity-50"
    >
      <div
        @mouseup.stop
        @mousedown.stop
        @mouseup="upInside"
        class="modal"
        :class="modalClass"
      >
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
    disabled: {
      type: Boolean,
      default: false,
    },
    modalClass: {
      type: String,
      default: '',
    },
    buttonClass: {
      type: String,
      default: '',
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
.modal {
  @apply fixed bg-white rounded-xl shadow-lg;
  top: 50%;
  left: 50%;
  width: minmax(max-content, 90vw);
  min-height: max-content;
  max-height: 90%;
  overflow: auto;
  transform: translate(-50%, -50%);
}

@screen md {
  .modal {
    max-height: calc(100vh - 80px);
  }
}
</style>
