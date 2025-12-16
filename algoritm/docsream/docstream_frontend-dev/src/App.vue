<script lang="ts" setup>
import AppLayout from '@/layouts/AppLayout.vue';
import './assets/fonts/stylesheet.css';
</script>

<template>
  <AppLayout>
    <RouterView/>
  </AppLayout>
</template>

<style lang="scss">
@import './assets/fonts/stylesheet.css';

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

</style>
