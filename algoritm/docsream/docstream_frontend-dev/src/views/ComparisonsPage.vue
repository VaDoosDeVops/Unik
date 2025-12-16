<script setup lang="ts">

import { onMounted, ref } from 'vue';
import { storeToRefs } from 'pinia';
import Document from '@/components/Document.vue';
import { FileNumber, useFileStore } from '@/stores/fileStore';
import { allowedSeparate, allowedTypes } from '@/types/types';
import { useNotesStore } from '@/stores/notificationStore';
import { getTypeFile } from '@/utils/files';

const fileStore = useFileStore();
const { firstFile, secondFile } = storeToRefs(fileStore);
const document1Ref = ref(null);
const document2Ref = ref(null);
const notesStore = useNotesStore();
let flag1 = 0;
let flag2 = 0;
const checkValue = (file: File) => {
  if (file) {
    if (!allowedTypes.includes(file.type)) {
      notesStore.append('fail', 'Произошла ошибка', 'Недопустимый формат файла', 3000);
      return false;
    }
    if (file.size > 10_240_000) {
      notesStore.append('fail', 'Произошла ошибка', 'Слишком большой размер файла', 3000);
      return false;
    }
    return true;
  }
  return false;
};

const updateFile = async (fileNumber: FileNumber, newFile: File) => {
  if (checkValue(newFile)) {
    const firstType = getTypeFile(newFile.name);
    if (fileNumber === FileNumber.FIRST) {
      const secondType = getTypeFile(localStorage.getItem('securedSourceSecondFilename') || '');
      const allowesArray = allowedSeparate.find((array) => array.includes(secondType));
      if (!allowesArray?.includes(firstType)) {
        notesStore.append('fail', 'Произошла ошибка', `Файлы разрешения ${firstType} и ${secondType} не сравниваются`, 3000);
        return;
      }
      firstFile.value = newFile;
      localStorage.setItem('firstFilename', newFile.name);
    } else if (fileNumber === FileNumber.SECOND) {
      const secondType = getTypeFile(localStorage.getItem('securedSourceFirstFilename') || '');
      const allowesArray = allowedSeparate.find((array) => array.includes(secondType));
      if (!allowesArray?.includes(firstType)) {
        notesStore.append('fail', 'Произошла ошибка', `Файлы разрешения ${firstType} и ${secondType} не сравниваются`, 3000);
        return;
      }
      secondFile.value = newFile;
      localStorage.setItem('secondFilename', newFile.name);
    }
  }
  fileStore.isLoading = true;
  await fileStore.upload(fileNumber, newFile);
  await fileStore.compareFiles();
  await Promise.all([
    fileStore.saveFile(FileNumber.FIRST),
    fileStore.saveFile(FileNumber.SECOND),
  ]);
  fileStore.isLoading = false;
};

const handleScroll1 = (scrollTop: number) => {
  if (document2Ref.value) {
    if (!flag2) {
      document2Ref.value.setScroll(scrollTop);
    }
    flag1 = 1;
    flag2 = 0;
  }
};

const handleScroll2 = (scrollTop: number) => {
  if (document1Ref.value) {
    flag2 = 1;
    if (!flag1) {
      document1Ref.value.setScroll(scrollTop);
    }
    flag1 = 0;
  }
};

onMounted(async () => {
  await Promise.all([
    fileStore.saveFile(FileNumber.FIRST),
    fileStore.saveFile(FileNumber.SECOND),
  ]);
});

</script>

<template>
  <div class="page-container">
    <div v-if="fileStore.firstCompareFile!==null && fileStore.secondCompareFile!==null"  class="documents-block block">
      <Document ref="document1Ref" :file="fileStore.firstCompareFile" @scroll="handleScroll1"
                file-id="first_document" :docNumber="1"
                @update-file="(newFile)=> updateFile(FileNumber.FIRST, newFile)"/>
      <Document ref="document2Ref" :file="fileStore.secondCompareFile" :docNumber="2"
                @scroll="handleScroll2" :has-scrollbar="false" file-id="second_document"
                @update-file="(newFile)=> updateFile(FileNumber.SECOND, newFile )"/>
    </div>

  </div>
</template>

<style  lang="scss">
td{
  border: 1px solid lightgray !important;
}
.page-container {
  width: 100%;
  height: calc(100dvh - 122px);
  display: flex;
  gap: 8px;

  & .documents-block {
    width: 100%;
    padding: 16px 16px 0;
    display: flex;
    justify-content: space-between;
  }

  & .difference-block {
    padding: 16px;
  }
}

</style>
