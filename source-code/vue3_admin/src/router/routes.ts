import type { RouteRecordRaw } from 'vue-router'
const constantRouter: RouteRecordRaw[] = [
  {
    path: '/dashboard',
    component: () => import('@/views/dashboard/index.vue'),
    meta: {
      title: '首页',
      hidden: false,
      icon: 'House',
    },
  },
  {
    path: '/login',
    component: () => import('@/views/login/index.vue'),
    meta: {
      title: '登录',
      hidden: true,
    },
  },
  {
    path: '/slot',
    component: () => import('@/views/slot/index.vue'),
    meta: {
      title: 'vue插槽的实现原理',
      hidden: false,
    },
  },
]

const asyncRouter = [
  {
    path: '/manage',
    redirect: '/manage/user',
    meta: {
      title: '权限管理',
      hidden: false,
      icon: 'Lock',
    },
    children: [
      {
        path: 'user',
        component: () => import('@/views/manage/user/index.vue'),
        meta: {
          title: '用户管理',
          hidden: false,
          icon: 'User',
        },
      },
      {
        path: 'role',
        component: () => import('@/views/manage/role/index.vue'),
        meta: {
          title: '角色管理',
          hidden: false,
          icon: 'UserFilled',
        },
      },
    ],
  },
]

const routes = [
  {
    path: '/',
    redirect: '/dashboard',
    meta: {
      title: '首页',
      hidden: true,
    },
  },
  ...constantRouter,
  ...asyncRouter,
]

export default routes
