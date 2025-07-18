const path = require('path') // nodejs 核心模块，专门用来处理路径问题
const ESLintPlugin = require('eslint-webpack-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
  // 入口
  entry: './src/main.js', // 相对路径
  // 输出
  output: {
    // 文件的输出路径
    // __dirname nodejs 的变量，当前文件的文件夹目录
    // 开发模式没有输出
    path: undefined,
    // 入口文件打包输出文件名
    filename: 'static/js/main.js',
    // 自动清空上次打包的内容
    // 原理：在打包前，将 path 整个目录内容情况，再进行打包
    clean: true
  },
  // 加载器
  module: {
    rules: [
      // loader 的配置
      {
        test: /\.css$/i,
        // use 执行顺序，从右到左（从下到上）
        use: [
          'style-loader', // 将 js 中的 css 通过创建 style 标签添加 html 文件中生效
          'css-loader' // 将 css 资源编译成 commonjs 的模块到 js 中
        ]
      },
      {
        test: /\.less$/i,
        // loader:'xxx',  // 只能使用一个 loader
        // use 可以使用多个 loader
        use: [
          // compiles Less to CSS
          'style-loader',
          'css-loader',
          'less-loader'
        ]
      },
      {
        test: /\.s[ac]ss$/i,
        use: [
          // compiles Less to CSS
          'style-loader',
          'css-loader',
          'sass-loader'
        ]
      },
      {
        test: /\.(png|jpe?g|gif|webp)$/,
        type: 'asset',
        parser: {
          dataUrlCondition: {
            // 优点：减少请求数量，缺点：体积会更大
            maxSize: 10 * 1024 // 小于 10kb 的图片转 base64
          }
        },
        generator: {
          // 输出图片名称
          // [hash:10] hash 的前 10 位
          // [ext]: 使用之前的文件扩展名
          // [query]: 添加之前的query参数
          filename: 'static/images/[hash:10][ext][query]'
        }
      },
      {
        test: /\.(ttf|woff2?|map4|map3|avi)$/,
        type: 'asset/resource',
        generator: {
          filename: 'static/media/[hash:10][ext][query]'
        }
      },
      {
        test: /\.(?:js|mjs|cjs)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      }
    ]
  },
  // 插件
  plugins: [
    // plugins 的配置
    new ESLintPlugin({
      // 检测哪些文件
      // context: path.resolve(__dirname, 'src'),
    }),
    new HtmlWebpackPlugin({
      template: path.resolve(__dirname, '../public/index.html')
    })
  ],
  // 模式
  mode: 'development',
  // 开发服务器: 不会输出资源，在内存中编译打包的
  devServer: {
    host: 'localhost',
    port: 3000,
    static: './dist'
  }
}
