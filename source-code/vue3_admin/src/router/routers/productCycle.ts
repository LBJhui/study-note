import { RouteRecordRaw } from 'vue-router'

const productCycle: RouteRecordRaw = {
  path: '/productCycle',
  meta: {
    fullPath: '/productCycle',
    title: '产品周期',
    isNav: true,
    icon: 'chanpinzhouqi',
    keepalive: true,
  },
  children: [
    {
      path: 'contract',
      meta: {
        fullPath: '/productCycle/contract',
        title: '合同管理',
        isNav: true,
        keepalive: true,
      },
      children: [
        {
          path: 'draft',
          meta: {
            fullPath: '/productCycle/contract/draft',
            title: '定稿合同管理',
            isNav: true,
            keepalive: true,
          },
          component: () => import('@/views/productCycle/contract/draft/index.vue'),
        },
        {
          path: 'print',
          meta: {
            fullPath: '/productCycle/contract/print',
            title: '合同印刷管理',
            isNav: true,
            keepalive: true,
          },
          component: () => import('@/views/productCycle/contract/print/index.vue'),
        },
        {
          path: 'eContract',
          meta: {
            fullPath: '/productCycle/contract/eContract',
            title: '电子合同管理',
            isNav: true,
            keepalive: true,
          },
          component: () => import('@/views/productCycle/contract/eContract/index.vue'),
        },
        {
          path: 'eSignPlatform',
          meta: {
            fullPath: '/productCycle/contract/eSignPlatform',
            title: '电子签约平台',
            isNav: true,
            keepalive: true,
          },
          component: () => import('@/views/productCycle/contract/eSignPlatform/index.vue'),
        },
        {
          path: 'change',
          meta: {
            fullPath: '/productCycle/contract/change',
            title: '产品合同变更',
            isNav: true,
            keepalive: true,
          },
          component: () => import('@/views/productCycle/contract/change/index.vue'),
        },
      ],
    },
  ],
}

export default productCycle
