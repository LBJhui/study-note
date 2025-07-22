const os = require('os')
const path = require('path') // nodejs 核心模块，专门用来处理路径问题
const ESLintPlugin = require('eslint-webpack-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin')
const TerserWebpackPlugin = require('terser-webpack-plugin')
const ImageMinimizerPlugin = require('image-minimizer-webpack-plugin')
const PreloadWebpackPlugin = require('@vue/preload-webpack-plugin')
const WorkboxPlugin = require('workbox-webpack-plugin')

const threads = os.cpus().length // CPU 核数
// 用来获取处理样式的loader
function getStyleLoader(pre) {
  return [
    MiniCssExtractPlugin.loader, // 提取css成单独文件
    'css-loader', // 将css资源编译成commonjs的模块到js中
    {
      loader: 'postcss-loader',
      options: {
        postcssOptions: {
          plugins: [
            'postcss-preset-env' // 能解决大多数样式兼容性问题
          ]
        }
      }
    },
    pre
  ].filter(Boolean)
}

module.exports = {
  // 入口
  entry: './src/main.js', // 相对路径
  // 输出
  output: {
    // 文件的输出路径
    // __dirname nodejs 的变量，当前文件的文件夹目录
    path: path.resolve(__dirname, '../dist'), // 绝对路径
    // 入口文件打包输出文件名
    filename: 'static/js/main.[contenthash:10].js',
    // 给打包输出的其他文件命名
    chunkFilename: 'static/js/[name].chunk.[contenthash:10].js',
    // 图片、字体等通过 type：asset 处理资源命名方式
    assetModuleFilename: 'static/media/[hash:10][ext][query]',
    // 自动清空上次打包的内容
    // 原理：在打包前，将 path 整个目录内容情况，再进行打包
    clean: true
  },
  // 加载器
  module: {
    rules: [
      {
        // 每个文件只能被其中一个 loader 配置处理
        oneOf: [
          // loader 的配置
          {
            test: /\.css$/i,
            // use 执行顺序，从右到左（从下到上）
            use: getStyleLoader() // 执行顺序：从右到左（从下到上）
          },
          {
            test: /\.less$/i,
            // loader:'xxx',  // 只能使用一个 loader
            // use 可以使用多个 loader
            use: getStyleLoader('less-loader')
          },
          {
            test: /\.s[ac]ss$/i,
            use: getStyleLoader('sass-loader')
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
              // filename: 'static/images/[hash:10][ext][query]'
            }
          },
          {
            test: /\.(ttf|woff2?|map4|map3|avi)$/,
            type: 'asset/resource'
            // generator: {
            //   filename: 'static/media/[hash:10][ext][query]'
            // }
          },
          {
            test: /\.(?:js|mjs|cjs)$/,
            exclude: /node_modules/, // 排除 node_modules 目录
            // include: path.resolve(__dirname, '../src'), // 只处理 src 目录下的文件
            use: [
              {
                loader: 'thread-loader', // 开启多进程
                options: {
                  works: threads // 进程数量
                }
              },
              {
                loader: 'babel-loader',
                options: {
                  cacheDirectory: true, // 开启babel缓存
                  cacheCompression: false, // 关闭缓存文件压缩
                  plugins: ['@babel/plugin-transform-runtime'] // 减少代码体积
                }
              }
            ]
          }
        ]
      }
    ]
  },
  optimization: {
    // 压缩的操作
    minimizer: [
      // For webpack v5, you can use the `...` syntax to extend existing minimizers (i.e. `terser-webpack-plugin`), uncomment the next line // `...`,
      // 压缩 css
      new CssMinimizerPlugin(),
      // 压缩 js
      new TerserWebpackPlugin({
        parallel: threads // 开启多线程打包
      }),
      // 压缩图片
      new ImageMinimizerPlugin({
        minimizer: {
          implementation: ImageMinimizerPlugin.imageminMinify,
          options: {
            // Lossless optimization with custom option
            // Feel free to experiment with options for better results
            plugins: [
              ['gifsicle', { interlaced: true }],
              ['jpegtran', { progressive: true }],
              ['optipng', { optimizationLevel: 5 }],
              // SVGO configuration here https://github.com/svg/svgo#configuration
              [
                'svgo',
                {
                  plugins: [
                    {
                      name: 'preset-default',
                      params: {
                        overrides: {
                          removeViewBox: false,
                          addAttributesToSVGElement: {
                            params: {
                              attributes: [{ xmlns: 'http://www.w3.org/2000/svg' }]
                            }
                          }
                        }
                      }
                    }
                  ]
                }
              ]
            ]
          }
        }
      })
    ],
    // 代码分割配置
    splitChunks: {
      chunks: 'all'
    },
    // 提取runtime文件
    runtimeChunk: {
      name: (entrypoint) => `runtime~${entrypoint.name}` // runtime文件命名规则
    }
  },
  // 插件
  plugins: [
    // plugins 的配置
    new ESLintPlugin({
      // 检测哪些文件
      // context: path.resolve(__dirname, 'src'),
      cache: true, // 开启缓存
      cacheLocation: path.resolve(__dirname, '../node_modules/.cache/eslintcache'),
      threads // 开启多线程打包
    }),
    new HtmlWebpackPlugin({
      template: path.resolve(__dirname, '../public/index.html')
    }),
    new MiniCssExtractPlugin({
      filename: 'static/css/[name].[contenthash:10].css',
      chunkFilename: 'static/css/[name].chunk.[contenthash:10].css'
    }),
    new PreloadWebpackPlugin({
      rel: 'preload', // preload兼容性更好
      as: 'script'
      // rel: 'prefetch' // prefetch兼容性更差
    }),
    new WorkboxPlugin.GenerateSW({
      // 这些选项帮助快速启用 ServiceWorkers
      // 不允许遗留任何“旧的” ServiceWorkers
      clientsClaim: true,
      skipWaiting: true
    })
  ],
  // 模式
  mode: 'production',
  devtool: 'cheap-module-source-map'
}
