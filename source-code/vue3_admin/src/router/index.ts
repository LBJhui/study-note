import { createRouter, createWebHashHistory } from 'vue-router'
import routes from './routes'
import { settingStore } from '@/store'
import { isLogin } from '@/utils/index'

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const setting = settingStore()
  const hidden = to.meta.hidden as boolean

  if (to.fullPath === '/login' || isLogin()) {
    setting.setHidden(hidden)
    next()
  }
  next('/login')
})

export default router
