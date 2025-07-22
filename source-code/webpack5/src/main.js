// 入口文件
// js 文件后缀名可以不写
import count from './js/count'

// 想要 webpack 打包资源，必须引入该资源

import './css/index.css'
import './less/index.less'
import './sass/index.scss'
import './css/iconfont.css'

console.log(count(2, 1))

document.getElementById('btn').onclick = function () {
  // 动态导入 --> 实现按需加载
  // 即使只被引用了一次，也会代码分割
  // webpackChunkName: "sum"：这是webpack动态导入模块命名的方式
  // "sum"将来就会作为[name]的值显示。
  import(/* webpackChunkName: "sum" */ './js/sum').then(({ sum }) => {
    console.log(sum(1, 2, 3, 4, 5))
  })
}

if (module.hot) {
  // 是否支持 HMR 功能
  module.hot.accept('./js/count.js', function () {
    console.log('count.js 发生了变化')
  })
}

Promise.resolve(1)

if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker
      .register('/service-worker.js')
      .then((registration) => {
        console.log('SW registered: ', registration)
      })
      .catch((registrationError) => {
        console.log('SW registration failed: ', registrationError)
      })
  })
}
