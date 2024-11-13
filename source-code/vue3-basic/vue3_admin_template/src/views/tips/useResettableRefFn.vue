<template>
  <div>{{ state.a }}</div>
  <div>{{ state.b }}</div>
  <div>{{ state.c }}</div>
  <el-button type="primary" @click="state.a++">a++</el-button>
  <el-button type="primary" @click="state.b++">b++</el-button>
  <el-button type="primary" @click="state.c.push(1)">push c</el-button>
  <el-button @click="reset">重置</el-button>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const useResettableRefFn = <T,>(value: () => T) => {
  const state = ref(value())

  const reset = () => {
    state.value = value()
  }
  return { state, reset }
}

const { state, reset } = useResettableRefFn(() => {
  return {
    a: 1,
    b: 2,
    c: [1, 2],
  }
})

// const state = ref({
//   a: 1,
//   b: 2,
//   c: [1, 2],
// })

// const reset = () => {
//   state.value = {
//     a: 1,
//     b: 2,
//     c: [1, 2],
//   }
// }
</script>

<style scoped lang=""></style>
