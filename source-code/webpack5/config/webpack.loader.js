const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')
module.exports = {
  entry: './src/loader.js',
  output: {
    path: path.resolve(__dirname, '../dist'),
    filename: 'loader.bundle.js',
    clean: true
  },
  module: {
    rules: [
      // {
      //   test: /\.js$/,
      //   loader: './loaders/test-loader.js'
      // },
      {
        test: /\.js$/,
        // use: [
        //   './loaders/demo/test1.js', // 同步 loader
        //   './loaders/demo/test2.js' // 异步 loader
        // ],
        // use: [
        //   './loaders/demo/test2.js', // 异步 loader
        //   './loaders/demo/test1.js' // 同步 loader
        // ],
        // loader: './loaders/demo/test3.js'
        // use: ['./loaders/demo/test4.js', './loaders/demo/test5.js', './loaders/demo/test6.js']
        loader: './loaders/clean-log-loader.js'
      },
      {
        test: /\.js$/,
        loader: './loaders/banner-loader.js',
        options: {
          author: 'LBJhui'
        }
      }
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: path.resolve(__dirname, '../public/index.html')
    })
  ],
  mode: 'development'
}
