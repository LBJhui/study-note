<template>
  <router-view />
</template>

<script setup lang="ts">
console.log(123)
</script>

<style>
body::-webkit-scrollbar {
  display: none;
}
body {
  padding: 0;
  margin: 0;
}
#app {
  font-family: PingFangSC-Regular, PingFang SC;
  font-weight: 400;
}
</style>
