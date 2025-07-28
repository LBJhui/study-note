module.exports = function (content, map, meta) {
  const callback = this.async() // 异步 loader
  setTimeout(() => {
    console.log('test2')
    callback(null, content, map, meta)
  }, 1000)
}
