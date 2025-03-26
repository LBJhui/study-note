import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import pinia from '@/store'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
//@ts-ignore忽略当前文件ts类型的检测否则有红色提示(打包会失败)
import zhCn from 'element-plus/dist/locale/zh-cn.mjs'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
//svg插件需要配置代码
import 'virtual:svg-icons-register'
import gloablComponent from './components/index'
import '@/styles/index.scss'
import '@/assets/iconfont/iconfont.css'
import router from '@/router'
const app = createApp(App)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}
app.use(ElementPlus, {
  locale: zhCn,
})
//注册模板路由
app.use(router)
app.use(pinia)
app.use(gloablComponent)
app.mount('#app')
