import Button from './Button'
import Input from './Input'

const MyUI = {}
const MyButton = {}
const MyInput = {}

MyButton.install = (Vue) => {
  Vue.component(Button.name, Button)
}

MyInput.install = (Vue) => {
  Vue.component(Input.name, Input)
}

export { MyButton, MyInput }

const COMPONENTS = [Button, Input]

MyUI.install = function (Vue, options) {
  if (options && options.components) {
    const components = options.components
    components.forEach((componentName) => {
      COMPONENTS.forEach((component) => {
        if (componentName === component.name) {
          Vue.component(component.name, component)
        }
      })
    })
  } else {
    COMPONENTS.forEach((component) => {
      Vue.component(component.name, component)
    })
  }
}

export default MyUI
