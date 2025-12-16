<script setup lang="ts">
import { watch } from 'vue';
import { storeToRefs } from 'pinia';
import DragnDrop from '@/components/DragnDrop.vue';
import { FileNumber, useFileStore } from '@/stores/fileStore';
import { useNotesStore } from '@/stores/notificationStore';
import { allowedSeparate } from '@/types/types';
import SpinnerIcon from '@/components/icons/SpinnerIcon.vue';
import { getTypeFile } from '@/utils/files';
import router from '@/router';

const fileStore = useFileStore();
const notesStore = useNotesStore();
const {
  isLoading, firstFile, secondFile, firstCompareFile, secondCompareFile,
} = storeToRefs(fileStore);

watch(() => firstFile.value, () => {
  if (secondFile.value && firstFile.value) {
    const firstType = getTypeFile(secondFile.value.name);
    const secondType = getTypeFile(firstFile.value.name);
    const allowesArray = allowedSeparate.find((array) => array.includes(firstType));
    if (!allowesArray?.includes(secondType) && secondFile.value && firstFile.value) {
      notesStore.append('fail', 'Произошла ошибка', `Файлы разрешения ${firstType} и ${secondType} не сравниваются`, 3000);
      firstFile.value = null;
    }
  }
});
watch(() => secondFile.value, () => {
  if (secondFile.value && firstFile.value) {
    const firstType = getTypeFile(firstFile.value.name);
    const secondType = getTypeFile(secondFile.value.name);
    const allowesArray = allowedSeparate.find((array) => array.includes(firstType));
    if (!allowesArray?.includes(secondType) && secondFile.value && firstFile.value) {
      notesStore.append('fail', 'Произошла ошибка', `Файлы разрешения ${firstType} и ${secondType} не сравниваются`, 3000);
      secondFile.value = null;
      firstFile.value = null;
    }
  }
});

const separateFiles = async () => {
  isLoading.value = true;
  localStorage.setItem('firstFilename', fileStore.firstFile?.name);
  localStorage.setItem('secondFilename', fileStore.secondFile?.name);
  await Promise.all([
    await fileStore.upload(FileNumber.FIRST, fileStore.firstFile),
    await fileStore.upload(FileNumber.SECOND, fileStore.secondFile),
  ]);
  await new Promise((resolve) => {
    setTimeout(() => {
      resolve(() => console.log('calculated'));
    }, 60000);
  });
  await fileStore.compareFiles();
  isLoading.value = false;

  router.push('/differences');
};
</script>

<template>
  <div  class="load page-container">
    <div class="first-mash mash"></div>
    <div class="forth-mash mash"></div>
    <div class="second-mash mash"></div>
    <div class="third-mash mash"></div>
    <div class="load__title">
      <div class="main-title">
        Вы ищете корпоративное решение для <span class="focus">сравнения</span>
        документов?
      </div>
      <div class="secondary-title">
        Откройте для себя наши профессиональные решения для юридических фирм,групп
        и крупных организаций
      </div>
    </div>
    <div class="wrapper">
      <div class="block first-block">
        <DragnDrop secondary-text="Размер до 10MB / Формат docx,<br> rtf, pdf, xlsx"
                   primary-text="Перетащите файл сюда" v-model="firstFile" unique-class="first"
                   :disabled="isLoading"/>
      </div>
      <div class="block second-block">
        <DragnDrop secondary-text="Размер до 10MB / Формат docx,<br> rtf, pdf, xlsx"
                   primary-text="Перетащите файл сюда" v-model="secondFile" unique-class="second"
                   :disabled="isLoading"/>
      </div>
      <div class="circle-with-padding">
        <div class="circle-content"
             :class="{disabled: !firstFile || !secondFile, loading: isLoading}"
             @click="separateFiles">
          <span class="text" v-if="!isLoading">Сравнить</span>
          <SpinnerIcon v-else :size="58"/>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">

.page-container {
  width: 100%;
  height: 100%;
  padding: 32px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  border-radius: 16px;
  row-gap: 70px;
  position: relative;

  .load__title {
    display: flex;
    flex-direction: column;
    row-gap: 24px;
    align-items: center;

    .main-title {
      font-family: 'Stem', sans-serif;
      color: $text_black;
      font-size: 44px;
      font-weight: 500;
      line-height: 48.4px;
      letter-spacing: -1px;
      text-align: center;
      max-width: 770px;

      .focus {
        color: $text-green;
      }
    }

    .secondary-title {
      font-family: 'Suisse Intl', sans-serif;
      font-weight: 400;
      max-width: 450px;
      font-size: 18px;
      line-height: 21.6px;
      text-align: center;
      color: $text_light-grey;
    }
  }

  .mash {
    position: absolute;
    border-radius: 50%;
    opacity: 60%;

    &.first-mash, &.forth-mash {
      width: 300px;
      height: 250px;
      background: radial-gradient(circle, rgba(116, 205, 255, 0.7) 0%, rgba(116, 205, 255, 0) 100%);
      filter: blur(50px);
    }

    &.second-mash, &.third-mash {
      width: 220px;
      height: 220px;
      background: radial-gradient(circle, rgb(69 225 140 / 70%) 0%, rgba(59, 219, 132, 0) 100%);
      filter: blur(35px);
    }
  }

  .first-mash {
    top: 199px;
    left: 0px;
  }

  .second-mash {
    top: 240px;
    left: 240px;
  }

  .third-mash {
    top: 240px;
    right: 240px;
  }

  .forth-mash {
    top: 199px;
    right: 0px;
  }
}

.wrapper {
  max-width: 1440px;
  display: flex;
  gap: 10px;
  width: 100%;
  position: relative;
  min-height: 483px;

  .block {
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    flex: 1;
    background: white;
    position: relative;
    border-radius: 24px;
    border: 1px dashed $bg_bright_blue;
  }

  .first-block::before,
  .second-block::before {
    content: '';
    position: absolute;
    background: inherit;
    top: -50px;
    border-radius: 50%;
    border: 1px dashed $bg_bright_blue;
    width: 196px;
    height: 196px;
    overflow: hidden;
    z-index: 10;
  }

  .first-block::before {
    right: -102.5px;

  }

  .second-block::before {
    left: -102px;
  }
}

.circle-with-padding {
  top: -48px;
  z-index: 10000;
  position: absolute;
  left: 50%;
  width: 200.5px;
  height: 195.5px;
  background: white;
  border-radius: 50%;
  transform: translateX(-50%);
}

.circle-content {
  top: 6px;
  background: $text-green;
  border-radius: 50%;
  z-index: 100;
  position: absolute;
  transform: translateX(-50%);
  left: 50%;
  width: 181px;
  height: 181px;
  pointer-events: auto;
  transition: $transition;
  justify-content: center;
  display: flex;
  align-items: center;

  &:not(.disabled):not(.loading):hover {
    background-color: $bg_dark_green;
    cursor: pointer;
  }

  &.loading {
    pointer-events: none;
  }

  &.disabled {
    opacity: 60%;
    pointer-events: none;
    cursor: auto;
  }
}

.text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-family: Stem, sans-serif;
  font-size: 24px;
  font-weight: 500;
  line-height: 26.4px;
  text-align: center;
  color: $text-white;
}
</style>
