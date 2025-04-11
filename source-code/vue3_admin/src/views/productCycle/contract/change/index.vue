<template>
  <!-- 产品合同变更 -->
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
          <MultipleSelect v-model="state.formData.product" :options="productList" placeholder="请选择产品" label="fundShowName" value="fundRegCode" :isFilter="true" width="300" />
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
          <el-table height="100%" :data="state.tableData" @selection-change="handlerSelectChange">
            <el-table-column type="selection" width="55" />
            <el-table-column property="product" label="产品" width="240" show-overflow-tooltip />
            <el-table-column property="changeType" label="合同变更方式" show-overflow-tooltip />
            <el-table-column property="validateDate" label="生效日期" show-overflow-tooltip />
            <el-table-column property="dqjd" label="当前节点" show-overflow-tooltip />
            <el-table-column property="status" label="流程状态" show-overflow-tooltip />
            <el-table-column property="apply" label="申请人" show-overflow-tooltip />
            <el-table-column property="createTime" label="创建时间" show-overflow-tooltip />
            <el-table-column fixed="right" label="操作" min-width="220">
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

  <el-dialog class="dialog" v-model="state.dialogVisible" align-center width="712px" :close-on-click-modal="false">
    <template #header>
      <div class="dialog-title">新增合同变更申请</div>
    </template>
    <div class="dialog-main-container">
      <el-form ref="addFormRef" :model="state.addFormData" :inline="true" label-width="105px" :rules="state.rules" scroll-to-error>
        <div class="info base-info">
          <div class="info-title">基本信息</div>
          <div class="form-item-container">
            <el-form-item prop="product" label="产品">
              <el-select v-model="state.addFormData.product" placeholder="请选择产品">
                <el-option v-for="item in productList" :key="item.fundRegCode" :label="item.fundShowName" :value="item.fundRegCode"></el-option>
              </el-select>
            </el-form-item>
          </div>
          <div class="form-item-container">
            <el-form-item prop="changeType" label="合同变更方式">
              <el-radio-group v-model="state.addFormData.changeType">
                <el-radio v-for="item in changeTypeList" :key="item.dictUnit" :value="item.dictUnit" :label="item.unitDesc"></el-radio>
              </el-radio-group>
            </el-form-item>
          </div>
          <div class="form-item-container">
            <el-form-item prop="changeContent" label="变更内容">
              <el-input v-model="state.addFormData.changeContent" style="width: 390px" :rows="2" type="textarea" placeholder="请填写合同变更内容或上传变更后的合同" />
            </el-form-item>
          </div>
          <div class="form-item-container">
            <el-form-item label=" " prop="changeDescriptionFile"> <Upload v-model="state.addFormData.changeDescriptionFile" type="dashbutton"></Upload> </el-form-item>
          </div>
          <div v-if="isManagerNotice">
            <div class="form-item-container">
              <el-form-item prop="effectDate" label="生效日期"> <el-date-picker v-model="state.addFormData.effectDate" type="date" placeholder="选择日期" /> </el-form-item>
            </div>
            <div class="form-item-container">
              <el-form-item label="上传公告文件" prop="noticeFile">
                <Upload v-model="state.addFormData.noticeFile" type="dashbutton" :tip="'如有多个文件请打包后上传，文件大小不超过30M'" style="width: 408px"></Upload>
              </el-form-item>
            </div>
          </div>
        </div>
        <div class="info business-contact-info">
          <div class="info-title">业务联系人</div>
          <div class="form-item-container">
            <el-form-item prop="contactPersonName" label="姓名">
              <el-select v-model="state.addFormData.contactPersonName" placeholder="请选择业务联系人" clearable @clear="clearContactPersonInfo">
                <el-option v-for="item in productList" :key="item.fundRegCode" :label="item.fundShowName" :value="item.fundRegCode"></el-option>
              </el-select>
            </el-form-item>
          </div>
          <div class="form-item-container">
            <el-form-item prop="contactPersonMobile" label="手机号"> <el-input v-model="state.addFormData.contactPersonMobile" disabled></el-input> </el-form-item>
          </div>
          <div class="form-item-container">
            <el-form-item prop="contactPersonPhone" label="电话"> <el-input v-model="state.addFormData.contactPersonPhone" disabled></el-input> </el-form-item>
          </div>
          <div class="form-item-container">
            <el-form-item prop="contactPersonEmail" label="邮箱"> <el-input v-model="state.addFormData.contactPersonEmail" disabled></el-input> </el-form-item>
          </div>
        </div>
      </el-form>
    </div>
    <template #footer>
      <div class="dialog-footer">
        <el-button @click="closeDialog">取消</el-button>
        <el-button type="primary"> 保存 </el-button>
        <el-button type="primary" @click="confirmAddContact"> 确认 </el-button>
      </div>
    </template>
  </el-dialog>
</template>

