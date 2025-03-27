import { RouteRecordRaw } from 'vue-router'

const constantRouter: RouteRecordRaw[] = [
  {
    path: '/dashboard',
    component: () => import('@/views/dashboard/index.vue'),
    title: '首页',
    isNav: false,
    icon: 'House',
  },
  {
    path: '/login',
    component: () => import('@/views/login/index.vue'),
    title: '登录',
    isNav: false,
  },
  {
    path: '/slot',
    component: () => import('@/views/slot/index.vue'),
    title: 'vue插槽的实现原理',
    isNav: false,
  },
  {
    path: '/uploadFile',
    component: () => import('@/views/uploadFile/index.vue'),
    title: '文件上传',
    isNav: false,
  },
  {
    path: '/ta',
    title: '直销与TA',
    isNav: true,
    icon: 'tuoguanhutazhilinghuakuan',
    children: [
      {
        path: 'transactionApplication',
        title: '直销交易申请管理',
        children: [
          {
            path: 'redeem',
            title: '赎回申请',
            component: () => import('@/views/TA/transactionApplication/redeem/index.vue'),
          },
        ],
      },
      {
        path: 'statistics',
        title: '直销统计查询',
        children: [
          {
            path: 'apply',
            title: '直销交易申请查询',
            component: () => import('@/views/TA/statistics/apply/index.vue'),
          },
          {
            path: 'confirm',
            title: '直销交易确认查询',
            component: () => import('@/views/TA/statistics/confirm/index.vue'),
          },
        ],
      },
    ],
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
  // ...asyncRouter,
]

export default routes

// const menuListVertical = [
//   {
//     title: '产品周期',
//     icon: 'chanpinzhouqi',
//   },
//   {
//     title: '转账划款',
//     icon: 'transaction',
//   },
//   {
//     title: '估值核算',
//     icon: 'guzhihesuan',
//   },
//   {
//     title: '税费中心',
//     icon: 'shuifeizhongxin',
//   },
//   {
//     title: '信息披露',
//     icon: 'xinxipilou',
//   },
//   {
//     title: '绩效分析',
//     icon: 'jixiao',
//   },
//   {
//     title: '综合管理',
//     icon: 'zongheguanli',
//   },
//   {
//     title: '系统管理',
//     icon: 'xitongguanli',
//   },
// ]
