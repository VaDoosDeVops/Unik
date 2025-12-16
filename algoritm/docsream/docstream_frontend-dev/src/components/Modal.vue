<script setup>
import { defineProps, defineEmits } from 'vue';
import CrossIcon from '@/components/icons/CrossIcon.vue';

defineProps({
  title: {
    type: String,
    required: true,
  },
  maxWidth: {
    type: String,
    default: '',
  },
});
const emit = defineEmits(['close']);

const handleClose = () => {
  emit('close');
};
</script>

<template>
  <div class="modal-bg" @click="handleClose"></div>
  <div class="modal" :style="maxWidth!==''?'max-width: '+maxWidth:''">
    <div class="modal-head">
      {{ title }}
      <span @click="handleClose" :style="{alignSelf: 'flex-start'}">
        <CrossIcon color="#25304C"/>
      </span>
    </div>
    <div class="modal-body">
      <slot></slot>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.modal {
  max-width: 500px;
  position: fixed;
  z-index: 9;
  padding: 24px;
  background-color: $text_white;
  border-radius: 24px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  min-width: 494px;

  &-head {
    display: flex;
    align-items: center;
    color: $text_black;
    font-size: 24px;
    font-style: normal;
    font-weight: 600;
    line-height: 120%;
    justify-content: space-between;
    margin-bottom: 24px;
    gap: 15px;

    span {
      display: flex;
      width: 32px;
      height: 32px;
      background-color: $bg_4;
      align-items: center;
      justify-content: center;
      border-radius: 8px;
      cursor: pointer;
      flex-shrink: 0;

      &:hover {
        background-color: $bg_5;
      }

      svg {
        width: 24px;
      }
    }
  }

  &-body {
    display: flex;
    flex-direction: column;
    row-gap: 24px;
  }

  &-bg {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba($text_black, .4);
    z-index: 8;
  }
}
</style>
