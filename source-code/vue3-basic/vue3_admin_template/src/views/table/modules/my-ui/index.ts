import MyTable from './MyTable/index'

const components = {
  MyTable,
}

export default {
  install(app) {
    for (const c in components) {
      app.component(c, components[c])
    }
  },
}
