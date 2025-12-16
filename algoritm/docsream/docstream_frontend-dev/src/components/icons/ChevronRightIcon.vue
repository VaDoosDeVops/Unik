<script setup lang="ts">
import { defineProps } from 'vue';

defineProps({
  colorBackground: {
    type: String,
    default: '#1A1F2C',
  },
  colorArrow: {
    type: String,
    default: '#FFFFFF',
  },
  width: {
    type: Number,
    default: 28,
  },
  height: {
    Type: Number,
    default: 28,
  },
});
</script>

<template>
  <svg :width="width" :height="height" viewBox="0 0 28 28" fill="none"
       xmlns="http://www.w3.org/2000/svg">
    <rect :width="width" :height="height" rx="8" :fill="colorBackground"/>
    <path fill-rule="evenodd" clip-rule="evenodd"
          d="M10.2929 7.29289C10.6834 6.90237 11.3166 6.90237 11.7071 7.29289L17.5303 13.1161C18.0185 13.6043 18.0185 14.3957 17.5303 14.8839L11.7071 20.7071C11.3166 21.0976 10.6834 21.0976 10.2929 20.7071C9.90237 20.3166 9.90237 19.6834 10.2929 19.2929L15.5858 14L10.2929 8.70711C9.90237 8.31658 9.90237 7.68342 10.2929 7.29289Z"
          :fill="colorArrow"/>
  </svg>

</template>

<style scoped lang="scss">

</style>
