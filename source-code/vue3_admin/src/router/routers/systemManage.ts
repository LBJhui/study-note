import { RouteRecordRaw } from 'vue-router'

const systemManage: RouteRecordRaw = {
  path: '/systemManage',
  meta: {
    fullPath: '/systemManage',
    title: '系统管理',
    isNav: true,
    icon: 'xitongguanli',
    keepalive: true,
  },
  children: [
    {
      path: 'administrators',
      meta: {
        fullPath: '/systemManage/administrators',
        title: '管理人用户',
        keepalive: true,
        isNav: true,
      },
      children: [
        {
          path: 'user',
          meta: {
            fullPath: '/systemManage/administrators/user',
            title: '用户管理',
            keepalive: true,
            isNav: true,
          },
          component: () => import('@/views/systemManage/administrators/user/index.vue'),
        },
        {
          path: 'productAuthorization',
          meta: {
            fullPath: '/systemManage/administrators/productAuthorization',
            title: '产品授权',
            keepalive: true,
            isNav: true,
          },
          component: () => import('@/views/systemManage/administrators/productAuthorization/index.vue'),
        },
        {
          path: 'role',
          meta: {
            fullPath: '/systemManage/administrators/role',
            title: '角色管理',
            keepalive: true,
            isNav: true,
          },
          component: () => import('@/views/systemManage/administrators/role/index.vue'),
        },
      ],
    },
  ],
}

export default systemManage
