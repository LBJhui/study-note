import { createRouter, createWebHashHistory } from 'vue-router'

const route = createRouter({
  history: createWebHashHistory(),
  routes: [
    // { path: '/', redirect: '/dashboard' },
    // { path: '/dashboard', component: () => import('@/views/dashboard/index.vue') },
    { path: '/login', component: () => import('@/views/login/index.vue') },
  ],
})

export default route
