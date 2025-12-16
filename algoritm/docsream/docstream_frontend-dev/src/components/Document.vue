<script setup lang="ts">
import {
  computed,
  defineEmits,
  defineExpose,
  defineProps,
  nextTick,
  onMounted,
  onUnmounted, provide,
  ref, watch,
} from 'vue';
import { storeToRefs } from 'pinia';
import SearchIcon from '@/components/icons/SearchIcon.vue';
import Input from '@/components/Input.vue';
import MinusIcon from '@/components/icons/MinusIcon.vue';
import PlusIcon from '@/components/icons/PlusIcon.vue';
import { documentIcons, getNameFile, getTypeFile } from '@/utils/files';
import UnknownFileIcon from '@/components/icons/UnknownFileIcon.vue';
import ChevronDownIcon from '@/components/icons/ChevronDownIcon.vue';
import WordViewer from '@/components/WordView.vue';
import SimpleButton from '@/components/SimpleButton.vue';
import Download from '@/components/icons/Download.vue';
import { allowedSeparate } from '@/types/types';
import ExelView from '@/components/ExelView.vue';
import { useFileStore } from '@/stores/fileStore';

const props = defineProps({
  file: {
    type: Object as () => File || null,
    required: true,
  },
  hasScrollbar: {
    type: Boolean,
    default: true,
  },
  fileId: {
    type: String,
    required: true,
  },
  docNumber: {
    type: Number,
    required: true,
  },

});

const emit = defineEmits(['scroll', 'save', 'update-file']);

const search = ref('');
const topArray = ref<number[]>([0]);
const currentPage = ref(1);
const {
  curPage, totalPages, scale, findCounters,
} = storeToRefs(useFileStore());
const {
  incrementPage,
  decrementPage,
  setCurPage,
  setTotalPages,
  incrementScale,
  decrementScale,
  clearFindCounters,
} = useFileStore();
const documentBlock = ref<HTMLDivElement | null>(null);
const container = ref<HTMLDivElement | null>(null);
let uploadInput: HTMLInputElement | null = null;

const documentIcon = computed(() => {
  if (props && props.file && props.file.type) {
    let elem = null;
    if (props.fileId === 'first_document') elem = documentIcons.find((el) => el.type.includes(getTypeFile(localStorage.getItem('firstFilename').toLowerCase())));
    if (props.fileId === 'second_document') elem = documentIcons.find((el) => el.type.includes(getTypeFile(localStorage.getItem('secondFilename').toLowerCase())));
    if (elem) {
      return elem.icon;
    }
  }
  return UnknownFileIcon;
});

const documentName = computed(() => {
  if (props && props.file) {
    if (props.fileId === 'first_document') return getNameFile(localStorage.getItem('firstFilename'));
    if (props.fileId === 'second_document') return getNameFile(localStorage.getItem('secondFilename'));
  }
  return '';
});

const validatePage = (currentValue) => {
  if (currentPage.value > 0) {
    return currentValue <= totalPages.value && currentValue >= 1;
  }
  return false;
};

function findPage(num: number) {
  for (let i = 0; i < topArray.value.length - 1; i += 1) {
    if (num < topArray.value[i + 1]) {
      return i + 1;
    }
  }
  return topArray.value.length;
}

const handleScroll = (event) => {
  if (documentBlock.value) {
    const scrollPosition = documentBlock.value.scrollTop;
    currentPage.value = findPage(scrollPosition);
    emit('scroll', scrollPosition);
  }
};

const setScroll = (scrollTop: number) => {
  if (documentBlock.value) {
    const elem = container.value.querySelector('.document-block');
    elem.scrollTop = scrollTop;
    currentPage.value = findPage(scrollTop);
  }
};

const scrollNeedPage = (immediate: boolean) => {
  // const smoothBehavior = immediate ? 'instant' : 'smooth';
  if (container.value) {
    const elem = container.value.querySelector('.document-block');
    if (currentPage.value === 1 && elem) {
      elem.scrollTo({
        top: 0,
        behavior: 'instant',
      });
      emit('scroll', 0);
    } else {
      const hrElements = container.value.querySelectorAll('#doc-content hr.page-break');
      const index = currentPage.value - 2;
      if (hrElements && index >= 0 && index < hrElements.length && elem) {
        const value = topArray.value[index + 1] + 5;
        elem.scrollTo({
          top: value,
          behavior: 'instant',
        });
        emit('scroll', value);
      }
    }
  }
};

const handlePageInput = (newVal) => {
  setCurPage(newVal);
  scrollNeedPage(true);
};
const handleUpArrowClick = () => {
  decrementPage();
  scrollNeedPage(false);
};
const handleDownArrowClick = async () => {
  incrementPage();
  scrollNeedPage(false);
};

