<template>
  <div v-resize="resize" id="app">
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
      <!-- 内容区域 -->
      <div class="vertical-container">
        <div class="top-nav">
          <div class="logo-container"></div>
          <div class="nav-container">
            <div class="nav-item">
              <div class="icon-container">
                <i class="iconfont icon-tuoguanhutazhilinghuakuan"></i>
              </div>
              <div class="title">TA交易</div>
            </div>
            <div class="nav-sub-container"></div>
          </div>
          <div class="avatar">
            <img src="@/assets/images/bg.png" alt="" />
          </div>
        </div>
        <div class="history-container"></div>
        <div class="main-container"> <router-view></router-view> </div
      ></div>
    </template>
  </div>
</template>

<script setup lang="ts">
import vResize from '@/directs/sizeDirect'
import { HORIZONTAL, VERTICAL, menuMode } from '@/settings'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import routes from '@/router/routes'

const router = useRouter()
const hiddenMenu = ref(false)

router.afterEach((to) => {
  hiddenMenu.value = to.meta.hidden as boolean
})

const resize = (value: any) => {
  console.log(value)
}

const menuList = routes
</script>

<style scoped lang="scss">
#app {
  width: 100vw;
  height: 100vh;
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

  .vertical-container {
    .top-nav {
      display: flex;
      background-color: $verticalTopNavColor;
      height: $verticalTopNavHeight;
      .logo-container {
        width: 365px;
      }
      .nav-container {
        flex: 1;

        .nav-item {
          display: flex;
          flex-direction: column;
          align-items: center;
          padding: 8px;
          width: 80px;
          height: 100%;
          color: #fff;
          .icon-container {
            width: 19px;
            height: 19px;
            margin: 7px auto 8px;
          }
          .title {
            font-size: 14px;
            line-height: 22px;
          }
        }
      }
      .avatar {
        width: 100px;
        height: 100%;
        padding: calc(($verticalTopNavHeight - 24px) / 2);
        img {
          width: 24px;
          height: 24px;
          border-radius: 50%;
        }
      }
    }

    .history-container {
      border-top: 1px solid #fff;
      height: $verticalhistoryheight;
      background-color: $verticalTopNavColor;
    }

    .main-container {
      background-color: navajowhite;
      height: calc(100vh - $verticalTopNavHeight);
      overflow: auto;
    }
  }

  .main-container::-webkit-scrollbar {
    width: 0;
  }
}
</style>
