module.exports = function (content) {
  console.log('clean log loader')
  // 清除文件内容中 console.log(xxx)
  return content.replace(/console\.log\(.*\);?/g, '')
}
