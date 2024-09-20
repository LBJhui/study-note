<template>
  <div>
    <Children :count="count" />
    <button @click="add">increase</button>
  </div>
</template>

<script setup lang="ts">
import Children from './children.vue';
const count = ref(1)
const add = () => {
  count.value++
}
</script>

<style scoped lang=""></style>
