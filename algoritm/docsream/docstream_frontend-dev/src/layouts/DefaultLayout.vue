<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { storeToRefs } from 'pinia';
import Logo from '@/components/Logo.vue';
import { useFileStore } from '@/stores/fileStore';

const appLayout = ref<null | HTMLElement>(null);
const router = useRouter();
const {
  firstFile, secondFile, files,
} = storeToRefs(useFileStore());
const toMainHandler = () => {
  firstFile.value = null;
  secondFile.value = null;
  router.push('/');
};
</script>

<template>
  <div class="default-layout">
    <header class="layout__header">
      <div class="header__logo" @click="toMainHandler">
        <Logo/>
      </div>
    </header>
    <main class="layout__main" ref="appLayout">
      <slot/>
    </main>
  </div>
</template>

<style scoped lang="scss">
.default-layout {
  font-family: 'Stem', sans-serif;
  display: flex;
  background: transparent;
  margin: 0 auto;
  flex-direction: column;
  min-height: 100dvh;
  width: 100%;
  max-width: 1440px;
  row-gap: 8px;
  padding: 16px;
}

.layout__main {
  background: $bg_white;
  border-radius: 16px;
}

.layout__header {
  background: $bg_white;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 22px;
  & .header__logo{
    &:hover{
      cursor: pointer;
    }
  }
}
</style>
