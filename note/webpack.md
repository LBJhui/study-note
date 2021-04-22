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

  /******/ 	// The module cache 先定义一个缓存
  var __webpack_module_cache__ = {}

  // The require function 配置了 实现了require
  function __webpack_require__ (moduleId) {
    // Check if module is in cache
    if (__webpack_module_cache__[moduleId]) { // 不在缓存中...
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



## 修改`webpack.config.my.js` 文件名

Package.json

```json
"scripts":{
	 "build": "webpack --config webpack.config.my.js"
},
```

## html 插件



## 样式处理



## 转化 es6 语法



## 处理 js 语法及校验



## 全局变量引入问题



## 图片处理



## 打包文件分类



## 打包多页应用



## 配置 source-map



## watch的用法



## wepack 跨域问题



## resolve 属性的配置



## 定义环境变量



## 区分不同环境



## noParse



## IgnorePlugin



## 

