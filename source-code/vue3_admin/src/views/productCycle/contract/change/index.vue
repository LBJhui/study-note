<template>
  <!-- 产品合同变更 -->
  <div>
    <FormLayout :pageInfo="state.pageInfo" @sizeChange="handleSizeChange" @currentChange="handleCurrentChange">
      <template #form>form</template>
      <template #table>
        <el-table height="100%"></el-table>
      </template>
    </FormLayout>
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue'
import FormLayout from '@/components/FormLayout/index.vue'

type PageInfo = {
  total: number
  currentPage: number
  pageSize: number
}

const state = reactive({
  pageInfo: {
    total: 400,
    currentPage: 1,
    pageSize: 10,
  } as PageInfo,
})

const handleSizeChange = (val: number) => {
  state.pageInfo.pageSize = val
}

const handleCurrentChange = (val: number) => {
  state.pageInfo.currentPage = val
}
</script>

<style scoped lang=""></style>
