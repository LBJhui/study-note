import { createApp } from 'vue'

import ElementPlus from 'element-plus'
import zhCn from 'element-plus/es/locale/lang/zh-cn'
import 'element-plus/dist/index.css'

import gloablComponent from './components/index'
import 'virtual:svg-icons-register'

import App from './App.vue'

const app = createApp(App)

app.use(ElementPlus, {
  locale: zhCn,
})

// import SvgIcon from '@/components/SvgIcon/index.vue'
// app.component('svg-icon', SvgIcon)

// 利用自定义插件注册
app.use(gloablComponent)

app.mount('#app')
