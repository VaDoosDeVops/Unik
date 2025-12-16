<template>
  <span v-if="highlightedText"  v-html="highlightedText"></span>

</template>

<script setup lang="ts">
import {
  defineProps, computed, watch, inject, watchEffect, ref,
} from 'vue';
// eslint-disable-next-line import/no-extraneous-dependencies
import DOMPurify from 'dompurify';
import { useFileStore } from '@/stores/fileStore';

const { addFindCounters } = useFileStore();
const props = defineProps({
  text: {
    type: String,
    required: true,
  },

  query: {
    type: String,
    required: true,
  },
});
const docNumber:number = inject('docNumber')!;

function replaceAndCount(str:string, find:RegExp, replaceWith:string) {
  const regex = new RegExp(find, 'g'); // глобальное регулярное выражение
  const matches = str.match(regex); // находим все совпадения
  const count = matches ? matches.length : 0; // подсчитываем их количество
  const newStr = str.replace(regex, replaceWith);// выполняем замену
  return { newStr, count }; // возвращаем новую строку и количество замен
}
const escapedQuery = computed(() => props?.query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
const regex = computed(() => new RegExp(`(${escapedQuery.value})`, 'gi'));
const highlightText = (html: string): string => {
  const tempDiv = document.createElement('div');
  tempDiv.innerHTML = html;
  const walk = (node: Node) => {
    if (node.nodeType === Node.TEXT_NODE) {
      const textContent = (node as Text).textContent || '';
      // const highlighted = textContent.replace(regex, '<mark>$1</mark>');
      const { count, newStr: highlighted } = replaceAndCount(textContent, regex.value, '<mark>$1</mark>');
      if (count > 0) { addFindCounters(docNumber, count); }
      if (highlighted !== textContent) {
        const span = document.createElement('span');
        span.innerHTML = highlighted;
        node.replaceWith(span);
      }
    } else if (node.nodeType === Node.ELEMENT_NODE) {
      const element = node as HTMLElement;
      element.childNodes.forEach(walk);
    }
  };
  walk(tempDiv);
  return DOMPurify.sanitize(tempDiv.innerHTML);
};

const highlightedText = ref(props.text);
watch(() => props.query, () => {
  highlightedText.value = highlightText(props.text);
});
</script>

<style lang="scss">
mark{
  background-color: orange;
}
.red-highlight{
  background-color: #FF9C9C99;
;
}

.yellow-highlight{
  background: #75FA9A99;

;
}
.green-highlight{
  background: #9CB8FF99;

}
</style>
