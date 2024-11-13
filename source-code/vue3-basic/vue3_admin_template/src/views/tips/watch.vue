<template>
  <div>
    <div>{{ count }}</div>
    <div>
      <button @click="count++">+1</button>
      <button @click="pause">暂停监听</button>
      <button @click="resume">恢复监听</button>
      <button @click="stop">停止</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
const count = ref(0)
const { stop, resume, pause } = watch(count, () => {
  console.log('触发了 watch')
})
// const stop = watch(count, () => {
//   console.log('触发了 watch')
// })
console.log('%c 🍑 resume', 'font-size:16px;color:#93c0a4', resume)
</script>

<style scoped lang=""></style>
