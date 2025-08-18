import { Directive } from 'vue'

const vClickOutside: Directive = {
  mounted(el, binding, vnode) {
    console.log('%c 🌶 el', 'font-size:16px;color:#4fff4B', el)
    console.log('%c 🍖 binding', 'font-size:16px;color:#e41a6a', binding)
    console.log('%c 🍡 vnode', 'font-size:16px;color:#6ec1c2', vnode)

    let handle = (e: Event) => {
      if (el.contains(e.target)) {
        // binding?.instance?.handleFocus()
        console.log('包含')
      } else {
        console.log('不包含')
        // binding?.instance?.handleBlur()
      }
    }
    el.handle = handle
    document.addEventListener('click', handle)
  },
  unmounted(el) {
    document.addEventListener('click', el.handle)
  },
}

export default vClickOutside
