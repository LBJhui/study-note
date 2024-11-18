<template>
  <div>
    <t-button>测试</t-button>
    <t-button type="success">测试</t-button>
    <t-button type="warning">测试</t-button>
    <t-input v-model="val"></t-input>
    {{ val }}
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'

const val = ref('')
</script>

<style lang="" scoped></style>
