<template>
  <div id="app">
    <!-- 左侧导航栏 -->
    <div class="left-nav">
      <div class="logo-container">
        <img src="/logo.svg" />
        <span>LBJ辉Vue3后台管理项目</span>
      </div>
      <el-menu background-color="#001529" active-text-color="yellowgreen" class="el-menu-vertical-demo" default-active="2" text-color="#fff" @open="handleOpen" @close="handleClose">
        <el-sub-menu index="1">
          <template #title>
            <el-icon><location /></el-icon>
            <span>Navigator One</span>
          </template>
          <el-menu-item-group title="Group One">
            <el-menu-item index="1-1">item one</el-menu-item>
            <el-menu-item index="1-2">item two</el-menu-item>
          </el-menu-item-group>
          <el-menu-item-group title="Group Two">
            <el-menu-item index="1-3">item three</el-menu-item>
          </el-menu-item-group>
          <el-sub-menu index="1-4">
            <template #title>item four</template>
            <el-menu-item index="1-4-1">item one</el-menu-item>
          </el-sub-menu>
        </el-sub-menu>
        <el-menu-item index="2">
          <el-icon><icon-menu /></el-icon>
          <span>Navigator Two</span>
        </el-menu-item>
        <el-menu-item index="3" disabled>
          <el-icon><document /></el-icon>
          <span>Navigator Three</span>
        </el-menu-item>
        <el-menu-item index="4">
          <el-icon><setting /></el-icon>
          <span>Navigator Four</span>
        </el-menu-item>
      </el-menu>
    </div>
    <div class="right-container">
      <!-- 顶部导航栏 -->
      <div class="top-nav"></div>
      <!-- 内容区域 -->
      <div class="main-container">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped lang="scss">
#app {
  display: flex;
  .left-nav {
    width: $leftnavwidth;
    height: 100vh;
    background-color: #001529;
    .logo-container {
      width: 100%;
      line-height: 60px;
      color: #fff;
      display: flex;
      align-items: center;
      padding-left: 10px;
      img {
        width: 40px;
        margin-right: 5px;
      }
    }
  }
  .right-container {
    flex: 1;
    .top-nav {
      width: 100%;
      height: $topNavHeight;
      background-color: aquamarine;
    }

    .main-container {
      width: 100%;
      height: calc(100vh - $topNavHeight);
      background-color: blanchedalmond;
    }
  }
}
</style>
