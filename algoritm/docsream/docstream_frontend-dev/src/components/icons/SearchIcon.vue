<script setup lang="ts">
import { defineProps } from 'vue';

defineProps({
  color: {
    type: String,
    default: '#959FB8',
  },
  width: {
    type: Number,
    default: 16,
  },
  height: {
    type: Number,
    default: 16,
  },
});
</script>

<template>
  <svg :width="width" :height="height" viewBox="0 0 16 16" fill="none"
       xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd"
          d="M7.6649 2.41309C4.72072 2.41309 2.33398 4.79982 2.33398 7.744C2.33398 10.6882 4.72072 13.0749 7.6649 13.0749C10.6091 13.0749 12.9958 10.6882 12.9958 7.744C12.9958 4.79982 10.6091 2.41309 7.6649 2.41309ZM1.33398 7.744C1.33398 4.24753 4.16843 1.41309 7.6649 1.41309C11.1614 1.41309 13.9958 4.24753 13.9958 7.744C13.9958 11.2405 11.1614 14.0749 7.6649 14.0749C4.16843 14.0749 1.33398 11.2405 1.33398 7.744Z"
          fill="#0B0B0B"/>
    <path fill-rule="evenodd" clip-rule="evenodd"
          d="M11.6367 11.5698C11.832 11.3745 12.1486 11.3745 12.3438 11.5698L14.5214 13.7478C14.7167 13.9431 14.7166 14.2597 14.5214 14.4549C14.3261 14.6502 14.0095 14.6502 13.8142 14.4549L11.6366 12.2769C11.4414 12.0816 11.4414 11.765 11.6367 11.5698Z"
          fill="#0B0B0B"/>
  </svg>

</template>

<style scoped lang="scss">

</style>
