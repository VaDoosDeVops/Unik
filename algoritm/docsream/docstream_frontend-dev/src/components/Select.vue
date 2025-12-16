<script setup lang="ts">
import {
  ref, onMounted, defineEmits, defineProps,
} from 'vue';
import { options } from 'floating-vue';
import ChevronDownIcon from '@/components/icons/ChevronDownIcon.vue';

const emits = defineEmits(['update:modelValue', 'update:selectedOption']);
const props = defineProps({
  modelValue: { type: Object, default: options[0] },
  selectedOption: {},
  placeholder: { type: String, default: 'Select an option' },
  options: { type: Array as () => { id: string, name: string }[], default: () => [] },
});

const active = ref(false);
const rotation = ref(0);
const selectHeight = ref(`${props.options.length * 32}px`);
const toggleDropdown = () => {
  active.value = !active.value;
  rotation.value += active.value ? 180 : -180;
};

const selectOption = (option: any) => {
  emits('update:modelValue', option);
  active.value = false;
  rotation.value = 0;
};

const handleClickOutside = (event: Event) => {
  if (!event.target.closest('.select')) {
    active.value = false;
    rotation.value = 0;
  }
};

onMounted(() => {
  document.addEventListener('click', handleClickOutside);
  return () => {
    document.removeEventListener('click', handleClickOutside);
  };
});
</script>

<template>
  <div class="select" @click="toggleDropdown">
    <div class="select-display">
      <span class="select__selected">{{ props.modelValue.name }}</span>
      <button class="chevron-icon">
        <ChevronDownIcon
          :style="{ transform: `rotate(${rotation}deg)` }"
          class="select-icon"
          color="#959FB8"
        />
      </button>
    </div>
    <transition name="fade">
      <ul v-if="active" class="options-list">
        <li
          v-for="option in props.options"
          :key="option.id"
          @click.stop="selectOption(option)"
        >
          {{ option.name }}
        </li>
      </ul>
    </transition>
  </div>
</template>

<style scoped lang="scss">
.select {
  position: relative;
  max-width: 130px;
  min-width: 120px;
  padding: 8px;
  border-radius: 8px;
  cursor: pointer;
  user-select: none;
  background-color: $bg_grey;

  & .select__selected {
    font-family: Inter, sans-serif;
    font-size: 12px;
    font-weight: 600;
    line-height: 16.8px;
    text-align: left;
    color: $text_black;
  }
}

.select-display {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.options-list {
  position: absolute;
  width: 100%;
  border: 1px solid #ccc;
  background-color: #fff;
  list-style: none;
  padding: 0;
  margin: 0;
  overflow-y: auto;
  top: 100%;
  left: 0;
  transition: all 0.3s ease;
  z-index: 2;
}

.options-list li {
  padding: 8px;
  cursor: pointer;
  font-family: Inter, sans-serif;
  font-size: 12px;
  font-weight: 600;
  line-height: 16.8px;
  text-align: left;
  color: $text_black;
  height: 32px;
}

.options-list li:hover {
  background-color: #f0f0f0;
}

.chevron-icon {
  display: flex;
  align-items: center;
  background: none;
  border: none;
  cursor: pointer;

  & .select-icon {
    transition: all 0.5s ease;
  }
}

.fade-enter-active, .fade-leave-active {
  transition: height 0.3s ease;
  overflow: hidden;
}

.fade-enter-to, .fade-leave-from {
  height: v-bind(selectHeight);
  overflow: hidden;
}

.fade-enter-from, .fade-leave-to {
  height: 0;
  overflow: hidden;
}
</style>
