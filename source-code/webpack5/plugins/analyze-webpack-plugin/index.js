class AnalyzeWebpackPlugin {
  apply(compiler) {
    compiler.hooks.emit.tap('AnalyzeWebpackPlugin', (compilation) => {
      // 1. 遍历所有即将输出文件，得到其大小
      const assets = Object.entries(compilation.assets)
      let content = `|资源名称|资源大小|
|:-:|:-:|`

      assets.forEach(([filename, value]) => {
        content += `\n|${filename}|${value.size() / 1024}kb|`
      })
      // 2. 生成一个 md 文件
      compilation.assets['analyze.md'] = {
        size() {
          return content.length
        },
        source() {
          return content
        }
      }
    })
  }
}

module.exports = AnalyzeWebpackPlugin
