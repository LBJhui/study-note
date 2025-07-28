/**
 * loader就是一个函数
 * 当 webpack 解析资源时，会调用相应的loader 去处理
 * loader 接收到文件内容作为参数，返回内容出去
 * content 文件内容
 * map Sourcemap
 * meta 别的 loader 传递的数据
 */

module.exports = function (content) {
  console.log('%c 🍉 content', 'font-size:16px;color:#7f2b82', content)
  return content
}
