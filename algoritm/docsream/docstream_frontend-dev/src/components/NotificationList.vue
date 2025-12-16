<script setup>
import { ref, watch } from 'vue';
import CheckIcon from '@/components/icons/CheckIcon.vue';
import CrossIcon from '@/components/icons/CrossIcon.vue';
import SpinnerIcon from '@/components/icons/SpinnerIcon.vue';
import { useNotesStore } from '@/stores/notificationStore';

const notes = useNotesStore();

const notifications = ref([]);

watch(notes, () => {
  notes.list.forEach((n) => {
    if (notifications.value.filter((note) => note.id === n.id).length <= 0) {
      notifications.value.push(n);
      setTimeout(() => {
        const note = document.querySelector(`.notes-item[data-id='${n.id}']`);
        note.classList.add('active');
        if (n.countdown != null) {
          setTimeout(() => {
            note.classList.remove('active');
            setTimeout(() => {
              notifications.value = notifications.value.filter((note) => note.id !== n.id);
              notes.remove(n.id);
            }, 1000);
          }, n.countdown);
        }
      }, 100);
    }
  });
});

function closeNote(id) {
  const note = document.querySelector(`.notes-item[data-id='${id}']`);
  note.classList.remove('active');
  setTimeout(() => {
    notifications.value = notifications.value.filter((note) => note.id !== id);
    notes.remove(id);
  }, 1000);
}
</script>

<template>
  <div class="notes">
    <div class="notes-item" v-for="(n) in notifications" :data-id="n.id" :key="n.id">
      <div class="notes-item__left" v-if="n.icon != null">
        <template v-if="n.icon==='loading'">
          <SpinnerIcon :size="2"/>
        </template>
        <template v-if="n.icon==='success'">
          <CheckIcon color="#0DC268" :width="17" :height="11"/>
        </template>
        <template v-if="n.icon==='fail'">
          <CrossIcon color="#E22446"/>
        </template>
      </div>
      <div class="notes-item__right">
        <div class="notes-item__primary">{{ n.text }}</div>
        <div class="notes-item__secondary" v-if="n.additional!=null">{{ n.additional }}</div>
      </div>
      <span class="notes-item__close" @click="closeNote(n.id)">
        <CrossIcon color="#161A2E" :width="15" :height="15"/>
      </span>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.notes {
  position: fixed;
  bottom: 24px;
  right: 24px;
  z-index: 999999;

  &-item {
    padding: 12px 40px 12px 16px;
    box-shadow: $shadow;
    border-radius: 12px;
    max-width: 360px;
    background-color: $text_white;
    position: relative;
    right: calc(-100% - 24px);
    margin-top: 16px;
    transition: all 1s ease;
    display: flex;
    align-items: center;
    height: 68px;

    &.active {
      right: 0;
    }

    &__close {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      right: 12px;
      width: 12px;
      height: 12px;
      cursor: pointer;

      svg {
        width: 100%;
        height: 100%;
        display: block;
      }
    }

    &__left {
      margin-right: 12px;
      width: 20px;
      height: 20px;
    }

    &__secondary {
      font-family: Suisse Intl, 'sans-serif';
      font-size: 14px;
      font-weight: 400;
      line-height: 19.6px;
      text-align: left;
      color: #5A6882;
    }

    &__primary {
      color: $text_black;
      font-size: 16px;
      font-style: normal;
      font-weight: 700;
      line-height: 20px;
    }
  }
}
</style>
