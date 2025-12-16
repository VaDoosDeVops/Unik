<script setup lang="ts">
import { defineProps } from 'vue';

defineProps({
  color: {
    type: String,
    default: '#808688',
  },
});
</script>

<template>
  <svg width="3" height="16" viewBox="0 0 3 16" fill="none" xmlns="http://www.w3.org/2000/svg">
    <ellipse cx="1.49996" cy="2.16666" rx="1.46627" ry="1.45833" :fill="color"/>
    <ellipse cx="1.49996" cy="7.99999" rx="1.46627" ry="1.45833" :fill="color"/>
    <ellipse cx="1.49996" cy="13.8333" rx="1.46627" ry="1.45833" :fill="color"/>
  </svg>

</template>

<style scoped lang="scss">

</style>
