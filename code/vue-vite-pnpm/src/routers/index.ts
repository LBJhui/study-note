import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  { path: '/', component: () => import('@/views/responsive/index.vue') },
  { path: '/todoList', component: () => import('@/views/todoList/index.vue') },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
