module.exports = function (content, map, meta) {
  console.log('nomral loader 2')
  return content
}

module.exports.pitch = function () {
  console.log('pitch loader 2')
  return 'result'
}
