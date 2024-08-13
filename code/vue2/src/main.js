import Vue from 'vue'
import App from './App.vue'
import { MyButton, MyInput } from '../modules/my-ui'
// import MyUI from '../modules/my-ui'
import '../modules/my-ui/common.css'

// Vue.use(MyUI, {
//   components: ['MyButton', 'MyInput'],
// })

// 按需加载
Vue.use(MyButton)
Vue.use(MyInput)

Vue.config.productionTip = false

new Vue({
  render: (h) => h(App),
}).$mount('#app')
