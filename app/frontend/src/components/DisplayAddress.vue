<template>
  <div v-if="hasAttributes" style="border: 1px solid black; border-radius: 5px; max-width: 50%; margin: 5rem auto;">
    <p> {{ address.name }} </p>
    <p> {{ address.street }} {{ address.number }} {{ address.flat }} </p>
    <p> {{ address.zipCode }} {{ address.city }} {{ address.state }} </p>
    <p> {{ address.country }} </p>
    <p> {{ address.details }} </p>
  </div>
</template>

<script>
export default {
  name: 'DisplayAddress',
  props: {
    address: Object,
  },
  computed: {
    hasAttributes() {
      return this.address.city && this.address.street && this.address.state && this.address.zipCode && this.address.country;
    }
  }
}
</script>