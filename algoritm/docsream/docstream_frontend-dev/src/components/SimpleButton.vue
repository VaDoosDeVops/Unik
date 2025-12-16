<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { defineProps } from 'vue';
import SpinnerIcon from '@/components/icons/SpinnerIcon.vue';

defineProps({
  disabled: {
    type: Boolean,
    default: false,
  },
  action: {
    type: String,
    default: '',
  },
  type: {
    type: String,
    default: 'primary',
  },
  centered: {
    type: Boolean,
    default: false,
  },
  routerLink: {
    type: String,
    default: '',
  },
});
</script>

<template>
  <template v-if="routerLink===''">
    <button
      :class="'button' + (disabled?' disabled':'') + (centered?' centered':'') + (action==='loading'?' loading':'') + ' ' + type">
      <template v-if="action===''">
        <slot></slot>
      </template>
      <template v-if="action==='loading'">
        <SpinnerIcon :white="type==='primary'" :size="3"/>
      </template>
    </button>
  </template>
  <template v-else>
    <router-link :to="routerLink"
                 :class="'button' + (disabled?' disabled':'') + (centered?' centered':'') + (action==='loading'?' loading':'') + ' ' + type">
      <template v-if="action===''">
        <slot></slot>
      </template>
      <template v-if="action==='loading'">
        <SpinnerIcon :white="type==='primary'"/>
      </template>
    </router-link>
  </template>
</template>

<style scoped lang="scss">
.button {
  border: 0;
  border-radius: 10px;
  display: flex;
  column-gap: 10px;
  align-items: center;
  padding-inline: 0;
  cursor: pointer;
  font-family: 'Stem', sans-serif;
  font-size: 16px;
  font-style: normal;
  font-weight: 600;
  line-height: 20px;
  text-decoration: none;
  transition: $transition;
  padding: 6px 23px;

  &.primary.router-link-active,
  &.secondary.router-link-active,
  &.thirdly.router-link-active {
    background-color: $bg_white;
    color: $text_dark_black;

    &:deep(svg) {
      filter: brightness(0) invert(1);
    }

    &:hover {
      background-color: $bg_white;
    }
  }

  &.primary {
    border: 1px solid $bg_light_grey;
    border-radius: 20px;
    background-color: $bg_white;
    color: $text_black;

    &:hover {
      background-color: #e8e7e7;
    }
  }

  &.disabled {
    pointer-events: none;
    opacity: .48;
  }
  &.green{
    background-color: $bg_bright_green;
    color: $text_white;
    padding: 12px 14px;
    &:hover{
      cursor: pointer;
      background-color: $bg_green;
    }
  }
  &.secondary{
    padding: 7px 12px;
    border-radius: 8px;
    background-color: $bg_grey;
    &:hover {
      cursor: pointer;
      background-color: #eff1f3;
    }
  }
  &.centered {
    justify-content: center;
  }

  &.loading {
    pointer-events: none;
  }
}
</style>
