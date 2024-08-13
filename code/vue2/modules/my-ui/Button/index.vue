<template>
  <button :class="['my-btn', type]" @click="btnClick">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: 'MyButton',
  props: {
    type: String
  },
  methods: {
    btnClick (e) {
      this.$emit('click', e)
    }
  }
}
</script>

<style lang="scss">
.my-btn {
  height: 34px;
  padding: 0 15px;
  border: 1px solid #ddd;
  background-color: #fff;

  &.primary {
    border: 1px solid #ddd;
    color: #fff;
    background-color: #409eff;
  }

  &.success {
    border: 1px solid #ddd;
    color: #fff;
    background-color: #67c23a;
  }

  &.error {
    border: 1px solid #ddd;
    color: #fff;
    background-color: #f56c6c;
  }
}
</style>