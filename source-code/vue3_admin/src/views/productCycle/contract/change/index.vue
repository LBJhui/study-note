<template>
  <!-- 产品合同变更 -->
  <div>
    <FormLayout :pageInfo="state.pageInfo" @sizeChange="handleSizeChange" @currentChange="handleCurrentChange">
      <template #form>
        <el-form :model="state.formData" :inline="true">
          <el-form-item label="创建日期：" prop="date">
            <el-date-picker v-model="state.formData.date" type="daterange" range-separator="~" start-placeholder="开始日期" end-placeholder="结束日期" />
          </el-form-item>
          <el-form-item label="产品：" prop="product">
            <MultipleSelect
              v-model="state.formData.product"
              :options="productList"
              placeholder="请选择产品"
              label="fundShowName"
              value="fundRegCode"
              :isFilter="true"
              width="240"
            />
          </el-form-item>
          <el-form-item label="合同变更方式：" prop="changeType">
            <MultipleSelect v-model="state.formData.changeType" :options="changeTypeList" placeholder="请选择合同变更方式" />
          </el-form-item>
          <el-form-item label="流程状态：" prop="workflowStatus">
            <MultipleSelect v-model="state.formData.workflowStatus" :options="workflowStatusList" placeholder="请选择流程状态" />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="getTableList">查询</el-button>
            <el-button @click="resetForm">重置</el-button>
            <el-button type="primary">批量导出</el-button>
          </el-form-item>
        </el-form>
      </template>
      <template #table>
        <el-table height="100%"></el-table>
      </template>
    </FormLayout>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import FormLayout from '@/components/FormLayout/index.vue'
import MultipleSelect from '@/components/MultipleSelect/index.vue'

import type { PageInfo } from '@/types/index'

const productList = [
  {
    fundManagerCode: 'P1001040',
    fundShortName: '明湾-鑫科FOF18号',
    fundCode: '941',
    fundShowName: 'SQT968-明湾-鑫科FOF18号私募证券投资基金',
    fundProcess: '6',
    nsightCode: '0144',
    fundCreateDate: '2021-06-28',
    nsightFundCode: '941',
    officeAddress: '上海市徐汇区徐汇区东湖路7号202室',
    institutionName: '上海明湾资产管理有限公司',
    fundName: '明湾-鑫科FOF18号私募证券投资基金',
    institutionCode: '297407',
    cooperationType: '00',
    fundRegCode: 'SQT968',
  },
]

const changeTypeList = [
  {
    companyCode: null,
    unitDesc: '以补充协议形式变更合同',
    dictUnit: '0',
    dictCode: null,
  },
  {
    companyCode: null,
    unitDesc: '以征询意见函形式变更合同',
    dictUnit: '1',
    dictCode: null,
  },
  {
    companyCode: null,
    unitDesc: '以管理人公告形式变更合同',
    dictUnit: '2',
    dictCode: null,
  },
]

const workflowStatusList = [
  {
    companyCode: null,
    unitDesc: '办理中',
    dictUnit: '0',
    dictCode: 'EXECUTION_STATUS',
  },
  {
    companyCode: null,
    unitDesc: '已办结',
    dictUnit: '1',
    dictCode: 'EXECUTION_STATUS',
  },
  {
    companyCode: null,
    unitDesc: '强制归档',
    dictUnit: '2',
    dictCode: 'EXECUTION_STATUS',
  },
  {
    companyCode: null,
    unitDesc: '未提交',
    dictUnit: '3',
    dictCode: 'EXECUTION_STATUS',
  },
  {
    companyCode: null,
    unitDesc: '审批退回',
    dictUnit: '4',
    dictCode: 'EXECUTION_STATUS',
  },
  {
    companyCode: null,
    unitDesc: '已撤回',
    dictUnit: '5',
    dictCode: 'EXECUTION_STATUS',
  },
  {
    companyCode: null,
    unitDesc: '已删除',
    dictUnit: '6',
    dictCode: 'EXECUTION_STATUS',
  },
]

const state = reactive({
  pageInfo: {
    total: 400,
    currentPage: 1,
    pageSize: 10,
  } as PageInfo,
  formData: {
    date: [],
    product: [] as string[],
    changeType: [] as string[],
    workflowStatus: [] as string[],
  },
})

const getTableList = () => {
  console.log('%c 🍡getTableList', 'font-size:16px;color:#6ec1c2', state.formData)
}

const resetForm = () => {
  state.formData = {
    date: [],
    product: [] as string[],
    changeType: [] as string[],
    workflowStatus: [] as string[],
  }
  getTableList()
}

const handleSizeChange = (val: number) => {
  state.pageInfo.pageSize = val
}

const handleCurrentChange = (val: number) => {
  state.pageInfo.currentPage = val
}
</script>

<style scoped lang="scss"></style>
