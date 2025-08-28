<template>
  <div id="app">
    <l-input type="number" maxlength="10" show-word-limit v-model="state.formData.value" @input="handleInput" placeholder="请输出内容"></l-input>
    <l-input type="number" v-model="state.formData.value" @input="handleInput" placeholder="请输出内容"></l-input>
    <el-input type="text" maxlength="10" show-word-limit v-model="state.formData.value" @input="handleInput" placeholder="请输出内容"></el-input>
    <el-input type="text" maxlength="10" show-word-limit v-model="state.formData.value" @input="handleInput" placeholder="请输出内容"></el-input>
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue'
const state = reactive({
  formData: {
    value: '',
  },
})

const handleInput = () => {
  console.log('app handleInput')
}
</script>

<style scoped lang="scss"></style>
