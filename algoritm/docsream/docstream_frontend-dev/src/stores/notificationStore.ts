import { defineStore } from 'pinia';

interface Notification {
  id: number;
  type: string;
  icon: string | null;
  text: string;
  additional: null | string;
  countdown: number;
}

export const useNotesStore = defineStore({
  id: 'notes',
  state: () => ({
    nIndex: 0,
    list: [] as Notification[],
  }),
  actions: {
    append(icon: string, text: string, additional: string | null, countdown: number, type = 'default'): number {
      const newNote = {
        id: this.nIndex += 1,
        type,
        icon,
        text,
        additional,
        countdown,
      };
      this.list.push(newNote);
      return newNote.id;
    },

    update(id: number, icon: string | null, text: string, additional: string, countdown: number): void {
      const note = this.list.find((n) => n.id === id);
      if (note) {
        if (icon !== null) note.icon = icon;
        if (text !== null) note.text = text;
        if (additional !== null) note.additional = additional;
        if (countdown !== null) note.countdown = countdown;
      }
    },

    remove(id: number): void {
      this.list = this.list.filter((n) => n.id !== id);
    },
  },
});
