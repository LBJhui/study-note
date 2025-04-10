<template>
  <el-button type="primary" @click="getTableList" v-if="buttonList.includes('查询')">查询</el-button>
  <el-button @click="resetForm" v-if="buttonList.includes('重置')">重置</el-button>
  <el-button type="primary" v-if="buttonList.includes('批量导出')">批量导出</el-button>
</template>

<script setup lang="ts">
const props = defineProps({
  buttonList: {
    type: Array as () => String[],
    default: (): String[] => [],
  },
})
const emit = defineEmits(['getTableList', 'resetForm'])

const getTableList = () => {
  emit('getTableList')
}

const resetForm = () => {
  emit('resetForm')
}
</script>

<style scoped lang=""></style>
