<template>
  <FormLayout :pageInfo="state.pageInfo" @sizeChange="handleSizeChange" @currentChange="handleCurrentChange">
    <template #form>
      <el-form v-model="filterForm" :inline="true">
        <el-form-item label="所属机构" prop="party">
          <el-select v-model="state.filterForm.party" :style="`width: ${selectWidthLarge}px`" placeholder="请选择所属机构">
            <el-option label="机构1" value="1"></el-option>
            <el-option label="机构2" value="2"></el-option>
            <el-option label="机构3" value="3"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="用户姓名" prop="userName">
          <el-input v-model="state.filterForm.userName" placeholder="请输入用户姓名"></el-input>
        </el-form-item>
        <el-form-item label="用户账号" prop="userAccount">
          <el-input v-model="state.filterForm.userAccount" placeholder="请输入用户账号"></el-input>
        </el-form-item>
        <el-form-item label="用户状态" prop="userStatus">
          <el-select v-model="state.filterForm.userStatus" :style="`width: ${selectWidthSmall}px`" placeholder="请选择用户状态">
            <el-option label="全部" value="1"></el-option>
            <el-option label="启用" value="2"></el-option>
            <el-option label="禁用" value="3"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item>
          <FilterButton @resetForm="resetForm" @getTableList="getTableList" :buttonList="['查询', '重置']" />
        </el-form-item>
      </el-form>
    </template>
    <template #btn>
      <div class="table-btn">
        <el-button type="primary">
          <i class="iconfont icon-tianjia"></i>
          新增用户</el-button
        >
      </div>
    </template>
    <template #table>
      <el-table :data="state.tableData">
        <el-table-column prop=""></el-table-column>
      </el-table>
    </template>
  </FormLayout>
</template>

<script setup lang="ts">
import { reactive } from 'vue'
import { selectWidthLarge, selectWidthSmall } from '@/utils/index.ts'

const state = reactive({
  filterForm: {
    party: '',
    userName: '',
    userAccount: '',
    userStatus: '1',
  },
  tableData: [{}],
  pageInfo: {
    total: 400,
    currentPage: 1,
    pageSize: 10,
  },
})

const getTableList = () => {}

const resetForm = () => {}

const handleSizeChange = (val: number) => {}
const handleCurrentChange = (val: number) => {}
</script>

<style scoped lang="scss">
.table-btn {
  .el-button {
    padding: 8px 15px 8px 10px;
  }
}
</style>
