<script setup>
import { defineProps } from 'vue';

defineProps({
  size: {
    type: Number,
    default: 1,
  },
  white: {
    type: Boolean,
    default: false,
  },
  type: {
    type: String,
    default: 'white',
  },
});

</script>

<template>
  <img v-if="type==='white'" src="@/assets/images/loader.svg"
       :style="(white?'filter: brightness(0) invert(1);':'')+'width:'+size+'px;height:'+size+'px'"
       alt="loading">
  <img v-if="type==='blue'" src="@/assets/images/blue-loader.svg"
       :style="(white?'filter: brightness(0) invert(1);':'')+'width:'+size+'px;height:'+size+'px'"
       alt="loading">
</template>

<style scoped>
img {
  display: block;
  width: 100%;
  height: 100%;
  -webkit-animation: rotate-center 2s linear infinite both;
  animation: rotate-center 2s linear infinite both;
}

@-webkit-keyframes rotate-center {
  0% {
    -webkit-transform: rotate(0);
    transform: rotate(0);
  }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@keyframes rotate-center {
  0% {
    -webkit-transform: rotate(0);
    transform: rotate(0);
  }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

</style>
