<template>
  <div class="login-container">
    <div class="login-title">LBJ辉</div>
    <div class="login-form">
      <button @click="login">登录</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
const login = () => {
  localStorage.setItem('token', '1')
  router.push('/')
}
</script>

<style scoped lang="scss">
.login-container {
  width: 100%;
  height: 100vh;
  /* 此属性是一个 简写属性，可以在一次声明中定义一个或多个属性：background-clip、background-color、background-image、background-origin、background-position、background-repeat、background-size，和 background-attachment。 */
  background: url('@/assets/images/bg.png') no-repeat;
  background-size: cover;
  display: flex;
  .login-title {
    padding: 80px 60px;
    color: #fff;
    font-size: 50px;
    flex: 1;
  }
  .login-form {
    width: 400px;
    height: 400px;
    background-color: #fff;
    margin-right: 200px;
    border-radius: 10px;
    background-color: #fff;
    margin: 200px;
  }
}
</style>
