<template>
  <div class="check-container">
    <div class="check-container-all">
      <el-checkbox v-model="state.checkAll" @change="handleCheckAllChange">全选</el-checkbox>
      <div class="check-container-all-text">
        共 <span class="check-container-all-num">{{ state.count }}</span> 个<span>角色</span> 已选 <span class="check-container-all-num">{{ state.value.length }}</span> 个
      </div>
    </div>
    <div clas="check-container-list">
      <el-checkbox-group v-model="state.value">
        <el-checkbox v-for="item in options" :value="item[value]" :key="item[value]">{{ item[label] }}</el-checkbox>
      </el-checkbox-group>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, computed, watch } from 'vue'
import type { CheckboxValueType } from 'element-plus'

const props = defineProps({
  options: {
    type: Array as () => any[],
    default: () => [],
  },
  label: { type: String, default: 'unitDesc' },
  value: { type: String, default: 'dictUnit' },
})

const selected = defineModel()

const state = reactive({
  value: [] as string[],
  checkAll: false,
  count: props.options.length,
})

watch(
  () => state.value,
  (val) => {
    selected.value = val
  },
)

computed(() => {
  state.checkAll = state.value.length === props.options.length
})

const handleCheckAllChange = (val: CheckboxValueType) => {
  if (val) {
    state.value = props.options.map((item) => item[props.value])
  } else {
    state.value = []
  }
}
</script>

<style scoped lang="scss">
.check-container {
  .check-container-all {
    display: flex;
    align-items: center;
    font-size: 14px;
    line-height: 1;

    .check-container-all-text {
      margin-left: 5px;
      .check-container-all-num {
        color: var(--el-color-primary);
      }
    }
  }
}
</style>
