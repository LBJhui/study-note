/**
 * 写法一
 */

// module.exports = function (content, map, meta) {
//   console.log(content)
//   return content
// }

// // raw loader
// module.exports.raw = true // 告诉 webpack 这个 loader 不需要处理二进制数据

/**
 * 写法二
 */

function test3Loader(content) {
  console.log('test3 loader')
  console.log(content)
  return content
}

test3Loader.raw = true // 告诉 webpack 这个 loader 不需要处理二进制数据

module.exports = test3Loader
