import type { App } from 'vue'

import MySelect from './index.vue'

export default {
  install(app: App) {
    app.component('my-select', MySelect)
  }
}