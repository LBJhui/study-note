const babel = require('@babel/core')

const schema = {
  type: 'object',
  properties: {
    presets: {
      type: 'array'
    }
  },
  additionalProperties: true
}

module.exports = function (content) {
  const callback = this.async()
  const options = this.getOptions(schema)

  // 使用 babel 对代码进行编译
  babel.transform(content, options, function (err, result) {
    if (err) callback(err)
    else callback(null, result.code)
  })
}
