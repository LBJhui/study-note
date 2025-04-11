<template>
  <div class="container" ref="containerRef" v-resize="resize">
    <div class="form-container" ref="formContainerRef"><slot name="form"></slot> </div>
    <div class="table-container" ref="tableContainerRef"><slot name="table"></slot></div>
    <div class="footer-container" ref="footerContainerRef">
      <div class="total-container">
        共 <span class="num">{{ pageInfo.total }}</span> 条数据，已选中 <span class="num">{{ pageInfo.selectedNum }}</span> 条数据
      </div>
      <div class="pagination-container">
        <el-pagination
          v-model:current-page="pageInfo.currentPage"
          v-model:page-size="pageInfo.pageSize"
          background
          :page-sizes="[10, 20, 50]"
          layout="prev, pager, next,sizes, jumper"
          :total="pageInfo.total"
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import vResize from '@/directs/sizeDirect'

const containerRef = ref()
const formContainerRef = ref()
const tableContainerRef = ref()
const footerContainerRef = ref()

defineProps(['pageInfo'])
const emit = defineEmits(['sizeChange', 'currentChange'])
const init = () => {
  computedHeight()
}

onMounted(() => {
  init()
})

// 计算表格区域的高度
const computedHeight = () => {
  const containerHeight = containerRef.value.clientHeight
  const formHeight = formContainerRef.value.clientHeight
  const footerHeight = footerContainerRef.value.clientHeight
  const tableContainerHeight = containerHeight - formHeight - footerHeight
  tableContainerRef.value.style.height = (tableContainerHeight < 200 ? 200 : tableContainerHeight) + 'px'
}

const resize = () => {
  computedHeight()
}

const handleSizeChange = (val: number) => {
  emit('sizeChange', val)
}

const handleCurrentChange = (val: number) => {
  emit('currentChange', val)
}
</script>

<style scoped lang="scss">
.container {
  height: calc(100vh - $verticalTopNavHeight - $verticalhistoryheight - $titleHeigth);
  position: relative;
  .form-container {
    padding: 0 $paddingLeft;
    border-bottom: 12px solid #f8f9fb;
  }

  .footer-container {
    padding: 0 $paddingLeft;
    height: $formLayoutFooterHeight;
    display: flex;
    justify-content: space-between;
    align-items: center;

    .total-container {
      font-size: 14px;
      color: rgb(49, 56, 54);
      .num {
        color: rgb(88, 112, 203);
      }
    }
    .pagination-container {
      height: 100%;
      .el-pagination {
        height: 100%;
        .el-pager li.is-active {
          background-color: #5870cb !important;
        }
      }
    }
  }
}
</style>
