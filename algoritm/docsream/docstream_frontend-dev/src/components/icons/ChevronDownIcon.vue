<script setup lang="ts">
import { defineProps } from 'vue';

defineProps({
  colorArrow: {
    type: String,
    default: '#292C33',
  },
  width: {
    type: Number,
    default: 16,
  },
  height: {
    Type: Number,
    default: 16,
  },
});
</script>

<template>
  <svg :width="width" :height="height" viewBox="0 0 16 16" fill="none"
       xmlns="http://www.w3.org/2000/svg">
    <path d="M12.6663 5.99984L7.99967 10.6665L3.33301 5.99984" :stroke="colorArrow"
          stroke-width="1.33333" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>

</template>

<style scoped lang="scss">

</style>
