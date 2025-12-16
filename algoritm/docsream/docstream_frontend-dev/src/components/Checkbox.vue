<script setup lang="ts">
import { defineEmits, defineProps } from 'vue';
import CheckIcon from '@/components/icons/CheckIcon.vue';

const props = defineProps({
  modelValue: { type: Boolean, default: false },
  disabled: { type: Boolean, default: false },
  title: { type: String, default: '' },
  theme: { type: String, default: '' },
});
const emits = defineEmits(['update:modelValue']);
const toggleCheckbox = () => {
  if (!props.disabled) {
    const newValue = !props.modelValue;
    emits('update:modelValue', newValue);
  }
};
</script>

<template>
  <div class="checkbox-container">
    <div class="checkbox"
         :class="[{ active: props.modelValue, disabled: props.disabled },props.theme]"
         @click="toggleCheckbox">
      <input type="checkbox" :disabled="props.disabled" class="hidden-input">
      <CheckIcon class="checkbox-icon"
                 :class="{ active: props.modelValue, disabled: props.disabled }"/>
    </div>
    <span v-if="props.title != ''">{{ props.title }}</span>
  </div>
</template>

<style scoped lang="scss">
.checkbox {
  position: relative;
  height: 24px;
  width: 24px;
  border: 1px solid #B9BFC8;
  background-color: $text_white;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color ease .1s;
  flex-shrink: 0;

  &-container {
    display: flex;
    align-items: center;
    column-gap: 12px;

    span {
      color: $text_black;
      font-weight: 500;
    }
  }

  &.active {
    background-color: $brand_green;
    border: 1px solid transparent;

    &.disabled {
      cursor: default;
    }
  }

  &.disabled {
    opacity: .5;
    cursor: default;
  }

  & .hidden-input {
    display: none;
  }

  &-icon {
    position: absolute;
    transform: translate(-50%, -50%);
    top: 50%;
    left: 53%;
    opacity: 0;
    transition: opacity ease .1s;

    &.active {
      opacity: 1;
    }
  }
}
</style>