const setScrollListener = () => {
  const allElements = container.value?.querySelectorAll('hr.page-break');
  topArray.value = [0];
  if (allElements) {
    allElements.forEach((hr: HTMLElement, idx) => {
      const { offsetTop } = hr;
      topArray.value.push(offsetTop);
    });
    // console.log(topArray.value.length);
    // totalPages.value = topArray.value.length;
  }
};

const zoomIn = async () => {
  if (scale.value > 0.5) {
    incrementScale();
    await nextTick();
    setScrollListener();
  }
};

const zoomOut = async () => {
  if (scale.value < 4) { decrementScale(); }
  await nextTick();
  setScrollListener();
};

const saveFiles = () => {
  if (props.file) {
    try {
      const url = URL.createObjectURL(props.file);
      const a = document.createElement('a');
      a.classList.add('download');
      a.href = url;
      a.download = props.file.name;
      container.value?.appendChild(a);
      a.click();
      container.value?.removeChild(a);
      URL.revokeObjectURL(url);
    } catch (err) {
      console.log('error', err);
    }
  }
};
const callInput = () => {
  uploadInput?.click();
};
const inputFile = (newVal) => {
  emit('update-file', newVal.target.files[0]);
};
onMounted(() => {
  setCurPage(1);
  setTotalPages(1);
  uploadInput = document.querySelector(`.select-file.${props.fileId}`) as HTMLInputElement;
  if (documentBlock.value) {
    documentBlock.value.addEventListener('scroll', handleScroll);
  }
  setScrollListener();
});

onUnmounted(() => {
  if (documentBlock.value) {
    documentBlock.value.removeEventListener('scroll', handleScroll);
  }
});
defineExpose({ setScroll });
watch(() => search.value, (newVal) => {
  clearFindCounters(props.docNumber);
});
provide('docNumber', props.docNumber);
</script>

<template>
  <div ref="container" class="container" :class="fileId">
    <div class="settings-block">
      <div class="left-block">
        <div v-if="allowedSeparate[1].includes(getTypeFile(props.file?.name))" class="settings__search">
          <SearchIcon :width="16" :height="16" class="search-icon"/>
          <Input v-model="search" title="Поиск"> </Input>
          <div class="find-counters" v-if="search!==''&&findCounters[props.docNumber]>0">Найденно {{findCounters[props.docNumber]}} совпадений </div>
        </div>
        <div class="scale">
          <span class="scale__title">Масштаб</span>
          <span class="scale__minus scale-change" @click="zoomIn"><MinusIcon/></span>
          <span class="scale__plus scale-change" @click="zoomOut"><PlusIcon/></span>
        </div>
      </div>
      <div class="settings__utilities right-block">
        <div class="file-actions">
          <SimpleButton @click="saveFiles" type="secondary" class="save">
            <Download/>
            <span class="download-text">Скачать</span>
          </SimpleButton>
          <SimpleButton type="secondary" class="select" @click="callInput">
            <span class="select-file">Выбрать новый файл</span>
            <input
              type="file"
              class="select-file"
              :class="fileId"
              accept=".doc,.docx,.rtf,.pdf,.xlsx,.xls"
              @input="inputFile($event);"
              hidden
            />
          </SimpleButton>
        </div>
      </div>
    </div>
    <div class="title-block">
      <div class="title">
        <component :is="documentIcon" :width="24" :height="24"/>
        <div class="title__text">{{ documentName }}</div>
      </div>
      <div v-if="!allowedSeparate[1].includes(getTypeFile(props.file?.name))" class="navigation">
        <div class="navigation__title">Номер страницы</div>
        <div class="navigation__data">
          <span class="navigation__current-page">
            <Input type="number" v-model.number="curPage" :max-value="totalPages"
                   @update:model-value="handlePageInput"
                   class="input-page"
                   :min-value="1"
                   :validate="validatePage"/>
          </span>
          из {{ totalPages }}
        </div>
      </div>
    </div>
    <div ref="documentBlock" class="document-block">
      <WordViewer v-if="allowedSeparate[1].includes(getTypeFile(props.file?.name))" :file="props.file" :search-query="search" :scale="scale"
                  :current-page="currentPage"
                  @set-scroll-listener="setScrollListener" :fileId="fileId"/>
      <ExelView :scale="scale" :page="currentPage-1" v-else :file="props.file" :key="file.name + curPage"/>
    </div>
    <div v-if="!allowedSeparate[1].includes(getTypeFile(props.file?.name)) && totalPages>1" class="arrows-block">
      <div class="arrow-up arrow" :class="{disabled: curPage<=1}" @click="handleUpArrowClick">
        <ChevronDownIcon color-arrow="currentColor" class="chevron" :width="32" :height="32"/>
      </div>
      <div class="arrow-down arrow" :class="{disabled: curPage >= totalPages}"
           @click="handleDownArrowClick">
        <ChevronDownIcon color-arrow="currentColor" :width="32" :height="32"/>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
