import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

const history = createWebHistory()
const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect: '/index',
  },
  {
    path: '/index',
    name: 'index',
    component: () => import('../views/index/index.vue'),
  },
  {
    path: '/introduction',
    name: 'introduction',
    component: () => import('../views/index/index.vue'),
  },
]
const router = createRouter({
  history,
  routes,
})
export default router
