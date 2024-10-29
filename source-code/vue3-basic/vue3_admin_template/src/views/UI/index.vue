<template>
  <div>UI组件二次封装</div>
  <MyInput ref="inputRef" v-model="data" placeholder="地址">
    <template #prefix>
      <el-icon class="el-input__icon"><search /></el-icon>
    </template>
  </MyInput>
  <button @click="clear">1111</button>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import MyInput from './components/MyInput.vue'

let data = ref('')
let inputRef = ref()

onMounted(() => {
  if (inputRef.value) {
    inputRef.value.focus()
  }
})

const clear = () => {
  inputRef.value.clear()
}
</script>

<style scoped></style>
