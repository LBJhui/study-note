import type { App } from 'vue'
import LLink from './L-Link/index.vue'
import LInput from './L-Input/index.vue'

export const setupLUIGlobComp = (app: App<Element>) => {
  app.component('LLink', LLink)
  app.component('LInput', LInput)
}
