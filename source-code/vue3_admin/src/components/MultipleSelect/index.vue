<template>
  <el-select v-model="selectedList" :placeholder="placeholder" :style="`width: ${width}px`" multiple clearable collapse-tags @clear="clearCheckbox">
    <template #header v-if="isFilter">header</template>
    <el-option label="全部" value="全部">
      <el-checkbox v-model="checkAll" :indeterminate="indeterminate" @change="handleCheckAll" style="width: 100%"> 全部 </el-checkbox>
    </el-option>
    <el-checkbox-group v-model="selectedList">
      <el-option v-for="item in options" :key="item[value]" :label="item[label]" :value="item[value]" @change="handleOption(item)">
        <div class="flex items-center">
          <el-checkbox :label="item[label]" :value="item[value]" style="width: 100%" :checked="selectedList.includes(item[value])">{{ item[label] }}</el-checkbox>
        </div>
      </el-option>
    </el-checkbox-group>
    <template #tag v-if="tag">
      <span class="tag">{{ tag }}</span>
    </template>
  </el-select>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'

// 定义选项的类型
interface Option {
  [key: string]: any // 动态键值对，可根据实际需求调整为更具体的类型
}

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
    default: '200',
  },
})

const root = document.documentElement.style
root.setProperty('--tag-width', +props.width * 0.7 + 'px')

const emit = defineEmits(['update:modelValue', 'change'])

const selectedList = ref<string[]>(props.modelValue)
const checkAll = ref(false)
const indeterminate = ref(false)
const tag = ref('')

const handleOption = (item: Option) => {
  selectedList.value = selectedList.value.includes(item[props.value]) ? selectedList.value.filter((_) => _ !== item[props.value]) : [...selectedList.value, item[props.value]]
  handleChange(selectedList.value)
}

const clearCheckbox = () => {
  handleChange([])
}
const handleCheckAll = (val: any) => {
  indeterminate.value = false
  let value: string[] = []
  if (val) {
    value = props.options.map((_) => _[props.value])
  } else {
    value = []
  }
  selectedList.value = value
  handleChange(value)
}

const handleChange = (value: string[]) => {
  emit('update:modelValue', value)
  emit('change', value)
}

const isCheckedAll = () => {
  const checkedCount = selectedList.value.length
  checkAll.value = !!checkedCount && checkedCount === props.options.length
  indeterminate.value = checkedCount > 0 && checkedCount < props.options.length
}

watch(
  () => props.modelValue,
  (val) => {
    selectedList.value = val
    isCheckedAll()
    if (checkAll.value) {
      tag.value = '全部'
    } else if (selectedList.value.length === 1) {
      tag.value = props?.options?.find((_) => _[props.value] === selectedList.value[0])?.[props.label]
    } else if (selectedList.value.length > 1) {
      tag.value = `已选 ${selectedList.value.length} 项`
    } else {
      tag.value = ''
    }
  },
)
</script>

<style scoped lang="scss">
.el-select-dropdown.is-multiple .el-select-dropdown__item.is-selected:after {
  display: none;
}

.tag {
  margin-left: 12px;
  overflow: hidden;
  line-clamp: 1;
  white-space: nowrap;
  text-overflow: ellipsis;
  width: var(--tag-width);
}
</style>
