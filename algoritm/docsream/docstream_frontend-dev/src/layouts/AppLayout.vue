<script setup lang="ts">
import { useRoute } from 'vue-router';
import NotificationList from '@/components/NotificationList.vue';

const route = useRoute();

</script>

<template>
  <div class="main-wrapper">
    <component :is="route.meta.layoutComponent">
      <slot/>
    </component>
    <NotificationList/>
  </div>
</template>

<style scoped lang="scss">
.main-wrapper {
  font-family: 'Stem', sans-serif;
  display: flex;
  background: $bg_light_grey;
  min-height: 100dvh;
  overflow: hidden;
}
</style>
