import { createRouter, createWebHashHistory } from 'vue-router'
import routes from './routes'

const route = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default route
