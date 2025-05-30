<template>
  <el-select v-model="selectedList" :placeholder="placeholder" :style="`width: ${width}px`" multiple clearable collapse-tags @clear="clearCheckbox" @visible-change="visibleChange">
    <template #header v-if="isFilter"><el-input v-model="search" placeholder="搜索"></el-input></template>
    <el-option label="全部" value="全部" v-if="showCheckAll">
      <el-checkbox v-model="checkAll" :indeterminate="indeterminate" @change="handleCheckAll" style="width: 100%"> 全部 </el-checkbox>
    </el-option>
    <el-checkbox-group v-model="selectedList">
      <template v-for="item in options" :key="item[value]">
        <el-option :label="item[label]" :value="item[value]" @change="handleOption(item)" v-if="item[label].includes(search)">
          <div class="flex items-center">
            <el-checkbox :label="item[label]" :value="item[value]" style="width: 100%" :checked="selectedList.includes(item[value])">{{ item[label] }}</el-checkbox>
          </div>
        </el-option>
      </template>
    </el-checkbox-group>
    <template #tag v-if="tagText">
      <span class="tag">{{ tagText }}</span>
    </template>
  </el-select>
</template>

<script setup lang="ts">
import { computed, ref, watch } from 'vue'
import type { Option } from '@/types/index'
import { selectWidth } from '@/utils/index'

const emit = defineEmits(['update:modelValue', 'change'])
const props = defineProps({
  options: {
    type: Array as () => Option[], // 明确 options 类型为 Option[]
    default: (): Option[] => [],
  },
  placeholder: {
    type: String,
  },
  modelValue: {
    type: Array as () => string[],
    default: (): string[] => [],
  },
  label: { type: String, default: 'unitDesc' },
  value: { type: String, default: 'dictUnit' },
  isFilter: {
    type: Boolean,
    default: false,
  },
  width: {
    type: String,
    default: selectWidth,
  },
})

watch(
  () => props.modelValue,
  (val) => {
    selectedList.value = val
    isCheckedAll()
    if (checkAll.value) {
      tagText.value = '全部'
    } else if (selectedList.value.length === 1) {
      tagText.value = props?.options?.find((_) => _[props.value] === selectedList.value[0])?.[props.label]
    } else if (selectedList.value.length > 1) {
      tagText.value = `已选 ${selectedList.value.length} 项`
    } else {
      tagText.value = ''
    }
  },
)

const showCheckAll = computed(() => {
  return props?.options?.find((_) => _[props.label].includes(search.value))
})

const selectedList = ref<string[]>(props.modelValue)
const search = ref('')
const checkAll = ref(false)
const indeterminate = ref(false)
const tagText = ref('')

const handleCheckAll = (val: any) => {
  indeterminate.value = false
  let value: string[] = []
  if (val) {
    const options = getFilterOptions()
    value = options.map((item) => item[props.value])
  } else {
    value = []
  }
  selectedList.value = value
  handleChange(value)
}

const clearCheckbox = () => {
  handleChange([])
}

const visibleChange = () => {
  search.value = ''
}
const handleOption = (item: Option) => {
  selectedList.value = selectedList.value.includes(item[props.value]) ? selectedList.value.filter((_) => _ !== item[props.value]) : [...selectedList.value, item[props.value]]
  handleChange(selectedList.value)
}

const handleChange = (value: string[]) => {
  emit('update:modelValue', value)
  emit('change', value)
}

const isCheckedAll = () => {
  const checkedCount = selectedList.value.length
  let options = getFilterOptions()
  checkAll.value = !!checkedCount && checkedCount === options.length
  indeterminate.value = checkedCount > 0 && checkedCount < options.length
}

const getFilterOptions = () => {
  return props.isFilter && search.value ? props.options.filter((item) => item[props.label].includes(search.value)) : props.options
}
</script>

<style scoped lang="scss">
.el-select-dropdown.is-multiple .el-select-dropdown__item.is-selected:after {
  display: none;
}

.tag {
  margin-left: 12px;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
</style>
