<script setup>
import { defineProps } from 'vue';
import LogoText from '@/components/icons/LogoText.vue';

defineProps({
  hasTextLogo: Boolean,
});
</script>

<template>
  <div v-if="hasTextLogo" class="logo-full">
    <img src="@/assets/images/logo-img.png" alt="Facebank Icon">
    <LogoText/>
  </div>
  <img class="logo-icon" v-else src="@/assets/images/logo-img.png"
       alt="Facebank Icon">
</template>

<style lang="scss" scoped>
.logo {
  &-full {
    display: flex;
    align-items: center;
    height: 48px;

    img {
      display: block;

      &[alt="Facebank Icon"] {
        height: 100%;
        margin-right: 10px;
      }

      &[alt="Facebank"] {
        height: 80%;
      }
    }
  }

  &-icon {
    display: block;
    height: 48px;
  }
}
</style>
