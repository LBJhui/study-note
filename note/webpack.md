## webpack安装

- 安装本地的webpack
- webpack    webpack-cli  -D



## webpack 可以进行0配置

- 打包工具 ➡️ 输出后的结果 ( js 模块 ) 
- 打包 ( 支持我们的 js 的模块 )



## 手动配置 webpack

- 默认配置文件的名字是 wepack.config.js

```javascript
// webpack 是 node 写出来的 node 的写法
const path = require('path')

module.exports = {
  mode: 'development', // 模式  默认两种 production development
  entry: './src/index.js', // 入口
  output: {
    filename: 'bundle.js', // 打包后的文件名
    path: path.resolve(__dirname, 'dist') // 路径必须是一个绝对路径
  }
}
```



## webpack 打包出来的文件解析

```javascript
(() => { // webpackBootstrap
  var __webpack_modules__ = ({

    './src/a.js':

() => {
  eval("console.log('LBJhui')\n\n//# sourceURL=webpack://webpack/./src/a.js?")
},

    './src/index.js':

(__unused_webpack_module, __unused_webpack_exports, __webpack_require__) => {
  eval('let str = __webpack_require__(/*! ./a.js */ "./src/a.js")\n\n//# sourceURL=webpack://webpack/./src/index.js?')
}

  })

  /******/ 	// The module cache
  var __webpack_module_cache__ = {}

  // The require function
  function __webpack_require__ (moduleId) {
    // Check if module is in cache
    if (__webpack_module_cache__[moduleId]) {
      return __webpack_module_cache__[moduleId].exports
    }
    // Create a new module (and put it into the cache)
    var module = __webpack_module_cache__[moduleId] = {
      // no module.id needed
      // no module.loaded needed
      exports: {}
    }

    // Execute the module function
    __webpack_modules__[moduleId](module, module.exports, __webpack_require__)

    // Return the exports of the module
    return module.exports
  }

  // startup
  // Load entry module and return exports
  // This entry module can't be inlined because the eval devtool is used.
  var __webpack_exports__ = __webpack_require__('./src/index.js')
})()
```

