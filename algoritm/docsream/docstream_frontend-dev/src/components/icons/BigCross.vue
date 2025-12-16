<script setup lang="ts">
import { defineProps } from 'vue';

defineProps({
  color: {
    type: String,
    default: '#FFFFFF',
  },
  width: {
    type: Number,
    default: 1,
  },
  height: {
    type: Number,
    default: 1,
  },
});
</script>

<template>
  <svg :fill="color" :height="height+'em'" :width="width+'em'"   xmlns="http://www.w3.org/2000/svg"
       viewBox="0 0 490 490" xml:space="preserve">
<polygon points='456.851,0 245,212.564 33.149,0 0.708,32.337 212.669,245.004 0.708,457.678 33.149,490 245,277.443 456.851,490
	489.292,457.678 277.331,245.004 489.292,32.337 '/>
</svg>

</template>

<style scoped lang="scss">

</style>
