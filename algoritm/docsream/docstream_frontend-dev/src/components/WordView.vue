<template>
  <div id="wrapper"  :class="!htmlContent ? 'loader-wrapper' : ''">
    <div v-if="htmlContent && !isLoading" id="doc-content">
      <HighlightText :text="htmlContent" :query="searchQuery" />
    </div>
    <div v-if="!htmlContent || isLoading" class="loader">
      <SpinnerIcon type="blue" :size="48"/>
    </div>
  </div>
</template>

<script setup lang="ts">
import {
  defineProps, ref, watch, defineEmits, nextTick,
} from 'vue';
import mammoth from 'mammoth';
import { storeToRefs } from 'pinia';
import { styleMap } from '@/utils/files';
import HighlightText from '@/components/HighlightText.vue';
import SpinnerIcon from '@/components/icons/SpinnerIcon.vue';
import { useFileStore } from '@/stores/fileStore';

const props = defineProps({
  file: {
    type: Object as () => File,
  },
  fileId: {
    type: String,
  },
  scale: {
    type: Number,
    default: 1,
  },
  currentPage: {
    type: Number,
    default: 1,
  },
  searchQuery: {
    type: String,
    default: '',
  },
});
const emits = defineEmits(['update:totalPages', 'setScrollListener']);
const { isLoading } = storeToRefs(useFileStore());
function transformParagraph(element) {
  const isEmptyParagraph = !element.children || element.children.every((child) => child.text === '');
  if (isEmptyParagraph) {
    return { ...element, styleName: 'empty-paragraph' };
  }
  if (element.alignment === 'center' && !element.styleId) {
    return { ...element, styleName: 'center-aligned' };
  }
  if (element.alignment === 'right' && !element.styleId) {
    return { ...element, styleName: 'right-aligned' };
  }
  if (element.alignment === 'left' && !element.styleId) {
    return { ...element, styleName: 'left-aligned' };
  }
  return element;
}

function transformElement(element) {
  let elementCopy = { ...element };
  if (elementCopy.children) {
    const children = elementCopy.children.map(transformElement);
    elementCopy = { ...elementCopy, children };
  }

  if (element.type === 'paragraph') {
    elementCopy = transformParagraph(element);
  }

  return elementCopy;
}

const options = {
  includeEmbeddedStyleMap: true,
  transformDocument: transformElement,
  ignoreEmptyParagraphs: false,
  styleMap,
};

const htmlContent = ref('');

const convertFileToHtml = async (file) => {
  if (file) {
    const arrayBuffer = await file.arrayBuffer();
    mammoth.convertToHtml({ arrayBuffer }, options)
      .then(async (result) => {
        htmlContent.value = result.value;
        await nextTick();
        const wrap = document.querySelector('#wrapper');
        const hrList = wrap?.querySelectorAll('hr');
        hrList?.forEach((el, idx) => {
          el.setAttribute('id', `${idx}`);
        });
        emits('update:totalPages', (hrList?.length || 0) + 1);
        emits('setScrollListener');
      })
      .catch((err) => {
        console.error('Ошибка при конвертации файла:', err);
      });
  }
};

watch(() => props.file, async (newFile) => {
  if (props.file !== null) {
    await convertFileToHtml(newFile);
    await nextTick();
    emits('update:totalPages', document.querySelectorAll('#doc-content hr.page-break').length + 1);
  }
}, { immediate: true });

watch(() => props.scale, () => {
  let root = document.documentElement;
  if (props.fileId) {
    root = document.querySelector(`.${props.fileId}`);
  }
  root.style.setProperty('--base-h1', `${32 * props.scale}px`);
  root.style.setProperty('--base-h2', `${28 * props.scale}px`);
  root.style.setProperty('--base-h3', `${20 * props.scale}px`);
  root.style.setProperty('--base-h4', `${18 * props.scale}px`);
  root.style.setProperty('--base-h5', `${17 * props.scale}px`);
  root.style.setProperty('--base-h6', `${16 * props.scale}px`);
  root.style.setProperty('--base-p', `${16 * props.scale}px`);
  root.style.setProperty('--base-subtitle', `${24 * props.scale}px`);
});

</script>

<style lang="scss">
.doc-content {
  position: relative;
  font-family: 'Times New Roman', serif;
  --base-h1: 32px;
  --base-h2: 28px;
  --base-h3: 20px;
  --base-h4: 18px;
  --base-h5: 17px;
  --base-h6: 16px;
  --base-p: 16px;
  --base-subtitle: 24px;
}
#wrapper{
  width: 100%;
}
.loader-wrapper{
  height: 100%;
}
.page {
  page-break-after: always;
  padding: 20px;
  border: 1px solid #ccc;
  margin-bottom: 20px;
  font-size: var(--base-p);
}

p {
  margin: 0.5em 0;
  font-size: var(--base-p);
  line-height: 1.5;
}

.normal {
  font-size: var(--base-p);
  font-weight: normal;
}

h1 {
  font-size: var(--base-h1);
  font-weight: bold;
}

h2 {
  font-size: var(--base-h2);
  font-weight: bold;
}

h3 {
  font-size: var(--base-h3);
  font-weight: bold;
}

h4 {
  font-size: var(--base-h4);
  font-weight: bold;
}

h5 {
  font-size: var(--base-h5);
  font-weight: bold;
}

h6 {
  font-size: var(--base-h6);
  font-weight: bold;
}

.subtitle {
  font-size: var(--base-subtitle);
  font-weight: normal;
  font-style: italic;
}

.text-center {
  text-align: center;
}

.text-right {
  text-align: right;
}

ul, ol {
  margin: 1em 0;
  padding-left: 40px;
}

blockquote {
  margin: 1em 0;
  padding-left: 20px;
  border-left: 5px solid #ccc;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 8px;
}

th {
  background-color: #f2f2f2;
}

pre {
  background-color: #f8f8f8;
  padding: 10px;
  overflow-x: auto;
}

code {
  background-color: #f8f8f8;
  padding: 2px 4px;
}

a {
  color: blue;
  text-decoration: underline;
}

sup {
  vertical-align: super;
  font-size: smaller;
}

sub {
  vertical-align: sub;
  font-size: smaller;
}

li {
  font-size: var(--base-p);
}

s {
  text-decoration: line-through;
}

.text-left {
  text-align: left;
}

.text-center {
  text-align: center;
}

.text-right {
  text-align: right;
}

p.center-aligned {
  font-size: var(--base-p);
  text-align: center;
}
.loader{
  left: 50%;
  position: absolute;
  top: calc(50% - 54px);
  transform: translate(-50%, -50%);
}
</style>
