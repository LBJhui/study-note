const HtmlWebpackPlugin = require('safe-require')('html-webpack-plugin')

class InlineChunkWebpackPlugin {
  constructor(tests) {
    this.tests = tests
  }

  apply(compiler) {
    compiler.hooks.compilation.tap('InlineChunkWebpackPlugin', (compilation) => {
      // 获取 html-webpack-plugin 的钩子
      const hooks = HtmlWebpackPlugin.getHooks(compilation)
      // 注册 html-webpack-plugin 的 hooks alterAssetTagGroups
      hooks.alterAssetTagGroups.tap('InlineChunkWebpackPlugin', (assets) => {
        // 从里面将 script 的 runtime 文件，变成 inline script
        assets.headTags = this.getInlineTag(assets.headTags, compilation.assets)
        assets.bodyTags = this.getInlineTag(assets.bodyTags, compilation.assets)
      })

      // 删除 rumtime 文件
      hooks.afterEmit.tap('InlineChunkHtmlPlugin', () => {
        Object.keys(compilation.assets).forEach((assetName) => {
          if (this.tests.some((test) => assetName.match(test))) {
            delete compilation.assets[assetName]
          }
        })
      })
    })
  }

  getInlineTag(tags, assets) {
    return tags.map((tag) => {
      if (tag.tagName !== 'script') return tag
      const scriptName = tag.attributes.src
      if (!this.tests.some((test) => scriptName.match(test))) return tag
      return { tagName: 'script', innerHTML: assets[scriptName].source(), closeTag: true }
    })
  }
}

module.exports = InlineChunkWebpackPlugin
