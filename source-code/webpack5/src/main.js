// 入口文件
// js 文件后缀名可以不写
import count from './js/count'
import sum from './js/sum'

// 想要 webpack 打包资源，必须引入该资源

import './css/index.css'
import './less/index.less'
import './sass/index.scss'
import './css/iconfont.css'

console.log(count(2, 1))
console.log(sum(1, 2, 3, 4))

if (module.hot) {
  // 是否支持 HMR 功能
  module.hot.accept('./js/count.js', function () {
    console.log('count.js 发生了变化')
  })
}
