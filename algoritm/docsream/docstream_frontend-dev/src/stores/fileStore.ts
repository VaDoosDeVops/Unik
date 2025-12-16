import { defineStore } from 'pinia';
import router from '@/router';
import { useNotesStore } from '@/stores/notificationStore';
import { fetchApi } from '@/utils/fetchWrapper';

export const enum FileNumber {
  FIRST,
  SECOND
}

export const useFileStore = defineStore({
  id: 'fileStore',
  state: () => ({
    files: [null, null] as (File | null)[],
    isLoading: false,
    firstFile: null as File | null,
    secondFile: null as File | null,
    firstCompareFile: null as File | null,
    secondCompareFile: null as File | null,
    securedSourceFirstFilename: '',
    securedSourceSecondFilename: '',
    fileContentHtml: '',
    securedFilename: '',
    securedFirstFilename: '',
    securedSecondFilename: '',
    curPage: 1,
    totalPages: 1,
    scale: 1,
    findCounters: [0, 0],

  }),
  actions: {

    setTotalPages(newTotalPages:number) {
      this.totalPages = newTotalPages;
    },
    setCurPage(pageNumber:number) {
      if (pageNumber > 0 && pageNumber <= this.totalPages) {
        this.curPage = pageNumber;
      }
    },
    addFindCounters(docNumber:number, val:number) {
      this.findCounters[docNumber] += val;
    },
    clearFindCounters(docNumber:number) {
      this.findCounters[docNumber] = 0;
    },
    incrementPage() {
      if (this.curPage < this.totalPages) {
        this.curPage += 1;
        return;
      }
      this.curPage = this.totalPages;
    },
    decrementPage() {
      if (this.curPage > 1) {
        this.curPage -= 1;
        return;
      }
      this.curPage = 1;
    },
    incrementScale() {
      if (this.scale < 5) {
        this.scale = parseFloat((this.scale - 0.2).toFixed(1));
      }
    },
    decrementScale() {
      if (this.scale > 0.5) {
        this.scale = parseFloat((this.scale + 0.2).toFixed(1));
      }
    },
    async saveFile(fileNumber: FileNumber) {
      const notesStore = useNotesStore();
      try {
        let securedFilename = '';
        let filename = '';
        if (fileNumber === FileNumber.FIRST) {
          securedFilename = localStorage.getItem('securedFirstFilename') || '';
          filename = localStorage.getItem('securedFirstFilename') || '';
        } else if (fileNumber === FileNumber.SECOND) {
          securedFilename = localStorage.getItem('securedSecondFilename') || '';
          filename = localStorage.getItem('securedSecondFilename') || '';
        }
        const url = `${import.meta.env.VITE_APP_API_URL}/download?filename=${securedFilename}`;
        const result: {response: any, status: any, headers: any} = await fetchApi(url, { method: 'GET' });
        const { response, headers } = result;
        const contentType = headers.get('Content-Type') || 'application/octet-stream';
        const reader = response.body.getReader();
        const stream = new ReadableStream({
          start(controller) {
            function push() {
              reader.read().then(({ done, value }) => {
                if (done) {
                  controller.close();
                  return;
                }
                controller.enqueue(value);
                push();
              });
            }
            push();
          },
        });
        const responseData = await new Response(stream).blob();
        const file = new File([responseData], filename, { type: contentType });
        if (fileNumber === FileNumber.FIRST) {
          this.firstCompareFile = file;
        } else if (fileNumber === FileNumber.SECOND) {
          this.secondCompareFile = file;
        }
      } catch (error) {
        router.push('/');
        notesStore.append('fail', 'Произошла ошибка при скачивании файлов', null, 3000);
      }
    },
    async upload(fileNumber: FileNumber, file: File | null) {
      if (!file) {
        router.push('/');
        return;
      }
      const formData = new FormData();
      if (fileNumber === FileNumber.FIRST) {
        const firstBlob = new Blob([file], { type: file.type });
        formData.append('file', firstBlob, file.name);
      } else if (fileNumber === FileNumber.SECOND) {
        const firstBlob = new Blob([file], { type: file.type });
        formData.append('file', firstBlob, file.name);
      }
      try {
        const result = await fetchApi(
          `${import.meta.env.VITE_APP_API_URL}/upload`,
          { method: 'POST', body: formData },
        );
        const res = await result.response.json();
        if (fileNumber === FileNumber.FIRST) {
          localStorage.setItem('securedSourceFirstFilename', res.filename);
        } else if (fileNumber === FileNumber.SECOND) {
          localStorage.setItem('securedSourceSecondFilename', res.filename);
        }
      } catch (error) {
        router.push('/');
      }
    },
    async compareFiles() {
      const notesStore = useNotesStore();
      this.firstCompareFile = null;
      this.secondCompareFile = null;
      const url = `${import.meta.env.VITE_APP_API_URL}/compare?file1=${localStorage.getItem('securedSourceFirstFilename')}&file2=${localStorage.getItem('securedSourceSecondFilename')}`;
      try {
        const responseCompare = await fetchApi(
          `${url}`,
          { method: 'GET' },
        );
        if (responseCompare.status === 400 && responseCompare.message) {
          notesStore.append('fail', `${responseCompare.message}`, null, 3000);
          return;
        }
        const response: {
          filename1: string,
          filename2: string,
          result1: any,
          result2: any
        } = await responseCompare.response.json();
        localStorage.setItem('securedFirstFilename', response.filename1);
        localStorage.setItem('securedSecondFilename', response.filename2);
        localStorage.setItem('securedFirstResult', response.result1);
        localStorage.setItem('securedFirstResult', response.result1);
        localStorage.setItem('securedSecondResult', response.result2);
      } catch (error) {
        router.push('/');
        notesStore.append('fail', 'Произошла ошибка при сравнении файлов', null, 3000);
      }
    },
  },
});
