const schema = {
  type: 'object',
  properties: {
    author: {
      type: 'string'
    }
  },
  additonalProperties: false
}

module.exports = function (content) {
  // schema 对 options 的验证规则
  // schema 符合 JSON Schema 规范
  const options = this.getOptions(schema)
  const prefix = `
  /**
   * Author: ${options.author}
   * Date: ${new Date().toLocaleDateString()}
   */
  `

  return prefix + content
}
