const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const TestPlugin = require('../plugins/test-plugin')
const BannerWebpackPlugin = require('../plugins/banner-webpack-plugin/index')
const CleanWebpackPlugin = require('../plugins/clean-webpack-plugin/index')
const AnalyzeWebpackPlugin = require('../plugins/analyze-webpack-plugin/index')
const InlineChunkWebpackPlugin = require('../plugins/inline-chunk-webpack-plugin/index')

module.exports = {
  entry: './src/loader.js',
  output: {
    path: path.resolve(__dirname, '../dist'),
    filename: 'js/[name].js'
    // clean: true
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
      // {
      //   test: /\.js$/,
      //   loader: './loaders/banner-loader.js',
      //   options: {
      //     author: 'LBJhui'
      //   }
      // },
      {
        test: /\.js$/,
        loader: './loaders/babel-loader/index.js',
        options: {
          presets: ['@babel/preset-env']
        }
      },
      {
        test: /\.css$/,
        // use: ['style-loader', 'css-loader']
        use: ['./loaders/style-loader', 'css-loader']
      },
      {
        test: /\.png$/,
        loader: './loaders/file-loader/index.js',
        type: 'javascript/auto' // 阻止 webpack 默认处理文件，只使用 file-loader 处理
      }
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: path.resolve(__dirname, '../public/index.html')
    }),
    // new TestPlugin()
    new BannerWebpackPlugin({
      author: 'LBJhui'
    }),
    new CleanWebpackPlugin(),
    new AnalyzeWebpackPlugin(),
    new InlineChunkWebpackPlugin([/runtime(.*)\.js/])
  ],
  optimization: {
    // 代码分割配置
    splitChunks: {
      chunks: 'all'
    },
    // 提取runtime文件
    runtimeChunk: {
      name: (entrypoint) => `runtime~${entrypoint.name}` // runtime文件命名规则
    }
  },
  mode: 'production'
}
