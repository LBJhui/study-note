module.exports = function (content, map, meta) {
  console.log('nomral loader 3')
  return content
}

module.exports.pitch = function () {
  console.log('pitch loader 3')
}
