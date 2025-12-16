<script setup lang="ts">
import { defineProps } from 'vue';

defineProps({
  colorBackground: {
    type: String,
    default: '#EFF2F6',
  },
  colorArrow: {
    type: String,
    default: '#1A1F2C',
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
          d="M17.7071 7.29289C18.0976 7.68342 18.0976 8.31658 17.7071 8.70711L12.4142 14L17.7071 19.2929C18.0976 19.6834 18.0976 20.3166 17.7071 20.7071C17.3166 21.0976 16.6834 21.0976 16.2929 20.7071L10.4697 14.8839C9.98151 14.3957 9.98151 13.6043 10.4697 13.1161L16.2929 7.29289C16.6834 6.90237 17.3166 6.90237 17.7071 7.29289Z"
          :fill="colorArrow"/>
  </svg>

</template>

<style scoped lang="scss">

</style>
