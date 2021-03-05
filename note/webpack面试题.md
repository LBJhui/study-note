# 处理图片

**dev**

```javascript
module: {
  rules:[
    {
      test: /\.(png|jpg)$/,
      loader: 'file-loader'
    }
  ]
}
```

**prod**

```javascript
module: {
  rules:[
    {
      test: /\.(png|jpg)$/,
      use: {
        loader: 'url-loader',
        options: {
          limit: 30 * 1024，
          outputPath: '/img/'
        }
      }
    }
  ]
}
```

比较小的图片，就转换成了 base64 格式，可以减少 http 请求

比较大的图片，依旧像 file-loader 一样，单独打包到 img 文件夹里，发送请求，防止页面首次渲染太慢

# 抽离 CSS

```javascript
module: {
  rules:[
    {
      test: /\.css$/,
      loader: [
        'style-loader',
        'css-loader',
        'postcss-loader'
      ]
    }
  ]
}
```

