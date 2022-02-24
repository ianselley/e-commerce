<template>
  <div class="backdrop">
    <div class="modal">
      <p>{{ modal_content }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Modal',
  props: {
    modal_content: String,
  },
};
</script>

<style>
.backdrop {
  position: fixed;
  top: 10%;
  left: 0;
  width: 100%;
  height: 90%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 10;
}

.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  width: 300px;
  height: 200px;
  border-radius: 5px;
  z-index: 11;
}

p {
  padding: auto;
}
</style>
