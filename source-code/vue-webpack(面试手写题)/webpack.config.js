const { resolve } = require('path')
const HTMLWebpackPlugin = require('html-webpack-plugin')

module.exports = {
  mode: 'development',
  entry: './src/main.js',
  output: {
    path: resolve(__dirname, 'dist'),
    filename: 'main.js',
  },
  resolveLoader: {
    modules: ['node_modules', resolve(__dirname, './modules')],
  },
  resolve: {
    extensions: ['.js', '.vue'],
  },
  module: {
    rules: [
      {
        test: /.vue$/i,
        loader: 'vue-loader',
      },
    ],
  },
  plugins: [
    new HTMLWebpackPlugin({
      template: resolve(__dirname, 'public/index.html'),
    }),
  ],
}
