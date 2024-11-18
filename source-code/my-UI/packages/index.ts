import tButton from './button'
import tInput from './input'

const install = (app: any) => {
  app.use(tButton)
  app.use(tInput)
}

const TUI = {
  install,
}

export { tButton, tInput }

export default TUI
