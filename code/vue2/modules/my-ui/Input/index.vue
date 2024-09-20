<template>
  <input class="my-input" type="text" :placeholder="placeholder" :value="value" />
</template>

<script>
export default {
  name: 'MyInput',
  props: {
    placeholder: String,
    value: String
  },
}
</script>

<style lang="scss">
.my-input {
  height: 34px;
  border: 1px solid #ddd;
  background-color: #fff;
}
</style>