<script setup lang="ts">
import { reactive, ref, computed, watch } from 'vue'
import FormLayout from '@/components/FormLayout/index.vue'
import MultipleSelect from '@/components/MultipleSelect/index.vue'
import FilterButton from '@/components/FilterButton/index.vue'
import Upload from '@/components/Upload/index.vue'
import type { PageInfo, Option } from '@/types/index'
import type { FormInstance } from 'element-plus'
import { TableDataItem } from './types/index'

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
  {
    fundManagerCode: 'P1068305',
    fundShortName: '简然慢牛1号',
    fundCode: '3283',
    fundShowName: 'SXX070-简然慢牛1号私募证券投资基金',
    fundProcess: '5',
    nsightCode: '0160',
    fundCreateDate: '2022-12-21',
    nsightFundCode: '3283',
    officeAddress: '重庆市江北区红石路12号17-5',
    institutionName: '重庆简然私募证券投资基金管理有限公司',
    fundName: '简然慢牛1号私募证券投资基金',
    institutionCode: '32239297',
    cooperationType: '00,02',
    fundRegCode: 'SXX070',
  },
]

const changeTypeList = [
  {
    unitDesc: '以补充协议形式变更合同',
    dictUnit: '0',
  },
  {
    unitDesc: '以征询意见函形式变更合同',
    dictUnit: '1',
  },
  {
    unitDesc: '以管理人公告形式变更合同',
    dictUnit: '2',
  },
]

const workflowStatusList = [
  {
    unitDesc: '办理中',
    dictUnit: '0',
    dictCode: 'EXECUTION_STATUS',
  },
  {
    unitDesc: '已办结',
    dictUnit: '1',
    dictCode: 'EXECUTION_STATUS',
  },
  {
    unitDesc: '强制归档',
    dictUnit: '2',
    dictCode: 'EXECUTION_STATUS',
  },
  {
    unitDesc: '未提交',
    dictUnit: '3',
    dictCode: 'EXECUTION_STATUS',
  },
  {
    unitDesc: '审批退回',
    dictUnit: '4',
    dictCode: 'EXECUTION_STATUS',
  },
  {
    unitDesc: '已撤回',
    dictUnit: '5',
    dictCode: 'EXECUTION_STATUS',
  },
  {
    unitDesc: '已删除',
    dictUnit: '6',
    dictCode: 'EXECUTION_STATUS',
  },
]

const addFormRef = ref<FormInstance>()
const validatechangeDescriptionFile = (_rule: any, _value: any, callback: any) => {
  if (state.addFormData.changeDescriptionFile.length === 0) {
    callback(new Error('请上传变更后的合同！'))
  } else {
    callback()
  }
}

const validatenoticeFile = (_rule: any, _value: any, callback: any) => {
  if (state.addFormData.noticeFile.length === 0) {
    callback(new Error('请上传公告文件！'))
  } else {
    callback()
  }
}

const state = reactive({
  dialogVisible: false,
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
    {
      product: '明湾-鑫科FOF19号',
      changeType: '以补充协议形式变更合同',
      validateDate: '2021-06-28',
      dqjd: '合同变更',
      status: '办理中',
      apply: '张三',
      createTime: '2021-06-28',
    },
  ] as Array<TableDataItem>,
  selectedTableData: [] as Array<TableDataItem>,
  addFormData: {
    product: '',
    changeType: '',
    changeContent: '',
    changeDescriptionFile: [],
    effectDate: '',
    noticeFile: [],
    contactPersonName: '',
    contactPersonMobile: '',
    contactPersonPhone: '',
    contactPersonEmail: '',
  },
  rules: {
    product: [{ required: true, message: '请选择产品！', trigger: 'change' }],
    changeType: [{ required: true, message: '请选择合同变更方式！', trigger: 'change' }],
    changeContent: [{ required: true, message: '请输入合同内容！', trigger: 'change' }],
    changeDescriptionFile: [{ validator: validatechangeDescriptionFile, trigger: 'change' }],
    contactPersonName: [{ required: true, message: '请选择业务联系人！', trigger: 'change' }],
    effectDate: [{ required: true, message: '请选择生效日期！', trigger: 'change' }],
    noticeFile: [{ required: true, validator: validatenoticeFile, trigger: 'change' }],
  },
  pageInfo: {
    total: 400,
    currentPage: 1,
    pageSize: 10,
    selectedNum: 0,
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

// “合同变更方式”是否为“以管理人公告形式变更合同”
const isManagerNotice = computed(() => {
  const label = state.addFormData.changeType ? (changeTypeList.find((item) => item.dictUnit === state.addFormData.changeType) as Option)['unitDesc'] : ''
  return label.includes('管理人')
})

const clearContactPersonInfo = () => {
  addFormRef.value?.clearValidate('contactPersonName')
  addFormRef.value?.clearValidate(['contactPersonName', 'contactPersonMobile', 'contactPersonPhone', 'contactPersonEmail'])
}

watch(
  () => state.addFormData.product,
  () => {
    clearContactPersonInfo()
  },
)

watch(
  () => state.addFormData.changeType,
  () => {
    addFormRef.value?.clearValidate(['noticeFile', 'effectDate'])
    addFormRef.value?.resetFields(['noticeFile', 'effectDate'])
  },
)

const closeDialog = () => {
  addFormRef.value?.resetFields()
  state.dialogVisible = false
}

const confirmAddContact = () => {
  addFormRef.value?.validate((valid: boolean) => {
    console.log('%c 🍧 valid', 'font-size:16px;color:#ea7e5c', valid)
  })
}

const handlerSelectChange = (val: Array<TableDataItem>) => {
  state.selectedTableData = val
  state.pageInfo.selectedNum = state.selectedTableData.length
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
