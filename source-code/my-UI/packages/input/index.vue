<template>
  <div>
    <input :value="props.modelValue" type="text" @input="input">
  </div>
</template>

<script lang="ts">
export default {
  name: 't-input',
}
</script>

<script lang="ts" setup>
const props = defineProps({
  modelValue: String
})
const emit = defineEmits([ 'update:modelValue' ])
const input = (e: any) => {
  emit('update:modelValue', e.target.value)
}

</script>

<style scoped>

</style>