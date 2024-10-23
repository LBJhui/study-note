<template>
  <div>
    111
    <svg-icon name="phone" color="red" width="100px" height="100px"></svg-icon>
  </div>
</template>

<script setup lang="ts">
import request from '@/utils/request'

request({
  url: '/user/login',
  method: 'post',
  data: {
    username: 'admin',
    password: '111111',
  },
})
</script>

<style scoped lang="scss">
div {
  color: $color;
}
</style>
