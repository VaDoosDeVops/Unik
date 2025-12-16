<script setup lang="ts">
import {
  onMounted, defineProps, defineEmits, computed, PropType, ref,
} from 'vue';
import UploadIcon from '@/components/icons/UploadIcon.vue';
import SimpleButton from '@/components/SimpleButton.vue';
import UnknownFileIcon from '@/components/icons/UnknownFileIcon.vue';
import CrossIcon from '@/components/icons/CrossIcon.vue';
import { useNotesStore } from '@/stores/notificationStore';
import { allowedTypes } from '@/types/types';
import { documentIcons, getTypeFile } from '@/utils/files';
import BigCross from '@/components/icons/BigCross.vue';

const props = defineProps({
  primaryText: String,
  secondaryText: String,
  state: {
    type: String,
    default: 'normal', // normal, info, error, success, disabled
  },
  progress: {
    type: Number,
    default: 0,
  },
  width: {
    type: String,
    default: '',
  },
  modelValue: {
    type: Object as PropType<File | null>,
  },
  maxSize: {
    type: Number,
    default: 10_240_000,
  },
  uniqueClass: {
    type: String,
    default: 'my-dragndrop',
  },
  disabled: {
    type: Boolean,
    default: false,
  },
});
const emit = defineEmits(['update:modelValue', 'removeDocument']);

let dragCounter = 0;
let dropFileZone: HTMLElement | null = null;
let uploadInput: HTMLInputElement | null = null;
const notesStore = useNotesStore();

const documentIcon = computed(() => {
  if (props && props.modelValue && props.modelValue.type) {
    const elem = documentIcons.find((el) => el.type.includes(getTypeFile(props.modelValue?.name.toLowerCase())));
    if (elem) {
      return elem.icon;
    }
  }
  return UnknownFileIcon;
});

const documentName = computed(() => props.modelValue?.name.split('.')[0]);

const documentSize = computed(() => {
  if (props && props.modelValue) {
    const units = ['B', 'KB', 'MB', 'GB'];
    let unitIdx = 0;
    let formattedSize = props.modelValue?.size;
    while (formattedSize >= 1024 && unitIdx < units.length - 1) {
      formattedSize /= 1024;
      unitIdx += 1;
    }
    return `${formattedSize.toFixed(2)} ${units[unitIdx]}`;
  }
  return '';
});

const checkValue = (file: File) => {
  if (file) {
    if (!allowedTypes.includes(file.type)) {
      notesStore.append('fail', 'Произошла ошибка', 'Недопустимый формат файла', 3000);
      return false;
    }
    if (file.size > props.maxSize) {
      notesStore.append('fail', 'Произошла ошибка', 'Слишком большой размер файла', 3000);
      return false;
    }
    return true;
  }
  return false;
};

onMounted(() => {
  dropFileZone = document.querySelector(`.uploader-zone.${props.uniqueClass}`) as HTMLElement;
  uploadInput = document.querySelector(`.uploader-handler.${props.uniqueClass}`) as HTMLInputElement;
  dropFileZone.addEventListener('dragenter', (event) => {
    if (event.target === dropFileZone || dropFileZone.contains(event.target as Node)) {
      dragCounter += 1;
      dropFileZone.classList.add('active');
    }
  });

  dropFileZone.addEventListener('dragleave', (event) => {
    if (event.target === dropFileZone || dropFileZone.contains(event.target as Node)) {
      dragCounter -= 1;
      if (dragCounter === 0) {
        dropFileZone.classList.remove('active');
      }
    }
  });

  dropFileZone.addEventListener('drop', (event) => {
    dragCounter = 0;
    dropFileZone?.classList.remove('active');
    const files = event.dataTransfer?.files;
    if (!files || files.length === 0) {
      return;
    }
    if (checkValue(files[0]) && !props.disabled) {
      emit('update:modelValue', files[0]);
    }
  });
});

const callInput = () => {
  uploadInput?.click();
};
['dragover', 'drop'].forEach((event) => {
  document.addEventListener(event, (evt) => {
    evt.preventDefault();
    return false;
  });
});
function resetInput() {
  if (uploadInput) {
    uploadInput.value = '';
  }
}

function encodeImageFileAsURL(element) {
  if (checkValue(element.target.files[0])) {
    emit('update:modelValue', element.target.files[0]);
  }
  resetInput();
}
const removeDocument = () => {
  if (!props.disabled) emit('update:modelValue', null);
};
const showCross = ref(true);
</script>

