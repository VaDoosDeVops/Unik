<script setup lang="ts">
import {
  computed, defineProps, ref, watch,
} from 'vue';
import { read, utils } from 'xlsx';
import { storeToRefs } from 'pinia';
import { useFileStore } from '@/stores/fileStore';

type Props = {
  file:File,
  scale:number
}
const props = defineProps<Props>();
const { curPage, totalPages } = storeToRefs(useFileStore());
const { setTotalPages, setCurPage } = useFileStore();
const tableData = ref();

const lastCell = computed(() => {
  if (tableData.value && tableData?.value['!ref']) {
    return tableData.value['!ref'].split(':')[1];
  }
  return null;
});
const wb = ref();
const decodedLastCell = computed(() => ({ ...utils.decode_cell(lastCell?.value || 'A1') }));
watch(() => [props.file, curPage.value], async () => {
  if (props.file) {
    wb.value = read(await props.file.arrayBuffer(), { cellStyles: true });
    if (totalPages.value < wb.value.SheetNames.length) {
      setTotalPages(wb.value.SheetNames.length);
    }
    tableData.value = wb.value.Sheets[wb.value.SheetNames[curPage.value - 1]];
  }
}, { deep: true, immediate: true });
const findCellBackgroundColorByCellAddress = function (columnIndex:number, rowIndex:number) {
  return tableData.value?.[utils.encode_cell({ c: columnIndex - 1, r: rowIndex - 1 })]?.s?.fgColor?.rgb;
};
const findCellValueVyCellAddress = function (columnIndex:number, rowIndex:number) {
  return tableData.value?.[utils.encode_cell({ c: columnIndex - 1, r: rowIndex - 1 })]?.v;
};

</script>

<template :key="curPage">
  <div v-if="!tableData" >Такого листа нет</div>
  <div v-else style="overflow: auto;width: fit-content" :key="curPage">
  <table :key="props.file.name +curPage">
    <tbody :key="curPage">
    <tr v-for="row in decodedLastCell.r+1" :key="'row-'+row+curPage">
      <td v-for="col in decodedLastCell.c+1"
          :key="'cell-'+col+curPage"
          :style="{
            border:'1px solid lightgray',
          padding:`${3*scale}px`,
          height:`${30*scale}px`,
          minWidth:`${100*scale}px`,
          maxWidth:`${150*scale}px`,
           textOverflow:'ellipsis',
           whiteSpace:'nowrap',
           overflow:'hidden',
           fontSize:`${scale}rem`,
          backgroundColor: '#'+ findCellBackgroundColorByCellAddress(col,row) || 'ffffff'}">
        {{findCellValueVyCellAddress(col,row)}}
      </td>
    </tr>
    </tbody>
  </table>
  </div>
</template>

<style scoped lang="scss">

</style>
