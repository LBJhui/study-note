<template>
  <div></div>
</template>

<script lang="ts" setup>
/**
 * install use
 *
 * Abc -> export default{ install(app){app.component}}
 *
 * use({
 *   install(app) {}
 * })
 */
import MyUI from './modules/my-ui' // 默认找 index.ts
console.log('=>(index.vue:16) MyUI', MyUI)
</script>

<style scoped></style>
