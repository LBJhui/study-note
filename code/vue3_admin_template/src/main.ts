import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import zhCn from 'element-plus/es/locale/lang/zh-cn'
import App from './App.vue'

// svg 插件配置代码
import 'virtual:svg-icons-register'
//引入自定义插件对象:注册整个项目全局组件
import gloalComponent from '@/components'

//引入模板的全局的样式
import '@/styles/index.scss'

// 引入路由
import router from './router'

createApp(App)
  .use(router)
  .use(ElementPlus, {
    locale: zhCn,
  })
  .use(gloalComponent)
  .mount('#app')
