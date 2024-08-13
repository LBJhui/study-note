```javascript
// webpack 默认安装了 terser
module.exports = defineConfig({
  transpileDependencies: true,
  terser: {
    terserOptions: {
      compress: {
        drop_console: true,
        drop_debugger: true,
      },
    },
  },
})
```

```javascript
// vite 需要 安装 terser，先安装开发依赖
export default defineConfig({
  build: {
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: true,
        drop_debugger: true,
      },
    },
  },
})
```
