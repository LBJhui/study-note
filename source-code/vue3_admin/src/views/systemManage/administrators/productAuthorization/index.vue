<template>
  <FormLayout :pageInfo="state.pageInfo" @sizeChange="handleSizeChange" @currentChange="handleCurrentChange">
    <template #form>
      <el-form :model="state.filterFormData" :inline="true" ref="filterFormRef">
        <el-form-item label="所属机构" prop="party">
          <el-select v-model="state.filterFormData.party" :style="`width: ${selectWidthLarge}px`" placeholder="请选择所属机构">
            <el-option label="机构1" value="1"></el-option>
            <el-option label="机构2" value="2"></el-option>
            <el-option label="机构3" value="3"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="用户姓名" prop="userName">
          <el-input v-model="state.filterFormData.userName" placeholder="请输入用户姓名"></el-input>
        </el-form-item>
        <el-form-item label="用户账号" prop="userAccount">
          <el-input v-model="state.filterFormData.userAccount" placeholder="请输入用户账号"></el-input>
        </el-form-item>
        <el-form-item>
          <FilterButton @resetForm="resetForm" @getTableList="getTableList" :buttonList="['查询', '重置']" />
        </el-form-item>
      </el-form>
    </template>
    <template #table>
      <el-table :data="state.tableData" v-loading="state.tableLoading">
        <el-table-column label="用户账户" prop="userAccount" min-width="120">
          <template #default="scope">
            {{ scope.row.userAccount || '--' }}
          </template>
        </el-table-column>
        <el-table-column label="用户姓名" prop="userName" min-width="120">
          <template #default="scope">
            {{ scope.row.userName || '--' }}
          </template>
        </el-table-column>
        <el-table-column label="所属机构" prop="party" min-width="240" show-overflow-tooltip>
          <template #default="scope">
            {{ scope.row.party || '--' }}
          </template>
        </el-table-column>
        <el-table-column label="已分配产品权限" prop="productPremission" min-width="200" show-overflow-tooltip>
          <template #default="scope">
            {{ scope.row.productPremission.join(',') || '--' }}
          </template>
        </el-table-column>
        <el-table-column label="最后操作时间" prop="lastOperationTime" min-width="180">
          <template #default="scope">
            {{ scope.row.lastOperationTime || '--' }}
          </template>
        </el-table-column>
        <el-table-column label="操作" fixed="right" width="180">
          <template #default="scope">
            <el-button link type="primary" @click="handleEidt(scope.row)"> 编辑 </el-button>
          </template>
        </el-table-column>
      </el-table>
    </template>
  </FormLayout>
</template>

<script setup lang="ts">
import { reactive, useTemplateRef } from 'vue'
import { selectWidthLarge } from '@/utils/index.ts'
import type { PageInfo } from '@/types/index'
import type { ElForm } from 'element-plus'
// 可以单独定义一个类型
type FormInstance = InstanceType<typeof ElForm>

const state = reactive({
  filterFormData: {
    party: '',
    userName: '',
    userAccount: '',
  },
  tableData: [
    {
      userName: '泉石用户',
      userAccount: '18333333333',
      party: '北京泉石私募基金管理有限公司',
      productPremission: [1, 2],
      lastOperationTime: '2021-01-01 00:00:00',
    },
  ],
  tableLoading: false,
  pageInfo: {
    total: 400,
    currentPage: 1,
    pageSize: 10,
  } as PageInfo,
})

const filterFormRef = useTemplateRef<FormInstance>('filterFormRef')

const resetForm = () => {
  ;(filterFormRef.value as FormInstance).resetFields()
  state.pageInfo = { ...state.pageInfo, currentPage: 1, pageSize: 10 }
  getTableList()
}

const getTableList = () => {}

const handleEidt = (row) => {}

const handleSizeChange = (val: number) => {
  state.pageInfo = { ...state.pageInfo, currentPage: 1, pageSize: val }
  getTableList()
}

const handleCurrentChange = (val: number) => {
  state.pageInfo = { ...state.pageInfo, currentPage: val }
  getTableList()
}
</script>

<style scoped lang=""></style>
