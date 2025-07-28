module.exports = function (content, map, meta) {
  console.log('nomral loader 1')
  return content
}

module.exports.pitch = function () {
  console.log('pitch loader 1')
}
