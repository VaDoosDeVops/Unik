<script setup lang="ts">
import { defineProps } from 'vue';

defineProps({
  color: {
    type: String,
    default: '#292C33',
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
    <path d="M2.66699 8L13.3337 8" :stroke="color" stroke-width="1.5" stroke-linecap="round"
          stroke-linejoin="round"/>
  </svg>
</template>

<style scoped lang="scss">

</style>
