import { createApp } from 'vue'
import App from './App.vue'
//引入路由
import router from './router'
//引入仓库
import pinia from './store'

import ElementPlus from 'element-plus'
import zhCn from 'element-plus/es/locale/lang/zh-cn'
import 'element-plus/dist/index.css'

//引入模板的全局的样式
import '@/styles/index.scss'

//引入自定义插件对象:注册整个项目全局组件
import gloablComponent from './components/index'
//svg插件需要配置代码
import 'virtual:svg-icons-register'

const app = createApp(App)

app.use(ElementPlus, {
  locale: zhCn,
})

// import SvgIcon from '@/components/SvgIcon/index.vue'
// app.component('svg-icon', SvgIcon)

// 利用自定义插件注册
app.use(gloablComponent)

app.use(router)
//安装仓库
app.use(pinia)

app.mount('#app')
