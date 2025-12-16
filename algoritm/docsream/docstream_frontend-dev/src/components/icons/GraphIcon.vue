<script setup>
import { defineProps } from 'vue';

defineProps({
  color: {
    type: String,
    default: '#8B8D97',
  },
});
</script>

<template>
  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd"
          d="M18 9C18.5523 9 19 9.44772 19 10L19 20C19 20.5523 18.5523 21 18 21C17.4477 21 17 20.5523 17 20L17 10C17 9.44772 17.4477 9 18 9ZM12 6.5C12.5523 6.5 13 6.94772 13 7.5L13 20C13 20.5523 12.5523 21 12 21C11.4477 21 11 20.5523 11 20L11 7.5C11 6.94772 11.4477 6.5 12 6.5ZM6 3C6.55229 3 7 3.44771 7 4L7 20C7 20.5523 6.55228 21 6 21C5.44771 21 5 20.5523 5 20L5 4C5 3.44771 5.44771 3 6 3Z"
          :fill="color"/>
  </svg>
</template>
