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
          <div class="nav-container" @mouseleave="closeSubMenu">
            <template v-for="item in menuList" :key="item.path">
              <div class="nav-item" @mouseenter="openSubMenu(item)" :class="{ active: state.activeMenu.title === item.title }" v-if="item?.isNav">
                <div class="nav-item-inset">
                  <div class="icon-container">
                    <span :class="`iconfont icon-${item?.icon}`"></span>
                  </div>
                  <div class="title">{{ item.title }}</div>
                </div>
              </div>
            </template>

            <div class="sub-nav-container" v-if="state.showSubMenu">
              <div class="title-container">
                <span :class="`iconfont icon-${state.activeMenu.icon}`"></span>
                {{ state.activeMenu.title }}</div
              >
              <div class="sub-nav-main-container" v-if="state.activeMenu.children">
                <div class="sub-nav-item-container" v-for="child in state.activeMenu.children">
                  <div class="sub-nav-item-title">{{ child.title }}</div>
                  <div class="sub-nav-item" v-for="navItem in child.children" @click="goToPage(navItem)">{{ navItem.title }} </div>
                </div>
              </div>
            </div>
          </div>
          <div class="avatar">
            <img src="@/assets/images/bg.png" alt="" />
          </div>
        </div>

        <div class="history-container" v-if="state.historyRouter.length !== 0">
          <div
            class="history-tab-item"
            :class="{ active: state.activeRouter.fullPath === item.fullPath }"
            v-for="(item, index) in state.historyRouter"
            :key="item.fullPath"
            @click.self="goToPage(item)"
            >{{ item.title }}<span v-if="item.title !== DASHBOARD" class="iconfont icon-close" @click="closeHistoryTab(index)"></span
          ></div>

          <div class="history-tab-item active close-all" @click="closeAll">关闭全部</div>
        </div>

        <div class="main-container">
          <div class="title-container" v-if="isNotDashBoard"> {{ state.activeRouter.title }} </div>
          <router-view> </router-view>
        </div>
      </div>
    </template>
  </div>
</template>

<script setup lang="ts">
import vResize from '@/directs/sizeDirect'
import { HORIZONTAL, VERTICAL, menuMode } from '@/settings'
import { ref, reactive, computed } from 'vue'
import { useRouter, RouteRecordRaw } from 'vue-router'
import routes from '@/router/routes'

const router = useRouter()
const hiddenMenu = ref(false)
const DASHBOARD = '首页'

const isNotDashBoard = computed(() => {
  return state.activeRouter.title !== DASHBOARD
})

router.afterEach((to) => {
  hiddenMenu.value = to.meta.hidden as boolean
})

const resize = (value: any) => {
  console.log(value)
}

const menuList = routes as RouteRecordRaw[]

const state = reactive({
  showSubMenu: false,
  activeMenu: {} as RouteRecordRaw,
  historyRouter: [] as RouteRecordRaw[],
  activeRouter: {} as RouteRecordRaw,
})
const openSubMenu = (item: RouteRecordRaw) => {
  state.activeMenu = item
  state.showSubMenu = true
}

const closeSubMenu = () => {
  state.showSubMenu = false
  state.activeMenu = {} as RouteRecordRaw
}

const goToPage = (navItem: RouteRecordRaw) => {
  if (navItem.title !== DASHBOARD && !state.historyRouter.find((item) => item.fullPath === navItem.fullPath)) {
    if (state.historyRouter.length === 0) {
      state.historyRouter.push(menuList[0])
    }
    state.historyRouter.push(navItem)
  }
  state.activeRouter = navItem
  closeSubMenu()
  router.push(navItem.fullPath)
}

const goToDashBoard = () => {
  goToPage(menuList[0])
}
const closeHistoryTab = (index: number) => {
  state.historyRouter.splice(index, 1)
  if (state.historyRouter.length === 1) {
    state.historyRouter = []
    goToDashBoard()
  }
  const newIndex = state.historyRouter[index] ? index : index - 1
  state.activeRouter = state.historyRouter[newIndex]
  goToPage(state.activeRouter)
}

const closeAll = () => {
  state.activeRouter = {} as RouteRecordRaw
  state.historyRouter = []
  goToDashBoard()
}
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
    position: relative;
    .top-nav {
      display: flex;
      background-color: $verticalTopNavColor;
      height: $verticalTopNavHeight;
      .logo-container {
        width: 365px;
      }
      .nav-container {
        display: flex;
        flex: 1;
        z-index: 10;
        .nav-item {
          padding: 8px;
          width: 80px;
          height: 100%;
          color: #fff;

          .nav-item-inset {
            display: flex;
            flex-direction: column;
            align-items: center;
            .icon-container {
              margin: 7px auto 8px;
              .iconfont {
                font-size: 24px;
              }
            }
            .title {
              font-size: 14px;
              line-height: 22px;
            }
          }
        }

        .active {
          background-color: #5870cb;
        }

        .sub-nav-container {
          position: absolute;
          top: $verticalTopNavHeight;
          left: 0;
          width: 100%;
          height: 50vh;
          background: rgb(248, 249, 251);
          box-shadow: 0 8px 16px 0 rgba(28, 50, 122, 0.15);
          display: flex;

          .title-container {
            width: 175px;
            height: 100%;
            background: #ffffff;
            background-image: url(@/assets/images/menu_h1_bg.png);
            background-repeat: no-repeat;
            background-size: 100%;
            background-position: bottom;
            padding-top: 27px;
            position: relative;
            font-size: 18px;
            font-family:
              PingFangSC-Semibold,
              PingFang SC;
            font-weight: 600;
            color: #313836;
            padding-left: 32px;
            span {
              width: 28px;
              height: 28px;
              color: #fff;
              display: inline-block;
              background: #5870cb;
              border-radius: 4px;
              text-align: center;
              line-height: 28px;
              font-weight: 400;
            }
          }

          .sub-nav-main-container {
            display: flex;
            flex: 1;
            padding-bottom: 5px;
            .sub-nav-item-container {
              margin-left: 40px;
              .sub-nav-item-title {
                padding-top: 25px;
                padding-bottom: 12px;
                border-bottom: 1px solid #e5e7ec;
                font-size: 16px;
                font-weight: 600;
                color: #5870cb;
              }

              .sub-nav-item {
                padding: 6px 0;
                font-size: 14px;
                color: #313836;
                cursor: pointer;
                line-height: 20px;
                &:hover {
                  font-weight: 600;
                  color: #5870cb;
                }
                &:nth-child(2) {
                  margin-top: 10px;
                }
              }
            }
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
      background-color: $verticalTopNavColor;
      display: flex;
      line-height: $verticalhistoryheight;
      position: relative;
      .history-tab-item {
        font-size: 14px;
        text-align: center;
        padding: 0 10px 0 12px;
        color: #fff;
        background-color: #2a4090;
        border-radius: 4px 4px 0 0;
        box-sizing: border-box;
        cursor: pointer;
        .iconfont {
          font-size: 10px;
          margin-left: 8px;
        }
      }
      .history-tab-item.active {
        color: #313836;
        background-color: #fff;
      }

      .close-all {
        position: absolute;
        right: 0;
        bottom: 0;
      }
    }

    .main-container {
      height: calc(100vh - $verticalTopNavHeight);
      overflow: auto;
    }
  }

  .main-container::-webkit-scrollbar {
    width: 0;
  }
}
</style>
