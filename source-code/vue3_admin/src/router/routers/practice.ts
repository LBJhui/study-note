import { RouteRecordRaw } from 'vue-router'

const practice: RouteRecordRaw = {
  path: '/practice',
  meta: {
    fullPath: '/practice',
    title: '练习',
    isNav: true,
    icon: 'practice',
    keepalive: true,
  },
  children: [
    {
      path: 'work',
      meta: {
        fullPath: '/practice/work',
        title: 'work',
        keepalive: true,
        isNav: true,
      },
      children: [],
    },
  ],
}

export default practice
