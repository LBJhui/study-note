<template>
  <div id="app">
    <template v-if="menuMode === HORIZONTAL">
      <template v-if="!hiddenMenu">
        <div class="horizontal-container">
          <!-- 左侧导航栏 -->
          <div class="left-nav">
            <div class="logo-container">
              <img src="/logo.svg" />
              <span>LBJ辉Vue3后台管理项目</span>
            </div>
            <el-menu background-color="#001529" class="menu-container" active-text-color="yellowgreen" text-color="#fff" :router="true">
              <template v-for="item in menuList" :key="item.path">
                <el-menu-item :index="item.path" v-if="!item.children && !item?.meta?.hidden">
                  <template #title>
                    <el-icon><House /></el-icon>
                    <span>{{ item?.meta?.title }}</span>
                  </template>
                </el-menu-item>
                <el-sub-menu :index="item.path" v-if="item.children && !item?.meta?.hidden">
                  <template #title>
                    <el-icon>
                      <component :is="item?.meta?.icon"></component>
                    </el-icon>
                    <span>{{ item?.meta?.title }}</span>
                  </template>
                  <el-menu-item v-for="child in item.children" :index="item.path + '/' + child.path" :key="child.path">
                    <template #title>
                      <el-icon>
                        <component :is="child?.meta?.icon"></component>
                      </el-icon>
                      <span>{{ child?.meta?.title }}</span>
                    </template>
                  </el-menu-item>
                </el-sub-menu>
              </template>
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
      <template v-else> <router-view></router-view> </template>
    </template>
    <template v-if="menuMode === VERTICAL">
      <VerticalNav> </VerticalNav>
    </template>
  </div>
</template>

<script setup lang="ts">
import { HORIZONTAL, VERTICAL, menuMode } from '@/settings'
import VerticalNav from '@/components/VerticalNav/index.vue'
</script>

<style scoped lang="scss">
#app {
  width: 100vw;
  height: 100vh;
  min-width: 1250px;
  overflow: hidden;
  font-family:
    PingFangSC,
    PingFang SC;
  font-weight: 400;
  font-style: normal;

  .horizontal-container {
    display: flex;
    .left-nav {
      width: $leftNavwidth;
      height: 100vh;
      background-color: #001529;

      .logo-container {
        width: 100%;
        line-height: $logoHeight;
        color: #fff;
        display: flex;
        align-items: center;
        padding-left: 10px;
        border-bottom: 1px solid #333;

        img {
          width: 40px;
          margin-right: 5px;
        }
      }

      .menu-container {
        width: 100%;
        height: calc(100vh - $logoHeight);
        border: none;
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
}
</style>
