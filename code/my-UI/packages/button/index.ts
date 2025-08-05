import  tButton from './index.vue'


tButton.install = (app:any) => {
  app.component(tButton.name, tButton)
}

export default tButton