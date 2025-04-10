<template>
  <!-- 产品合同变更 -->
  <div>
    <FormLayout :pageInfo="state.pageInfo" @sizeChange="handleSizeChange" @currentChange="handleCurrentChange">
      <template #form>
        <el-form :model="state.formData" :inline="true">
          <el-form-item label="创建日期：" prop="date">
            <el-date-picker
              v-model="state.formData.date"
              type="daterange"
              range-separator="~"
              start-placeholder="开始日期"
              end-placeholder="结束日期"
              value-format="yyyy-MM-dd"
              placement="bottom-start"
            />
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
            <FilterButton @resetForm="resetForm" @getTableList="getTableList" :buttonList="['查询', '重置', '批量导出']" />
          </el-form-item>
        </el-form>
      </template>
      <template #table>
        <div class="main-container">
          <div class="btn">
            <el-button type="primary" @click="addApply">新增合同变更申请</el-button>
          </div>
          <div class="table">
            <el-table height="100%" :data="state.tableData">
              <el-table-column property="product" label="产品" width="240" show-overflow-tooltip />
              <el-table-column property="changeType" label="合同变更方式" show-overflow-tooltip />
              <el-table-column property="validateDate" label="生效日期" show-overflow-tooltip />
              <el-table-column property="dqjd" label="当前节点" show-overflow-tooltip />
              <el-table-column property="status" label="流程状态" show-overflow-tooltip />
              <el-table-column property="apply" label="申请人" show-overflow-tooltip />
              <el-table-column property="createTime" label="创建时间" show-overflow-tooltip />
              <el-table-column fixed="right" label="操作" min-width="120">
                <template #default>
                  <el-button link type="primary" size="small"> 详情 </el-button>
                  <el-button link type="primary" size="small">下载合同变更文件</el-button>
                </template>
              </el-table-column>
            </el-table>
          </div>
        </div>
      </template>
    </FormLayout>

    <el-dialog class="dialog" v-model="state.dialogVisible" align-center>
      <template #header>
        <div class="dialog-title">新增合同变更申请</div>
      </template>
      <div class="dialog-main-container">
        <el-form ref="addFormRef" v-model="state.addFormData" :inline="true" label-width="105px" :rules="rules">
          <div class="info base-info">
            <div class="info-title">基本信息</div>
            <el-form-item prop="product" label="产品">
              <el-select v-model="state.addFormData.product" placeholder="请选择产品">
                <el-option v-for="item in productList" :key="item.fundRegCode" :label="item.fundShowName" :value="item.fundRegCode"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item prop="changeType" label="合同变更方式">
              <el-radio-group v-model="state.addFormData.changeType">
                <el-radio v-for="item in changeTypeList" :key="item.dictUnit" :value="item.dictUnit" :label="item.unitDesc"></el-radio>
              </el-radio-group>
            </el-form-item>
            <el-form-item prop="changeContent" label="变更内容">
              <el-input v-model="state.addFormData.changeContent" style="width: 390px" :rows="2" type="textarea" placeholder="请填写合同变更内容或上传变更后的合同" />
            </el-form-item>
            <el-form-item label=" " prop="changeDescriptionFileList">
              <Upload v-model="state.addFormData.changeDescriptionFileList" type="dashbutton"></Upload>
            </el-form-item>
          </div>
          <div class="info business-contact-info">
            <div class="info-title">业务联系人</div>
            <el-form-item prop="contactPersonName" label="姓名">
              <el-select v-model="state.contactPersonInfo.contactPersonName" placeholder="请选择业务联系人" clearable>
                <el-option v-for="item in productList" :key="item.fundRegCode" :label="item.fundShowName" :value="item.fundRegCode"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item prop="contactPersonMobile" label="手机号">
              <el-input v-model="state.contactPersonInfo.contactPersonMobile" disabled></el-input>
            </el-form-item>
            <el-form-item prop="contactPersonPhone" label="电话">
              <el-input v-model="state.contactPersonInfo.contactPersonPhone" disabled></el-input>
            </el-form-item>
            <el-form-item prop="contactPersonEmail" label="邮箱">
              <el-input v-model="state.contactPersonInfo.contactPersonEmail" disabled></el-input>
            </el-form-item>
          </div>
        </el-form>
      </div>
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="closeDialog">取消</el-button>
          <el-button type="primary" @click="state.dialogVisible = false"> 保存 </el-button>
          <el-button type="primary" @click="state.dialogVisible = false"> 确认 </el-button>
        </div>
      </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'
import FormLayout from '@/components/FormLayout/index.vue'
import MultipleSelect from '@/components/MultipleSelect/index.vue'
import FilterButton from '@/components/FilterButton/index.vue'
import Upload from '@/components/Upload/index.vue'
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

const addFormRef = ref()
const rules = {
  product: [{ required: true }],
  changeType: [{ required: true }],
  changeContent: [{ required: true }],
  contactPersonName: [{ required: true }],
}

const state = reactive({
  dialogVisible: true,
  formData: {
    date: [],
    product: [] as string[],
    changeType: [] as string[],
    workflowStatus: [] as string[],
  },
  tableData: [
    {
      product: '明湾-鑫科FOF18号',
      changeType: '以补充协议形式变更合同',
      validateDate: '2021-06-28',
      dqjd: '合同变更',
      status: '办理中',
      apply: '张三',
      createTime: '2021-06-28',
    },
  ],
  addFormData: {
    product: '',
    changeType: '',
    changeContent: '',
    changeDescriptionFileList: [],
  },
  contactPersonInfo: {
    contactPersonName: 'contactPersonName',
    contactPersonMobile: 'contactPersonName',
    contactPersonPhone: 'contactPersonName',
    contactPersonEmail: 'contactPersonName',
  },
  pageInfo: {
    total: 400,
    currentPage: 1,
    pageSize: 10,
  } as PageInfo,
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

const addApply = () => {
  state.dialogVisible = true
}

const closeDialog = () => {
  addFormRef.value.resetFields()
  state.dialogVisible = false
}

const handleSizeChange = (val: number) => {
  state.pageInfo.pageSize = val
}

const handleCurrentChange = (val: number) => {
  state.pageInfo.currentPage = val
}
</script>

<style scoped lang="scss">
.main-container {
  display: flex;
  flex-direction: column;
  height: 100%;
  .btn {
    height: $tableContainerButtonHeight;
    padding-left: $paddingLeft;
    display: flex;
    align-items: center;
  }
  .table {
    flex: 1;
  }
}

.dialog {
  .dialog-title {
    line-height: $elDialogHeaderHeight;
    padding-left: $elDialogHeaderPaddingLeft;
    font-weight: bold;
    border-bottom: 1px solid #e5e7ec;
  }
  .dialog-main-container {
    max-height: 482px;
    overflow-y: auto;
    padding: 15px 72px;
    .info {
      .info-title {
        font-size: 14px;

        font-weight: 600;
        color: #0f1a30;
        line-height: 22px;
        padding: 16px 0;
        margin-left: 36px;
      }

      .el-select,
      .el-input {
        width: 290px;
      }
    }
  }

  .dialog-footer {
    padding: 30px 0 20px;
    text-align: center;
    box-shadow: rgba(28, 50, 122, 0.15) 0 -1px 6px 0;
  }
}
</style>