a.download {
  display: none;
}

.document-wrapper {
  overflow: hidden;
  position: relative;
}

.container {
  display: flex;
  flex-direction: column;
  gap: 16px;
  overflow: hidden;
  max-width: 660px;
  position: relative;
  flex: 1;
  .settings-block {
    flex-wrap: wrap;
    justify-content: space-between;
    display: flex;
    padding: 8px;
    border: 1px solid rgba(244, 247, 249, 1);
    gap: 16px;
    border-radius: 8px;
    & .left-block{
      display: flex;
      align-items: center;
      gap: 4px;
      & .scale {
        display: flex;
        align-items: center;

        & .scale-change {
          width: 32px;
          height: 32px;
          background-color: $bg_grey;
          border-radius: 8px;
          display: flex;
          align-items: center;
          justify-content: center;
          transition: $transition;

          &:hover {
            cursor: pointer;
            background-color: #eff1f3;
          }
        }

        & .scale__title {
          margin-right: 8px;
          color: $text-grey;
          font-family: Inter, serif;
          font-size: 12px;
          font-weight: 500;
          line-height: 16.8px;
          text-align: left;
        }

        & .scale__minus {
          margin-right: 4px;
        }

      }
      & .settings__search {
        width: 200px;
        display: flex;
        align-items: center;
        background-color: $bg_grey;
        border-radius: 8px;
        padding: 0px;
        gap: 8px;
        min-height: 37px;

        & .search-icon {
          margin-left: 8px
        }
        & .find-counters{
          font-size: 10px;
          color: gray;
          font-weight: 500;
        }
      }
    }
    & .settings__utilities {
      display: flex;
      gap: 12px;
      align-items: center;
      & .file-actions{
        display: flex;
        gap: 4px;
        & .download-text, .select-file{
          font-family: Stem;
          font-size: 12px;
          font-weight: 500;
          line-height: 18px;
          text-align: left;
          color: $text_black;
        }
      }
    }
  }
}

.title-block {
  display: flex;
  align-items: center;
  justify-content: space-between;

  & .title {
    display: flex;
    align-items: center;
    gap: 5px;

    & .title__text {
      font-family: Stem, 'sans-serif';
      font-size: 18px;
      font-weight: 500;
      line-height: 26px;
      text-align: left;
      color: $text_black;
    }
  }

  & .navigation {
    display: flex;
    align-items: center;
    gap: 8px;

    & .navigation__title {
      font-family: Inter, 'sans-serif';
      font-size: 12px;
      font-weight: 500;
      line-height: 16.8px;
      text-align: left;
      color: $text_grey
    }

    & .navigation__data {
      display: flex;
      align-items: center;
      gap: 4px;

      &, .input-page {
        color: $text-black;
        font-family: Inter, 'sans-serif';
        font-size: 12px;
        font-weight: 600;
        line-height: 16.8px;
        text-align: left;
      }

      & .input-page {
        background-color: $bg_grey;
        max-width: 40px;
        border-radius: 8px;
        height: 32px;
        display: inline-flex;
        margin-right: 4px;
        padding: 3px;
        align-items: center;
        justify-content: center;
      }
    }
  }
}

.document-block {
  height: 100%;
  background-color: white;
  position: relative;
  transition: transform 0.3s ease;
  overflow: auto;
  padding-left: 20px;
  padding-bottom: 70px;
}

.arrows-block {
  display: flex;
  align-items: center;
  gap: 8px;
  position: absolute;
  bottom: 10px;
  left: 50%;
  transform: translateX(-50%);

  & .arrow {
    display: inline-flex;
    width: 64px;
    height: 64px;
    background-color: $bg_white;
    box-shadow: 0px 0px 15.9px 0px #43434352;
    color: $text_black;
    align-items: center;
    justify-content: center;
    border-radius: 16px;
    cursor: pointer;
    transition: $transition;
    z-index: 2;

    &:not(.disabled):hover {
      background-color: #efeeee;
    }

    &.disabled {
      color: $text_grey;
      cursor: auto;
      pointer-events: none;
    }

    &.arrow-up {
      & .chevron {
        transform: rotate(180deg);
      }
    }
  }
}
</style>
