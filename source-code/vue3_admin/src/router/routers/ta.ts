import { RouteRecordRaw } from 'vue-router'

const ta: RouteRecordRaw = {
  path: '/ta',
  meta: {
    fullPath: '/ta',
    title: '直销与TA',
    isNav: true,
    icon: 'tuoguanhutazhilinghuakuan',
    keepalive: true,
  },
  children: [
    {
      path: 'transactionApplication',
      meta: {
        fullPath: '/ta/transactionApplication',
        title: '直销交易申请管理',
        keepalive: true,
        isNav: true,
      },
      children: [
        {
          path: 'redeem',
          component: () => import('@/views/TA/transactionApplication/redeem/index.vue'),
          meta: {
            fullPath: '/ta/transactionApplication/redeem',
            title: '赎回申请',
            keepalive: true,
            isNav: true,
          },
        },
      ],
    },
    {
      path: 'statistics',
      meta: {
        fullPath: '/ta/statistics',
        title: '直销统计查询',
        keepalive: true,
        isNav: true,
      },
      children: [
        {
          path: 'apply',
          component: () => import('@/views/TA/statistics/apply/index.vue'),
          meta: {
            fullPath: '/ta/statistics/apply',
            title: '直销交易申请查询',
            keepalive: true,
            isNav: true,
          },
        },
        {
          path: 'confirm',
          component: () => import('@/views/TA/statistics/confirm/index.vue'),
          meta: {
            fullPath: '/ta/statistics/confirm',
            title: '直销交易确认查询',
            keepalive: true,
            isNav: true,
          },
        },
      ],
    },
  ],
}

export default ta
