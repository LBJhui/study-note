/**
 * 1. webpack 加载 webpack.config.js 中所有配置，此时就会 new TestPlugin()，执行插件的 constructor
 * 2. webpack 创建 compiler 对象
 * 3. 遍历所有 plugins 中插件，调用插件的 apply 方法
 * 4. 执行剩下编译流程（触发各个 hooks 事件）
 */

class TestPlugin {
  constructor() {
    console.log('TestPlugin constructor')
  }
  apply(compiler) {
    debugger
    console.log('TestPlugin apply')

    // 由文档可知，environment 是同步钩子，所以需要使用 tap 注册
    compiler.hooks.environment.tap('TestPlugin', () => {
      console.log('TestPlugin environment')
    })

    // emit 是异步串行钩子
    compiler.hooks.emit.tap('TestPlugin', (compilation) => {
      console.log('TestPlugin emit')
    })

    compiler.hooks.emit.tapAsync('TestPlugin', (compilation, callback) => {
      setTimeout(() => {
        console.log('TestPlugin emit tapAsync')
        callback()
      }, 2000)
    })
    compiler.hooks.emit.tapPromise('TestPlugin', (compilation) => {
      return new Promise((resolve) => {
        setTimeout(() => {
          console.log('TestPlugin emit tapPromise')
          resolve()
        }, 1000)
      })
    })

    // make 是异步并行钩子
    compiler.hooks.make.tapAsync('TestPlugin', (compilation, callback) => {
      // 需要在 compilation hooks 触发前注册才能使用
      compilation.hooks.seal.tap('TestPlugin', (compilation) => {
        console.log('TestPlugin seal tapAsync')
      })
      setTimeout(() => {
        console.log('TestPlugin make tapAsync 1')
        callback()
      }, 3000)
    })
    compiler.hooks.make.tapAsync('TestPlugin', (compilation, callback) => {
      setTimeout(() => {
        console.log('TestPlugin make tapAsync 2')
        callback()
      }, 1000)
    })
    compiler.hooks.make.tapAsync('TestPlugin', (compilation, callback) => {
      setTimeout(() => {
        console.log('TestPlugin make tapAsync 3')
        callback()
      }, 2000)
    })
  }
}

module.exports = TestPlugin
