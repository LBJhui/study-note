<template>
  <div class="l-link">111</div>
</template>

<script setup lang="ts">
import { defineProps } from 'vue'
const props = defineProps(['type'])
console.log('%c 🍡 props', 'font-size:16px;color:#fca650', props)
</script>

<style scoped lang="scss">
.l-link {
  color: LUI.$l-primary-color;
}
</style>
