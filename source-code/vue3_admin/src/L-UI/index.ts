import type { App } from 'vue'
import LLink from './L-Link/index.vue'


export const setupLUIGlobComp = (app: App<Element>) => {
  app.component('LLink', LLink)
}
