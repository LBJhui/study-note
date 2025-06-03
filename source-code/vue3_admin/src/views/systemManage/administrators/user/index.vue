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
        <el-form-item label="用户状态" prop="userStatus">
          <el-select v-model="state.filterFormData.userStatus" :style="`width: ${selectWidthSmall}px`" placeholder="请选择用户状态">
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
        <el-button type="primary" @click="HandlerAddUser">
          <i class="iconfont icon-tianjia"></i>
          新增用户</el-button
        >
      </div>
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
        <el-table-column label="角色" prop="role" min-width="200" show-overflow-tooltip>
          <template #default="scope">
            {{ scope.row.role.join(',') || '--' }}
          </template>
        </el-table-column>
        <el-table-column label="用户状态" prop="userStatus" min-width="120">
          <template #default="scope">
            <span class="table-switch-active-text" v-if="scope.row.userStatus === '1'">启用</span>
            <span class="table-switch-inactive-text" v-else>禁用</span>
            <el-switch v-model="scope.row.userStatus" active-value="1" inactive-value="0"></el-switch>
          </template>
        </el-table-column>
        <el-table-column label="邮箱" prop="email" min-width="180">
          <template #default="scope">
            {{ scope.row.email || '--' }}
          </template>
        </el-table-column>
        <el-table-column label="座机电话" prop="telephone" min-width="120">
          <template #default="scope">
            {{ scope.row.telephone || '--' }}
          </template>
        </el-table-column>
        <el-table-column label="证件类型" prop="IDType" min-width="120">
          <template #default="scope">
            {{ scope.row.IDType || '--' }}
          </template>
        </el-table-column>
        <el-table-column label="证件号码" prop="IDNumber" min-width="120">
          <template #default="scope">
            {{ scope.row.IDNumber || '--' }}
          </template>
        </el-table-column>
        <el-table-column label="备注" prop="comment" min-width="180" show-overflow-tooltip>
          <template #default="scope">
            {{ scope.row.comment || '--' }}
          </template>
        </el-table-column>
        <el-table-column label="操作" fixed="right" width="180">
          <template #default="scope">
            <el-button link type="primary" @click="handleEidt(scope.row)"> 编辑 </el-button>
            <el-button link type="primary" @click="handleViewProductPermissions(scope.row)"> 查看产品权限 </el-button>
          </template>
        </el-table-column>
      </el-table>
    </template>
  </FormLayout>

  <el-dialog v-model="state.dialogVisible" width="786" class="dialog-container" top="15vh" max-height="70vh">
    <template #header>
      <div class="dialog-container-header">
        <i class="iconfont icon-addteam"></i>
        新增用户
      </div>
    </template>
    <div class="dialog-container-content">
      <el-form :model="state.dialogFormData" ref="dialogFormRef" :inline="true" label-width="140px">
        <div class="dialog-container-content-baseInfo">
          <div class="dialog-container-content-title">基本信息</div>
          <div class="dialog-container-content-baseInfo-form">
            <el-form-item label="所属机构：">
              <el-select v-model="state.dialogFormData.party"></el-select>
            </el-form-item>
            <el-form-item label="用户姓名：">
              <el-input v-model="state.dialogFormData.userName"></el-input>
            </el-form-item>
            <el-form-item label="手机号：">
              <el-input v-model="state.dialogFormData.userName"></el-input>
            </el-form-item>
            <el-form-item label="邮箱：">
              <el-input v-model="state.dialogFormData.userName"></el-input>
            </el-form-item>
            <el-form-item label="座机电话：">
              <el-input v-model="state.dialogFormData.userName"></el-input>
            </el-form-item>
            <el-form-item label="证件类型：">
              <el-select v-model="state.dialogFormData.party"></el-select>
            </el-form-item>
            <el-form-item label="证件号码：">
              <el-input v-model="state.dialogFormData.userName"></el-input>
            </el-form-item>
            <el-form-item label="是否添加至联系人："> </el-form-item>
            <el-form-item label="联系人类型："> </el-form-item>
            <el-form-item label="备注："> </el-form-item>
          </div>
        </div>
        <div class="dialog-container-content-role">
          <div class="dialog-container-content-title">角色分配</div>
        </div>
        <div class="dialog-container-content-product">
          <div class="dialog-container-content-title">产品权限分配</div>
        </div>
      </el-form>
    </div>
    <template #footer>
      <div class="dialog-container-footer">
        <el-button @click="closeDialog">取消</el-button>
        <el-button type="primary">添加</el-button>
      </div>
    </template>
  </el-dialog>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { selectWidthLarge, selectWidthSmall } from '@/utils/index.ts'