<template>
  <div class="uploader">
    <div class="uploader-zone"
         :class="[uniqueClass, { disabled: state === 'disabled', activeDragnDrop: modelValue!==null }]">
      <div class="uploader-zone__progress" :style="{ width: progress + '%' }"></div>
      <div class="empty-block" v-if="!modelValue">
        <UploadIcon color="#161A2E" class="uploader-zone__icon"/>
        <div class="uploader-zone__title">
          <div class="uploader-zone__title-primary">
            <span>{{ primaryText }}</span>
          </div>
          <div class="uploader-zone__title-secondary" :class="state" v-if="secondaryText !== ''"
               v-html="secondaryText"></div>
        </div>
      </div>
      <div   class="fill-block" v-else>
        <div @mouseenter="showCross=true" @mouseleave="showCross=false"  class="component">
        <component :is="documentIcon"/>
          <Transition>
          <div v-if="showCross" @click="removeDocument" class="big-cross">
            <big-cross :height="0.7" :width="0.7" color="#959FB8"/>
          </div>
          </Transition>
        </div>

        <div class="file-description">
          <div class="file-name">
            {{ documentName }}
          </div>
          <div class="file-size">
            {{ documentSize }}
          </div>
        </div>
        <div  class="cross-container" @click="removeDocument" :class="{disabled: disabled}">

        </div>

      </div>
      <SimpleButton @click="callInput" v-if="!modelValue">Выбрать</SimpleButton>
    </div>
    <input
      type="file"
      id="uploader-handler"
      class="uploader-handler"
      :class="uniqueClass"
      accept=".doc,.docx,.rtf,.pdf,.xlsx,.xls"
      @input="encodeImageFileAsURL($event);"
      hidden
    />
  </div>
</template>

<style lang="scss" scoped>
.uploader {
  height: 100%;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;

  &-zone {
    height: 100%;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px dashed white;
    border-radius: 24px;
    padding: 24px 16px;
    background-color: white;
    position: relative;
    overflow: hidden;
    flex-direction: column;
    row-gap: 15px;
    transition: $transition;

    &.active {
      background-color: $bg_light_blue;
    }

    &.activeDragnDrop {
      background-color: $bg_light_blue;
    }

    & .empty-block, & .fill-block {

      display: flex;
      flex-direction: column;
      row-gap: 15px;
      align-items: center;
      justify-content: center;
      position: relative;
      min-width: 150px;
      .component{
        position: relative;
          :hover{
            cursor:pointer
          }
        .big-cross{
          display: flex;
          justify-content: center;
          align-items: center;
          width: 2rem;
          height: 2rem;
          border-radius: 100%;
          box-shadow: 0px 2px 9px 0px #0000001C;
          background-color: rgba(255, 255, 255, 1);
          top: -10%;
          left: 75%;
          position: absolute;
          transition: $transition;
        }
      }

    }

    & .cross-container {
      padding: 5px;
      top: -5px;
      right: 0;
      position: absolute;
      color: $text_grey;
      transition: $transition;

      &:not(.disabled):hover {
        cursor: pointer;
        color: $text_black;
      }
    }

    .file-description {
      display: flex;
      flex-direction: column;
      row-gap: 4px;
      align-items: center;
      justify-content: center;
      font-family: Stem, sans-serif;
      font-size: 18.2px;
      font-weight: 500;
      line-height: 26px;
      text-align: left;
      color: $text_dark_black
    }

    & .file-size {
      font-family: Suisse Intl, sans-serif;
      font-size: 13px;
      font-weight: 450;
      line-height: 20.8px;
      text-align: center;
      color: $text_grey;
    }

    &.disabled {
      pointer-events: none;
      opacity: .48;
      user-select: none;
    }

    &__progress {
      height: 100%;
      background-color: white;
      position: absolute;
      top: 0;
      left: 0;
      transition: white;
    }

    &__button {
      border: 1px solid #E8E8E8;
      color: $text_dark_black;
      padding: 6px 23px;
      width: fit-content;
      font-family: Stem, sans-serif;
      font-size: 12px;
      font-weight: 500;
      line-height: 18px;
      text-align: left;
      border-radius: 20px;
    }

    &__title {
      row-gap: 10px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;

      &-primary {
        font-family: Stem, sans-serif;
        font-size: 18px;
        font-weight: 500;
        line-height: 26px;
        text-align: left;
        color: $text_dark_black
      }

      &-secondary {
        font-family: 'Suisse Intl', sans-serif;
        font-size: 13px;
        font-weight: 450;
        line-height: 20.8px;
        text-align: center;
        color: $text_light-grey;

        &.info {
          color: white;
        }

        &.error {
          color: white;
        }

        &.success {
          color: white;
        }
      }
    }
  }
}
.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
