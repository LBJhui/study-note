const path = require('path') // nodejs 核心模块，专门用来处理路径问题

module.exports = {
  // 入口
  entry: './src/main.js', // 相对路径
  // 输出
  output: {
    // 文件的输出路径
    // __dirname nodejs 的变量，当前文件的文件夹目录
    path: path.resolve(__dirname, 'dist'), // 绝对路径
    // 文件名
    filename: 'main.js'
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
      }
    ]
  },
  // 插件
  plugins: [
    // plugins 的配置
  ],
  // 模式
  mode: 'development'
}
