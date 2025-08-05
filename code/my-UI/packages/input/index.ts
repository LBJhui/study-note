import tInput from './index.vue'


tInput.install = (app: any) => {
  app.component(tInput.name, tInput)
}

export default tInput