import type { TableDataItem } from './type/index'
import type { PageInfo } from '@/types/index'

const filterFormRef = ref()

const state = reactive({
  dialogVisible: false,
  tableLoading: false,
  filterFormData: {
    party: '',
    userName: '',
    userAccount: '',
    userStatus: '1',
  },
  tableData: [] as TableDataItem[],
  pageInfo: {
    total: 400,
    currentPage: 1,
    pageSize: 10,
  } as PageInfo,
  dialogFormData: {
    party: '',
    userName: '',
  },
})

const getTableList = () => {
  state.tableLoading = true
  setTimeout(() => {
    state.tableData = [
      {
        userAccount: '18333333333',
        userName: '泉石用户1',
        party: '北京泉石私募基金管理有限公司',
        role: ['泉石自定义角色'],
        userStatus: '1',
        email: 'yuanxuejun@n-sight.com.cn',
        telephone: '',
        IDType: '',
        IDNumber: '',
        comment: '',
      },
    ]
    state.tableLoading = false
  }, 1000)
}

const resetForm = () => {
  filterFormRef.value.resetFields()
  handleSetPageInfo({ ...state.pageInfo, currentPage: 1, pageSize: 10 })
  getTableList()
}

const HandlerAddUser = () => {
  state.dialogVisible = true
}
const handleEidt = (row: TableDataItem) => {}

const handleViewProductPermissions = (row: TableDataItem) => {}

const handleSetPageInfo = (option: PageInfo) => {
  state.pageInfo.currentPage = option.currentPage
  state.pageInfo.total = option.total
  state.pageInfo.pageSize = option.pageSize
}

const handleSizeChange = (val: number) => {
  handleSetPageInfo({ ...state.pageInfo, currentPage: 1, pageSize: val })
  getTableList()
}

const handleCurrentChange = (val: number) => {
  handleSetPageInfo({ ...state.pageInfo, currentPage: val })
  getTableList()
}

const closeDialog = () => {
  state.dialogVisible = false
}

const init = () => {
  getTableList()
}
init()
</script>

<style scoped lang="scss">
.table-btn {
  .el-button {
    padding: 8px 15px 8px 10px;
  }
}

.table-switch-active-text {
  color: var(--el-color-primary);
}

.table-switch-inactive-text {
  color: var(--el-switch-off-color);
}

.dialog-container {
  .dialog-container-header {
    line-height: $elDialogHeaderHeight;
    padding-left: $elDialogHeaderPadding;
    border-bottom: 1px solid $elDialogHrColor;
    i {
      color: var(--el-color-primary);
    }
  }
  .dialog-container-content {
    max-height: 60vh;
    overflow-y: auto;
    overflow-x: hidden;
    .el-form > div {
      padding: 0 $elDialogHeaderPadding;
    }
    .dialog-container-content-title {
      font-size: 14px;
      font-family: PingFangSC-Semibold, 'PingFang SC';
      font-weight: 600;
      color: rgb(15, 26, 48);
      line-height: 60px;
    }

    .dialog-container-content-baseInfo {
      border-bottom: 1px solid $elDialogHrColor;
      .dialog-container-content-baseInfo-form {
        display: grid;
        grid-template-rows: 7;
        grid-template-areas: 'a .' 'b c' 'd e' 'f g' 'h h' 'i i' 'j j';
      }
      .dialog-container-content-baseInfo-form .el-form-item:nth-child(1) {
        grid-area: a;
      }
      .dialog-container-content-baseInfo-form .el-form-item:nth-child(2) {
        grid-area: b;
      }
      .dialog-container-content-baseInfo-form .el-form-item:nth-child(3) {
        grid-area: c;
      }
      .dialog-container-content-baseInfo-form .el-form-item:nth-child(4) {
        grid-area: d;
      }
      .dialog-container-content-baseInfo-form .el-form-item:nth-child(5) {
        grid-area: e;
      }
      .dialog-container-content-baseInfo-form .el-form-item:nth-child(6) {
        grid-area: f;
      }
      .dialog-container-content-baseInfo-form .el-form-item:nth-child(7) {
        grid-area: g;
      }
      .dialog-container-content-baseInfo-form .el-form-item:nth-child(8) {
        grid-area: h;
      }
      .dialog-container-content-baseInfo-form .el-form-item:nth-child(9) {
        grid-area: i;
      }
      .dialog-container-content-baseInfo-form .el-form-item:nth-child(10) {
        grid-area: j;
      }
    }
    .dialog-container-content-role {
      display: flex;
      border-bottom: 1px solid $elDialogHrColor;
    }
  }

  .dialog-container-footer {
    text-align: center;
    padding: $elDialogHeaderPadding 0;
  }
}
</style>
