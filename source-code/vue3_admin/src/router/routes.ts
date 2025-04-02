import { RouteRecordRaw } from 'vue-router'

const constantRouter: RouteRecordRaw[] = [
  {
    path: '/',
    fullPath: '/dashboard',
    redirect: '/dashboard',
    title: '首页',
    keepalive: true,
  },
  {
    path: '/communication',
    fullPath: '/communication',
    component: () => import('@/views/communication/06_ref-children-parent/RefChildrenParentTest.vue'),
    title: 'Vue组件通信',
    isNav: false,
    icon: 'House',
    keepalive: true,
  },
  {
    path: '/dashboard',
    fullPath: '/dashboard',
    component: () => import('@/views/dashboard/index.vue'),
    title: '首页',
    isNav: false,
    icon: 'House',
    keepalive: true,
  },
  {
    path: '/login',
    fullPath: '/login',
    component: () => import('@/views/login/index.vue'),
    title: '登录',
    isNav: false,
    keepalive: true,
  },
  {
    path: '/slot',
    fullPath: '/slot',
    component: () => import('@/views/slot/index.vue'),
    title: 'vue插槽的实现原理',
    isNav: false,
    keepalive: true,
  },
  {
    path: '/uploadFile',
    fullPath: '/uploadFile',
    component: () => import('@/views/uploadFile/index.vue'),
    title: '文件上传',
    isNav: false,
    keepalive: true,
  },
  {
    path: '/ta',
    fullPath: '/ta',
    title: '直销与TA',
    isNav: true,
    icon: 'tuoguanhutazhilinghuakuan',
    keepalive: true,
    children: [
      {
        path: 'transactionApplication',
        fullPath: '/ta/transactionApplication',
        title: '直销交易申请管理',
        keepalive: true,
        children: [
          {
            path: 'redeem',
            fullPath: '/ta/transactionApplication/redeem',
            title: '赎回申请',
            component: () => import('@/views/TA/transactionApplication/redeem/index.vue'),
            keepalive: true,
          },
        ],
      },
      {
        path: 'statistics',
        fullPath: '/ta/statistics',
        title: '直销统计查询',
        keepalive: true,
        children: [
          {
            path: 'apply',
            fullPath: '/ta/statistics/apply',
            title: '直销交易申请查询',
            component: () => import('@/views/TA/statistics/apply/index.vue'),
            keepalive: true,
          },
          {
            path: 'confirm',
            fullPath: '/ta/statistics/confirm',
            title: '直销交易确认查询',
            component: () => import('@/views/TA/statistics/confirm/index.vue'),
            keepalive: true,
          },
        ],
      },
    ],
  },
]

export default constantRouter

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
