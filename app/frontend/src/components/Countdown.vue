<template>
  <div>
    <span>{{ timer.days }}</span
    >:<span>{{ timer.hours }}</span
    >:<span>{{ timer.minutes }}</span>
  </div>
</template>

<script>
import { useTimer } from 'vue-timer-hook';
export default {
  name: 'Countdown',
  props: {
    deadline: Date,
  },
  data() {
    const timer = useTimer(this.deadline);
    return {
      timer,
    };
  },
};
</script>

<style lang="postcss" scoped></style>
