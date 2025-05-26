# web 应用中如何对静态资源加载失败的场景做降级处理

## 场景

1. 图片
2. css 文件
3. JavaScript 文件
4. CDN
5. 字体文件
6. 服务端渲染失败

## 解决方案

### 图片处理

1. 占位图，alt 来描述图片
2. 重试机制（404、无权限）
3. 上报

```html
<img src="" alt="图片描述" onerror="handleImageError(this)" />

<script>
  function handleImageError(img) {
    img.onerror = null // 防止死循环
    img.src = 'placeholder.png' // 使用占位图
  }
</script>
```

### css 文件处理

资源没加载到

1. 关键性样式，通过内联
2. 备用样式
3. 上报

```html
<style>
  /* 内联关键样式 */
  body {
    font-family: 'Arial', 'Helvetica Neue', Helvetica, sans-serif;
  }
</style>
<link rel="stylesheet" href="style.css" onerror="handleStyleError()" />

<script>
  function handleStyleError() {
    // 加载备用样式
    const fallbackCSS = document.createElement('link')
    fallbackCSS.rel = 'stylesheet'
    fallbackCSS.href = 'fallback.css'
    document.head.appendChild(fallbackCSS)
  }
</script>
```

### JavaScript 文件处理

网络异常，导致资源没加载

1. 内联脚本
2. 备用脚本
3. 上报

```html
<script>
  // 内联脚本
  function basicFunctionality() {
    console.log('This is a basic functionality.')
  }
  basicFunctionality()
</script>
<script src="script.js" onerror="handleScriptError()"></script>

<script>
  function handleScriptError() {
    // 加载备用脚本
    const fallbackScript = document.createElement('script')
    fallbackScript.src = 'fallback.js'
    document.head.appendChild(fallbackScript)
  }
</script>
```

### CDN

1. 本地备份，如果 cdn 出错了，就使用本地备份
2. 动态切换，切到另一个有用的 cdn 服务

```html
<script src="https://cdn.example.com/library.js" onerror="handleCdnError()"></script>
<script>
  function handleCdnError() {
    // 加载本地备份
    const localBackup = document.createElement('script')
    localBackup.src = 'local-backup.js'
    document.head.appendChild(localBackup)

    // 或者动态切换到另一个 cdn
    const alternativeCdn = document.createElement('script')
    alternativeCdn.src = 'https://alternative.cdn.com/library.js'
    document.head.appendChild(alternativeCdn)
  }
</script>
```

### 字体文件处理

1. 使用降级字体 apple、微软雅黑
2. webfont 处理字体问题

```css
@font-face {
  font-family: 'MyFont';
  src: url('myFont.woff2') format('woff2');
  font-display: swap;
}

body {
  font-family: 'MyFont', 'Arial', 'Helvetica Neue', Helvetica, sans-serif;
}
```

### 服务端渲染失败 ssr

1. 降级的 html 用作渲染
2. 切换为 CSR
