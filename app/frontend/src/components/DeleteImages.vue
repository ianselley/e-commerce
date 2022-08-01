<template>
  <div>
    <Modal button-text="Select images to delete" button-class="w-full">
      <div class="bg-white big-width sticky top-0 py-4 z-20">
        <button :disabled="loading || noneChecked" @click="deleteImages">
          Delete Images
        </button>
      </div>
      <div class="grid grid-cols-3 gap-y-8 gap-x-3 m-8 mt-0">
        <div
          v-for="image in images"
          :key="image"
          class="h-0 w-full pb-full relative mb-6 space-x-2"
        >
          <input
            :id="image.id"
            type="checkbox"
            :value="image.id"
            @change="check($event, image.id)"
          />
          <label :for="image.id" class="flex items-center justify-center">
            <Image :src="image.id" :alt="image.filename" class="image" />
          </label>
        </div>
      </div>
    </Modal>
  </div>
</template>

<script>
import Image from '@/components/Image.vue';
import Modal from '@/components/Modal.vue';
export default {
  name: 'DeleteImages',
  components: {
    Image,
    Modal,
  },
  props: {
    productId: Number,
    images: Array,
  },
  data() {
    return {
      loading: false,
      checkedIds: {},
    };
  },
  mounted() {
    this.initializeCheckedIds();
  },
  computed: {
    noneChecked() {
      return Object.values(this.checkedIds).every((item) => item === false);
    },
  },
  methods: {
    initializeCheckedIds() {
      for (let image of this.$props.images) {
        this.checkedIds = {};
        this.checkedIds[image.id] = false;
      }
    },
    check(e, id) {
      this.checkedIds[id] = e.target.checked;
    },
    deleteImages() {
      this.loading = true;
      let imageIds = [];
      for (let [id, checked] of Object.entries(this.checkedIds)) {
        if (checked) {
          imageIds.push(id);
        }
      }
      imageIds = imageIds.join(',');
      this.$store
        .dispatch('product/deleteImages', {
          productId: this.$props.productId,
          imageIds,
        })
        .then(() => {
          this.loading = false;
          this.initializeCheckedIds();
        })
        .catch((error) => {
          this.loading = false;
          this.$store.dispatch('alert/setMessage', error);
        });
    },
  },
};
</script>

<style lang="postcss" scoped>
.big-width {
  width: 50rem;
}

.image {
  margin-top: 100%;
  max-width: 100%;
  @apply absolute max-h-full w-auto h-auto;
}
</style>
