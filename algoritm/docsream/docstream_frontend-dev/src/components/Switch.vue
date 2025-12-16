<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  rtl: Boolean,
  primaryText: String,
  secondaryText: String,
  disabled: Boolean,
  modelValue: Boolean,
});
const emit = defineEmits(['update:modelValue', 'change']);

const toggleSwitch = () => {
  if (!props.disabled) {
    emit('update:modelValue', !props.modelValue);
  }
};
</script>

<template>
  <div class="switch" :class="{'checked': modelValue, 'disabled': disabled, 'rtl': rtl}"
       @click="toggleSwitch">
    <div class="switch-area">
      <span :class="{'moved': modelValue}"></span>
    </div>
    <div class="switch-title" v-if="primaryText || secondaryText">
      <div class="switch-title__primary" v-if="primaryText">{{ primaryText }}</div>
      <div class="switch-title__secondary" v-if="secondaryText">{{ secondaryText }}</div>
    </div>
    <div style="margin-left: auto;" v-if="$slots.additional">
      <slot name="additional"></slot>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.switch {
  display: flex;
  align-items: start;
  cursor: pointer;

  &:hover {
    .switch {
      &-area {
        background-color: #dfdede;
      }
    }
  }

  &-area {
    width: 32px;
    height: 20px;
    background-color: $bg_4;
    position: relative;
    border-radius: 24px;
    margin-right: 10px;
    transition: $transition;

    span {
      position: absolute;
      top: 2px;
      left: 2px;
      width: 16px;
      height: 16px;
      background-color: $text_white;
      border-radius: 24px;
      transition: $transition;
    }
  }

  &-title {
    &__primary {
      color: $text-black;
      font-size: 16px;
      font-style: normal;
      font-weight: 500;
      line-height: 20px;
    }

    &__secondary {
      color: $bg_2;
      font-size: 13px;
      font-style: normal;
      font-weight: 500;
      line-height: 16px;
    }
  }

  &.rtl {
    flex-direction: row-reverse;
    justify-content: space-between;
  }

  &.checked {
    .switch {
      &-area {
        background-color: $brand-green;

        span {
          left: 14px;
        }
      }
    }

    &:hover {
      .switch-area {
        background-color: $brand_dark-green;
      }
    }
  }
}
</style>
