<script setup>
import {
  onMounted, ref, useSlots, watch, defineProps, defineEmits, defineExpose, nextTick,
} from 'vue';
import { clickOutSide as vClickOutSide } from '@mahdikhashan/vue3-click-outside';
import SpinnerIcon from '@/components/icons/SpinnerIcon.vue';
import CrossIcon from '@/components/icons/CrossIcon.vue';
import HideIcon from '@/components/icons/HideIcon.vue';
import ShowIcon from '@/components/icons/ShowIcon.vue';

const slots = useSlots();
const props = defineProps({
  type: {
    type: String, // text,password,phone,email,number
    default: 'text',
  },
  title: {
    type: String,
    required: false,
  },
  error: {
    type: String,
    default: '',
  },
  status: {
    type: String,
    default: '',
  },
  maxWidth: {
    type: String,
    default: '100%',
  },
  required: {
    type: Boolean,
    default: false,
  },
  minValue: {
    type: Number,
    default: 0,
  },
  maxValue: {
    type: Number,
    default: 0,
  },
  modelValue: [String, Number],
  placeholder: {
    type: String,
    default: '',
  },
  hasBorder: {
    type: Boolean,
    default: true,
  },
  validate: {
    type: Function,
    default: null,
  },
});
const emits = defineEmits(['update:modelValue', 'checkInputValue', 'enter']);

const activeInput = ref(false);
const showPass = ref(false);
const customInput = ref();
const inputRef = ref();

function focusToInput(e) {
  if (!activeInput.value) {
    activeInput.value = true;
  }
  const inputWrapper = e.target;
  if (e.target.classList.contains('input')) {
    setTimeout(() => inputWrapper.querySelector('.input-form').focus(), 0);
  }
}

function focus() {
  if (!activeInput.value) {
    activeInput.value = true;
  }
  nextTick(() => {
    if (customInput.value) {
      customInput.value.querySelector('input').focus();
    }
  });
}

function unfocus() {
  if (props.modelValue === '' || props.modelValue === null) {
    activeInput.value = false;
  }
}

const preventInput = (e) => {
  if (props.type === 'number') {
    if ((e.keyCode > 47 && e.keyCode < 58) || (e.keyCode > 36 && e.keyCode < 41) || e.keyCode === 8 || e.keyCode === 46) {
      // if(Number(e.target.value) < (props.minValue!=null?props.minValue:0)){
      //   e.target.value = props.minValue
      //   e.preventDefault()
      // }
      // if(Number(e.target.value) > (props.maxValue!=null?props.maxValue:99999999999)){
      //   e.target.value = props.maxValue
      //   e.preventDefault()
      // }
    } else {
      e.preventDefault();
    }
  }
};

onMounted(() => {
  if (customInput.value.querySelector('.input-form').value !== '') {
    activeInput.value = true;
  }
});

watch(() => [props.modelValue], (newValues, oldValues) => {
  if (newValues[0] !== '') {
    activeInput.value = true;
  }
});
const checkInputValue = () => {
  emits('checkInputValue', props.modelValue);
};
const clickCross = async () => {
  await emits('update:modelValue', '');
  emits('checkInputValue', props.modelValue);
};
const validateFunc = (newVal) => {
  if (!props.validate(newVal)) {
    if (newVal > props.maxValue) emits('update:modelValue', props.maxValue);
    else emits('update:modelValue', props.minValue);
  }
};
defineExpose({ focus });

</script>

<template>
  <div class="main-wrapper">
    <div ref="customInput" class="input" :style="'max-width:'+maxWidth" @click="focusToInput"
         :class="[{'active':activeInput},{'disabled':status==='disabled'},{'error':status==='error'}, {'withBorder' : hasBorder}]"
         v-click-out-side="unfocus">
      <span class="input-label" v-if="title">{{ title }}</span>
      <template v-if="type==='number'">
        <input
          :required="required"
          :type="type==='password'? (showPass?'text':'password'):type"
          class="input-form"
          :class="[{'with-placeholder': placeholder.length>0}]"
          :min="minValue!=null?minValue:0"
          :max="maxValue!=null?maxValue:99999999999"
          :value="modelValue"
          @input="$emit('update:modelValue', $event.target.value)"
          @focusout="validateFunc($event.target.value)" v-on:keydown="preventInput">
      </template>
      <template v-if="type!=='number'">
        <input
          ref="inputRef"
          :placeholder="placeholder"
          :required="required"
          :type="type==='password'? (showPass?'text':'password'):type"
          class="input-form"
          :class="[{'with-placeholder': placeholder.length>0}]"
          :value="modelValue"
          @input="$emit('update:modelValue', $event.target.value)" @focusin="focus"
          @focusout="checkInputValue" v-on:keydown="preventInput"
          @keydown.enter="$emit('enter')">
      </template>
      <div class="input-icon" v-if="type!=='number'">
        <template v-if="$slots.icon">
          <slot name="icon"></slot>
        </template>
        <template v-if="type==='password' && !showPass">
          <HideIcon color="#9BA3B2" @click.stop="showPass=!showPass"/>
        </template>
        <template v-if="type==='password' && showPass">
          <ShowIcon color="#9BA3B2" @click.stop="showPass=!showPass"/>
        </template>
        <template v-else>
          <template v-if="status==='error' && type !== 'password'">
            <CrossIcon color="#E22446" @click="clickCross" class="cross-icon"/>
          </template>
          <template v-if="status==='loading'">
            <SpinnerIcon/>
          </template>
        </template>
      </div>
    </div>
    <Transition name="fade">
      <span class="input-error" v-if="error!==''">{{ error }}</span>
    </Transition>
  </div>

</template>

<style lang="scss" scoped>
.main-wrapper {
  width: 100%;
}

.input {
  width: 100%;
  min-height: 32px;
  position: relative;
  background-color: $bg_grey;
  border: none;
  border-radius: 16px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  cursor: text;
  transition: $transition;
  font-size: 14px;

  &.disabled {
    pointer-events: none;
  }

  &.error {
    background-color: $red-light;
    border: 2px solid $red;
  }

  &.active {
    .input {
      &-label {
        font-size: 12px;
        font-style: normal;
        font-weight: 600;
        line-height: 120%;
        margin-bottom: 3px;
        pointer-events: none;
      }

      &-form {
        height: 16px;
        display: block;
        width: 100%;
      }
    }
  }

  &-label {
    position: relative;
    font-family: Manrope;
    font-size: 14px;
    font-weight: 600;
    line-height: 14.4px;
    text-align: left;
    color: $text_grey;
    font-feature-settings: 'clig' off, 'liga' off;
    font-style: normal;
    pointer-events: none;
    transition: all 0.3s ease;

  }

  &-form {
    color: $text_black;
    background-color: transparent;
    border: 0;
    outline: 0;
    height: 0;
    width: calc(100% - 40px);
    font-family: 'Manrope', sans-serif;
    display: none;

    &.with-placeholder {
      display: block;
      height: auto;
    }
  }

  &-icon {
    display: block;
    position: absolute;
    top: calc(50% - 12px);
    right: 12px;
    width: 24px;
    height: 24px;
  }

  &-error {
    color: $red;
    font-feature-settings: 'clig' off, 'liga' off;
    font-size: 12px;
    font-style: normal;
    font-weight: 500;
    line-height: 120%;
    left: 0;
    top: calc(100% + 4px);
    pointer-events: none;
  }
}

.cross-icon {
  cursor: pointer;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input[type="number"] {
  -moz-appearance: textfield;
  text-align: center;
}
</style>
