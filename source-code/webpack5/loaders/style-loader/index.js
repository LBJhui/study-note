module.exports = function (content) {
  /**
   * 1. 直接使用 style-loader，只能处理样式，不能处理样式中引入的其他资源
   *
   * 2. 借助 css-loader 处理样式中的其他资源
   *
   * 问题是 css-loader 暴露了一段 js 代码，style-loader 需要执行 js 代码，得到返回值，再动态创建 style 标签，插入到页面中，不好操作
   *
   * 3. style-loader 使用 pitch loader 方法
   */
  // const script = `
  // const styleEl = document.createElement('style')
  // styleEl.innerHTML = ${JSON.stringify(content)}
  // document.head.appendChild(styleEl)
  // `
  // return script
}

module.exports.pitch = function (remainingRequest) {
  // remainingRequest 剩下还需要处理的 loader
  console.log('%c 🌰 remainingRequest', 'font-size:16px;color:#ed9ec7', remainingRequest)
  // D:\Desktop\study-note\source-code\webpack5\node_modules\.pnpm\css-loader@7.1.2_webpack@5.100.2\node_modules\css-loader\dist\cjs.js!D:\Desktop\study-note\source-code\webpack5\src\css\index.css
  // 1. 将 remainingRequest 中绝对路径改为相对路径
  const relativePath = remainingRequest
    .split('!')
    .map((absolutePath) => {
      return this.utils.contextify(this.context, absolutePath)
    })
    .join('!')

  // 2. 引入 css-loader 处理后的资源
  // 3. 创建 style 标签，将内容插入页面中生效
  const script = `
  import style from "!!${relativePath}"
  const styleEl = document.createElement('style')
  styleEl.innerHTML = style
  document.head.appendChild(styleEl)
  `
  return script
}
