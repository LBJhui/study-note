- promise
- 虚拟 DOM
- Vue3 中 watch 和 watchEffect

https://fe.duyiedu.com/p/t_pc/goods_pc_detail/goods_detail/course_2VKbErGXkTSzvbl9aQ9HgndEtIz?type=2

```javascript
// 脚本加载失败如何重试

// 在项目中遇到的一个难点，无论是我们用的原生js还是用的框架最后上线的时候都会是打包好之后，打包好之后的js文件中都会自己或者自动引入script，在生产环境中会出现其中有一个script无法加载成功的时候怎么处理，当js加载不出来的时候页面是显示不出来的，最起码功能是不正常的，现在都是单页面应用，js加载不成功的话对页面影响还是比较大的，所以我们需要去处理这个问题。。。

// 1. 什么时间重试 捕获
// 2. 如何重试
// 在 head 标签中添加 script 元素
const backupDomains = [
  'https://www.baidu.com',
  'https://www.google.com',
  'https://www.bing.com',
  'https://www.yahoo.com',
  'https://www.youtube.com',
  'https://www.facebook.com',
  'https://www.twitter.com',
  'https://www.instagram.com',
  'https://www.tiktok.com'
]
const nextDomain = {}
window.addEventListener(
  'error',
  (e) => {
    // 只捕获脚本错误
    if (e instanceof ErrorEvent && e.target.tagName !== 'SCRIPT') {
      return
    }
    const url = new URL(e.target.src)
    const pathname = url.pathname
    if (!nextDomain[pathname]) {
      nextDomain[pathname] = 0
    }

    const index = nextDomain[pathname]
    if (index >= backupDomains.length) {
      return
    }
    const domain = backupDomains[index]
    url.hostname = domain
    const newUrl = url.toString()
    // 阻塞页面
    document.write(`<script src="${newUrl}"></script>`)
    // const script = document.createElement('script')
    // script.src = newUrl
    // e.target.parentElement.insertBefore(script, e.target)
    nextDomain[pathname]++
  },
  true
)
```

```markdown
重绘和回流
何时发生重排？何时发生重绘？
**重排**：
所有对布局树的更改，以及所有对布局树的读取，都会引发重排
更改：异步重排
读取：同步重排
**重绘**
对所有非几何信息的读写所造成的可见样式的变化

- 重绘和回流有什么区别？
  1. 重绘
  - 元素样式的可见属性发生改变（颜色、背景色），但布局不改变的时候
  - 重绘不影响页面布局，只会重绘受影响的元素
  2. 回流
  - 布局的变化导致元素的尺寸、位置或隐藏状态的变化，需要重新计算整个布局
  - 回流会造成重绘，但重绘不一定会回流
```

```markdown
[es6](https://es6.ruanyifeng.com/)
[Pinia 中文文档](https://pinia.web3doc.top/)
[webpack](https://www.webpackjs.com/)
[vite](https://vitejs.cn/)
[蚂蚁金服前端团队](https://www.yuque.com/ant-h5)
[张鑫旭](https://www.zhangxinxu.com/)
[大厂面试题每日一题](https://q.shanyue.tech/)
[阮一峰的网络日志](https://www.ruanyifeng.com/blog/)
```

```text
structuredClone https://www.zhangxinxu.com/wordpress/2025/01/js-api-structuredclone/
[Vue3 之 script-setup 全面解析](https://www.jianshu.com/p/5096bfb42e5a)
纯前端图片压缩 图转base64读出宽高，canvas画图
对等依赖 peerDependencies(package.json) npm i --legacy-peer-deps
函数管道
vue3 h函数
effectScope 嵌套 https://www.jianshu.com/p/1a1731806e19
box-shadow
协同处理 yjs+crdt算法+oj
依赖倒置原则
prefetch preload
https://www.zhangxinxu.com/wordpress/2024/11/js-selectionchange-event/
https://www.zhangxinxu.com/wordpress/2022/07/css-font-palette/
免费课合集：https://qmdqi.xetlk.com/s/376rbn
https://www.zhangxinxu.com/wordpress/2024/09/js-scrollend-event/
https://www.zhangxinxu.com/wordpress/2024/09/js-object-groupby/
https://www.zhangxinxu.com/wordpress/2024/09/css-math-round-function/
CSS文本自定义高亮AP简介 https://www.zhangxinxu.com/wordpress/2024/07/css-custom-highlight-api/
initial-letter https://www.zhangxinxu.com/wordpress/2024/03/css-initial-letter/
margin-trim 属性设置在容器元素上，可以让子元素(需边缘接触) margin 设置计算值变成 0 https://www.zhangxinxu.com/wordpress/2023/05/css-margin-trim/
align-content也适用于普通元素
grid-template-rows: masonry;
vue方法中属性丢失的问题 methods配置的方法与组件实例的方法 https://blog.csdn.net/xiaotangyu7dong/article/details/131713991
展示组件和容器组件
使用computed拦截v-model https://juejin.cn/post/7338634091397431330
v-model 父传子值，元素更改后获取值滞后，nextTick
右键菜单组件的封装 https://blog.csdn.net/DuyiZiChen/article/details/131405493
SocketIO
全局导入和局部导入的区别
ESModule 的工作原理
transform 从右到左 translate3d
依赖检查工具 depcheck
mask-image
vue3 expose defineExpose markRaw、withModifiers
正则匹配的贪婪模式和惰性模式有什么区别
BFF 层 backends for frontends
函数签名 = 函数名称 + 函数参数 + 函数参数类型 + 返回值类型
改变 webkit 表单输入框 placeholder 的颜色值：input::-webkit-input-placehold
去掉 ios 系统中元素被触摸时产生的半透明灰色遮罩：tip-highlight-color:rgba(0,0,0,0)
http accept-lang/navigator.lang
content-type
showDirectoryPicker FileSystem API
俄罗斯方块实现思路
conic-gradient
web-vitals
?? 运算符 返回第一个已定义的值
Object.defineProperty 只能监听到对象属性的读取或者是写入，而 Proxy 除读写外还可以监听对象中属性的删除，对对象当中方法的调用
object-fit
addEventListener compositionstart 'contextmenu'
禁止触发系统菜单和长按选中：`touch-callout:none` contextmenu
数组新增的纯函数 API：toSorted、toReversed、toSpliced、with(修改数组)
font-variant、text-transform
ElementUI 日期选择器时间选择范围限制
自定义指令控制权限的弊端 https://blog.csdn.net/layonly/article/details/139402930 DOM 元素删除后，生命周期会正常进行，还会请求数据
组件循环依赖：动态导入
符号绑定
防截屏防录制：Encrypted Media Extensions API
使用data url预览图片 https://blog.csdn.net/u012804440/article/details/136018598
```

```Typescript
// 用TS构建长属性列表
// type Result = ['p0', 'p1', 'p2']
type ResultField<Count extends number, Result extends string[] = []> = Result['length'] extends Count ? Result[number] : ResultField<Count, [...Result, `p${Result['length']}`]>

type GenerateObject<Count extends number> = {
  [key in ResultField<Count>]: string
}

type MyObject = Omit<GenerateObject<99>, 'p0'> & { type: number }
```

```javascript
fun([() => console.log('start'), () => sleep(1000), () => console.log('1'), () => sleep(2000), () => console.log('2'), () => sleep(3000), () => console.log('end')])

function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms)
  })
}

async function fun(arr) {
  arr.myForEach(async (item) => await item())
  // for (let i = 0; i < arr.length; i++) {
  //   await arr[i]()
  // }
  //
  /**
   * arr.forEach(async (item) => await item())
   *  async (item1)=>await item1()
   *  async (item2)=>await item2()
   */
}
```

```css
/* CSS锚点定位 https://segmentfault.com/a/1190000045077175 */

/* 隐式锚点 适用于 1v1 */
.trigger {
  anchor-name: --my-anchor;
}

.target {
  position-anchor: --my-anchor;
  left: anchor(left);
  /* 居中对齐 */
  /* justify-self: anchor-center;  */
  /* inset-area: bottom; */
}

/* 显示锚点 适用于多元素定位 */
.trigger1 {
  anchor-name: --anchor-a;
}

.trigger2 {
  anchor-name: --anchor-b;
}

.target {
  position: absolute;
  left: anchor(--anchor-a right);
  right: anchor(--anchor-b left);
}
```

```text
跨标签页通信常见方案
  BroadcastChannel API https://www.zhangxinxu.com/wordpress/2025/01/js-broadcast-channel-api/
  Service Worker
  LocalStorage  window.onstorage 监听
  Shared Worker 定时器轮询 setInterval
  IndexedDB 定时器轮询
  cookie 定时器轮询
  window.open、window.postMessage
  WebSocket
```

```javascript
// 任务执行的洋葱模型
class TaskPro {
  #tasksList
  #isRunning
  #currentIndex
  #next

  constructor() {
    this.#tasksList = []
    this.#isRunning = false
    this.#currentIndex = 0
    this.#next = async () => {
      this.#currentIndex++
      await this.#runTask()
    }
  }

  addTask(task) {
    this.#tasksList.push(task)
  }

  run() {
    if (this.#isRunning || this.#tasksList.length === 0) return undefined
    this.#isRunning = true
    this.#runTask()
  }

  /**
   * 取出一个任务执行
   */
  async #runTask() {
    if (this.#currentIndex >= this.#tasksList.length) {
      this.#reset()
      return undefined
    }
    const i = this.#currentIndex
    const task = this.#tasksList[this.#currentIndex]
    await task(this.#next)
    const j = this.#currentIndex
    if (i === j) {
      await this.#next()
    }
  }

  #reset() {
    this.#currentIndex = 0
    this.#isRunning = false
    this.#tasksList = []
  }
}

const t = new TaskPro()

t.addTask(async (next) => {
  console.log('task1 start')
  await next()
  console.log('task1 end')
})
t.addTask((next) => {
  console.log('task2')
})
t.addTask((next) => {
  console.log('task3')
})

t.run()
```

```text
打包结果分析工具
  Webpack:webpack-bundle-analyzer
  vite:vite-bundle-visualizer
       rollup-bundle-visualizer
```

```text
元素的绘制顺序
  可替换元素
    元素本身
    元素内容
  堆叠上下文、层叠上下文
    z-index,position:relative
    transform
```

```javascript
/**
 * File 对象：它表示一组文件，我们使用 <input type="file"> 选择文件时，这些文件被存储在 File 对象中
 *
 * Blob 对象：Blob 对象表示二进制数据，常用来表示大型数据对象（如图片、音频等）。File 对象是 Blob 对象的一个子类，它继承了 Blob 对象的所有属性和方法
 *
 * formData 对象：前端先将文件存储在 formData 对象中，才能传给后端
 *
 * slice 方法
 *  File 对象的 slice 方法是从其父类 Blob 对象继承来的。用于从文件中提取一段范围的数据。参数如下：
 *    - start：开始提取数据的字节偏移量。如果未指定，默认为0
 *    - end：结束提取数据的字节偏移量。如果未指定，默认为文件或 Blob 对象的总字节数
 *  slice 方法的返回值是一个新的 Blob 对象，包含从原始文件或 Blob 对象中提取的指定字节范围的数据
 */

const fileInput = document.getElementById('file')
const file = fileInput.files[0]

// 创建一个新的 formData 对象
const formData = new FormData()

// 将 file 对象添加到 FormData 对象中
formData.append('file', file)
formData.append('fileName', file.name)

fetch('url', {
  method: 'POST',
  body: formData,
})

// 文件上传
//   单文件上传 multiport/form-data
//   二进制格式上传文件 binary/application/octet-stream Content-Type:application/octet-stream

// 文件下载
// 下载的流式传输
// 如果前端直接打开文件，没有触发下载 a 元素 download

// 数据的流式获取
async function getRespnse(content) {
  const resp = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(content),
  })
  // const data = awit resp.text()
  const reder = resp.body.getReader()
  const decoder = new TextDecoder()
  while (true) {
    const { done, value } = await reader.read()
    if (done) {
      break
    }
    const txt = decoder.decode(value)
  }
}

// 分块加载大数据
async function loadNovel() {
  const url = 'https://duyi-static.oss-cn-beijing.aliyuncs.com/files/novel.txt'
  const res = await fetch(url)
  const reader = res.body.getReader()
  const { value, done } = await reader.read()
  const decoder = new TextDecoder()
  const text = decoder.decode(value)
  for (;;) {
    const { value, done } = await reader.read()
    if (done) {
      break
    }
    const text = decoder.decode(value) // 可能存在乱码
  }
}

// 服务器端：
  res.setHeader('Content-Disposition', 'attachment;filename=es6.pdf')
// 前端
  <a download=''></a>
// https://blog.csdn.net/weixin_64684095/article/details/139484213

// 触发迅雷下载
const link = '需要下载的地址'
const newHref = btoa(`AA${link}ZZ`) // a 标签的地址

a.href = `thunder://${newHref}`
```

```javascript
// 从视频文件提取画面帧 https://juejin.cn/post/7352079398072746047
const inp = document.querySelector('input[type=file]')
inp.onchange = (e) => {
  const file = e.target.files[0]
  captureFrame(file, 1).then(({ url }) => {
    const img = document.createElement('img')
    img.src = url
    document.body.appendChild(img)
  })
}

function captureFrame(file, time = 0) {
  return new Promise((resolve, reject) => {
    const vdo = document.createElement('video')
    vdo.currentTime = time
    vdo.muted = true
    vdo.autoplay = true
    vdo.src = URL.createObjectURL(file)
    vdo.oncanplay = () => {
      const cvs = document.createElement('canvas')
      cvs.width = vdo.videoWidth
      cvs.height = vdo.videoHeight
      const ctx = cvs.getContext('2d')
      ctx.drawImage(vdo, 0, 0, cvs.width, cvs.height)
      // document.body.appendChild(cvs)

      cvs.toBlob((blob) => {
        const url = URL.createObjectURL(blob)
        resolve({ url, blob })
      })
    }
  })
  // return {
  //   url:图片的url地址
  //   blob:图片的二进制数据
  // }
}
```

```js
// 深度克隆的一般实现
const cache = new WeakMap()

function deepClone(value) {
  if (typeof value !== 'object' || value === null) {
    return value
  }
  // value 是对象
  if (cache.has(value)) {
    return cache.get(value)
  }
  const result = Array.isArray(value) ? [] : {}
  Object.setPrototypeOf(result, Object.getPrototypeOf(value))
  cache.set(value, result)
  for (const key in value) {
    if (value.hasOwnProperty(key)) {
      result[key] = deepClone(value[key])
    }
  }
  return result
}

function deepClone(origin, target) {
  var tar = target || {}
  var toStr = Object.prototype.toString
  var arrType = '[object Array]'
  for (var k in origin) {
    if (origin.hasOwnProperty(k)) {
      if (typeof origin[k] === 'object' && origin[k] !== null) {
        tar[k] = toStr.call(origin[k]) === arrType ? [] : {}
        deepClone(origin[k], tar[k])
      } else {
        tar[k] = origin[k]
      }
    }
  }
  return tar
}

function deepClone(origin, hashMap = new WeakMap()) {
  // undefined null origin == undefined
  if (origin === undefined || origin === null || typeof origin !== 'object') {
    return origin
  }
  if (origin instanceof Date) {
    return new Date(origin)
  }
  if (origin instanceof RegExp) {
    return new RegExp(origin)
  }

  const hasKey = hashMap.get(origin)
  if (hasKey) {
    return hasKey
  }

  const target = new origin.constructor()
  for (let k in origin) {
    hashMap.set(origin, target)
    if (origin.hasOwnProperty(k)) {
      target[k] = deepClone(origin[k], hashMap)
    }
  }
  return target
}
```

```text
值传递
引用传递
js 引用传递 具名导入 import { n as main } from 'a.js'
https://blog.csdn.net/brilliantSt/article/details/136300491
```

```js
// 手写memoize
class MemoizeMap {
  #map
  #weakMap

  constructor() {
    this.#map = new Map()
    this.#weakMap = new WeakMap()
  }

  _isObject(v) {
    return typeof v === 'object' && v !== null
  }

  set(key, value) {
    if (this._isObject(key)) {
      this.#weakMap.set(key, value)
    } else {
      this.#map.set(key, value)
    }
  }

  get(key) {
    if (this._isObject(key)) {
      return this.#weakMap.get(key)
    } else {
      return this.#map.get(key)
    }
  }

  has(key) {
    if (this._isObject(key)) {
      return this.#weakMap.get(key)
    } else {
      return this.#map.get(key)
    }
  }
}

function memoize(fn, resolver) {
  function memoized(...args) {
    const key = resolver ? resolver(...args) : args[0]
    const cache = memoized.cache
    if (cache.has(key)) {
      return cache.get(key)
    }
    const result = fn.apply(this, args)
    cache.set(key, result)
    return result
  }

  memoized.cache = new MemoizeMap()
  return memoized
}
```

```javascript
// 目录的自动高亮
function highlight(id) {
  document.querySelectorAll('a.highlight').forEach((a) => {
    a.classList.remove('highlight')
  })
  if (id instanceof HTMLElement) {
    id.classList.add('highlight')
    return
  }
  if (id.startsWith('#')) {
    id = id.substring(1)
  }
  document.querySelector(`a[href="${id}"`).classList.add('highlight')
}

const links = document.querySelectorAll('.toc a[href^="#"')
const titles = []
for (const link of links) {
  link.addEventListener('click', (e) => {
    highlight(link)
  })
  const url = new URL(link.href)
  const dom = document.querySelector(url.hash)
  if (dom) {
    titles.push(dom)
  }
}

/**
 * 函数防抖
 */
const debounce = (fn, delay) => {
  let timer = null
  return function (...args) {
    clearTimeout(timer)
    timer = setTimeout(() => {
      fn.apply(this, args)
    }, delay)
  }
}

const scrollHandler = debounce(() => {
  const rects = titles.map((title) => title.getBoundingClientRect())
  const toRange = 300
  for (let i = 0; i < titles.length; i++) {
    const rect = rects[i] // 标题的位置信息
    const title = titles[i] // 标题的 Dom
    if (rect.top >= 0 && rect.top <= toRange) {
      highlight(title.id)
      break
    } else if (rect.top < 0 && rect[i + 1] && rect[i + 1].top > document.documentElement.clientHeight) {
      highlight(title.id)
      break
    }
  }
}, 100)

window.addEventListener('scroll', scrollHandler)
```

```ts
协变和逆变
//blog.csdn.net/u014676858/article/details/141826960
// https: 类型安全 所有成员可用

// 收：Fans: 父类型 成员少
// 给：Ikun: 子类型 成员多

interface Fans {
  call(): void
}

interface IKun extends Fans {
  sing(): void
  dance(): void
  basketball(): void
  rap(): void
}

let fans: Fans
let ikun: IKun

fans = ikun
ikun = fans // 不能赋值

// 联合类型转交叉类型
type UnionToIntersection<T> = (T extends any ? (x: T) => any : never) extends (x: infer R) => any ? R : never

type Test = UnionToIntersection<{ a: 1; b: 2 } | { c: 3; d: 4 }>
```

```javascript
// 2048游戏核心逻辑
const matrix = [
  [0, 2, 2, 0],
  [0, 0, 2, 2],
  [2, 4, 4, 2],
  [2, 4, 4, 4]
]

function move(matrix, direction) {
  const rows = matrix.length
  const cols = matrix[0].length

  function _inRange(i, j) {
    return i >= 0 && i < rows && j >= 0 && j < cols
  }

  const nexts = {
    up: (i, j) => [i + 1, j],
    down: (i, j) => [i - 1, j],
    left: (i, j) => [i, j + 1],
    right: (i, j) => [i, j - 1]
  }

  // 得到下一个非零的位置 [r, c, value]
  function _nextNonZero(i, j) {
    // 得到下一个位置
    let [nextI, nextJ] = nexts[direction](i, j)
    if (!_inRange(nextI, nextJ)) return null
    while (_inRange(nextI, nextJ)) {
      const value = matrix[nextI][nextJ]
      if (value !== 0) {
        return [nextI, nextJ, value]
      }
      ;[nextI, nextJ] = nexts[direction](nextI, nextJ)
    }
    return null
  }

  // 从 i，j 出发，依次处理某行或某列的数据
  function _cal(i, j) {
    if (!_inRange(i, j)) return
    const next = _nextNonZero(i, j)
    if (!next) {
      return
    }
    const [nextI, nextJ, nextValue] = next
    if (matrix[i][j] === 0) {
      matrix[i][j] = nextValue
      matrix[nextI][nextJ] = 0
      _cal(i, j)
    } else if (matrix[i][j] === nextValue) {
      matrix[i][j] *= 2
      matrix[nextI][nextJ] = 0
    }
    const [ni, nj] = nexts[direction](i, j)
    _cal(ni, nj)
  }

  if (direction === 'up') {
    for (let j = 0; j < cols; j++) {
      _cal(0, j)
    }
  } else if (direction === 'down') {
    for (let j = 0; j < cols; j++) {
      _cal(rows - 1, j)
    }
  } else if (direction === 'left') {
    for (let i = 0; i < rows; i++) {
      _cal(i, 0)
    }
  } else if (direction === 'right') {
    for (let i = 0; i < rows; i++) {
      _cal(i, cols - 1)
    }
  }
  return matrix
}

console.log(move(matrix, 'up'))

/**
 * [
 *  [4, 2, 4, 4],
 *  [0, 8, 8, 4],
 *  [0, 0, 0, 0],
 *  [0, 0, 0, 0]
 * ]
 */
```

```js
// 消除异步的传染性 https://blog.csdn.net/weixin_51351053/article/details/140050295
async function getUser() {
  return await fetch('./1.json')
}

async function m1() {
  const user = await getUser()
  return user
}

async function m2() {
  const user = await m1()
  return user
}

async function m3() {
  const user = await m2()
  return user
}

/**
 * main->getUser->fetch(error)--->main->getUser->fetch->getUser->main
 *                      fetch-->cache-->main
 */
function main() {
  const user = m3()
  console.log(user)
}

function run(func) {
  // 1. 改动 Fetch
  const oldFetch = window.fetch
  const cache = {
    status: 'pending',
    value: null
  }

  function newFetch(...args) {
    // 有缓存返回缓存
    if (cache.status === 'fulfilled') {
      return cache
    } else if (cache.status === 'rejected') {
      throw new Error(cache.value)
    }
    // 没有缓存
    const p = oldFetch(...arguments)
      .then((data) => data.json)
      .then((data) => {
        cache.status = 'fulfilled'
        cache.value = data
      })
      .catch((err) => {
        cache.status = 'rejected'
        cache.value = err
      })
    // 抛出错误
    throw 123
  }

  window.fetch = newFetch
  // 2. 执行 func
  try {
    func()
  } catch (e) {
    // 等待请求完成后重新运行 func
    if (err instanceof Promise) {
      err.finall(() => {
        window.fetch = newFetch
        func()
        window.fetch = oldFetch
      })
    }
  }
  // 3. 改回 fetch
  window.fetch = oldFetch
}

run(main)
```

```javascript
// 如果 call()方法的第一个参数是 Number、String 或 Boolean 基本类型，最终 this 会指向对应的包装类型对象。
// call 方法第一个参数为 null 或 undefined，this 会被设置为全局对象
// call和apply的链式调用
const r = console.log.call.call.call.call.call.call.call.apply((a) => a, [1, 2])

console.log(r)

console.log(console.log.__proto__ === Function.prototype)
console.log(console.log.call === Function.prototype.call)

// const r = Function.prototype.call.apply((a) => a, [1, 2])
```

```js
// 高量级任务执行优化
/**
 * 运行一个耗时任务
 * 如果要异步执行任务，请返回 Promise
 * 要尽快完成任务，同时不要让页面产生卡顿
 * 尽量兼容更多的浏览器
 * @param {Function} task

 */
//直接运行任务 阻塞
function runTask(task) {
  task()
}

// 微任务 阻塞
function runTask(task) {
  return new Promise((resolve) => {
    Promise.resolve().then(() => {
      task()
      resolve()
    })
  })
}

// 宏任务 卡顿
function runTask(task) {
  return new Promise((resolve) => {
    setTimeout(() => {
      task()
      resolve()
    }, 0)
  })
}

// requestAnimationFrame 阻塞
function runTask(task) {
  return new Promise((resolve) => {
    requestAnimationFrame(() => {
      task()
      resolve()
    })
  })
}

function _runTask(task, callback) {
  // requestIdleCallback 兼容性差
  // requestIdleCallback((idle) => {
  //   if (idle.timeRemaining > 0) {
  //     task()
  //     callback()
  //   } else {
  //     _runTask(task, callback)
  //   }
  // })
  let start = Date.now()
  requestAnimationFrame(() => {
    if (Date.now() - start < 16.6) {
      task()
      callback()
    } else {
      _runTask(task, callback)
    }
  })
}

function runTask(task) {
  return new Promise((resolve) => {
    _runTask(task, resolve)
  })
}
```

```markdown
- 样式计算
- 视觉格式化模型 包含块
  - 元素的 width 百分比相对的是包含块宽度
  - 元素的 height 百分比相对的是包含块高度
  - 元素的 margin 百分比相对的是包含块宽度
  - 元素的 padding 百分比相对是的包含块宽度
  - 元素的 left 相对的是包含块的左边缘
  - 元素的 top 相对的是包含块的上边缘

最近可滚动祖先

包含块的确定规则：

1. 常规元素和浮动元素
   父元素的内容盒
2. 绝对定位元素
   第一个定位祖先的填充盒
3. 固定定位
   无变形祖先：视口
   有变形祖先：变形祖先的填充盒
```

```scss
// SASS中的模块化开发
// @import
//   运行时 css
//   编译时
//     混淆
//     污染 变量污染
//     无私有
// @use

@use 'common.scss';
@use 'var.scss' as b;

$_n: 6; // 私有变量

.foo {
  color: common.$color;
}
```

```scss
// sass 混合 @mixin @include
// sass 继承 extends %(抽象类)

// 使用SASS实现主题切换
$themes: (
  light: (
    textColor: #333,
    bgColor: #fff
  ),
  dark: (
    textColor: #fff,
    bgColor: #333
  )
);
$themeMap: ();
@mixin useTheme() {
  @each $key, $value in $themes {
    $themeMap: $value !global;
    html [data-theme='#{$key}'] & {
      @content;
    }
  }
}

@function getVar($paramName) {
  @return map-get($themeMap, $paramName);
}

.item {
  font-size: 14px;
  @include useTheme {
    background: getVar('bgColor');
    color: getVar('textColor');
  }
}
```

```js
// CommonJS的本质 https://blog.csdn.net/huangpb123/article/details/138473608
// 2.js
this.a = 1
exports.b = 2
exports = {
  c: 3
}
module.exports = {
  d: 4
}
exports.e = 5
this.f = 6

//1.js
const a = require('./2')
console.log(a)
```

```js
// 可缓存的方法 计算属性如何传参
import { computed } from 'vue'

function useComputed(fn) {
  const map = new Map()
  return function (...args) {
    const key = JSON.stringify(args)
    if (map.has(key)) {
      return map.get(key)
    }
    const result = computed(() => {
      return fn(...args)
    })
    map.set(key, result)
    return result
  }
}
```

```js
// 数组扁平化
Array.prototype.customFlatten = function () {
  // 转化结果
  let flat = []
  for (let item of this) {
    if (Array.isArray(item)) {
      flat = flat.concat(item.customFlatten())
    } else {
      flat.push(item)
    }
  }
  return flat
}
```

```js
// 访问器成员
function Product(name, unitPrice, chooseNumber) {
  this.name = name
  this.unitPrice = unitPrice
  this.chooseNumber = chooseNumber
  // ES5
  Object.defineProperty(this, 'totalPrice', {
    get() {
      return this.unitPrice * this.chooseNumber
    }
  })
  // ES6
  get
  totalPrice()
  {
    return this.unitPrice * this.chooseNumber
  }
}
```

```js
// 使用代理拦截动态属性
function createProxy (values = []) {
  return new Proxy(
    {},
    {
      get (target, p) {
        if (p === Symbol.toPrimitive) {
          return () => values.reduce((a, b) => a + b, 0)
        }
        return createProxy([...values, +p])
      },
    }
  )
}

const add = createProxy()
add + 4 // 期望结果 4
const r1 = add[1][2][3] + 4 // 期望结果 10
const r2 = add[10][20] + 30 // 期望结果 60
const r3 = add[100][200][300] + 400 // 期望结果 1000

const add = new Proxy(
  { sum: 0 },
  {
    get(target, key, receiver) {
      // 遇到 + 操作，会触发隐式类型转换
      if (key === Symbol.toPrimitive) {
        const tmp = target.sum
        // 清零，可以重复调用多次
        target.sum = 0
        // Symbol.toPrimitive 是函数内部属性，所以需要返回一个函数
        return () => tmp
      } else {
        target.sum += Number(key)
        return receiver
      }
    }
  }
)

// 链式调用
function chain (value) {
  const handler = {
    get: function(obj, prop) {
      if (prop === 'end') {
        return obj.value
      }
      if (typedof window[prop] === 'function'
    )
      {
        obj.value = window[prop](obj.value)
        return proxy
      }
      return obj[prop]
    }
  }
  const proxy = new Proxy({ value }, handler)
  return proxy
}
```

```js
// 循环转递归
// 实现一个求和函数，不能使用循环，不能使用数组方法
function sum(arr, i = 0) {
  if (i >= arr.length) {
    return 0
  }
  return arr[i] + sum(arr, i + 1)
}

function demo1() {
  // 前面的代码
  for (初始代码; 条件; 后置代码) {
    // 循环体
  }
  // 后面的代码
}

function demo2() {
  // 前面的代码
  初始代码

  function _m() {
    if (!条件) {
      return
    }
    // 循环体
    后置代码
    _m()
  }

  _m()
  // 后面的代码
}

function demo1(arr) {
  let sum = 0
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i]
  }
  return sum
}

function demo2(arr) {
  let sum = 0
  let i = 0

  function _m() {
    if (i >= arr.length) {
      return
    }
    sum += arr[i++]
    _m()
  }

  _m()
  return sum
}
```

```js
// 分时函数的封装
const tasks = Array.from({ length: 300000 }, (_, i) => {
  const div = document.createElement('div')
  div.innerText = i
  document.body.appendChild(div)
})

const btn = document.querySelector('.btn')
btn.onclick = () => {
  // for (const task of tasks) {
  //   task()
  // }
  performTasks(tasks)
}

// 浏览器的微任务队列
function performTasks(tasks) {
  if (tasks.length === 0) {
    return
  }
  let i = 0

  // 每一次的执行
  function _run() {
    requestIdleCallback((idle) => {
      while (i < tasks.length && idle.timeRemaining() > 0) {
        tasks[i++]()
      }
      _run()
    })
  }

  _run()
}

// 自定义调度器
btn.onclick = () => {
  const scheduler = (chunkTask) => {
    setTimeout(() => {
      const now = performance.now()
      chunkTask(() => performance.noew() - now < 1)
    }, 1000)
  }
  performTasks(tasks, scheduler)
}

function performTasks(tasks, scheduler) {
  if (tasks.length === 0) {
    return
  }
  let i = 0

  // 每一次的执行
  function _run() {
    scheduler((goOn) => {
      while (i < tasks.length && goOn()) {
        tasks[i++]()
      }
      _run()
    })
  }

  _run()
}

function idlePerformTasks(tasks) {
  const scheduler = (chunkTask) => {
    requestIdleCallback((deadline) => {
      chunkTask(() => deadline.timeRemaining() > 0)
    })
  }
  performanceTasks(tasks, scheduler)
}
```

```scss
// 用Sass简化媒介查询
// 1. 函数的参数默认值
@mixin flex {
  display: flex;
  align-items: center;
  justify-content: center;
}

.container {
  @include flex;
}

// 2. 函数的参数默认值 + 内容块
@mixin flex($layout) {
  display: flex;
  align-items: $layout;
  justify-content: center;
  @content;
}

.container {
  @include flex(start) {
    gap: 20px;
  }
}

// 3. 函数的参数默认值 + 响应式
@mixin respondTo($breakname) {
  @if $breakname == 'phone' {
    @media (min-width: 320px) and (max-width: 480px) {
      @content;
    }
  }
  @if $breakname == 'pad' {
    @media (min-width: 481px) and (max-width: 768px) {
      @content;
    }
  }
}

.header {
  width: 100%;
  @include respondTo('phone') {
    height: 50px;
  }
  @include respondTo('pad') {
    height: 60px;
  }
}

// 4. 媒介查询的参数是对象
$breakpoints= {
  phone: (320px, 480px);
  pad: (481px, 768px);
  notebook: (769px, 1024px);
  desktop: (1025px, 1280px);
  tv: 1281px;
}

@mixin respondTo($breakname) {
  $bp: map-get($breakpoints, $breakname);
  @if type-of($bp) == 'list' {
    $min: nth($bp, 1);
    $max: nth($bp, 2);
    @media (min-width: $min) and (max-width: $max) {
      @content;
    }
  } @else {
    @media (min-width: $bp) {
      @content;
    }
  }
}
```

```text
https://juejin.cn/post/7362587412067385354
拖拽API
<div draggable="true></div>


dragstart
e.dataTransfer.effect = 'move'
dragend
dragenter
```

- 如何封装命令式组件
- https://blog.csdn.net/qq_42582773/article/details/140424340
- https://blog.csdn.net/qq_45487080/article/details/142994198
- https://blog.csdn.net/weixin_52648900/article/details/143166740

```js
const o = (function () {
  const obj = {
    a: 1,
    b: 2
  }
  return {
    get: function (k) {
      return obj[k]
    }
  }
})()
// 闭包代码的提权漏洞
// 如何在不改变上面代码的情况下，修改 obj 对象
Object.defineProperty(Object.prototype, 'abc', {
  get() {
    return this
  }
})
console.log(o.get('abc'))

// 解决
const o = (function () {
  // var obj = Object.create(null)
  const obj = {
    a: 1,
    b: 2
  }
  // Object.setPropertytypeOf(obj, null)
  return {
    get: function (k) {
      if (obj.hasOwnProperty(k)) {
        return obj[k]
      }
    }
  }
})()
```

```js
// 手写 call
Function.prototype.myCall = function (ctx, ...args) {
  ctx = ctx === null || ctx === undefined ? globalThis : Object(ctx)
  const fn = this
  const key = Symbol()
  Object.defineProperty(ctx, key, {
    value: fn,
    enumerable: false
  })
  const r = ctx[key](...args)
  delete ctx[key]
  return r
}

// 手写 bind
Function.prototype.myBind = function (ctx, ...args) {
  const fn = this
  return function (...restArgs) {
    // new.target 可以判断函数是否被 new 调用
    if (new.target) {
      return new fn(...args, ...restArgs)
    }
    return fn.apply(ctx, [...args, ...restArgs])
  }
}
```

```js
// 并发请求
function concurRequest(urls, maxNum) {
  if (urls.length === 0) return Promise.resolve([])
  return new Promise((resolve) => {
    let index = 0 // 指向下一次请求的 url 对应的下标
    const result = [] // 存储所有请求的结果
    let count = 0 // 当前完成的请求数量
    async function _request() {
      const i = index
      const url = urls[index]
      index++
      try {
        const resp = await fetch(url)
        result[i] = resp
      } catch (err) {
        result[i] = err
      } finally {
        count++
        if (count === urls.length) {
          resolve(result)
        }
        if (index < urls.length) {
          _request()
        }
      }
    }

    for (let i = 0; i < Math.min(urls.length, maxNum); i++) {
      _request()
    }
  })
}

/**
 * 可以重试的请求
 * 发出请求，返回 Promise
 * @param {string} url 请求地址
 * @param {number} maxCount 最大重试次数
 */
function request(url, maxCount = 5) {
  return fetch(url).catch((err) => {
    maxCount <= 0 ? Promise.reject(err) : request(url, maxCount - 1)
  })
}
```

```ts
// 对柯里化进行类型标注
type Curried<A extends any[], R> = A extends [] ? () => R : A extends [infer P] ? (x: P) => R : A extends [infer P, ...infer Rest] ? (x: p) => Curried<Rest, R> : never

declare function curry<A extends any[], R> (fn: (...args: A) => R): Curried<A, R>

柯里化是将接收多个参数的函数转换成接收一个单一参数的函数

组合是将两个或多个函数组合成一个新的函数，并且组合的函数从右到左执行

管道函数与组合函数
共同点：都可以将两个或多个函数组合成一个新的函数，新函数的执行结果等于连续调用多个原函数的执行结果
区别：组合函数是从右到左执行，而管道函数是从左到右执行

function pipe (...fns) {
  return function(x) {
    return fns.reduce(function(acc, fn) {
      return fn(acc)
    }, x)
  }
}
```

```js
// 构造函数内和外的方法有什么区别
class Person {
  constructor (name) {
    this.name = name
    this.say1 = () => {
      console.log('我在里面', this.name)
    }
  }

  say2 () {
    console.log('我在外面', this.name)
  }
}

const A = new Person('A')
const B = new Person('B')

A.say1()
A.say2()
A.say1 === B.say1
A.say2 === B.say2

①
在构造函数内部定义的方法，实际上是在 ** 每个对象实例 ** 上创建了一个新的函数
在构造函数外部定义的方法是在
Person
的原型对象(Person.prototype)
上创建的

②
在构造函数内部定义的方法是各个实例对象独有的
在构造函数外部定义的方法，所有Person实例共享的

③
在构造函数内部定义的方法可以被`Object.keys()`
遍历
在构造函数外部定义的方法不能被`Object.keys()`
遍历
```

```javascript
BigInt('0b' + a)
```

```css
/* 图片边框 */
border-image-source
border-image-slice
border-image-repeat
```

```js
// 如何将 class 转换为 function
// 初始化之前不能new
class Example {
  constructor(name) {
    this.name = name
  }

  func() {
    console.log(this.name)
  }
}

;('use strict') // 严格模式
function Example(name) {
  // 验证 this 的指向
  if (!(this instanceof Example)) {
    throw new TypeError('Class constructor Example cannot be invoked without "new"')
  }
  this.name = name
}

// 不可枚举
Object.defineProperty(Example.prototype, 'func', {
  value: function () {
    // 不可通过 new 调用
    if (!(this instanceof Example)) {
      throw new TypeError('Class constructor Example cannot be invoked without "new"')
    }
    console.log(this.name)
  },
  enumerable: false
})
```

```js
// 字符串比较
/**
 * 比较两个字符串的大小
 * 两个字符串都是用-连接的数字，比如1-2-33-41-5
 * 比较方式是从左到右，依次比较每个数字的大小，遇到相等的数字继续往后比较，遇到不同的数字直接得到比较结果
 * s1 > s2 return 1
 * s1 < s2 return -1
 * s1 === s2 return 0
 */
function compare(s1, s2) {
  while (1) {
    const iter1 = walk(s1)
    const iter2 = walk(s2)
    if (iter1.done && iter2.done) {
      return 0
    } else if (n1.done) {
      return -1
    } else if (n2.done) {
      return 1
    } else if (n1.value > n2.value) {
      return 1
    } else if (n1.value < n2.value) {
      return -1
    } else {
      continue
    }
  }
}

function* walk(str) {
  let n = ''
  for (let i = 0; i < str.length; i++) {
    const char = str[i]
    if (char === '-') {
      if (n) {
        yield +n
        n = ''
      }
    } else {
      n += char
    }
  }
  if (n) {
    yield +n
  }
}
```

```js
执行上下文
// ①
var name = 'global'
const obj = {
  name: 'LBJhui',
  fun1() {
    ;(() => {
      console.log(this.name)
    })()
  },
  fun2: () => {
    console.log(this.name)
  }
}
obj.fun1()
obj.fun2()

// ②
var length = 1

function fun() {
  console.log(this.length)
}

let arr = [fun, 'a', 'b']
arr[0]()
let fun2 = arr[0]
fun2()

// ③
var name = 'LBJhui'
let obj = {
  name: 'objLBJhui',
  say: function () {
    console.log(this.name)
  }
}
obj.say()
setTimeout(obj.say, 10)

// ④
var name = 'LBJhui'

function outerFunction() {
  this.name = 'outerFunction'
  return () => {
    console.log(this.name)
  }
}

const obj = {
  name: 'objLBJhui',
  innerFunction1: outerFunction(),
  innerFunction2: () => {
    console.log(this.name)
  }
}
obj.innerFunction1()
obj.innerFunction2()
```

```text
高阶函数：可以接收一个或多个函数作为参数，并且返回一个函数的函数称为高阶函数
  1.代码复用
  2.模块化和解耦
  3.延迟执行
  4.函数组合

用途：
  1.数组操作
  2.函数式编程
  3.异步编程
  4.代码重构和优化
  5.事件监听

使用高阶函数时需要考虑哪些性能因素
  1.函数调用开销
  2.内存使用
  3.垃圾回收
  4.并行和异步处理
  5.编译器优化
```

```text
如何在不同设备间同步用户的本地存储数据
  1.云同步服务
  2.websockets
  3.合并同步策略
  4.增量同步
  5.周期性全量同步增量更新
  6.第三方服务
  7.端到端加密
```

```text
如何处理跨域请求中的安全问题
  1.CORS策略
  2.HTTPS
  3.预检请求
  4.限制跨站请求伪造
  5.token验证
```

```text
禁用了js，本地存储还能使用吗
不能使用
  1.技术依赖
  2.数据交互通道封锁
  3.安全和隐私考量
```

```js
// 原型方法和实例方法
function Person() {
  Person.say = function () {
    console.log('a')
  }
  this.say = function () {
    console.log('b')
  }
}

Person.prototype.say = function () {
  console.log('c')
}

Person.say = function () {
  console.log('d')
}

Person.say()
var p = new Person()
p.say()
Person.say()
```

```ts
// 实现Optional
interface Article {
  title: string
  content: string
  tags: string[]
  comments: string[]
  likeCount: number
}

type Optional<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>

type CreateArticleOptions = Optional<Article, 'tags' | 'comments'>

// 实现GetOptionals
interface Article {
  title: string
  content: string
  tags: string[]
  comments?: string[]
  likeCount?: number
}

type GetOptional<T> = {
  [P in keyof T]: T[P]
}

type GetOptional1<T> = {
  [P in keyof T as `get${Capitalize<P & string>}`]: T[P]
}
type GetOptional2<T> = {
  [P in keyof T as never]: T[P]
}

Required<Article>
type GetOptional<T> = {
  [P in keyof T as T[P] extends Required<T>[p] ? never : P]: T[P]
}
```

```text
node 的模块查找策略
  文件查找
  文件夹查找
    默认 index.js
    可通过文件夹中 package.json 中 main 字段修改配置
  内置模块
  第三方
    node_modules
```

```text
Reflect
Proxy 和 DefineProperty
vue 3.0 使用 proxy 替代了 vue 2.x 中使用的 Object.defineProperty 来实现响应式系统，这种变化有以下几个原因：
1.更强大的拦截能力:Proxy 提供了更丰富的拦截器,可以拦截更多的的操作,包括属性的读取、设置、删除、函数调用、in运算符等。这使得Vue可以更好地跟踪数据的变化,并在之前无法拦截的场景下提供更精确的响应式行为。
2.更直观和高效的代码:Proxy 的拦截能力更加直观和灵活,可以通过简单且可读性更高的代码实现复杂的操作。相比之下,使用 Object.defineProperty 手动地处理每个属性的getter和setter更加繁琐和冗长。
3.更好的性能和更少的内存消耗:Proxy 采用代理对象的方式,只需要在读取和修改属性时触发拦截器,而不需要获取和设置属性的特性。这种方式可以带来更好的性能,并且不会对每个属性都添加额外的setter和getter。
4.支持嵌套对象的响应式:使用 Proxy 可以实现对嵌套对象的响应式处理,而 Object.defineProperty 在处理嵌套对象时需要遍历和递归操作,相比之下,Proxy 更加高效和简洁。
总而言之,Vue 3.0选择使用 Proxy 替代 Object.defineProperty 是为了提供更强大、直观、高效的响应式能力,并且能够支持更复杂的场景,同时带来更好的性能和更少的内存消耗。这使得Vue3.0在开发体验和性能方面均有很大的提升。

vue2和3有什么区别
  1.用组合式api替换选项式api，方便逻辑更加的聚合
  2.一些细节的使用点改变
    1.因为改成组合式api所以没有this
    2.生命周期没有create，setup等同于create，卸载改成unmount
    3.vue3中v-if高于v-for的优先级
    4.根实例的创建从new app变成了createApp方法
    5.一些全局注册，比如mixin，注册全局组件，use改成了用app实例调用，而不是vue类调用
    6.新增了传送门teleport组件
    7.template模板可以不包在一个根div里

  1.响应式原理改成了用proxy，解决了数组无法通过下标修改，无法监听到对象属性的新增和删除的问题。也提升了响应式的效率
  2.可以额外叙述vue3并不是完全抛弃了defineProperty，通过reactive定义的响应式数据使用proxy包装出来，而ref还是用的defineProperty去给一个空对象，定义了一个value属性来做的响应式
  3.组合式api的写法下，源码改成了函数式编程，方便按需引入，因为tree-shaking功能必须配合按需引入写法。所以vue3更好地配合tree-shaking能让打包体积更小
  4.性能优化，增加了静态节点标记。会标记静态节点，不对静态节点进行比对，从而增加效率
  5.此外大家可以叙述具体标记策略，从而提升自己的印象
```

```text
vue-watch value 更新 → 触发回调函数 → DOM 更新
{flush:'pre'}
pre(默认)：回调函数会在 DOM 更新之前执行
post：回调函数会在 DOM 更新之后执行，在实际开发中，假设你希望滚动到页面的某个位置再执行回调，可以用这个
sync:回调函数会同步执行，也就是在响应式数据发生变化时立即执行

watch 只能收集同步代码的依赖，如果存在 await 依赖收集会出现问题

①
watchEffect 会自动追踪函数内部使用的数据变化，数据变化时重新执行该函数
watch 需要显示地指定监听的数据，若指定的数据发生变化，重新执行该函数

②
watchEffect 的函数会立即执行一次，并在依赖的数据变化时再次执行
watch 的回调函数只有在侦听的数据源发生变化时才会执行，不会立即执行

③
watch 可以更精细地控制监听行为，如 deep、immediate、flush
watchEffect 更适合简单的场景，不需要额外的配置。相当于默认开启了 deep、immediate
```

```vue
<script>
// ①
let clicked = false
watchEffect(() => {
  if (clicked) {
    console.log('更新了 msg', msg.value)
  }
})

// ②
watchEffect(async () => {
  await fetchData()
  console.log(`第${count}次请求数据`)
})
</script>
```

```js
// 统计字符频率的风骚写法
const str = 'dlskdlkdsowjfood'
const result = [...str].reduce((a, b) => (a[b]++ || (a[b] = 1), a), {})

// 数字格式化
const str = '10000000000'
const s = str.replace(/\B(?=(\d{3})+$)/g, ',')
```

```js
// vue-router
base: '/'

// vue.config.js
publicPath: '/' // 浏览器如何找资源
```

```css
/* 系统主题 */
@media (prefers-color-scheme: dark) {
}

@media (prefers-color-scheme: light) {
}

/* js */
const match =matchMedia

(
'(prefers-color-scheme: dark)')
match.
addEventListener

(
'change'
,
(
e

)
=
> {
}

)
```

```scss
// SASS中的颜色函数
$btnColors: #409eff, #67c23a, #f56c6c, #e6a23c, #909399;

@for $i from 1 through length($btnColors) {
  .btn.type-#{$i} {
    $color: nth($btnColors, $i);
    background: $color;
    color: #fff;

    &:hover {
      background: lighten($color, 10%);
    }

    &:active {
      background: darken($color, 10%);
    }

    &:disabled {
      background: lighten($color, 20%);
    }
  }
}
```

```text
Cookie 中的 SameSite：用于限制跨站请求
None:不作任何限制，使用该值必须保证 Cookie 为 Secure，否则无效
lax:阻止发送 Cookie，但对超链接放行，默认值
strict:阻止发送 Cookie
```

- Typescript 中的 this 和 JavaScript 中的 this 有什么差异？
  TS：noImplicitThis:true 必须去声明 this 类型，才能在函数或者对象中使用 this
- 对象展开会有什么副作用
  1. 展开对象后面的属性会覆盖前面的属性
  2. 仅包含可枚举的属性，不可枚举属性丢失

```text
CSS属性值的计算过程
getComputedStyle
1.确定声明值
2.层叠
  1. 比较重要性
    重要性从高到低：
      1.带有 important 的作者样式
      2.带有 important 的默认样式
      3.作者样式
      4.默认样式
  2.比较特定性（权重）
  3.比较源次序：源码中靠后的覆盖靠前的
3.继承
  对仍然没有值的属性，若可以继承则使用继承
4.使用默认值
  对仍然没有值的属性，使用默认值
```

```text
垃圾回收监听：FinalizationRegistry
引用计数
标记清除
memory
management
```

```text
如何优化js代码的执行效率
  1.代码压缩与合并
  2.模块化和懒加载
  3.缓存和持久化
  4.优化循环和数组操作
  5.减少 DOM 操作
  6.避免阻塞 UI 线程
  7.减少重绘和回流
```

```css
/* 你不知道的 CSS 选择器 */
:focus-within
:has()
::first-letter
::selection
```

```text
什么是WebSocket，以及它与传统的HTTP长轮询相比的优势
  1.持久链接
  2.双向通信
  3.低延迟
  4.减少资源消耗
  5.消息帧格式
```

```js
// 状态仓库持久化
// vuex 全部
//store.js
import persistPlugin from './persistPlugin'

const store = createStore({
  modules: {
    counter,
    test,
  },
  plugins: [persistPlugin],
})

// persistPlugin
const KEY = 'VUEX"STATE'

export default function(store) {
  // 存
  window.addEventListener('beforeunload', () => {
    localStorage.setItem(KEY, JSON.stringify(store.state))
  })
  // 取
  try {
    const state = JSON.parse(localStorage.getItem(KEY))
    if (state) {
      store.replaceState(state)
    }
  } catch {
    console.log('存储的数据有误')
  }
}

// pinia 单个模块
//main.js
import { createPinia } from 'pinia'
import persistPlugin from './store/persistPlugin'

const pinia = createPinia()
pinia.use(persistPlugin)

// persistPlugin
const KEY_PREFIX = 'PINIA:STATE'
export default function(context) {
  // 存
  window.addEventListener('beforeunload', () => {
    localStorage.setItem(KEY_PREFIX + store.$id, JSON.stringify(store.$state))
  })
  // 取
  try {
    const state = JSON.parse(localStorage.getItem(KEY_PREFIX + store.$id))
    if (state) {
      store.$patch(state)
    }
  } catch {
  }
}
```

```js
// 统一vite中的图片转换逻辑
import fs from 'node:fs'

const myPlugin = (limit = 4096) => {
  return {
    name: 'my-plugin',
    transform: async (code, id) => {
      if (process.env.NODE_ENV !== 'development') return
      if (!/\.(png|jpe?g|gif|webp|svg)$/.test(id)) {
        return
      }
      const state = await fs.promise.stat(id)
      if (state.size > limit) {
        return
      }
      const buffer = await fs.promise.readFile(id)
      const base64 = buffer.toString('base64')
      const dataurl = `data:image/png;base64,${base64}`
      return {
        code: `export default ${dataurl}`
      }
    }
  }
}

export default definConfig({
  build: {
    // 统一vite中的图片转换逻辑
    assetsInlineLimit: 0,
    rollupOptions: {
      // 在vite中手动分包
      manualChunks(id) {
        if (id.includes('node_modules')) {
          return 'vendor'
        }
      },
      // vite打包结构控制
      output: {
        entryFileNames: 'js/[name]-[hash].js',
        chunkFileNames: 'js/[name]-[hash].js',
        assetFileNames(assetInfo) {
          if (assetInfo.name.endsWith('.css')) {
            return 'css/[name]-[hash].css'
          }
          const imgExts = ['.png', '.jpg', '.jpeg', '.webp', '.svg', '.gif', '.ico']
          if (imgExt.some((e) => assetInfo.name.endsWith(e))) {
            return 'imgs/[name]-[hash].[ext]'
          }
          return 'asset/[name]-[hash].[ext]'
        }
      }
    }
  }
})
```

```
什么是 vue 的响应式？
**vue 数据响应式设计的初衷是为了实现数据和函数的联动**，当数据变化后，用到该数据的联动函数会自动重新运行。
具体在 vue 开发中，数据和组件的 render 函数关联在一起，从而实现了数据变化自动运行 render，在感官上就看到了组件的重新渲染。
除了 vue 自动关联的 render 函数，其他还有很多使用到 vue 响应式的场景，比如 computed、watch 等等，不能仅把 vue 的数据响应式想象成和 render 的关联。

函数与数据的关联
  1. 被监控的函数
    render
    computed 回调
    watch
    watchEffect
  2. 函数运行期间用到了响应式数据
  3. 响应式数据变化会导致函数重新运行
```

```txt
GET 和 POST 的区别？
协议层面：**语义区别**
应用层面：**GET 请求体为空**
浏览器层面：
```

```js
// 打包体积的分析和优化:webpack-bundle-analyzer
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin
if (process.env.NODE_ENV === 'production') {
  let aPlugin = new BundleAnalyzerPlugin()
  module.exports = {
    devtool: 'none',
    plugins: [aPlugin],
    externals: {
      // 公共库通过 cdn 引入，浏览器会缓存
      vue: 'Vue'
    }
  }
}
```

```
拼音标注
<ruby></ruby>
import pinyin from 'pinyin';
判断是不是中文
```

```js
// 监控页面是否出现卡顿 performance API
const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
  }
})
observer.observe({ entryTypes: ['longtask'] })
```

```text
网络
  五层网络模型
  TCP/IP
  HTTP
  AJAX
  跨域及解决方案
  JWT
  cookie
  sessionnavigator.hardwareConcurrency
  缓存协议
  CSRF
  XSS
  网络性能优化
  分片传输
  SSL/TLS/HTTPS
  HTTP2
  WebSocket
```

```text
动画
Web Animation API: element.
animate()


element.getAnimations()
requestAnimationFrame
dom.addEventListener('transitionend') transitionstart  view transitions API
document.startViewTransition()
animationend
逐帧动画 step anima
tion: name 1s steps(5)
动画的暂停和恢复:animation-play-state paused running
dom.style.setProperty('--name','value')


display none元素也能transition过渡
transition-behavior:allow-discrete; 隐藏动画
transition-behavior:normal;
@starting-style 显示动画

img{
  transition-duration:.25s;
  transition-behavior:allow-discrete;
}
@starting-style{
  img{
    opacity: 0;
  }
}


平滑滚动
css:scroll-behavior
js: window.scrollTo({
  top: 0,
  behavior: 'smooth'
})

如何阻止滚动嵌套冒泡 ` overscroll-behavior:contain`
  /* 设置滚动条样式 */
scrollbar-face-color: #eaeaea;
scrollbar-shadow-color: #eaeaea;
scrollbar-highlight-color: #eaeaea;
scrollbar-3dlight-color: #eaeaea;
scrollbar-darkshadow-color: #697074;
scrollbar-track-color: #f7f7f7;
scrollbar-arrow-color: #666666;

/* 使用CSS实现滚动吸附效果 */
scroll-snap-type: mandatory;
scroll-snap-align: center;
scroll-snap-stop: always;

/* 纯css实现页面滚动动画 */
scroll-timelin-name
animation-timeline /* https://www.zhangxinxu.com/wordpress/2024/08/css-scroll-timeline/ */
animation-range
动画库 vueusemotion
cubic-bezier
css 动画只支持数值类的属性
Houdini API @property https://developer.mozilla.org/zh-CN/docs/Web/API/Houdini_APIs

剪切函数 clip-path
background-clip
mix-blend-mode background-blend-mode
```

```html
鼠标位置信息：pageX,clientX,offsetX,movementX 原始尺寸 naturalWidth naturalHeight 样式尺寸 缩放倍率 window.devicePixelRatio

<img srcset="https:picsum.photos/200/300?random=1 1x, https:picsum.photos/400/600?random=1 2x" />
<img
  srcset="https:picsum.photos/200/300?random=1 200w, https:picsum.photos/400/600?random=1 400w"
  sizes="
    (max-width: 300px)50vw,
    (max-width: 600px) 50vw,
    50vw
  " />

原始尺寸=样式尺寸*缩放倍率 元素尺寸： - clientWidth：content + padding - offsetWidth：content + padding + scroll(滚动条) + border - scrollWidth：visible + invisible - 可见尺寸 getBoundingClientRect()
dom.style.width DOM树 getComputedStyle(dom).width CSSOM树 layout tree 布局树 几何信息
```

```js
addEventListener('onerror', {
  passive: false
})

// Clipboard API
navigator.clipboard.readText().then((text) => {})

// 事件
copy paste
document.addEventListener('copy', (e) => {
  e.preventDefault()
  navigator.clipboard.writeText("不准复制")
})
```

```css
/* 调整文字方向： */
writing-mode、
margin-block-start、
margin-block-end、
text-combine-upright
margin-inline-start
text-align:start/end;
text-orientation
```

```js
// 读取文件原始内容
// webpack: raw-loader
module.exports = defineConfig({
  configureWebpack: {
    module: {
      rules: [
        {
          test: /\.dataurl$/,
          loader: 'raw-loader'
        }
      ]
    }
  }
})

// vite: ?raw
import data from './data.dataurl?raw'

// vite 寻找 views 文件夹中所有的 page.js
import.meta.glob('../views/**/page.js', {
  eager: true,
  import: 'default'
})
```

```
保持元素宽高比
css 属性: aspect-ratio
padding 相对于包含块宽度
```

```js
// 手动解析 DOM 树: removeTag
new DOMParser().parseFromString(str, 'text/html')
```

```html
show,showModel
<dialog open></dialog>
::backdrop
```

- 说说 webpack5 联邦模块在微前端的应用
- 说说现有的几种微前端框架，它们的优缺点？

```markdown
**小程序 已被代码依赖分析忽略，无法被其他模块引用。你可根据控制台中的【代码依赖分析】告警信息修改代码，或关闭【过滤无依赖文件】功能**

只需在“project.config.json”=>“setting”里面将"ignoreDevUnusedFiles"和"ignoreUploadUnusedFiles"都设置为 false，然后保存，重新编译即可。

"ignoreDevUnusedFiles": false,
"ignoreUploadUnusedFiles": false,
```

```js
// js将大数字单位转化成 千、万、千万、亿
function transform(value: number) {
  let newValue = ['', '', '']
  let fr = 1000
  const ad = 1
  let num = 3
  const fm = 1
  while (value / fr >= 1) {
    fr *= 10
    num += 1
    console.log('数字', value / fr, 'num:', num)
  }
  if (num <= 4) {
    // 千
    newValue[1] = '千'
    newValue[0] = parseInt(value / 1000) + ''
  } else if (num <= 8) {
    // 万
    const text1 = parseInt(num - 4) / 3 > 1 ? '千万' : '万'
    // tslint:disable-next-line:no-shadowed-variable
    const fm = '万' === text1 ? 10000 : 10000000
    newValue[1] = text1
    newValue[0] = value / fm + ''
  } else if (num <= 16) {
    // 亿
    let text1 = (num - 8) / 3 > 1 ? '千亿' : '亿'
    text1 = (num - 8) / 4 > 1 ? '万亿' : text1
    text1 = (num - 8) / 7 > 1 ? '千万亿' : text1
    // tslint:disable-next-line:no-shadowed-variable
    let fm = 1
    if ('亿' === text1) {
      fm = 100000000
    } else if ('千亿' === text1) {
      fm = 100000000000
    } else if ('万亿' === text1) {
      fm = 1000000000000
    } else if ('千万亿' === text1) {
      fm = 1000000000000000
    }
    newValue[1] = text1
    newValue[0] = parseInt(value / fm) + ''
  }
  if (value < 1000) {
    newValue[1] = ''
    newValue[0] = value + ''
  }
  return newValue.join('')
}
```

```text
-webkit-text-stroke 居中描边
paint-order 配合 -webkit-text-stroke 使用，值为 stroke 时，外描边
paint-order:markers|stroke|fill
text-shadow：只适合小的外描边
```

- 简单介绍 requestIdleCallback 及使用场景
  `requestIdleCallback` 维护一个队列，将在浏览器空闲时间内执行。它属于 Background Tasks API，你可以使用 `setTimeout` 来模拟实现

  ```javascript
  window.requestIdleCallback =
    window.requestIdleCallback ||
    function (handler) {
      let startTime = Date.now()

      return setTimeout(function () {
        handler({
          didTimeout: false,
          timeRemaining: function () {
            return Math.max(0, 50.0 - (Date.now() - startTime))
          }
        })
      }, 1)
    }
  ```

  可以在 `ric` 中执行任务时需要注意以下几点：

  1. 执行重计算而非紧急任务
  2. 空闲回调执行时间应该小于 50ms，最好更少
  3. 空闲回调中不要操作 DOM，因为它本来就是利用的重拍重绘后的间隙空闲时间，重新操作 DOM 又会造成重拍重绘

- 前端上传文件时如何读取文件内容
  ```html
  <input type="file" id="input" onchange="handleFiles(this.files)" />
  ```
  在浏览器中，通过 `input[type=file]` 来点击上传文件，此时监听 `onChange` 事件，可以获取到 `File` 对象，其中从中可以读取文件内容
  而读取文件内容，需要转化 `File/Blob` 到 `Text`，一般使用以下两种方案
  **FileReader API**
  这是最常用处理上传文件的 API，但是却繁琐冗余难记，每次使用基本上都要查文档！
  `FileReader API` 用以读取 File/Blob 内容，正因为繁琐难记，以下实现一个 `readBlob` 函数读取内容。
  ```javascript
  function readBlob(blob) {
    return new Promise((resolve) => {
      const reader = new FileReader()
      reader.onload = function (e) {
        resolve(e.target.result)
      }
      reader.readAsText(blob)
    })
  }
  ```
  **Response API** 而是用 `Response API` 只需要一行内容
  ```javascript
  const readBlob = (blob) => new Response(blob).text()
  ```
- computed、methods、watch 有什么区别？
  1. computed 和 methods 的区别
     computed 是有缓存的，methods 没有缓存
  2. computed 和 watch 的区别
     watch 是监听，数据或者路由发生了改变才可以响应（执行）
     computed 计算某一个属性的改变，如果某一个值改变了，计算属性会监测到进行返回
     watch 是当前监听到数据改变了，才会执行内部代码
- computed 的值可以用 v-model 绑定吗？
  不可以。准确地说，用 v-model 绑定了 computed 的值后，可以在绑定的元素中得到 computed 的结果，但不能实现双向绑定。
  v-model 通常用来绑定 input、select 等标签，目的是为了实现双向绑定，当原始属性发生变化时，绑定标签的值也会发生变化；当标签的值发生变化时，原始属性同样变化。而 computed
  是通过原始属性计算出的结果，是单向只读的，不能直接修改。
- mutations 和 actions 区别
  action 提交的是 mutation，而不是直接变更状态
  action 可以包含任意异步操作
- JS 中的计时器是否能精确计时？为什么？
  1. 硬件
     原子钟
  2. 系统
     操作系统的计时
  3. 标准 w3c
     setTimeout `>=5` 的嵌套层级，最小 4ms
  4. 事件循环
- ref 与 toRef 的区别是什么？
  1. ref 本质是将原数据进行拷贝，然后通过 proxy 转为响应式数据；所以不管是修改原数据还是修改响应式数据，它们是不会受到影响的
  2. toRef 本质是将一个对象的一个属性，通过 ref 转为响应式数据，是引用关系；且不管是修改源数据还是修改 toRef 后的数据，两者都会改变
  3. ref 数据发生变化后，界面会马上更新；toRef 数据发生变化后，界面不会自动更新
  4. ref 方法只接收一个参数，toRef 接收两个参数
- vue3 如何实现一个组件的异步加载？
  1. Suspense
  2. defineAsyncComponent
- 前端性能优化的手段？
  1. 减少重绘和回流
  - 使用 transform 和 opacity 替代 position、width 和 height 来进行动画
  - 使用 will-change 来提前告知浏览器某个属性将要发生变化
  2. 减少 HTTP 请求：
  - 合并和压缩 css、JavaScript 和图像文件
  - 使用字体图标代替图像
  3. 使用缓存
  - 利用浏览器缓存机制，设置合适的缓存头
  - 利用 Service Workers 实现离线缓存
  4. 异步加载资源
  - 将脚本移到页面底部
  - 使用异步加载脚本或延迟加载脚本
  5. 优化图像
  - 使用适当的图像格式
  - 压缩图像以减小文件大小
  - 使用图像懒加载，仅加载用户可见区域的图像
  6. 优化 CSS 和 JavaScrip
  - 合并和压缩 css、JavaScript 文件
  - 移除不必要的注释和空白
  - 使用 Tree-shaking（对于 JavaScript）来去除未使用的代码
  7. 使用 CDN（内容分发网络）
  - 将静态资源部署到全球 CDN 上，减少网络延迟
  8. 懒加载和分块加载
  - 使用懒加载加载视口内的内容
  - 使用按需加载（Code Splitting）分割大型 JavaScript 文件
  9. 优化字体加载
  - 仅加载页面所需的字体变体
  - 使用 font-display: swap 属性来优化字体加载
- 如何将一个字符串转为二进制？
  1. 将字符串转为字符数组
  2. 遍历字符数组，使用 charCodeAt() 将每个字符元素转为 ASCII 码
  3. 使用 toString(2) 将 ASCII 码元素转为二进制
  4. 使用 join() 拼接数组元素，转为二进制字符串\
- 微信小程序面试题：组件与普通页面有什么不同？
  1. 组件的 .js 文件执行的 Component() 函数，页面 .js 文件执行的是 Page() 函数
  2. 组件在 .json 文件中必须声明 "component": true 属性
  3. 组件的事件处理函数需要定义到 methods 节点中
  4. 生命周期不同
- rgba 和 opacity 都可以设置透明度，它们有什么不同？
  1. rgba 指的是颜色，rgb 分别是红、绿、蓝，a 指 Alpha 透明度。所以 rgba 只能作用于颜色；而 opacity 作用于整个元素
  2. opacity 会被子元素继承；rgba 不会
- 匹配字符
  ```javascript
  let reg = new RegExp(key, 'gi')
  str.replace(reg, '替换值或回调函数')
  ```
- 如何实现自适应布局
  无限适配方案 + rem 单位
  无限适配的核心原理：把屏幕划分为一定的份数（10 份），通过 JS 动态监测屏幕尺寸宽度，实时计算并设置 html 元素的基础字体大小
- CDN
  CDN：内容分发网络，是一组分布在世界各地的服务器网络，可以为全球用户提供快速、安全的内容传送服务
  原理：
  1. CDN 服务器在全球各地分布
  2. 用户访问网站的时候，用户浏览器会向最近的 CDN 发送请求
  3. CDN 服务会把内容缓存在离用户最近的服务器上面，把内容返回给用户
     作用：
  4. 提高页面的加载速度
  5. 减轻源服务器的负担
  6. 提高网站的可用性
- 文字转语音
  如何把文字转语音
  web api：语音不统一/兼容性
  第三方平台
  优化：
  断句
  并发控制
  缓存
  客户端 localStorage（md5 base64）
  服务器

- SPA 的优缺点，以及在何种场景下更适合使用 SPA
  优点：
  用户体验好
  性能好
  前后端分离
  组件化和模块化
  更好的客户逻辑处理
  缺点：
  初始化加载时间比较长
  SEO 问题比较严重
  复杂性比较高
  不利于离线浏览
  场景：
  项目侧重于用户体验
  对于一些需要保持高度一致性的 UI 设计和交互
  对项目有足够的资源投入，并且可以承担初始化加载时间较长
- 如何避免 JavaScript 中的全局变量污染？
  1. 立即执行函数
  2. 严格模式
- 谈谈移动端布局的几种方式

  1. 流式布局
     相对单位定义元素的宽高
  2. 固定宽度布局
  3. 响应式布局
     弹性布局+媒体查询
  4. 栅格布局
  5. flex 布局（弹性布局）
  6. 瀑布流

- 响应式设计
  网站在不同的设备和屏幕尺寸上都可以提供一致的用户体验
  原理：
  1. 弹性和网格布局
  2. 弹性图片：图片会根据屏幕大小进行调整
  3. 媒体查询
  4. 流式布局
  5. 适应图片
- rem 和 em 的区别是什么？
  px em rem 区别
  1. px：固定值绝对单位
  2. em：相对单位：相对于它的父元素的字体大小
  3. rem：相对单位：相对于根元素（html）字体大小
  4. rem
     相对于根元素的字体大小来计算的
     根元素的 font-size：16px，另外一个元素 width:1rem
  5. em
     em 相对于当前元素的父元素字体大小来计算
     如果父元素设置了字体大小，子元素使用 em 单位，它的大小会受到父元素字体大小的影响
- 清除浮动的方法有哪些？伪元素清除的原理是什么？
  1. 额外标签法
     浮动元素之后添加一个空 div 或其他块级元素，并设置 clear:both
  2. 使用 overflow 属性触发 BFC
     浮动元素的父容器上设置 overflow:hidden
  3. 伪元素清除法
     利用 after 伪元素为浮动元素的父容器添加看不见的内容，然后设置 clear:both;display:block;content:''
  4. 直接设置高度

```javascript
// 手写 forEach
const arr = [1, 2, 3]
arr.forEach((item) => {
  arr.push(2)
  console.log('arr', item)
})

arr.forEach((item, i) => {
  arr.splice(i, 1)
  console.log('arr', item)
})

const arr1 = [, , 3]
arr1.forEach((item) => {
  console.log('arr', item)
})

Array.prototype.forEach = function (callback) {
  const len = this.length
  if (typeof callback !== 'function') {
    throw new TypeError(callback + 'is not a function')
  }
  let k = 0
  while (k < len) {
    if (k in ths) {
      callback(this[k], k, this)
    }
    k++
  }
}
```

```javascript
// 立即执行函数
;(function test() {
  test = 'LBJhui'
  console.log(test)
})()
// 函数的名称是只读的，所以不能在函数内部修改函数的名称。因此函数内部 test = 'LBJhui' 这行代码其实是无效的
```

- 在前端开发中如何优化 DOM 操作以提高页面性能
  1. 减少 DOM 查询
  2. 批量处理 DOM 操作
  3. 避免不必要的重排重绘
  4. 使用现代 api
  5. 异步编程和延迟加载
  6. 使用原生方法替代字符串操作
  7. 事件委托
- CORS 的工作原理是什么？
  预检请求
  服务器响应
  实际请求和响应
  浏览器检验
- JSONP 是什么？它是如何绕过同源策略的
  利用浏览器对 script 标签的特殊处理来规避同源策略的限制
  原理核心：
  机制
  - 客户端请求
  - 服务端响应
  - 客户端处理
    绕过同源策略
    场景限制：GET
- scoped 原理
  1. 作用：让样式在本组件中生效，不影响其他组件
  2. 原理：给结点新增自定义属性，然后 css 根据属性选择器添加样式
- 什么是 XSS 攻击？如何防止 XSS 攻击？
  XSS：指攻击者通过在目标网站输入字段中注入恶意脚本代码，当其他用户浏览这个网站的时候，脚本会在他的浏览器中执行，获取用户的敏感信息。
  防止措施：
  1. 输入验证和过滤
  2. 输出编码
  3. 使用 HTTP 头部设置
  4. 妥善管理 cookies
  5. 建立安全的开发实践
  6. 更新和软件升级
- Vue 路由模式
  路由模式有两种：history、hash
  区别：
  1. 表现形态不同
  2. 跳转请求，路径不存在时，history 会发送请求，hash 不会发送请求
  3. 打包后前端自测要使用 hash，如果使用 history 会出现空白页
- 在处理跨域时，如果考虑安全性因素
  1. 精确控制允许的源
  2. 限制请求方法和头信息
  3. 预检请求验证
  4. 使用 https
  5. 设置适当的 CSP 策略
  6. 验证和过滤请求数据
  7. 限制第三方 API 使用
  8. 实施速率限制
  9. 日志和监控
- post 请求和 get 请求在跨域时有何不同？
  当涉及到跨域请求（Cross-Origin Requests）时，POST 请求和 GET 请求之间存在一些关键的不同点，特别是在处理浏览器中的 CORS（跨来源资源共享）策略时。以下是它们之间的主要差异：
  1. **预检请求（Preflight Request）**：
  - 对于某些 CORS 请求，浏览器会首先发送一个 OPTIONS 请求作为预检请求，以检查服务器是否允许跨域请求。这通常发生在“非简单请求”中，即那些不符合简单请求条件的请求。简单请求的条件包括：请求方法只能是
    HEAD、GET 或 POST，请求头只能包含一些特定的字段（如 Accept、Accept-Language、Content-Language、Content-Type 等），且 Content-Type 的值仅限于`application/x-www-form-urlencoded`、
    `multipart/form-data`或`text/plain`。
  - 对于 POST 请求，如果它包含自定义的 HTTP 头或 Content-Type 字段的值不是上述的“简单”值，那么它通常会触发预检请求。而 GET 请求由于其性质（通常只用于检索数据）和简单性，很少会触发预检请求。
  2. **缓存**：
  - 浏览器可能会对 GET 请求的响应进行缓存，这意味着对于相同的 URL 和请求头，浏览器可能会从缓存中加载响应而不是重新发送请求到服务器。但是，POST 请求通常不会被缓存，因为它们是用于提交数据的，而数据可能会经常变化。
  - 在跨域场景中，这种缓存行为可能会影响请求的性能和结果。如果 GET 请求的响应被缓存，并且服务器上的数据已经更改，那么客户端可能会获取到旧的、不准确的数据。
  3. **安全性**：
  - 从安全性的角度来看，POST 请求通常用于提交数据（如表单数据、文件上传等），而 GET 请求则用于检索数据。因此，在跨域场景中，使用 POST 请求提交敏感数据可能更安全一些，因为它不太可能被缓存或记录在浏览器的历史记录中。但是，这并不意味着
    POST 请求本身就更安全；它仍然需要适当的安全措施（如 HTTPS、身份验证和授权等）来保护数据。
  4. **请求体（Request Body）**：
  - GET 请求通常没有请求体（尽管某些 HTTP 客户端和服务器可能允许在 GET 请求中包含请求体，但这并不是标准做法）。因此，跨域 GET 请求不能用于发送大量数据到服务器。相反，POST
    请求可以包含请求体，并用于发送大量数据到服务器。
  5. **幂等性**：
  - GET 请求是幂等的，即多次执行相同的 GET 请求不会产生不同的结果（除非有副作用，如数据更新或删除）。这使得 GET 请求在跨域场景中更加可靠和可预测。相比之下，POST 请求通常不是幂等的，因为每次执行
  - POST 请求都可能会产生不同的结果（例如，创建新的资源或更新现有资源）。
  6. **浏览器限制**：
  - 某些浏览器可能会对 GET 请求的 URL 长度施加限制（尽管这个限制可能因浏览器和版本而异）。如果 URL 超过了这个限制，那么 GET 请求可能会失败。相比之下，POST 请求没有这样的限制，因为数据可以包含在请求体中而不是 URL 中。因此，在需要发送大量数据或复杂查询参数的跨域场景中，POST 请求可能更合适。
- 解释一下 CSP 与跨域的关系
  CSP（Content Security Policy）与跨域（Cross-Origin）在 Web 安全领域中是两个重要的概念，但它们各自关注的安全问题和实现机制有所不同。以下是关于 CSP 与跨域关系的详细解释：
- CSP（内容安全策略）
  1. **定义**：CSP 是为了缓解跨站脚本（XSS）等安全威胁而引入的一种安全机制。它允许网站开发者创建并强制应用一些规则，以管理网站允许加载的内容。
  2. **工作原理**：CSP 以白名单的机制对网站加载或执行的资源起作用。在网页中，这样的策略通过 HTTP 头信息或者 meta 元素定义。例如，通过设置`Content-Security-Policy` HTTP
     头，可以限制哪些外部资源（如脚本、样式表、图片等）可以被加载和执行。
  3. **限制与影响**：CSP 虽然提供了强大的安全保护，但也可能造成一些限制，如 Eval 及相关函数被禁用、内嵌的 JavaScript 代码将不会执行、只能通过白名单来加载远程脚本等。这些限制可能会增加开发者的工作量，需要花费更多时间来分离内嵌的
     JavaScript 代码和调整应用逻辑。
- 跨域（Cross-Origin）
  1. **定义**：跨域是指一个域下的文档或脚本试图去请求另一个域下的资源。由于浏览器的同源策略（Same-Origin Policy），跨域请求通常会被限制或阻止，以防止恶意脚本攻击和数据泄露。
  2. **同源策略**：同源策略要求协议、域名和端口三者都相同才被认为是同源的。如果其中任何一个不同，则被视为跨域。
  3. **解决方案**：为了实现跨域请求，开发者可以采用一些技术手段，如 CORS（跨来源资源共享）、Proxy（代理）和 JSONP 等。这些技术允许服务器设置特定的响应头（如`Access-Control-Allow-Origin`），以允许来自不同源的请求。
- CSP 与跨域的关系
  - **独立性**：CSP 和跨域是两个独立的概念，各自关注不同的安全问题。CSP 关注的是如何限制和管理网站加载的内容，而跨域关注的是如何允许或限制来自不同源的请求。
  - **相互影响**：在某些情况下，CSP 的设置可能会影响跨域请求的实现。例如，在使用 CSP 限制脚本加载时，如果跨域请求需要加载并执行远程脚本，可能会受到 CSP 策略的限制。同样，跨域请求的实现也可能需要考虑
    CSP 策略的影响，以确保请求的资源符合 CSP 规则。
    综上所述，CSP 和跨域在 Web 安全领域中各自扮演着重要的角色。开发者需要根据实际需求合理配置 CSP 策略和跨域请求的实现方式，以确保 Web 应用的安全性和可用性。
- 对于多机型是怎么进行做到兼容的？
- 营销活动页面性能应该是很重要的，在性能方面是怎么做保障的？
- 对页面的性能怎么做优化的？
- 懒加载是怎么做的？路由级别还是组件级别的？
- 假设做到一个组件级别的懒加载要怎么做？
- 提到了 Webpack5，Webpack 中的 MF 是什么？相比于 npm 包有什么区别？
- webpack 优化
- webpack 的 require 是如何查找依赖的
- webpack 如何实现动态加载
- webpack 插件原理，如何写一个插件
- 组件支持嵌套吗？
- 图片上画热区，让你实现一下你要怎么做？
- 用户在你们平台配置完之后，点击发布，需要做一下构建吗？
- 这算是一个中心化的页面，组件比较多，而且都是写在一个页面上，风险比较大？
- source-map 的解析的工作怎么做的？
- source-map 要和项目关联？怎么做的？
- source-map 的接入成本较高怎么办？如果你动态更新了，如何通知用户？
- 假设让你去设计上报这个 sdk，你怎么设计？
- 如何保证你的 sdk，不影响业务，不阻断，不报错，无感知。
- SSR 相对于 CSR，改造成 SSR 的成本
- 首屏加载时长如何获取？直接获取可能不准？
- 怎么去劫持 AJAX？
- 假设我的 sdk 要在业务代码之后加载，但是业务代码中又调用了 sdk 的 API 怎么办？
- h5 页面搭建工具当时是怎么分工的？
- 假设你的 h5 页面搭建平台要和组件的发布能力解耦，要怎么做？
- 场景题：假设一个组件没有版本号的概念，假设 1.0 和 2.0 版本的数据结构有差异，怎么解决？
- 当你的页面组件无限增加的话，怎么做？
- requestidlecallback
- resizeObserver
- 幻影依赖
- pnpm
- mix-blend-mode
- setup
- defer 执行时间在 contentloaded 之前
- defineExpose defineProps defineEmits
- 前端路由
- instanceof 实现原理
- pushState
- sass @extend @minin %占位符
- PageSpy
- getComputedStyle
- filter：blur contrast
- 事件循环
- will-change
- EyeDropper
- 购物车
- 属性描述符
- Object.freeze .seal isFrozen
- addEventListener passive：false
- 函数式组件 v-model.lazy
- box-decoration-break
- resizeobserver
- lattics
- 隐式转换
- 异步代码同步化
- vite
- lint-staged
- cspell
- commitizen
- cz-git
- husky
- zx
- tsno
- commitlint
- stylelint
- prettier
- eslint
- editorconfig
- smooth-dnd
- vue-flow/core
- 协变与逆变
- promise 限制并发数
- 手写继承
- flex 1 全写
- vue 双向绑定原理
- https 实现原理（越详细越好）
- node 进程之间如何通讯
- graghgl 如何优化请求速度
- node 跟浏览器的 event loop 区别
- 浏览器渲染页面过程
- 如何性能优化 CDN 优化有哪些
- 缓存有哪些，区别是什么
- 手写 bind、reduce
- 遍历树，求树的最大层数。求某层最多的节点数
- node 开启进程的方法有哪些，区别是什么
- node 如何部署的
- node check 阶段做了什么，触发了什么事件
- node 如何处理错误的
- 数字在计算机怎么储存的
- 跨域有哪些
- 网络安全
- 链表与数组的区别，链表如何遍历
- script 标签中 async 跟 defer 的区别
- 如何检查一个数字是否为整数 Number.isInteger()

  ```javascript
  console.log(Number.isInteger(25))
  console.log(Number.isInteger(25.0))
  console.log(Number.isInteger(25.1))
  ```

  检查一个数字是小数还是整数，可以使用一种非常简单的方法，就是将它对 1 进行取模，看看是否有余数。

  ```JavaScript
  function isInt(num) {
    return num % 1 === 0;
  }

  console.log(isInt(4)); // true
  console.log(isInt(12.2)); // false
  console.log(isInt(0.3)); // false
  ```

- 对于对象的深度比较，可以使用 deep-equal 这个库，或者自己实现递归比较算法。
- Javascript 中的“闭包”是什么？举个例子？
  闭包是在另一个函数（称为父函数）中定义的函数，并且可以访问在父函数作用域中声明和定义的变量。
  闭包可以访问三个作用域中的变量：

  - 在自己作用域中声明的变量；
  - 在父函数中声明的变量；
  - 在全局作用域中声明的变量。

  ```javascript
  var globalVar = 'abc'

  // 自调用函数
  ;(function outerFunction(outerArg) {
    // outerFunction 作用域开始
    // 在 outerFunction 函数作用域中声明的变量
    var outerFuncVar = 'x'
    // 闭包自调用函数
    ;(function innerFunction(innerArg) {
      // innerFunction 作用域开始
      // 在 innerFunction 函数作用域中声明的变量
      var innerFuncVar = 'y'
      console.log('outerArg = ' + outerArg + '\n' + 'outerFuncVar = ' + outerFuncVar + '\n' + 'innerArg = ' + innerArg + '\n' + 'innerFuncVar = ' + innerFuncVar + '\n' + 'globalVar = ' + globalVar)
      // innerFunction 作用域结束
    })(5) // 将 5 作为参数
    // outerFunction 作用域结束
  })(7) // 将 7 作为参数
  ```

  innerFunction 是在 outerFunction 中定义的闭包，可以访问在 outerFunction 作用域内声明和定义的所有变量。除此之外，闭包还可以访问在全局命名空间中声明的变量。
  上述代码的输出将是：

  ```javascript
  outerArg = 7
  outerFuncVar = x
  innerArg = 5
  innerFuncVar = y
  globalVar = abc
  ```

- 请解释原型设计模式。
  原型模式可用于创建新对象，但它创建的不是非初始化的对象，而是使用原型对象（或样本对象）的值进行初始化的对象。原型模式也称为属性模式。
  原型模式在初始化业务对象时非常有用，业务对象的值与数据库中的默认值相匹配。原型对象中的默认值被复制到新创建的业务对象中。
  经典的编程语言很少使用原型模式，但作为原型语言的 JavaScript 在构造新对象及其原型时使用了这个模式。
- 判断一个给定的字符串是否是同构的。
  如果两个字符串是同构的，那么字符串 A 中所有出现的字符都可以用另一个字符替换，以便获得字符串 B，而且必须保留字符的顺序。字符串 A 中的每个字符必须与字符串 B 的每个字符一对一对应。

  - paper 和 title 将返回 true。
  - egg 和 sad 将返回 false。
  - dgg 和 add 将返回 true。

  ```javascript
  isIsomorphic('egg', 'add') // true
  isIsomorphic('paper', 'title') // true
  isIsomorphic('kick', 'side') // false

  function isIsomorphic(firstString, secondString) {
    // 检查长度是否相等，如果不相等, 它们不可能是同构的
    if (firstString.length !== secondString.length) return false

    var letterMap = {}

    for (var i = 0; i < firstString.length; i++) {
      var letterA = firstString[i],
        letterB = secondString[i]

      // 如果 letterA 不存在, 创建一个 map，并将 letterB 赋值给它
      if (letterMap[letterA] === undefined) {
        letterMap[letterA] = letterB
      } else if (letterMap[letterA] !== letterB) {
        // 如果 letterA 在 map 中已存在, 但不是与 letterB 对应，
        // 那么这意味着 letterA 与多个字符相对应。
        return false
      }
    }
    // 迭代完毕，如果满足条件，那么返回 true。
    // 它们是同构的。
    return true
  }
  ```

- “Transpiling”是什么意思？
  对于语言中新加入的语法，无法进行 polyfill。因此，更好的办法是使用一种工具，可以将较新代码转换为较旧的等效代码。这个过程通常称为转换（transpiling），就是 transforming + compiling 的意思。
  通常，你会将转换器（transpiler）加入到构建过程中，类似于 linter 或 minifier。现在有很多很棒的转换器可选择：

  - Babel：将 ES6+ 转换为 ES5
  - Traceur：将 ES6、ES7 转换为 ES5

- “this”关键字的原理是什么？请提供一些代码示例。
  在 JavaScript 中，this 是指正在执行的函数的“所有者”，或者更确切地说，指将当前函数作为方法的对象。

  ```javascript
  function foo() {
    console.log(this.bar)
  }

  var bar = 'global'

  var obj1 = {
    bar: 'obj1',
    foo: foo
  }

  var obj2 = {
    bar: 'obj2'
  }

  foo() // "global"
  obj1.foo() // "obj1"
  foo.call(obj2) // "obj2"
  new foo() // undefined
  ```

- 请描述一下 Revealing Module Pattern 设计模式。
  暴露模块模式（Revealing Module Pattern）是模块模式的一个变体，目的是维护封装性并暴露在对象中返回的某些变量和方法。如下所示：

  ```javascript
  var Exposer = (function () {
    var privateVariable = 10

    var privateMethod = function () {
      console.log('Inside a private method!')
      privateVariable++
    }

    var methodToExpose = function () {
      console.log('This is a method I want to expose!')
    }

    var otherMethodIWantToExpose = function () {
      privateMethod()
    }

    return {
      first: methodToExpose,
      second: otherMethodIWantToExpose
    }
  })()

  Exposer.first() // 输出: This is a method I want to expose!
  Exposer.second() // 输出: Inside a private method!
  Exposer.methodToExpose // undefined
  ```

  它的一个明显的缺点是无法引用私有方法。

- 使用过的 koa2 中间件
- koa-body 原理
- 介绍自己写过的中间件
- 有没有涉及到 Cluster
- 介绍 pm2，master 挂了的话 pm2 怎么处理
- 如何和 MySQL 进行通信
- 路由的动态加载模块
- 服务端渲染 SSR
- 介绍路由的 history
- 如何解决跨域的问题
- 常见 Http 请求头
- 移动端适配 1px 的问题
- 介绍 flex 布局
- 其他 css 方式设置垂直居中
- 居中为什么要使用 transform（为什么不使用 marginLeft/Top）
- 使用过 webpack 里面哪些 plugin 和 loader
- webpack 里面的插件是怎么实现的
- dev-server 是怎么跑起来
- 项目优化
- 抽取公共文件是怎么配置的
- 项目中如何处理安全问题
- 怎么实现 this 对象的深拷贝
- 文件上传如何做断点续传
- 表单可以跨域吗
- promise、async 有什么区别
- 介绍观察者模式
- 介绍中介者模式
- 观察者和订阅-发布的区别，各自用在哪里
- 介绍 http2.0
- 通过什么做到并发请求
- http1.1 时如何复用 tcp 连接
- 介绍 service worker
- 浏览器事件流向
- 介绍事件代理以及优缺点
- 前端怎么控制管理路由
- 使用路由时出现问题如何解决
- 整个前端性能提升大致分几类
- `import { Button } from 'antd'`，打包的时候只打包`button`，分模块加载，是怎么做到的
- 使用`import`时，`webpack`对`node_modules`里的依赖会做什么
- JS 异步解决方案的发展历程以及优缺点
- Http 报文的请求会有几个部分
- `cookie`放哪里，`cookie`能做的事情和存在的价值
- `cookie`和`token`都存放在`header`里面，为什么只劫持前者
- `cookie`和`session`有哪些方面的区别
- key 主要是解决哪一类的问题，为什么不建议用索引 index（重绘）
- 柯里化函数两端的参数具体是什么东西
- koa 中 response.send、response.rounded、response.json 发生了什么事，浏览器为什么能识别到它是一个 json 结构或是 html
- koa-bodyparser 怎么来解析 request
- webpack 整个生命周期，loader 和 plugin 有什么区别
- 介绍 AST（Abstract Syntax Tree）抽象语法树
- 安卓 Activity 之间数据是怎么传递的
- 安卓 4.0 到 6.0 过程中 WebView 对 js 兼容性的变化
- WebView 和原生是如何通信
- 跨域怎么解决，有没有使用过 Apache 等方案
- 对 async、await 的理解，内部原理
- 介绍下 Promise，内部实现
- 清除浮动
- 定位问题（绝对定位、相对定位等）
- 从输入 URL 到页面加载全过程
- tcp3 次握手
- tcp 属于哪一层（1 物理层 -> 2 数据链路层 -> 3 网络层(ip)-> 4 传输层(tcp) -> 5 应用层(http)）
- webpack 介绍
- == 和 ===的区别，什么情况下用相等==
- bind、call、apply 的区别
- 动画的了解
- 介绍下原型链（解决的是继承问题吗）
- 对跨域的了解
- 介绍冒泡排序，选择排序，冒泡排序如何优化
- transform 动画和直接使用 left、top 改变位置有什么优缺点
- 如何判断链表是否有环
- 介绍二叉搜索树的特点
- 观察者和发布-订阅的区别
- 前端性能优化
- 如何设计一个 localStorage，保证数据的实效性
- sum(2, 3) 实现 sum(2)(3)的效果
- 两个对象如何比较
- 变量作用域链
- call、apply、bind 的区别
- 介绍各种异步方案
- 前端性能优化
- 介绍 DOM 树对比
- 如何设计状态树
- 介绍 css，xsrf
- http 缓存控制
- 项目中如何应用数据结构
- 如何做工程上的优化
- 前端怎么做单元测试
- webpack 生命周期
- webpack 打包的整个过程
- 常用的 plugins
- pm2 怎么做进程管理，进程挂掉怎么处理
- 不用 pm2 怎么做进程管理
- 介绍下浏览器跨域
- 怎么去解决跨域问题
- jsonp 方案需要服务端怎么配合
- Ajax 发生跨域要设置什么（前端）
- 加上 CORS 之后从发起到请求正式成功的过程
- xsrf 跨域攻击的安全性问题怎么防范
- 使用 Async 会注意哪些东西
- Async 里面有多个 await 请求，可以怎么优化（请求是否有依赖）
- Promise 和 Async 处理失败的时候有什么区别
- 对应的生命周期做什么事
- 遇到性能问题一般在哪个生命周期里解决
- 怎么做性能优化（异步加载组件...）
- 介绍下事件代理，主要解决什么问题
- 前端开发中用到哪些设计模式
- JS 变量类型分为几种，区别是什么
- JS 里垃圾回收机制是什么，常用的是哪种，怎么处理的
- 一般怎么组织 CSS（Webpack）
- 小程序里面开页面最多多少
- Emit 事件怎么发，需要引入什么
- 在哪个生命周期里写
- 其中有几个 name 不存在，通过异步接口获取，如何做
- 渲染的时候 key 给什么值，可以使用 index 吗，用 id 好还是 index 好
- webpack 如何配 sass，需要配哪些 loader
- 配 css 需要哪些 loader
- 如何配置把 js、css、html 单独打包成一个文件
- div 垂直水平居中（flex、绝对定位）
- 两个元素块，一左一右，中间相距 10 像素
- 上下固定，中间滚动布局如何实现
- 取数组的最大值（ES5、ES6）
- apply 和 call 的区别
- some、every、find、filter、map、forEach 有什么区别
- 上述数组随机取数，每次返回的值都不一样
- 页面上有 1 万个 button 如何绑定事件
- 如何判断是 button
- 页面上生成一万个 button，并且绑定事件，如何做（JS 原生操作 DOM）
- 页面上有一个 input，还有一个 p 标签，改变 input 后 p 标签就跟着变化，如何处理
- 监听 input 的哪个事件，在什么时候触发
- 对闭包的看法，为什么要用闭包
- 手写数组去重函数
- 手写数组扁平化函数
- ES6 新的特性
- 说一下闭包
- 网站 SEO 怎么处理
- 介绍下 HTTP 状态码
- 403、301、302 是什么
- 缓存相关的 HTTP 请求头
- 介绍 HTTPS
- HTTPS 怎么建立安全通道
- 用户体验做过什么优化
- 对 PWA 有什么了解
- 对安全有什么了解
- 介绍下数字签名的原理
- 前后端通信使用什么方案
- RESTful 常用的 Method
- 介绍下跨域
- Access-Control-Allow-Origin 在服务端哪里配置
- csrf 跨站攻击怎么解决
- localStorage 和 cookie 有什么区别
- CSS 选择器有哪些
- 盒子模型，以及标准情况和 IE 下的区别
- 如何实现高度自适应
- prototype 和`__proto__`区别
- `_construct`是什么
- `new`是怎么实现的
- 如何实现 H5 手机端的适配
- `rem`、`flex`的区别（root em）
- `em`和`px`的区别
- 如何去除 url 中的#号
- Redux 状态管理器和变量挂载到 window 中有什么区别
- webpack 和 gulp 的优缺点
- 如何实现异步加载
- 如何实现分模块打包（多入口）
- 前端性能优化（1js css；2 图片；3 缓存预加载； 4 SSR； 5 多域名加载；6 负载均衡）
- 并发请求资源数上限（6 个）
- base64 为什么能提升性能，缺点
- 介绍 webp 这个图片文件格式
- 介绍 koa2
- 异步请求，低版本 fetch 如何低版本适配
- ajax 如何处理跨域
- CORS 如何设置
- jsonp 为什么不支持 post 方法
- 介绍同源策略
- 如何继承
- Array 是 Object 类型吗
- 栈和堆具体怎么存储
- 垃圾回收时栈和堆的区别
- 介绍闭包以及闭包为什么没清除，闭包的使用场景
- JS 怎么实现异步
- 异步整个执行周期
- Async/Await 怎么实现
- JS 为什么要区分微任务和宏任务
- 发布-订阅和观察者模式的区别
- JS 执行过程中分为哪些阶段
- 词法作用域和 this 的区别
- 平常是怎么做继承
- 深拷贝和浅拷贝
- loadsh 深拷贝实现原理
- ES6 中`let`块作用域是怎么实现的
- 304 是什么
- 打包时 Hash 码是怎么生成的
- 随机值存在一样的情况，如何避免
- 使用 webpack 构建时有无做一些自定义操作
- webpack 做了什么
- a，b 两个按钮，点击 aba，返回顺序可能是 baa，如何保证是 aba（Promise.then）
- `node`接口转发有无做什么优化
- `node`起服务如何保证稳定性，平缓降级，重启等
- 什么是单页项目
- 介绍排序算法和快排原理
- 介绍闭包
- 闭包的核心是什么
- 网络的五层模型
- HTTP 和 HTTPS 的区别
- HTTPS 的加密过程
- 介绍 SSL 和 TLS
- JS 的继承方法
- 介绍垃圾回收
- cookie 的引用为了解决什么问题
- cookie 和 localStorage 的区别
- 如何解决跨域问题
- 前端性能优化
- 使用 canvas 绘图时如何组织成通用组件
- formData 和原生的 ajax 有什么区别
- 介绍下表单提交，和 formData 有什么关系
- 介绍 MVP 怎么组织
- 介绍异步方案
- koa2 中间件原理
- 常用的中间件
- 服务端怎么做统一的状态处理
- 如何对相对路径引用进行优化
- node 文件查找优先级
- npm2 和 npm3+有什么区别
- 介绍异步方案
- 如何处理异常捕获
- 前端性能优化
- JS 继承方案
- 如何判断一个变量是不是数组
- 多个<li>标签生成的 Dom 结构是一个类数组 类数组和数组的区别
- dom 的类数组如何转成数组
- 介绍单页面应用和多页面应用
- 介绍 localstorage 的 API
- html 语义化的理解
- 语义化版本
- `<b>`和`<strong>`的区别
- 对闭包的理解
- 工程中闭包使用场景
- 介绍 this 和原型
- 使用原型最大的好处
- 单例、工厂、观察者项目中实际场景
- 项目中树的使用场景以及了解
- 添加原生事件不移除为什么会内存泄露
- 还有哪些地方会内存泄露
- setInterval 需要注意的点
- 定时器为什么是不精确的
- 介绍宏任务和微任务
- 介绍 class 和 ES5 的类以及区别
- 介绍 defineProperty 方法，什么时候需要用到
- for..in 和 object.keys 的区别
- 使用闭包特权函数的使用场景
- get 和 post 有什么区别
- 介绍快速排序
- 算法：前 K 个最大的元素
- 使用过程中遇到的问题，如何解决的
- JS 是什么范式语言(面向对象还是函数式编程)
- koa 原理，为什么要用 koa(express 和 koa 对比)
- 使用的 koa 中间件
- ES6 使用的语法
- Promise 和 async/await 和 callback 的区别
- Promise 有没有解决异步的问题（promise 链是真正强大的地方）
- Promise 和 setTimeout 的区别（Event Loop）
- 进程和线程的区别（一个 node 实例就是一个进程，node 是单线程，通过事件循环来实现异步）
- 介绍下 DFS 深度优先
- 介绍下观察者模式
- 观察者模式里面使用的数据结构(不具备顺序 ，是一个 list)
- 为什么在 Node.js 中，require()加载模块是同步而非异步？
- 埋点的实现思路
- 非递归的二叉树遍历
- 文件上传断点、续传
- 设计模式的应用场景考核
- VUE 双向绑定原理
- VUE/React diff 算法的大概思路
- 现有的状态管理的实现
- webpack 中 loader、plugin 的实现思路
- 简易版 webpack 的实现
- KOA、Express 中间件的实现
- React fiber 的理解和原理
- 前端构建工具的、vue-cli、create-react-app 的原理和实现思路
- 主要围绕几个点：两者的模板渲染、两者的虚拟 dom、diff 差异（vue2、vue3、react 16）、react fiber 能解决什么问题、vue2 的响应式原理和 vue3 的响应式原理；vue 关于 Proxy 与 Object.defineProperty 的区别；两者的批量更新，还有路由差异、常用的优化手段、怎么进行数据通信、讲点新鲜的内容：新发布的 vue3 有什么特性、最后总结，谈谈两者的如今的生态……
- 项目的性能优化，主要围绕几个点：项目技术栈的性能优化，比如使用 react 可以讲避免重复渲染的一些手段，比如 electron 可以将如何更接近原生；针对浏览器做的优化（你需要了解浏览器相关原理，比如缓存/存储、代理、SSR 等，针对渲染引擎的工作内容想到的优化，比如解析 css 解析会影响 dom 渲染、合成优化减少回流重绘、web worker、Event Loop 等）；打包工具提供的优化，特指 webpack；针对具体的页面做的优化，比如首页该做什么，首页最新指标；最后讲讲应用场景、我的项目里用到了哪些方法，针对中等项目、大型项目的性能选择。
- 权限页面的细节：
  各个模块、按钮怎么设计权限；
  分角色、分地域怎么设计？
  要加个表头，还要控制展示的顺序，在各个浏览器表现一致，怎么设计？说出所有方案，想到什么自由发挥了……
- 聊到本地存储，问：localStorage 在各浏览器、移动端浏览器的 size 一致吗？
- 计算多个区间的交集
  区间用长度为 2 的数字数组表示，如[2, 5]表示区间 2 到 5（包括 2 和 5）；
  区间不限定方向，如[5, 2]等同于[2, 5]；
  实现`getIntersection 函数`
  可接收多个区间，并返回所有区间的交集（用区间表示），如空集用 null 表示
  示例：
  - getIntersection([5, 2], [4, 9], [3, 6]); // [4, 5]
  - getIntersection([1, 7], [8, 9]); // null
- DOM 的体积过大会影响页面性能，假如你想在用户关闭页面时统计（计算并反馈给服务器）
  当前页面中元素节点的数量总和、元素节点的最大嵌套深度以及最大子元素个数，请用 JS 配合
  原生 DOM API 实现该需求（不用考虑陈旧浏览器以及在现代浏览器中的兼容性，可以使用任意
  浏览器的最新特性；不用考虑 shadow DOM）。比如在如下页面中运行后：

  ```
  <html>
    &lt;head&gt;&lt;/head&gt;
    &lt;body&gt;
      <section>
        <span>f</span>
        <span>o</span>
        <span>o</span>
      </section>
    &lt;/body&gt;
  </html>
  会输出：

  {
  totalElementsCount: 7,
  maxDOMTreeDepth: 4,
  maxChildrenCount: 3
  }
  ```

- 请使用原生代码实现一个 Events 模块，可以实现自定义事件的订阅、触发、移除功能

  ```javascript
  const fn1 = (... args)=>console.log('I want sleep1', ... args)
  const fn2 = (... args)=>console.log('I want sleep2', ... args)
  const event = new Events();
  event.on('sleep', fn1, 1, 2, 3);
  event.on('sleep', fn2, 1, 2, 3);
  event.fire('sleep', 4, 5, 6);
  // I want sleep1 1 2 3 4 5 6
  // I want sleep2 1 2 3 4 5 6
  event.off('sleep', fn1);
  event.once('sleep', ()=>console.log('I want sleep));
  event.fire('sleep');
  ```

- 跨端的原理？我讲了几个例子：taro、uni-app，顺便提了 flutter、react native、小程序等的架构，具体怎么设计的。
- 动态表单能够运用在什么场景？我举了 7、8 个例子。
- 移动端适配相关的问题，应用场景。
- react 与 vue 的技术栈对比，说下区别
- 数据展示的优化、数据截取和处理
- 实际场景中，哪些地方应用到了堆、链表、多叉树结构
- es6 及 es6+ 的能力集，你最常用的，这其中最有用的，都解决了什么问题。
- GC 相关问题：es6+ ，eventloop 中涉及 GC 的部分。
- 数组 flat 展开的各种解法，数组 map 应用
- 讲下 V8 sort 的大概思路
- Promise 并发限制
- 省市区拼接查字段，要求 O(n) 内解出
- node 限流算法
- 最有效的性能优化方法
- 你提到性能指标，能说说都是怎么计算的吗？比如 LCP，FID
- 算法题：数组全排列 https://leetcode.cn/problems/permutations/description/
- input type 都有哪些类型，还记得其他 attrs 呢
- css 的伪类和伪元素有哪些？有什么区别？
- 在一个未知宽度的父元素内如何创建一个等边正方形
- 异步加载 js 会阻塞什么
- 数组所有方法都有哪些？findIndex 的参数说明
- vue 和 react 的异同
- 如何优化 vue 框架，注意是优化框架
- vue 和 react 的 jsx 使用
- id key 真的能使列表比对更高效吗？举个反例？
- webpack 优化的手段
- tree-shaking 怎么配置，如何 「避免」 tree-shaking？
- electron 和小程序遇到什么坑？
- 说下微信自动化测试
- es2015 到 es2020 的新特性，你最常用什么，给你收益最大的。
- weakMap 和 Map 的区别，weakMap 原理，为什么能被 GC？
- 如何干扰 GC ？
- webpack import 动态加载原理
- 知道 webpack 中的 devTool 吗？
- 如何进行错误定位和数据上报，线上异常的处理
- 为什么有时候配置了 webpack caching，chunk 还是更新了？
- 讲讲浏览器和 node 的 eventloop
- 微任务后面还有哪些？requestAnimationFrame 是怎么调用的？requestAnimationFrame 帧内总是有任务吗？分情况说下。
- 帧数怎么计算？
- 了解网络安全吗？
- 如何避免数据被 iframe 截获
- 说下状态码
- 说下 304，什么情况会 304？协商缓存的头部字段？
- 工程化实践的看法
- 项目是如何收集问题的，用户量如何？
- 工程化实践和深入的一个点
- webpack 提高构建速度的方式
- loader 输入什么产出什么 ？
- webpack 原理
- webpack 动态加载的原理
- webpack 热更新
- 如何写一个 webpack plugin
- AST 的应用
- 如何解析一个 html 文本，还是考 AST
- 如何设计一个沙盒 sandbox ？
- 小程序的 API 做了什么处理，能够做到全局变量的隐藏，如果是你，怎么设计 ？
- 基础题考闭包的，我讲对了思路，结果没做对。
- 实现颜色转换 'rgb(255, 255, 255)' -> '#FFFFFF' 的多种思路。
- 提供一个数字 n，生成一组 0\~n-1 的整数，打乱顺序组成数组，打乱几次，如何能够看起来平衡，说出你能想到的所有方法-
- 如何处理一个重大事故 bug
- 监控体系
- webpack 的缺点，让你设计一个新的构建打包工具，你会怎么设计？
- 在线文档编辑，如何处理两人的冲突，如何展示，考虑各种场景
- excel 文档冲突高级处理，文章冲突呢？是上个问题的深化。
- 基础题：简单实现一个 LRU
- 看源码，整理 Vue 与 React 框架的所有横向对比，包括渲染原理、虚拟 dom、diff、patch、fiber、批量更新，手写响应式，框架用到的模式、设计思想，性能优化，相关生态技术等等。
- webpack 原理、热更新原理、动态加载原理、常见 plugins、loader、常见优化，怎么打包、怎么分 chunk，怎么写一个 plugins，生命周期，微内核源码等内容，以及 rollup、gulp 的使用、应用场景。（我记得有一面一个考官对我说，你对整个研发流程都很清楚，但都并不深入，比如一个 webpack 打包分包的依据怎么判定……emmmm，我倒是会，你也不问我啊！）
- 跨端框架的研究，工程化的梳理，使用的技术栈的坑，移动端的一些实践，面试时额外准备的项目复盘，竞品调查，对方产品的资料，测试系列，还有很多如微前端、中台、serverless、可视化、Wasm 等就不举例了。
- JS 原型及原型链
  ![prototype.jpg](https://mmbiz.qpic.cn/mmbiz_jpg/Mpt86EGjlpto9HhomHK7L1seAgwXicwqtBKicXCQ7uykJptnOnGKt3F6IjqxDLcCaEgWACu8wmmBYzx9ery9zIiaQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)
- JS 继承的几种方式
  1. 原型继承
  ```javascript
  function Parent() {
    this.name = 'Parent'
    this.sex = 'boy'
  }
  function Child() {
    this.name = 'child'
  }
  // 将子类的原型对象指向父类的实例
  Child.prototype = new Parent()
  //优：继承了父类的模板，又继承了父类的原型对象
  //缺：1.无法实现多继承(因为已经指定了原型对象了)
  // 2.创建子类时，无法向父类构造函数传参数
  ```
  2. 构造函数继承
     在子类构造函数内部使用`call或apply`来调用父类构造函数，复制父类的实例属性给子类。
  ```javascript
  function Parent(name) {
    this.name = name
  }
  function Child() {
    //用.call 来改变 Parent 构造函数内的指向
    Parent.call(this, 'child')
  }
  ```
  //优：解决了原型链继承中子类实例共享父类引用对象的问题，实现多继承，创建子类实例时，可以向父类传递参数
  //缺：构造继承只能继承父类的实例属性和方法，不能继承父类原型的属性和方法 3. 组合继承
  组合继承就是将原型链继承与构造函数继承组合在一起。 - 使用**原型链继承**来保证子类能继承到父类原型中的属性和方法 - 使用**构造继承**来保证子类能继承到父类的实例属性和方法 4. 寄生组合继承 5. class 继承
  在`class` 中继承主要是依靠两个东西：
  - `extends`
  - `super`
- Event Loop 事件循环
  同步与异步、宏任务和微任务分别是函数两个不同维度的描述。
  同步任务指的是，在主线程上排队执行的任务，只有前一个任务执行完毕，才能执行后一个任务；**异步任务**指的是，不进入主线程、而进入**任务队列**（`task queue`）的任务，只有等主线程任务执行完毕，任务队列开始通知主线程，请求执行任务，该任务才会进入主线程执行。
  当某个宏任务执行完后,会查看是否有微任务队列。如果有，先执行微任务队列中的所有任务；如果没有，在执行环境栈中会读取宏任务队列中排在最前的任务；执行宏任务的过程中，遇到微任务，依次加入微任务队列。栈空后，再次读取微任务队列里的任务，依次类推。
  同步（Promise）>异步（微任务（process.nextTick ，Promises.then, Promise.catch ，resove,reject,MutationObserver)>宏任务（setTimeout，setInterval，setImmediate））
  **await 阻塞** 后面的代码执行，因此**跳出 async 函数**执行下一个微任务
- Promise 与 **Async/Await** 区别
  async/await 是基于 Promise 实现的，看起来更像同步代码，

  - 不需要写匿名函数处理 Promise 的 resolve 值
  - **错误处理**：　 Async/Await 让 try/catch 可以同时处理同步和异步错误。
  - 条件语句也跟错误处理一样简洁一点
  - 中间值处理（第一个方法返回值，用作第二个方法参数） 解决嵌套问题
  - 调试方便

  ```javascript
  const makeRequest = () => {
    try {
      getJSON().then((result) => {
        // JSON.parse 可能会出错
        const data = JSON.parse(result)
        console.log(data)
      })
      // 取消注释，处理异步代码的错误
      // .catch((err) => {
      // console.log(err)
      // })
    } catch (err) {
      console.log(err)
    }
  }
  ```

  使用`aync/await`的话，catch 能处理`JSON.parse`错误:

  ```javascript
  const makeRequest = async () => {
    try {
      // this parse may fail
      const data = JSON.parse(await getJSON())
      console.log(data)
    } catch (err) {
      console.log(err)
    }
  }
  ```

- 函数柯里化
  `柯里化(Currying)` 是把接收多个参数的原函数变换成接受一个单一参数（原来函数的第一个参数的函数)并返回一个新的函数，新的函数能够接受余下的参数，并返回和原函数相同的结果。

  1.  参数对复用
  2.  提高实用性
  3.  延迟执行 只传递给函数一部分参数来调用它，让它返回一个函数去处理剩下的参数。柯里化的函数可以延迟接收参数，就是比如一个函数需要接收的参数是两个，执行的时候必须接收两个参数，否则没法执行。但是柯里化后的函数，可以先接收一个参数

  ```javascript
  // 普通的 add 函数
  function add(x, y) {
    return x + y
  }

  // Currying 后
  function curryingAdd(x) {
    return function (y) {
      return x + y
    }
  }

  add(1, 2) // 3
  curryingAdd(1)(2) // 3
  ```

- JS 对象深克隆
  递归遍历对象，解决循环引用问题
  解决循环引用问题，我们需要一个存储容器存放当前对象和拷贝对象的对应关系（适合用 key-value 的数据结构进行存储，也就是 map），当进行拷贝当前对象的时候，我们先查找存储容器是否已经拷贝过当前对象，如果已经拷贝过，那么直接把返回，没有的话则是继续拷贝。

  ```javascript
  function deepClone(target) {
    const map = new Map()
    function clone(target) {
      if (isObject(target)) {
        let cloneTarget = isArray(target) ? [] : {}
        if (map.get(target)) {
          return map.get(target)
        }
        map.set(target, cloneTarget)
        for (const key in target) {
          cloneTarget[key] = clone(target[key])
        }
        return cloneTarget
      } else {
        return target
      }
    }
    return clone(target)
  }
  ```

- JS 模块化
  `nodeJS`里面的模块是基于`commonJS`规范实现的，原理是文件的读写，导出文件要使用`exports`、`module.exports`，引入文件用`require`。每个文件就是一个模块；每个文件里面的代码会用默认写在一个闭包函数里面`AMD`规范则是非同步加载模块，允许指定回调函数，`AMD` 是 `RequireJS` 在推广过程中对模块定义的规范化产出。
  `AMD`推崇**依赖前置**, `CMD`推崇**依赖就近**。对于依赖的模块 AMD 是提前执行，CMD 是延迟执行。
  在`ES6`中，我们可以使用 `import` 关键字引入模块，通过 `exprot` 关键字导出模块，但是由于 ES6 目前无法在浏览器中执行，所以，我们只能通过`babel`将不被支持的`import`编译为当前受到广泛支持的 `require`。
  CommonJs 和 ES6 模块化的区别：
  1.  CommonJS 模块输出的是一个值的拷贝，ES6 模块输出的是值的引用。
  2.  CommonJS 模块是运行时加载，ES6 模块是编译时输出接口。
      前端模块化：CommonJS,AMD,CMD,ES6
- import 和 require 导入的区别
  import 的 ES6 标准模块；require 是 AMD 规范引入方式；
  import 是编译时调用，所以必须放在文件开头;是解构过程 require 是运行时调用，所以 require 理论上可以运用在代码的任何地方;是赋值过程。其实 require 的结果就是对象、数字、字符串、函数等，再把 require 的结果赋值给某个变量
- 异步加载 JS 方式
  1. 匿名函数自调动态创建 script 标签加载 js
  ```javascript
  ;(function () {
    var scriptEle = document.createElement('script')
    scriptEle.type = 'text/javasctipt'
    scriptEle.async = true
    scriptEle.src = '<http://cdn.bootcss.com/jquery/3.0.0-beta1/jquery.min.js>'
    var x = document.getElementsByTagName('head')[0]
    x.insertBefore(scriptEle, x.firstChild)
  })()
  ```
  2. async 属性
  async 属性规定一旦加载脚本可用，则会异步执行
  <script type="text/javascript" src="xxx.js" async="async"></script>
  3. defer 属性
  defer 属性规定是否对脚本执行进行延迟，直到页面加载为止
  <script type="text/javascript" src="xxx.js" defer="defer"></script>
- call、apply
  `call( this,a,b,c )` 在第一个参数之后的，后续所有参数就是传入该函数的值。`apply( this,[a,b,c] )` 只有两个参数，第一个是对象，第二个是数组，这个数组就是该函数的参数。
  共同之处：都可以用来代替另一个对象调用一个方法，将一个函数的对象上下文从初始的上下文改变为由 thisObj 指定的新对象。
- addEventListener 的第三个参数干嘛的，为 true 时捕获，false 时冒泡
- `Object.prototype.toString.call()` 判断对象类型
- 词法作用域与作用域链
  作用域规定了如何查找变量，也就是确定当前执行代码对变量的访问权限。
  ES5 只有全局作用域没和函数作用域，ES6 增加块级作用域
  暂时性死区：在代码块内，使用 **let** 和 **const** 命令声明变量之前，该变量都是不可用的，语法上被称为暂时性死区。
  JavaScript 采用词法作用域(lexical scoping)，也就是静态作用域。
  **函数的作用域在函数定义的时候就决定了。**
  当查找变量的时候，会先从当前上下文的变量对象中查找，如果没有找到，就会从父级(词法层面上的父级**执行上下文**的变量对象中查找，一直找到全局上下文的变量对象，也就是全局对象。这样由多个执行上下文的变量对象构成的链表就叫做**作用域链**。
- new 关键字做了 4 件事:

  ```javascript
  function _new(constructor, ...arg) {
    // 创建一个空对象
    var obj = {}
    // 空对象的`__proto__`指向构造函数的`prototype`, 为这个新对象添加属性
    obj.__proto__ = constructor.prototype
    // 构造函数的作用域赋给新对象
    var res = constructor.apply(obj, arg)
    // 返回新对象.如果没有显式return语句，则返回this
    return Object.prototype.toString.call(res) === '[object Object]' ? res : obj
  }
  ```

- 判断数组的四种方法

  1. **Array.isArray()** 判断
  2. **instanceof** 判断: 检验构造函数的 prototype 属性是否出现在对象的原型链中，返回一个布尔值。`let a = []; a instanceof Array; //true`

  ```javascript
  const obj = {}
  Object.setPropertyOf(obj, Array.prototype)

  console.log(obj instanceof Array)

  // 页面中有 iframe 时
  const Array1 = window.Array
  const frame = document.querySelector('iframe')
  const Array2 = frame.contentWindow.Array
  console.log(Array1 === Array2)
  ```

  3. **constructor**判断: 实例的构造函数属性 constructor 指向构造函数`let a = [1,3,4]; a.constructor === Array;//true`
  4. **Object.prototype.toString.call()** 判断`let a = [1,2,3]; Object.prototype.toString.call(a) === '[object Array]';//true`

  ```javascript
  const obj = {
    [Symbol.toStringTag]: 'Array'
  }

  console.log(Object.prototype.toString.call(obj))
  ```

- TS 有什么优势
  1. 静态输入：静态类型化是一种功能，可以在开发人员编写脚本时检测错误。
  2. 大型的开发项目：使用 TypeScript 工具来进行重构更变的容易、快捷。
  3. 更好的协作：类型安全是在编码期间检测错误，而不是在编译项目时检测错误。
  4. 更强的生产力：干净的 ECMAScript 6 代码，自动完成和动态输入等因素有助于提高开发人员的工作效率。
- interface 和 type 的区别
  interface 只能定义对象类型。type 声明可以声明任何类型。
  interface 能够声明合并，两个相同接口会合并。Type 声明合并会报错
  type 可以类型推导
- 双向数据绑定 Proxy
  代理,可以理解为在对象之前设置一个“拦截”，当该对象被访问的时候，都必须经过这层拦截。意味着你可以在这层拦截中进行各种操作。比如你可以在这层拦截中对原对象进行处理，返回你想返回的数据结构。
  ES6 原生提供 Proxy 构造函数，MDN 上的解释为：Proxy 对象用于定义基本操作的自定义行为（如属性查找，赋值，枚举，函数调用等）。

  ```javascript
  const p = new Proxy(target, handler)
  //target： 所要拦截的目标对象（可以是任何类型的对象，包括原生数组，函数，甚至另一个代理）
  //handler：一个对象，定义要拦截的行为

  const p = new Proxy(
    {},
    {
      get(target, propKey) {
        return '哈哈，你被我拦截了'
      }
    }
  )

  console.log(p.name)
  ```

  新增的属性，并不需要重新添加响应式处理，因为 Proxy 是对对象的操作，只要你访问对象，就会走到 Proxy 的逻辑中。

- Vue3 Composition API
  `Vue3.x` 推出了`Composition API`。`setup` 是组件内使用 Composition API 的入口。`setup` 执行时机是在 `beforeCreate` 之前执行.
- reactive、ref 与 toRefs、isRef
  Vue3.x 可以使用 reactive 和 ref 来进行数据定义。

  ```javascript
  // props 传入组件对属性
  // context 一个上下文对象,包含了一些有用的属性:attrs,parent,refs
  setup(props, context) {
    // ref 定义数据
    const year = ref(0)
    // reactive 处理对象的双向绑定
    const user = reactive({ nickname: 'xiaofan', age: 26, gender: '女' })
    setInterval(() => {
      year.value++
      user.age++
    }, 1000)
    return {
      year,
      // 使用toRefs,结构解构
      ...toRefs(user)
    }
  }
  // 提供isRef，用于检查一个对象是否是ref对象
  ```

- watchEffect 监听函数
  watchEffect 不需要手动传入依赖
  watchEffect 会先执行一次用来自动收集依赖
  watchEffect 无法获取到变化前的值， 只能获取变化后的值
- computed 可传入 get 和 set
  用于定义可更改的计算属性

  ```javascript
  const plusOne = computed({
    get: () => count.value + 1,
    set: (val) => {
      count.value = val - 1
    }
  })
  ```

- 使用 TypeScript 和 JSX
  `setup`现在支持返回一个渲染函数，这个函数返回一个`JSX`，`JSX`可以直接使用声明在`setup`作用域的响应式状态：

  ```javascript
  export default {
    setup() {
      const count = ref(0)
      return () => <div>{count.value}</div>
    }
  }
  ```

- Vue 跟 React 对比？
  相同点：
  1. 都有虚拟 DOM（Virtual DOM 是一个映射真实 DOM 的 JavaScript 对象）
  2. 都提供了响应式和组件化的视图组件。
     不同点：Vue 是`MVVM`框架，双向数据绑定，当`ViewModel`对`Model`进行更新时，通过数据绑定更新到`View`。
     React 是一个单向数据流的库，状态驱动视图。`State --> View --> New State --> New View` `ui = render (data)`
     模板渲染方式不同。React 是通过 JSX 来渲染模板，而 Vue 是通过扩展的 HTML 来进行模板的渲染。
     组件形式不同，Vue 文件里将 HTML，JS，CSS 组合在一起。react 提供 class 组件和 function 组
     Vue 封装好了一些 v-if，v-for，React 什么都是自己实现，自由度更高
- Vue 初始化过程，双向数据绑定原理
  vue.js 则是采用数据劫持结合发布者-订阅者模式的方式，通过`Object.defineProperty()`来劫持各个属性的`setter`，`getter`，`dep.addSub`来收集订阅的依赖，`watcher`监听数据的变化，在数据变动时发布消息给订阅者，触发相应的监听回调。
  监听器`Observer`，用来劫持并监听所有属性，如果有变动的，就通知订阅者。订阅者`Watcher`，可以收到属性的变化通知并执行相应的函数，从而调用对应 update 更新视图。![图片](https://mmbiz.qpic.cn/mmbiz_png/Mpt86EGjlpto9HhomHK7L1seAgwXicwqtZmEicRKJ6fHdia2ayPCgwJMxzjNPCZlqhYFIE5Xsic54tKAqNLsWY04vQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
  `v-model` 指令，它能轻松实现表单输入和应用状态之间的双向绑定。
  **computed:** 支持缓存，只有依赖数据结果发生改变，才会重新进行计算，不支持异步操作，如果一个属性依赖其他属性，多对一，一般用 computed
  **watch:** 数据变，直接触发相应操作，支持异步，监听数据必须`data`中声明过或者父组件传递过来的`props中`的数据，当数据变化时，触发其他操作，函数有两个参数
- vue-router 实现原理
  端路由简介以及 vue-router 实现原理原理核心就是 更新视图但不重新请求页面。路径之间的切换，也就是组件的切换。vue-router 实现单页面路由跳转模式：hash 模式、history 模式。根据设置 mode 参数
  `hash模式`：通过锚点值的改变，根据不同的值，渲染指定 DOM 位置的不同数据。每一次改变`#`后的部分，都会在浏览器的访问历史中增加一个记录，使用”后退”按钮，就可以回到上一个位置。`history模式`：利用 `window.history.pushState` API 来完成 URL 跳转而无须重新加载页面。
- vuex 实现原理：
  `Vue.use(vuex)`会调用 vuex 的 install 方法
  在`beforeCreate`钩子前混入`vuexInit`方法，`vuexInit`方法实现了`store`注入`vue组件实例`，并注册了`vuex` `store`的引用属性`$store`。
  `Vuex`的`state`状态是响应式，是借助`vue`的`data`是响应式，将`state`存入 vue 实例组件的 data 中；
  `Vuex`的`getters`则是借助 vue 的计算属性`computed`实现数据实时监听。
- nextTick 的原理以及运行机制？
  nextTick 的源码分析
  vue 进行 DOM 更新内部也是调用 nextTick 来做异步队列控制。只要观察到数据变化，Vue 将开启一个队列，并缓冲在同一事件循环中发生的所有数据改变。如果同一个 watcher 被多次触发，只会被推入到队列中一次。
  DOM 至少会在当前事件循环里面的所有数据变化完成之后，再统一更新视图。而当我们自己**调用 nextTick 的时候**，它就在更新 DOM 的 microtask(微任务队列)后**追加了我们自己的回调函数**，
  从而确保我们的代码在 DOM 更新后执行，同时也避免了 setTimeout 可能存在的多次执行问题。确保队列中的微任务在一次事件循环前被执行完毕。
- Vue 实现一个高阶组件
  高阶组件就是一个函数，且该函数接受一个组件作为参数，并返回一个新的组件。**在不改变对象自身的前提下在程序运行期间动态的给对象添加一些额外的属性或行为**。

  ```javascript
  // 高阶组件(HOC)接收到的 props 应该透传给被包装组件即直接将原组件prop传给包装组件
  // 高阶组件完全可以添加、删除、修改 props
  export default function Console(BaseComponent) {
    return {
      props: BaseComponent.props,
      mounted() {
        console.log('高阶组件')
      },
      render(h) {
        console.log(this)
        // 将 this.$slots 格式化为数组，因为 h 函数第三个参数是子节点，是一个数组
        const slots = Object.keys(this.$slots)
          .reduce((arr, key) => arr.concat(this.$slots[key]), [])
          .map((vnode) => {
            vnode.context = this._self // 绑定到高阶组件上，vm：解决具名插槽被作为默认插槽进行渲染
            return vnode
          })

        // 透传props、透传事件、透传slots
        return h(
          BaseComponent,
          {
            on: this.$listeners,
            attrs: this.$attrs, // attrs 指的是那些没有被声明为 props 的属性
            props: this.$props
          },
          slots
        )
      }
    }
  }
  ```

- Vue.component()、Vue.use()、this.\$xxx()
  Vue.component()方法注册全局组件。

  - 第一个参数是自定义元素名称，也就是将来在别的组件中使用这个组件的标签名称。
  - 第二个参数是将要注册的 Vue 组件。

  ```javascript
  import Vue from 'vue'
  // 引入 loading 组件
  import Loading from './loading.vue'
  // 将 loading 注册为全局组件，在别的组件中通过\<loading>标签使用 Loading 组件
  Vue.component('loading', Loading)
  ```

  Vue.use 注册插件,这接收一个参数。这个参数必须具有 install 方法。Vue.use 函数内部会调用参数的 install 方法。

  - 如果插件没有被注册过，那么注册成功之后会给插件添加一个 installed 的属性值为 true。Vue.use 方法内部会检测插件的 installed 属性，从而避免重复注册插件。
  - 插件的 install 方法将接收两个参数，第一个是参数是 Vue，第二个参数是配置项 options。
  - 在 install 方法内部可以添加全局方法或者属性

  ```javascript
  import Vue from 'vue'

  // 这个插件必须具有 install 方法
  const plugin = {
    install(Vue, options) {
      // 添加全局方法或者属性
      Vue.myGlobMethod = function () {}
      // 添加全局指令
      Vue.directive()
      // 添加混入
      Vue.mixin()
      // 添加实例方法
      Vue.prototype.$xxx = function () {}
      // 注册全局组件
      Vue.component()
    }
  }

  // Vue.use 内部会调用 plugin 的 install 方法
  Vue.use(plugin)
  ```

  将 Hello 方法挂载到 Vue 的 prototype 上.

  ```javascript
  import Vue from 'vue'
  import Hello from './hello.js'
  Vue.prototype.$hello = Hello
  ```

  vue 组件中就可以 this.$hello('hello world')

- Vue 父组件传递 props 数据，子组件修改参数
  父子组件传值时，父组件传递的参数，数组和对象，子组件接受之后可以直接进行修改，并且父组件相应的值也会修改。控制台中发出警告。
  如果传递的值是字符串，直接修改会报错。单向数据流，每次父级组件发生更新时，子组件中所有的 prop 都将会刷新为最新的值。
  如果子组件想修改 prop 中数据：
  1. 定义一个局部变量，使用 prop 的值赋值
  2. 定义一个计算属性，处理 prop 的值并返回
- Vue 父子组件生命周期执行顺序
  加载渲染过程 父 beforeCreate -> 父 created -> 父 beforeMount-> 子 beforeCreate -> 子 created -> 子 beforeMount -> 子 mounted -> 父 mounted
  子组件更新过程 父 beforeUpdate -> 子 beforeUpdate -> 子 updated -> 父 updated
  父组件更新过程 父 beforeUpdate -> 父 updated
  销毁过程 父 beforeDestroy -> 子 beforeDestroy -> 子 destroyed -> 父 destroyed
- Vue 自定义指令
  自定义指令提供了几个钩子函数：`bind`：指令第一次绑定到元素时调用`inserted`：被绑定元素插入父节点时调用`update`：所在组件的 VNode 更新时调用
- 使用**slot**后可以在子组件内显示**插入的新标签**

- webpack 的生命周期及钩子
  **compiler**（整个生命周期 [kəmˈpaɪlər]） 钩子 <https://webpack.docschina.org/api/compiler-hooks/**compilation**（编译> \[ˌkɑːmpɪˈleɪʃn]） 钩子
  `compiler`对象包含了 Webpack 环境所有的的配置信息。这个对象在启动 webpack 时被一次性建立，并配置好所有可操作的设置，包括 options，loader 和 plugin。当在 webpack 环境中应用一个插件时，插件将收到此 compiler 对象的引用。可以使用它来访问 webpack 的主环境。
  `compilation`对象包含了当前的模块资源、编译生成资源、变化的文件等。当运行 webpack 开发环境中间件时，每当检测到一个文件变化，就会创建一个新的 compilation，从而生成一组新的编译资源。compilation 对象也提供了很多关键时机的回调，以供插件做自定义处理时选择使用。
  compiler`代表了整个`webpack`从启动到关闭的`生命周期`，而`compilation` 只是代表了一次新的`编译过程
- webpack 编译过程
  Webpack 的编译流程是一个串行的过程，从启动到结束会依次执行以下流程：
  1. 初始化参数：从配置文件和 Shell 语句中读取与合并参数，得出最终的参数；
  2. 开始编译：用上一步得到的参数初始化 `Compiler` 对象，加载所有配置的插件，执行对象的 `run`方法开始执行编译；
  3. 确定入口：根据配置中的 `entry` 找出所有的入口文件；
  4. 编译模块：从入口文件出发，调用所有配置的 `Loader` 对模块进行翻译，再找出该模块依赖的模块，再递归本步骤直到所有入口依赖的文件都经过了本步骤的处理；
  5. 完成模块编译：在经过第 4 步使用 `Loader` 翻译完所有模块后，得到了每个模块被翻译后的最终内容以及它们之间的依赖关系；
  6. 输出资源：根据入口和模块之间的依赖关系，组装成一个个包含多个模块的`Chunk`，再把每个 `Chunk` 转换成一个单独的文件加入到输出列表，这步是可以修改输出内容的最后机会；
  7. 输出完成：在确定好输出内容后，根据配置确定输出的路径和文件名，把文件内容写入到文件系统。
- 优化项目的 webpack 打包编译过程
  **1.构建打点**：构建过程中，每一个`Loader` 和 `Plugin` 的执行时长，在编译 JS、CSS 的 Loader 以及对这两类代码执行压缩操作的 Plugin 上消耗时长 。一款工具：speed-measure-webpack-plugin
  **2.缓存**：大部分 Loader 都提供了`cache` 配置项。`cache-loader` ，将 loader 的编译结果写入硬盘缓存
  **3.多核编译**，`happypack`项目接入多核编译，理解为`happypack` 将编译工作灌满所有线程
  **4.抽离**，`webpack-dll-plugin` 将这些静态依赖从每一次的构建逻辑中抽离出去，静态依赖单独打包，`Externals`将不需要打包的静态资源从构建逻辑中剔除出去，使用`CDN 引用`
  **5.`tree-shaking`**，虽然依赖了某个模块，但其实只使用其中的某些功能。通过 `tree-shaking`，将没有使用的模块剔除，来达到删除无用代码的目的。
- 首屏加载优化
  **路由懒加载**：改为用`import`引用，以函数的形式动态引入，可以把各自的路由文件分别打包，只有在解析给定的路由时，才会下载路由组件；
  **`element-ui`按需加载**：引用实际上用到的组件 ；
  **组件重复打包**：`CommonsChunkPlugin`配置来拆包，把使用 2 次及以上的包抽离出来，放进公共依赖文件，首页也有复用的组件，也会下载这个公共依赖文件；
  **gzip**: 拆完包之后，再用`gzip`做一下压缩，关闭 sourcemap。
  **UglifyJsPlugin:** 生产环境，压缩混淆代码，移除 console 代码
  CDN 部署静态资源：静态请求打在 nginx 时，将获取静态资源的地址进行重定向 CDN 内容分发网络
  **移动端首屏**加载可以使用**骨架屏**，自定义**loading**，首页单独做**服务端渲染**。
- webpack 热更新机制
  热更新流程总结:
  - 启动本地`server`，让浏览器可以请求本地的**静态资源**
  - 页面首次打开后，服务端与客户端通过 websocket 建立通信渠道，把下一次的 hash 返回前端
  - 客户端获取到 hash，这个 hash 将作为下一次请求服务端 hot-update.js 和 hot-update.json 的 hash
  - 修改页面代码后，Webpack 监听到文件修改后，开始编译，编译完成后，发送 build 消息给客户端
  - 客户端获取到 hash，成功后客户端构造 hot-update.js script 链接，然后插入主文档
  - hot-update.js 插入成功后，执行 hotAPI 的 createRecord 和 reload 方法，获取到 Vue 组件的 render 方法，重新 render 组件， 继而实现 UI 无刷新更新。
- webpack 的 loader 和 plugin 介绍，css-loader，style-loader 的区别
  **loader** 它就是一个转换器，将 A 文件进行编译形成 B 文件，
  **plugin** ，它就是一个扩展器，来操作的是文件，针对是 loader 结束后，webpack 打包的整个过程，它并不直接操作文件，会监听 webpack 打包过程中的某些节点（run, build-module, program）
  **Babel** 能把 ES6/ES7 的代码转化成指定浏览器能支持的代码。
  `css-loader` 的作用是把 css 文件进行转码`style-loader`: 使用`<style>`将`css-loader`内部样式注入到我们的 HTML 页面
  先使用 `css-loader`转码，然后再使用 `style-loader`插入到文件
- 如何编写一个 webpack 的 plugin？ <https://segmentfault.com/a/1190000037513682>
  webpack 插件的组成：
  - 一个 JS 命名函数或一个类（可以想下我们平时使用插件就是 `new XXXPlugin()`的方式）
  - 在插件类/函数的 (prototype) 上定义一个 apply 方法。
  - 通过 apply 函数中传入 compiler 并插入指定的事件钩子，在钩子回调中取到 compilation 对象
  - 通过 compilation 处理 webpack 内部特定的实例数据
  - 如果是插件是异步的，在插件的逻辑编写完后调用 webpack 提供的 callback
- 为什么 Vite 启动这么快
  Webpack 会`先打包`，然后启动开发服务器，请求服务器时直接给予打包结果。
  而 Vite 是`直接启动`开发服务器，请求哪个模块再对该模块进行`实时编译`。
  Vite 将开发环境下的模块文件，就作为浏览器要执行的文件，而不是像 Webpack 那样进行`打包合并`。
  由于 Vite 在启动的时候`不需要打包`，也就意味着`不需要分析模块的依赖`、`不需要编译`。因此启动速度非常快。当浏览器请求某个模块时，再根据需要对模块内容进行编译。
- 你的脚手架是怎么做的
  使用 `download-git-repo` 下载仓库代码 demo`commander`：完整的 `node.js` 命令行解决方案。声明`program`，使用`.option()` 方法来定义选项`Inquirer.js`：命令行用户界面的集合。
- 前端监控
  前端监控通常包括**行为监控**(PV/UV,埋点接口统计)、**异常监控**、**性能监控**。
  一个监控系统，大致可以分为四个阶段：**日志采集**、**日志存储**、**统计与分析**、**报告和警告**。
- 错误监控
  Vue 专门的错误警告的方法 `Vue.config.errorHandler`,（Vue 提供只能捕获其页面生命周期内的函数，比如 created,mounted）

  ```javascript
  Vue.config.errorHandler = function (err) {
    console.error('Vue.error', err.stack)
    // 逻辑处理
  }
  ```

  框架：**betterjs**，**fundebug**（收费） 捕获错误的脚本要放置在最前面，确保可以收集到错误信息 方法：

  1.  `window.onerror()`当有 js 运行时错误触发时,onerror 可以接受多个参数(message, source, lineno, colno, error)。
  2.  `window.addEventListener('error'), function(e) {}, true` 会比 window.onerror 先触发,不能阻止默认事件处理函数的执行，但可以全局捕获资源加载异常的错误
      前端 JS 错误捕获--sourceMap

- 如何监控网页崩溃？崩溃和卡顿有何差别？监控错误

  1. Service Worker 有自己独立的工作线程，与网页区分开，网页崩溃了，Service Worker 一般情况下不会崩溃；
  2. Service Worker 生命周期一般要比网页还要长，可以用来监控网页的状态；
     **卡顿**：加载中，渲染遇到阻塞

- 性能监控 && 性能优化
  性能指标：
  - `FP`（首次绘制）
  - `FCP`（首次内容绘制 First contentful paint）
  - `LCP`（最大内容绘制时间 Largest contentful paint）
  - `FPS`（每秒传输帧数）
  - `TTI`（页面可交互时间 Time to Interactive）
  - `HTTP` 请求响应时间
  - `DNS` 解析时间
  - `TCP` 连接时间
    性能数据采集需要使用 `window.performance API` ， JS 库 `web-vitals`：`import {getLCP} from 'web-vitals'`;
    // 重定向耗时 redirect: timing.redirectEnd - timing.redirectStart,
    // DOM 渲染耗时 dom: timing.domComplete - timing.domLoading,
    // 页面加载耗时 load: timing.loadEventEnd - timing.navigationStart,
    // 页面卸载耗时 unload: timing.unloadEventEnd - timing.unloadEventStart,
    // 请求耗时 request: timing.responseEnd - timing.requestStart,
    // 获取性能信息时当前时间 time: new Date().getTime(),
    // DNS 查询耗时 domainLookupEnd - domainLookupStart
    // TCP 链接耗时 connectEnd - connectStart
    // request 请求耗时 responseEnd - responseStart
    // 解析 dom 树耗时 domComplete - domInteractive
    // 白屏时间 domloadng - fetchStart
    // onload 时间 loadEventEnd - fetchStart
    性能优化常用手段：缓存技术、 预加载技术、 渲染方案。
  1. **缓存** ：主要有 cdn、浏览器缓存、本地缓存以及应用离线包
  2. **预加载** ：资源预拉取（prefetch）则是另一种性能优化的技术。通过预拉取可以告诉浏览器用户在未来可能用到哪些资源。
- prefetch 支持预拉取图片、脚本或者任何可以被浏览器缓存的资源。
  在 head 里 添加 `<linkrel="prefetch"href="image.png">`
- prerender 是一个重量级的选项，它可以让浏览器提前加载指定页面的所有资源。
- subresource 可以用来指定资源是最高优先级的。当前页面需要，或者马上就会用到时。
- **渲染方案**：
  静态渲染（SR）
  前端渲染（CSR）
  服务端渲染（SSR）
  客户端渲染（NSR）：NSR 数据请求，首屏数据请求和数据线上与 webview 的一个初始化和框架 JS 初始化并行了起来，大大缩短了首屏时间。
- 常见的六种设计模式以及应用场景 <https://www.cnblogs.com/whu-2017/p/9471670.html>
- 观察者模式的概念
  观察者模式模式，属于行为型模式的一种，它定义了一种一对多的依赖关系，**让多个观察者对象同时监听某一个主题对象**。这个主体对象在状态变化时，会通知所有的观察者对象。
- 发布订阅者模式的概念
  发布-订阅模式，消息的发送方，叫做**发布者**（publishers），消息不会直接发送给特定的接收者，叫做**订阅者**。意思就是发布者和订阅者不知道对方的存在。需要一个第三方组件，叫做信息中介，它将订阅者和发布者串联起来，它过滤和分配所有输入的消息。换句话说，发布-订阅模式**用来处理不同系统组件的信息交流**，即使这些组件不知道对方的存在。
  需要一个第三方组件，叫做**信息中介**，它将订阅者和发布者串联起来
- 工厂模式\*\* 主要是为创建对象提供了接口。场景：在编码时不能预见需要创建哪种类的实例。
- 代理模式 命令模式
- 单例模式
  保证一个类仅有一个实例，并提供一个访问它的全局访问点。（window）
- 七层网络模型
  应用层、表示层、会话层、传输层、网络层、数据链路层、物理层
  **TCP**：面向连接、传输可靠(保证数据正确性,保证数据顺序)、用于传输大量数据(流模式)、速度慢，建立连接需要开销较多(时间，系统资源) 。（应用场景：HTP，HTTP，邮件）
  **UDP**：面向非连接、传输不可靠、用于传输少量数据(数据包模式)、速度快 ,可能丢包（应用场景：即时通讯）
  是否连接 面向连接 面向非连接
  传输可靠性 可靠 不可靠
  应用场合 少量数据 传输大量数据
  https
  客户端先向服务器端索要公钥，然后用公钥加密信息，服务器收到密文后，用自己的私钥解密。服务器公钥放在数字证书中。
- http2
  **多路复用**：相同域名多个请求，共享同一个 TCP 连接，降低了延迟
  **请求优先级**：给每个 request 设置优先级
  **二进制传输**；之前是用纯文本传输
  **数据流**：数据包不是按顺序发送，对数据包做标记。每个请求或回应的所有数据包成为一个数据流，
  **服务端推送**：可以主动向客户端发送消息。
  **头部压缩**：减少包的大小跟数量
  HTTP/1.1 中的管道（ pipeline）传输中如果有一个`请求阻塞`了，那么队列后请求也统统被阻塞住了 HTTP/2 多请求复用一个 TCP 连接，一旦发生丢包，就会阻塞住所有的 HTTP 请求。HTTP/3 把 HTTP 下层的 TCP 协议改成了 **UDP**！http1 keep alive 串行传输
- http 中的 keep-alive 有什么作用
  响应头中设置 `keep-alive` 可以在一个 TCP 连接上发送**多个 http** 请求
- 浏览器缓存策略
  强缓存：cache-control；no-cache max-age=<10000000>；expires；其中 Cache-Conctrol 的优先级比 Expires 高；
  控制强制缓存的字段分别是 Expires 和 Cache-Control，如果客户端的时间小于 Expires 的值时，直接使用缓存结果。
  协商缓存：**Last-Modified / If-Modified-Since 和 Etag / If-None-Match**，其中 Etag / If-None-Match 的优先级比 Last-Modified / 首次请求，服务器会在返回的响应头中加上 Last-Modified 字段，表示资源最后修改的时间。
  浏览器再次请求时，请求头中会带上 If-Modified-Since 字段，比较两个字段，一样则证明资源未修改，返回 304，否则重新返回资源，状态码为 200；
- 垃圾回收机制：
  `标记清除`：进入执行环境的变量都被标记，然后执行完，清除这些标记跟变量。查看变量是否被引用。
  `引用计数`：会记录每个值被引用的次数，当引用次数变成 0 后，就会被释放掉。
- 前端安全
  同源策略：如果两个 URL 的**协议、域名和端口**都相同，我们就称这两个 URL 同源。因为浏览器有`cookies`。
- **XSS**：跨站脚本攻击(Cross Site Scripting) **input, textarea**等所有可能输入文本信息的区域，输入`<script src="http://恶意网站"></script>`等，提交后信息会存在服务器中 。
- **CSRF**：跨站请求伪造 。引诱用户打开黑客的网站，在黑客的网站中，利用用户的登录状态发起的跨站请求。
  `A`站点`img`的`src=B`站点的请求接口，可以访问；解决：`referer`携带请求来源
  访问该页面后，表单自动提交, 模拟完成了一次 POST 操作,发送 post 请求
  **解决**：后端注入一个`随机串`到`Cookie`，前端请求取出随机串添加传给后端。
  **http 劫持**：电信运营商劫持
  **SQL 注入**
  **点击劫持**：诱使用户点击看似无害的按钮（实则点击了透明 `iframe`中的按钮） ，解决后端请求头加一个字段 `X-Frame-Options`
  **文件上传漏洞** ：服务器未校验上传的文件
- 什么是 BFC（块级格式化上下文）、**IFC**（内联格式化上下文 ）、**FFC**（弹性盒模型）
  `BFC（Block formatting context）`，即`块级格式化上下文`，它作为 HTML 页面上的一个`独立渲染区域`，只有区域内元素参与渲染，且不会影响其外部元素。简单来说，可以将 BFC 看做是一个“围城”，外面的元素进不来，里面的元素出不去（互不干扰）。
  一个决定如何渲染元素的容器 ，渲染规则 ：
  - 1、内部的块级元素会在垂直方向，一个接一个地放置。
  - 2、块级元素垂直方向的距离由 margin 决定。属于同一个 BFC 的两个相邻块级元素的 margin 会发生重叠。
  - 3、对于从左往右的格式化，每个元素（块级元素与行内元素）的左边缘，与包含块的左边缘相接触，(对于从右往左的格式化则相反)。即使包含块中的元素存在浮动也是如此，除非其中元素再生成一个 BFC。
  - 4、BFC 的区域不会与浮动元素重叠。
  - 5、BFC 是一个隔离的独立容器，容器里面的子元素和外面的元素互不影响。
  - **6、计算 BFC 容器的高度时，浮动元素也参与计算。**
    形成 BFC 的条件:
    1、浮动元素，float 除 none 以外的值；
    2、定位元素，position（absolute，fixed）；
    3、display 为以下其中之一的值 inline-block，table-cell，table-caption；
    4、overflow 除了 visible 以外的值（hidden，auto，scroll）；
    BFC 一般用来解决以下几个问题
  - 边距重叠问题
  - 消除浮动问题
  - 自适应布局问题
- `flex: 0 1 auto;` 是什么意思？
  元素会根据自身宽高设置尺寸。它会缩短自身以适应 `flex` 容器，但不会伸长并吸收 `flex` 容器中的额外自由空间来适应 `flex` 容器 。水平的主轴（`main axis`）和垂直的交叉轴（`cross axis`）几个属性决定按哪个轴的排列方向
  - `flex-grow`: `0` 一个无单位**数()**: 它会被当作`<flex-grow>的值。`
  - `flex-shrink`: `1` 一个有效的**宽度(width)**值: 它会被当作 `<flex-basis>的值。`
  - `flex-basis`: `auto` 关键字`none`，`auto`或`initial`.
    放大比例、缩小比例、分配多余空间之前占据的主轴空间。
- 避免 CSS 全局污染
  scoped 属性
  css in js
  CSS Modules
  使用 less，尽量少使用全局对选择器
- CSS Modules
  阮一峰 CSS Modules
  CSS Modules 是一种构建步骤中的一个进程。通过构建工具来使`指定class`达到`scope`的过程。
  `CSS Modules` 允许使用:`:global(.className)`的语法，声明一个全局规则。凡是这样声明的`class`，都不会被编译成`哈希字符串`。`:local(className)`: 做 localIdentName 规则处理,编译唯一哈希类名。
  CSS Modules 使用特点:
  - 不使用选择器，只使用 class 名来定义样式
  - 不层叠多个 class，只使用一个 class 把所有样式定义好
  - 不嵌套 class
- 盒子模型和 `box-sizing` 属性
  width: 160px; padding: 20px; border: 8px solid orange;`标准 box-sizing: `content-box;`元素的总宽度 = 160 + 20*2 + 8*2; IE的`border-box`：总宽度`160
  `margin/padding`取**百分比**的值时 ，基于**父元素的宽度和高度**的。
- css 绘制三角形

  1. 通过 border 处理

  ```css
  // border 处理
  .class {
    width: 0;
    height: 0;
    border-left: 50px solid transparent;
    border-right: 50px solid transparent;
    border-bottom: 100px solid red;
  }
  // 宽高+border
  div {
    width: 50px;
    height: 50px;
    border: 2px solid orange;
  }
  ```

  2. clip-path 裁剪获得

  ```css
  div {
    clip-path: polygon(0 100%, 50% 0, 100% 100%);
  }
  ```

  3.  渐变 linear-gradient 实现

  ```css
  div {
    width: 200px;
    height: 200px;
    background: linear-gradient(to bottom right, #fff 0%, #fff 49.9%, rgba(148, 88, 255, 1) 50%, rgba(185, 88, 255, 1) 100%);
  }
  ```

- CSS 实现了三角形后如何给三角形添加阴影
- CSS 两列布局的 N 种实现
  两列布局分为两种，一种是左侧定宽、右侧自适应，另一种是两列都自适应（即左侧宽度由子元素决定，右侧补齐剩余空间）。

  1.  左侧定宽、右侧自适应如何实现

  ```css
  // 两个元素都设置 dislpay:inline-block
  .left {
    display: inline-block;
    width: 100px;
    height: 200px;
    background-color: red;
    vertical-align: top;
  }
  .right {
    display: inline-block;
    width: calc(100% - 100px);
    height: 400px;
    background-color: blue;
    vertical-align: top;
  }
  // 两个元素设置浮动，右侧自适应元素宽度使用 calc 函数计算
  .left {
    float: left;
    width: 100px;
    height: 200px;
    background-color: red;
  }
  .right {
    float: left;
    width: calc(100% - 100px);
    height: 400px;
    background-color: blue;
  }
  // 父元素设置 display：flex，自适应元素设置 flex：1
  .box {
    height: 600px;
    width: 100%;
    display: flex;
  }
  .left {
    width: 100px;
    height: 200px;
    background-color: red;
  }
  .right {
    flex: 1;
    height: 400px;
    background-color: blue;
  }
  // 父元素相对定位，左侧元素绝对定位，右侧自适应元素设置 margin-left 的值大于定宽元素的宽度
  .left {
    position: absolute;
    width: 100px;
    height: 200px;
    background-color: red;
  }
  .right {
    margin-left: 100px;
    height: 400px;
    background-color: blue;
  }
  ```

  2. 左右两侧元素都自适应

  ```css
  // flex 布局 同上
  // 父元素设置 display：grid; grid-template-columns\:auto 1fr;（这个属性定义列宽，auto 关键字表示由浏览器自己决定长度。fr 是一个相对尺寸单位，表示剩余空间做等分）grid-gap:20px（行间距）
  .parent {
    display: grid;
    grid-template-columns: auto 1fr;
    grid-gap: 20px;
  }
  .left {
    background-color: red;
    height: 200px;
  }
  .right {
    height: 300px;
    background-color: blue;
  }
  // 浮动+BFC 父元素设置 overflow\:hidden,左侧定宽元素浮动，右侧自适应元素设置 overflow\:auto 创建 BFC
  .box {
    height: 600px;
    width: 100%;
    overflow: hidden;
  }
  .left {
    float: left;
    width: 100px;
    height: 200px;
    background-color: red;
  }
  .right {
    overflow: auto;
    height: 400px;
    background-color: blue;
  }
  ```

- CSS 三列布局
  1. float 布局：左边左浮动，右边右浮动，中间 margin：0 100px;
  2. Position 布局: 左边 left：0; 右边 right：0; 中间 left: 100px; right: 100px;
  3. table 布局: 父元素 display: table; 左右 width: 100px; 三个元素 display: table-cell;
  4. 弹性(flex)布局:父元素 display: flex; 左右 width: 100px;
  5. 网格（gird）布局：
  ```css
  // gird 提供了 gird-template-columns、grid-template-rows 属性让我们设置行和列的高、宽
  .div {
    width: 100%;
    display: grid;
    grid-template-rows: 100px;
    grid-template-columns: 300px auto 300px;
  }
  ```
- app 与 H5 如何通讯交互的？

  ```javascript
  // 兼容IOS和安卓
  function callMobile(parameters, messageHandlerName) {
    //handlerInterface由iOS addScriptMessageHandler与andorid addJavascriptInterface 代码注入而来。
    if (/(iPhone|iPad|iPod|iOS)/i.test(navigator.userAgent)) {
      // alert('ios')
      window.webkit.messageHandlers[messageHandlerName].postMessage(JSON.stringify(parameters))
    } else {
      // alert('安卓')
      //安卓传输不了js json对象，只能传输string
      window.webkit[messageHandlerName](JSON.stringify(parameters))
    }
  }
  ```

  由 app 将原生方法注入到 window 上供 js 调用
  `messageHandlerName` 约定的通信方法`parameters`需要传入的参数

- 移动端适配方案
  `rem`是相对于 HTML 的根元素`em`相对于父级元素的字体大小。`VW,VH` 屏幕宽度高度的高分比
  ```javascript
  //按照宽度375图算， 1rem = 100px;
  ;(function (win, doc) {
    function changeSize() {
      doc.documentElement.style.fontSize = doc.documentElement.clientWidth / 3.75 + 'px'
      console.log((100 * doc.documentElement.clientWidht) / 3.75)
    }
    changeSize()
    win.addEventListener('resize', changeSize, false)
  })(window, document)
  ```
- 实现发布订阅

  ```javascript
  /* Pubsub */
  function Pubsub() {
    //存放事件和对应的处理方法
    this.handles = {}
  }

  Pubsub.prototype = {
    //传入事件类型type和事件处理handle
    on: function (type, handle) {
      if (!this.handles[type]) {
        this.handles[type] = []
      }
      this.handles[type].push(handle)
    },
    emit: function () {
      //通过传入参数获取事件类型
      //将arguments转为真数组
      var type = Array.prototype.shift.call(arguments)
      if (!this.handles[type]) {
        return false
      }
      for (var i = 0; i < this.handles[type].length; i++) {
        var handle = this.handles[type][i]
        //执行事件
        handle.apply(this, arguments)
      }
    },
    off: function (type, handle) {
      handles = this.handles[type]
      if (handles) {
        if (!handle) {
          handles.length = 0 //清空数组
        } else {
          for (var i = 0; i < handles.length; i++) {
            var _handle = handles[i]
            if (_handle === handle) {
              //从数组中删除
              handles.splice(i, 1)
            }
          }
        }
      }
    }
  }
  ```

- 对象数组转换成 tree 数组
  将 entries 按照 level 转换成 result 数据结构

  ```javascript
  const entries = [
    {
      province: '浙江',
      city: '杭州',
      name: '西湖'
    },
    {
      province: '四川',
      city: '成都',
      name: '锦里'
    },
    {
      province: '四川',
      city: '成都',
      name: '方所'
    },
    {
      province: '四川',
      city: '阿坝',
      name: '九寨沟'
    }
  ]

  const level = ['province', 'city', 'name']

  const result = [
    {
      value: '浙江',
      children: [
        {
          value: '杭州',
          children: [
            {
              value: '西湖'
            }
          ]
        }
      ]
    },
    {
      value: '四川',
      children: [
        {
          value: '成都',
          children: [
            {
              value: '锦里'
            },
            {
              value: '方所'
            }
          ]
        },
        {
          value: '阿坝',
          children: [
            {
              value: '九寨沟'
            }
          ]
        }
      ]
    }
  ]
  ```

  思路：涉及到树形数组，采用递归遍历的方式

  ```javascript
  function transfrom(list, level) {
    const res = []
    list.forEach((item) => {
      pushItem(res, item, 0)
    })

    function pushItem(arr, obj, i) {
      const o = {
        value: obj[level[i]],
        children: []
      }
      // 判断传入数组里是否有value等于要传入的项
      const hasItem = arr.find((el) => el.value === obj[level[i]])
      let nowArr
      if (hasItem) {
        // 存在，则下一次遍历传入存在项的children
        nowArr = hasItem.children
      } else {
        // 不存在 压入arr，下一次遍历传入此项的children
        arr.push(o)
        nowArr = o.children
      }
      if (i === level.length - 1) delete o.children
      i++
      if (i < level.length) {
        // 递归进行层级的遍历
        pushItem(nowArr, obj, i)
      }
    }
  }

  transfrom(entries, level)
  ```

- JS instanceof 方法原生实现

  ```javascript
  // left instanceof right
  function _instanceof(left, right) {
    // 构造函数原型
    const prototype = right.prototype
    // 实列对象属性，指向其构造函数原型
    left = left.__proto__
    // 查实原型链
    while (true) {
      // 如果为null，说明原型链已经查找到最顶层了，真接返回false
      if (left === null) {
        return false
      }
      // 查找到原型
      if (prototype === left) {
        return true
      }
      // 继续向上查找
      left = left.__proto__
    }
  }

  const str = 'abc'
  _instanceof(str, String) // true
  ```

- 将有同样元素的数组进行合并

  ```javascript
  // 例如：
  const arr = [['a', 'b', 'c'], ['a', 'd'], ['d', 'e'], ['f', 'g'], ['h', 'g'], ['i']]

  // 运行后的返回结果是：
  ;[['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h'], ['i']]

  // 思路一：
  const arr = [['a', 'b', 'c'], ['a', 'd'], ['d', 'e'], ['f', 'g'], ['h', 'g'], ['i']]
  function transform(arr) {
    let res = []
    arr = arr.map((el) => el.sort()).sort()
    const item = arr.reduce((pre, cur) => {
      if (cur.some((el) => pre && pre.includes(el))) {
        pre = pre.concat(cur)
      } else {
        res.push(pre)
        pre = cur
      }
      return [...new Set(pre)]
    })
    res.push(item)
    return res
  }
  transform(arr)
  // console.log(transform(arr));

  // 思路二：

  function r(arr) {
    const map = new Map()
    arr.forEach((array, index) => {
      const findAlp = array.find((v) => map.get(v))
      if (findAlp) {
        const set = map.get(findAlp)
        array.forEach((alp) => {
          set.add(alp)
          const findAlp2 = map.get(alp)
          if (findAlp2 && findAlp2 !== set) {
            for (const v of findAlp2.values()) {
              set.add(v)
              map.set(v, set)
            }
          }
          map.set(alp, set)
        })
      } else {
        const set = new Set(arr[index])
        array.forEach((alp) => map.set(alp, set))
      }
    })
    const set = new Set()
    const ret = []
    for (const [key, value] of map.entries()) {
      if (set.has(value)) continue
      set.add(value)
      ret.push([...value])
    }
    return ret
  }
  ```

- HTTPS 建立连接过程
  ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/2wV7LicL762Ym8XMXlVCQuYt9NB2ZQOCzmjW2I6ffG1c44PyPcMn6kia6qGaCoicmX12F9LGuAUgU8AxXOBhu291A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
- http 缓存，强缓存时 cache-control 字符集是什么 publichttps\://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Cache-Control
- 深拷贝的实现，如果遇到 function 怎么办
  需要判断类型，对于基础类型，直接赋值，对于复杂类型则需要递归处理，并同时设置 map，避免嵌套。对于 function 可以通过 new Function(' return '+ fn.toString())的方式拷贝
- webpack 有用过哪些 loader、webpack 做过哪些优化
  loader：babel-loader、ts-loader、style-loader、css-loader、less-loader
  优化：提取公共代码、代码分割、代码压缩、按需加载、预加载
- 微前端的问题，设计思路，有遇到哪些问题，如何做样式隔离。
  公用路由的设计
  采用路由分层的方式，将路由划分为 4 层，第一层用来区分是 iframe 还是微应用，第二层用来区分具体的 app 页面名称由此在配置表中拿到具体的配置信息，第三层为子应用的路由，第 4 层为子应用的参数。由此实现基座与微应用的路由共享。
  样式隔离，一是通过 qiankun 自身提供的样式沙箱 `{ sandbox : { experimentalStyleIsolation: true } }` ，二是 vue 组件样式使用 scoped，三是顶层样式增加私有类名
  面试官反馈说，iframe 还是微应用对于用户来说是无感的，配置表区分 iframe 还是微应用即可，不必多占一层路由
- 为什么要使用 composition-api
  首先因为业务性质需要兼容 ie 所以项目只能使用 vue2
  通过使用@vue/composition-api 方式使用新特性。转变以往的 vue 选项式开发，为更贴近函数式的代码开发。使原本关联逻辑分散在各个选项中，组件代码庞大的问题的问题得到解决，提高代码易读性、可维护性。同时通过抽取 hook 实现逻辑复用，提升效率。相较于 mixin 具有隐式依赖等缺点，更具备可用性。
- 纯数字版本号数组排序

  ```javascript
  function versionSort(versions) {
    return versions.sort((a, b) => {
      const aArr = a.split('.')
      const bArr = b.split('.')
      while (aArr.length || bArr.length) {
        const A = aArr.shift() || 0
        const B = bArr.shift() || 0
        if (A - B !== 0) {
          return A - B
        }
      }
    })
  }
  ```

- http 请求头有哪些字段
  Accept 系列、Cache-Control、Cookie、Host 等等<https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers>
- 原型链 <https://juejin.cn/post/6934498361475072014>
- 工作中遇到的具有挑战的事情 从零开始搭建完善的工具库，如何组织代码？如何保持资源的动态引入？如何来做单元测试？
- 单页面通信，多页面通信 这个我一下蒙了。但是感觉应该是路由通信、借助 cookie、localStorage 通信，以及 iframe 的通过 addEventListener 和 postMessage 通信
- 微前端样式隔离
- 网络安全展开说
  几种安全问题：XXS CSRF、点击嵌套劫持、CDN 劫持等
  防范主要围绕同源策略，cookie 的 sameSite 、http-only，referer 的验证，CSP 等方式来避免
  <https://zhuanlan.zhihu.com/p/83865185>
- webpack 与 rollup 的区别
  webpack 大而全，功能全面配置完善，同时 loader 与 plugin 非常丰富。并且具有 deveServer 方便开发调试
  rollup 小而美，相较没有 webpack 完善但是同样体积更小速度更快。类似压缩等基础功能也要通过插件实现。更适合做一些工具库的打包处理
- 介绍一下你写的 webpack loader
  工具为了兼容 vue2、vue3 两个版本，核心代码是完全相同的，差异只是在 vue 特性 api 的引入上，vue2 从@vue/composition-api 中引入，vue3 从 vue 中引入.所以 loader 做的事情就是在构建 vue2 版本的时候将`import { *** } from 'vue' `替换为 `import { *** } from '@vue/composition-api'`
- 实现具有并发限制的 promise.all

  ```javascript
  function promsieTask(taskList, maxNum) {
    return new Promise((resolve, rejuct) => {
      let runCount = 0
      let complated = 0
      const taskNum = taskList.length
      const resArr = []
      let current = 0
      function handler() {
        if (runCount >= maxNum) return
        const a = taskNum - complated
        const b = maxNum - runCount
        const arr = taskList.splice(0, a > b ? b : a)
        arr.forEach((task, index) => {
          const d = current + index
          task
            .then(
              (res) => {
                console.log(current, index, res)
                resArr[current] = res
              },
              (reason) => {
                resArr[current] = reason
              }
            )
            .finally(() => {
              complated++
              runCount--
              if (complated === taskNum) {
                resolve(resArr)
              }
              handler()
            })
        })
        current += taskList.length
      }
      handler()
    })
  }
  ```

- 输入一个正整数，输出他的两个素数因子，如没有输出 -1 -1
- 输入两个数组，分别从两个数组中取出一个元素相加，和作为一个元素，求 K 个这样的元素的最小和。坐标完全相同，属于同一个元素。
- 输入一个 n\*m 的多维数组，输出一个字符串，按顺序将字符串中的每一个字符在数组中查找，要求查找位置必须相邻，且每一个元素只能使用一次。输出字符串在数组中的坐标
- http 请求头有哪些关键字，反映客户端信息的是那个字段
  同上 User-Agent
- http 请求触发 catch 的原因可能有哪些
  拦截器捕获其他异常，比如 204，请求处理函数执行异常，返回资源异常（不符合接口定义）
- 微前端的技术方案是怎么确定的，有没有遇到什么问题，样式隔离，数据管理，路由冲突
  是主要由我决定的。采用 qiankun 的原因，一是方案成熟，文档健全，社区案例多。二是我自身以前有过一些经验，对 qiankun 比较了解，能够快速落地
  样式隔离，一是通过 qiankun 自身提供的样式沙箱 `{ sandbox : { experimentalStyleIsolation: true } }` ，二是 vue 组件样式使用 scoped，三是顶层样式增加私有类名
  数据管理，qiankun 本身有提供 globalState 相关 api，但是子应用只能在 onchange 事件触发时才能拿到公共数据。所以先声明公共数据，通过 initGlobalState 注册，然后在微应用注册阶段通过 props 方式预先传递给子应用。在子应用侧，通过 mounted 钩子和 onClobalStateChange 共同维护公共数据
  路由冲突，子应用是需要与基座共享路由的，所以在路由激活子应用的模式下。预先分配给子应用一个激活路由，这个路由同时也是子应用的 baseRoute，在挂载阶段通过 props 传递，子应用拿到 baseRoute 作为前缀注册路由。从而实现路由共享。
  qiankun 的打包配置 <https://qiankun.umijs.org/zh/guide>
  了解市面上其他的微前端方案么
  是类似乾坤、飞冰这种基于 singleSpa 的方案
  是类似美团那种，相同技术架构的，自研原生实现
  为什么使用 Monorepo 组织代码仓库
  我们这个库，设计上就是要能够支持 vue2、vue3 两个版本，以及不同业务需要的 采用 Monorepo 组织代码仓库，方便管理维护不同的功能包、既做到了独立发布，又能在项目中统一维护
- webpack 知道有哪些插件 lodaer 么？
- webpack 你知道哪些优化
  构建阶段、多线程、缓存
  资源产物 代码压缩、代码分割、提取公共代码、懒加载、预加载
- leetcode 452 题<https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/>
- http1 和 http2 的区别
  压缩请求头，二进制分帧、多路复用<https://zhuanlan.zhihu.com/p/102561034>
- 讲一下 loader 和 plugin
  webpack 的 loader 主要用来处理特定的文件，进行转换
  plugin 通过 wepack 提供的构建钩子可以实现 loader 无法实现的功能，比如 deveServer、代码分割等
- extenral
  通过`extenrals` 选项，可以将依赖从输出的 bundle 中移除，并保持资源引入
- 讲一下微前端
  微前端并不是为了取代 iframe，他们都有所适用的场景。对于部分相互独立并没有什么复杂数据交互的项目来说 iframe 就很合适，而且天生具备很好的隔离。
  而对于具有数据交互，尤其是在一个大项目中拆解出不同的业务功能模块来说，微前端的模式更合适。
- vue2 和 vue3 的响应式
  vue2 的响应式是基于`Object.definePropert` 数据劫持与数组常用方法的改写来实现的。对于复杂数据类型，需要层层递归劫持，性能较差
  vue3 是通过原生 api `proxy` 代理实现的，不需要递归，也不需要改写方法，性能更好，支持更好。但是由于代理只是对目标对象，在传递响应式对象时，操作不当容易丢失响应性。
- promise、promise.all ,promise 与 async await 的区别，async await 如并发 promise
- 计算岛屿周长
  ```javascript
  // 给定一个 row x col 的二维网格地图 grid ，其中：grid[i][j] = 1 表示陆地， grid[i][j] = 0 表示水域。
  // 网格中的格子 水平和垂直 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
  // 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。
  // 示例 1：输入：grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
  // 输出：16
  // 解释：它的周长是上面图片中的 16 个黄色的边
  // 示例 2：输入：grid = [[1]]
  // 输出：4
  ```
- http 缓存 cache-control 字符集
  max-age public private no-cache no-store
- 网络安全，页面出现广告什么原因
  XSS 脚本添加页面？页面劫持、代理？CDN，iframe 嵌套 同上
- 微前端样式隔离，js 隔离原理
- babel 原理
- loader 和 plugin 的区别
- Object.assgin 与 ...复制对象的区别
  这个除了使用方式上，并没有感觉有什么不同，之后尝试了一下表现也是一样的
- 有做过组件库，或者这种公共基础么？有考虑哪些设计原则
  单一原则、拓展性、可靠性
- 有用过哪些 ide 的能力（变更函数名？）
- 尾递归优化
  这个是从调用栈的角度来讲的，通过尾递归优化的方式，释放中间变量 <https://zhuanlan.zhihu.com/p/393711134>
- ts 用过那些函数，interface 和 type 的区别
  interface 可以拓展 extends
  interface 能够声明合并
  type 不可以 extends、implement 但是可以类型交叉
  type 可以声明类型别名、联合类型、元组 interface 不可以
- 扁平化嵌套数组有几种方式
  flat
  toString().split(',')
  递归
- 介绍数据流，是否了解市面上其他公共状态管理工具
  有了解 Pinia https://pinia.vuejs.org/introduction.html#basic-example
  通过 vue3 提供的响应式 api，我们获得了无需借助第三方工具，即可实现公共响应式数据的维护。
  我们总结了一些经验，可以直接定义响应式数据，以及更新他的 set 方法通过代码引入，props 传递以及 porvide/inject 的方式灵活使用。
  感觉这部分表达为什么不用市面上已有的状态管理库而用我们的方案，这部分讲的不够自信，理由不够充分
- 问微前端的选型原因
  一是 qiankun 的技术方案相对比较完善，无论是常见问题还是社区经验都比较丰富
  二是我个人之前有一定的知识储备，使用 qiankun 能够容易落地
- 如何寻找到两个 dom 节点的最近公共父节点
  通过从下向上递归，并将父节点储存，比较
- 常用那几种浏览器测试？有哪些内核(Layout Engine)?
  (Q1)浏览器：IE，Chrome，FireFox，Safari，Opera。
  (Q2)内核：Trident，Gecko，Presto，Webkit。
- 说下行内元素和块级元素的区别？行内块元素的兼容性使用？（IE8 以下）
  (Q1)行内元素：会在水平方向排列，不能包含块级元素，设置 width 无效，height 无效(可以设置 line-height)，margin 上下无效，padding 上下无效。
  块级元素：各占据一行，垂直方向排列。从新行开始结束接着一个断行。
  (Q2)兼容性：display:inline-block;display:inline;zoom:1;
- 清除浮动有哪些方式？比较好的方式是哪一种？
  (Q1)
  （1）父级 div 定义 height。
  （2）结尾处加空 div 标签 clear:both。
  （3）父级 div 定义伪类:after 和 zoom。
  （4）父级 div 定义 overflow:hidden。
  （5）父级 div 定义 overflow:auto。
  （6）父级 div 也浮动，需要定义宽度。
  （7）父级 div 定义 display:table。
  （8）结尾处加 br 标签 clear:both。
  (Q2)比较好的是第 3 种方式，好多网站都这么用。
- box-sizing 常用的属性有哪些？分别有什么作用？
  (Q1)box-sizing: content-box|border-box|inherit;
  (Q2)content-box:宽度和高度分别应用到元素的内容框。在宽度和高度之外绘制元素的内边距和边框(元素默认效果)。
  border-box:元素指定的任何内边距和边框都将在已设定的宽度和高度内进行绘制。通过从已设定的宽度和高度分别减去边框和内边距才能得到内容的宽度和高度。
- Doctype 作用？标准模式与兼容模式各有什么区别?
  (Q1)告知浏览器的解析器用什么文档标准解析这个文档。DOCTYPE 不存在或格式不正确会导致文档以兼容模式呈现。
  (Q2)标准模式的排版和 JS 运作模式都是以该浏览器支持的最高标准运行。在兼容模式中，页面以宽松的向后兼容的方式显示,模拟老式浏览器的行为以防止站点无法工作。
- HTML5 为什么只需要写 <!DOCTYPE HTML>
  HTML5 不基于 SGML，因此不需要对 DTD 进行引用，但是需要 doctype 来规范浏览器的行为（让浏览器按照它们应该的方式来运行）。
  而 HTML4.01 基于 SGML,所以需要对 DTD 进行引用，才能告知浏览器文档所使用的文档类型。
- 页面导入样式时，使用 link 和@import 有什么区别？
  （1）link 属于 XHTML 标签，除了加载 CSS 外，还能用于定义 RSS, 定义 rel 连接属性等作用；而@import 是 CSS 提供的，只能用于加载 CSS;
  （2）页面被加载的时，link 会同时被加载，而@import 引用的 CSS 会等到页面被加载完再加载;
  （3）import 是 CSS2.1 提出的，只在 IE5 以上才能被识别，而 link 是 XHTML 标签，无兼容问题;
- 介绍一下你对浏览器内核的理解？
  主要分成两部分：渲染引擎(layout engineer 或 Rendering Engine)和 JS 引擎。
  渲染引擎：负责取得网页的内容（HTML、XML、图像等等）、整理讯息（例如加入 CSS 等），以及计算网页的显示方式，然后会输出至显示器或打印机。浏览器的内核的不同对于网页的语法解释会有不同，所以渲染的效果也不相同。所有网页浏览器、电子邮件客户端以及其它需要编辑、显示网络内容的应用程序都需要内核。
  JS 引擎则：解析和执行 javascript 来实现网页的动态效果。
  最开始渲染引擎和 JS 引擎并没有区分的很明确，后来 JS 引擎越来越独立，内核就倾向于只指渲染引擎。
- html5 有哪些新特性？如何处理 HTML5 新标签的浏览器兼容问题？如何区分 HTML 和 HTML5？
  （Q1）
  HTML5 现在已经不是 SGML 的子集，主要是关于图像，位置，存储，多任务等功能的增加。
  (1)绘画 canvas;
  (2)用于媒介回放的 video 和 audio 元素;
  (3)本地离线存储 localStorage 长期存储数据，浏览器关闭后数据不丢失;
  (4)sessionStorage 的数据在浏览器关闭后自动删除;
  (5)语意化更好的内容元素，比如 article、footer、header、nav、section;
  (6)表单控件，calendar、date、time、email、url、search;
  (7)新的技术 webworker, websocket, Geolocation;
  (Q2)
  IE8/IE7/IE6 支持通过 document.createElement 方法产生的标签，
  可以利用这一特性让这些浏览器支持 HTML5 新标签，
  浏览器支持新标签后，还需要添加标签默认的样式。
  当然也可以直接使用成熟的框架、比如 html5shim;
- 简述一下你对 HTML 语义化的理解？
  用正确的标签做正确的事情。
  html 语义化让页面的内容结构化，结构更清晰，便于对浏览器、搜索引擎解析;
  即使在没有样式 CSS 情况下也以一种文档格式显示，并且是容易阅读的;
  搜索引擎的爬虫也依赖于 HTML 标记来确定上下文和各个关键字的权重，利于 SEO;
  使阅读源代码的人对网站更容易将网站分块，便于阅读维护理解。
- eval 是做什么的？
  它的功能是把对应的字符串解析成 JS 代码并运行；
  应该避免使用 eval，不安全，非常耗性能（2 次，一次解析成 js 语句，一次执行）。
  由 JSON 字符串转换为 JSON 对象的时候可以用 eval，var obj =eval('('+ str +')');
- DOM 怎样添加、移除、移动、复制、创建和查找节点
- null 和 undefined 的区别？
  null 是一个表示"无"的对象，转为数值时为 0；undefined 是一个表示"无"的原始值，转为数值时为 NaN。
  undefined：
  （1）变量被声明了，但没有赋值时，就等于 undefined。
  （2) 调用函数时，应该提供的参数没有提供，该参数等于 undefined。
  （3）对象没有赋值的属性，该属性的值为 undefined。
  （4）函数没有返回值时，默认返回 undefined。
  null：
  （1） 作为函数的参数，表示该函数的参数不是对象。
  （2） 作为对象原型链的终点。
- new 操作符具体干了什么呢?
  （1）创建一个空对象，并且 this 变量引用该对象，同时还继承了该函数的原型。
  （2）属性和方法被加入到 this 引用的对象中。
  （3）新创建的对象由 this 所引用，并且最后隐式的返回 this 。
- JSON 的了解？
  JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式。它是基于 JavaScript 的一个子集。数据格式简单, 易于读写, 占用带宽小。
  格式：采用键值对，例如：{'age':'12', 'name':'back'}
- call() 和 apply() 的区别和作用？
  apply()函数有两个参数：第一个参数是上下文，第二个参数是参数组成的数组。如果上下文是 null，则使用全局对象代替。如：function.apply(this,[1,2,3]);
  call()的第一个参数是上下文，后续是实例传入的参数序列。 如：function.call(this,1,2,3);
- 如何获取 UA？
- HTTP 状态码知道哪些？
  100 Continue 继续，一般在发送 post 请求时，已发送了 http header 之后服务端将返回此信息，表示确认，之后发送具体参数信息
  200 OK 正常返回信息
  201 Created 请求成功并且服务器创建了新的资源
  202 Accepted 服务器已接受请求，但尚未处理
  301 Moved Permanently 请求的网页已永久移动到新位置。
  302 Found 临时性重定向。
  303 See Other 临时性重定向，且总是使用 GET 请求新的 URI。
  304 Not Modified 自从上次请求后，请求的网页未修改过。资源未修改，使用缓存
  400 Bad Request 服务器无法理解请求的格式，客户端不应当尝试再次使用相同的内容发起请求。
  401 Unauthorized 请求未授权。
  403 Forbidden 禁止访问。
  404 Not Found 找不到如何与 URI 相匹配的资源。
  500 Internal Server Error 最常见的服务器端错误。
  503 Service Unavailable 服务器端暂时无法处理请求（可能是过载或维护）。
- 你有哪些性能优化的方法？
  （1） 减少 http 请求次数：CSS Sprites, JS、CSS 源码压缩、图片大小控制合适；网页 Gzip，CDN 托管，data 缓存 ，图片服务器。
  （2） 前端模板 JS+数据，减少由于 HTML 标签导致的带宽浪费，前端用变量保存 AJAX 请求结果，每次操作本地变量，不用请求，减少请求次数
  （3） 用 innerHTML 代替 DOM 操作，减少 DOM 操作次数，优化 javascript 性能。
  （4） 当需要设置的样式很多时设置 className 而不是直接操作 style。
  （5） 少用全局变量、缓存 DOM 节点查找的结果。减少 IO 读取操作。
  （6） 避免使用 CSS Expression（css 表达式）又称 Dynamic properties(动态属性)。
  （7） 图片预加载，将样式表放在顶部，将脚本放在底部 加上时间戳。
- 什么叫优雅降级和渐进增强？
  优雅降级：Web 站点在所有新式浏览器中都能正常工作，如果用户使用的是老式浏览器，则代码会检查以确认它们是否能正常工作。由于 IE 独特的盒模型布局问题，针对不同版本的 IE 的 hack 实践过优雅降级了,为那些无法支持功能的浏览器增加候选方案，使之在旧式浏览器上以某种形式降级体验却不至于完全失效.
  渐进增强：从被所有浏览器支持的基本功能开始，逐步地添加那些只有新式浏览器才支持的功能,向页面增加无害于基础浏览器的额外样式和功能的。当浏览器支持时，它们会自动地呈现出来并发挥作用。
- 哪些常见操作会造成内存泄漏？
  内存泄漏指任何对象在您不再拥有或需要它之后仍然存在。
  垃圾回收器定期扫描对象，并计算引用了每个对象的其他对象的数量。如果一个对象的引用数量为 0（没有其他对象引用过该对象），或对该对象的惟一引用是循环的，那么该对象的内存即可回收。
  setTimeout 的第一个参数使用字符串而非函数的话，会引发内存泄漏。
  闭包、控制台日志、循环（在两个对象彼此引用且彼此保留时，就会产生一个循环）
- 线程与进程的区别
  一个程序至少有一个进程,一个进程至少有一个线程.
  线程的划分尺度小于进程，使得多线程程序的并发性高。
  另外，进程在执行过程中拥有独立的内存单元，而多个线程共享内存，从而极大地提高了程序的运行效率。
  线程在执行过程中与进程还是有区别的。每个独立的线程有一个程序运行的入口、顺序执行序列和程序的出口。但是线程不能够独立执行，必须依存在应用程序中，由应用程序提供多个线程执行控制。
  从逻辑角度来看，多线程的意义在于一个应用程序中，有多个执行部分可以同时执行。但操作系统并没有将多个线程看做多个独立的应用，来实现进程的调度和管理以及资源分配。这就是进程和线程的重要区别。
- 解析 URL
  出现得挺高频的，把一个 url 的 query 参数，解析成指定格式的对象。
- 对象的合并，key 值的转化
  出现得也比较多，给你一个对象，也是把它转化成指定的格式。比如把 _a_b_ 这种下划线的 key 值转化为驼峰 _aB_，或者给你一个些数据，转化成对象。
  比如把 _a.b.c_ 变成 { a: { b: c } }
- 实现 vue 的双向绑定
- 实现 eventListener
- webpack 的 plugin 和 loader 有啥区别，有写过什么 loader 和 plugin 吗
- 打包优化，性能提升
- promise async await。
- import 和 require
- 原型链, new
- 跨域(cors), http 请求
- XSS 和 CSRF
- setTimeout 为什么最小只能设置 4ms，怎么实现一个 0ms 的 setTimeout?
- 看你简历上有写到 rem 和 vw，能讲讲吗？为什么你选择使用 rem 而不是 vw？
  当时回答是 rem 兼容性更好，且 px 转 rem 后可以避免过长小数。
- 浏览器对于小数单位是怎么计算的？
- interface 和 type 的区别是什么？你日常工作中是用 interface 还是 type？
- ts 的逆变和协变有没有了解过？
- 能不能讲讲小程序的原理？
- 小程序有没有 HMR，能不能讲讲 HMR 的原理？
  小程序没有 HMR，当时只讲出来了保存代码小程序是怎么刷新的，HMR 没有讲出来。
- 讲讲 z-index
- 实现一个 ts Include
- 实现一个 useInterval
- js event loop 执行顺序
- options 请求是什么？有什么作用？
- cdn 的原理是什么，是在网络哪一层起的作用？
- 项目性能是如何做优化的？
  - 我主要从网络，缓存，js，css，接口合并等几个方面讲的，该题比较宽泛，可自行发挥。
- 动态创建 script 标签并插入到页面上，说执行时机
- 给你一个“A2B3”这样的字符串，输出“AABBB”
- 接上题“C4(A(A3B)2)2”，带嵌套的，这两题都不是原题，但是类似
- 写一个 curry，要求 add(1)(2)(3)(4) 打印 10
  一开始我洗的 add(1)(2)(3)(4)()，面试官问我能不能把最后的()去掉，最后寻求提示，他说 console.log 是怎么打印函数的，豁然开朗，复写 toString 即可。
- loader 和 plugin 的区别是什么？
- webpack 打包优化，我还提到了 vite，顺便讲了下 vite
- 小程序原理，以及 Taro 原理
- xss 和 csrf
- http2
- Tree Shaking 原理
- 最长回文子串
- 聊了很多工程化相关的问题，主要是项目从开发到上线这一整套流程，聊完之后他也指出了我说的这一套流程有什么不完善的地方。
- React fiber
- http2
- Tree Shaking 原理
- 项目优化和网络优化
- 股票最大收益
- 各个模块、按钮怎么设计权限；
- 分角色、分地域怎么设计？
- 要加个表头，还要控制展示的顺序，在各个浏览器表现一致，怎么设计？说出所有方案，想到什么自由发挥了……
- 聊到本地存储，问：localStorage 在各浏览器、移动端浏览器的 size 一致吗？
- 这一段是我简历的项目，略过……
- 继续聊阿里的产品，简单使用后，请提出几个可以优化的地方？
- 啥也没透露，让你预测下这款产品的接下来的方向，如果是你，你会着手哪个方向，并且凭啥让你来干，说下你擅长的……
- 正式讨论产品，大家都在做什么，团队协作的情况，公布接下来的迭代方向，针对的人群，目标……
- 计算多个区间的交集
  ```javascript
  /**
   *   区间用长度为2的数字数组表示，如[2, 5]表示区间2到5（包括2和5）；
   *   区间不限定方向，如[5, 2]等同于[2, 5]；
   *   实现`getIntersection 函数`
   *   可接收多个区间，并返回所有区间的交集（用区间表示），如空集用null表示
   * 示例：
   *   getIntersection([5, 2], [4, 9], [3, 6]); // [4, 5]
   *   getIntersection([1, 7], [8, 9]); // null
   */
  ```
- DOM 的体积过大会影响页面性能，假如你想在用户关闭页面时统计（计算并反馈给服务器）当前页面中元素节点的数量总和、元素节点的最大嵌套深度以及最大子元素个数，请用 JS 配合原生 DOM API 实现该需求（不用考虑陈旧浏览器以及在现代浏览器中的兼容性，可以使用任意浏览器的最新特性；不用考虑 shadow DOM）。比如在如下页面中运行后：

  ```html
  <html>
    <head></head>
    <body>
      <div>
        <span>f</span>
        <span>o</span>
        <span>o</span>
      </div>
    </body>
  </html>
  <!--
      {
        totalElementsCount: 7,
        maxDOMTreeDepth: 4,
        maxChildrenCount: 3
      }
      -->
  ```

- 请使用原生代码实现一个 Events 模块，可以实现自定义事件的订阅、触发、移除功能

  ```javascript
  const fn1 = (...args) => console.log('I want sleep1', ...args)
  const fn2 = (...args) => console.log('I want sleep2', ...args)
  const event = new Events()
  event.on('sleep', fn1, 1, 2, 3)
  event.on('sleep', fn2, 1, 2, 3)
  event.fire('sleep', 4, 5, 6)
  // I want sleep1 1 2 3 4 5 6
  // I want sleep2 1 2 3 4 5 6
  event.off('sleep', fn1)
  event.once('sleep', () => console.log('I want sleep'))
  event.fire('sleep')
  ```

- 跨端的原理？我讲了几个例子：taro、uni-app，顺便提了 flutter、react native、小程序等的架构，具体怎么设计的。
- 动态表单能够运用在什么场景？我举了 7、8 个例子。
- 移动端适配相关的问题，应用场景。
- B 端遇到的最复杂的数据结构是什么
- 数据展示的优化、数据截取和处理
- 实际场景中，哪些地方应用到了堆、链表、多叉树结构
- es6 及 es6+ 的能力集，你最常用的，这其中最有用的，都解决了什么问题。
- GC 相关问题：es6+ ，eventloop 中涉及 GC 的部分。
- 数组 flat 展开的各种解法，数组 map 应用
- 讲下 V8 sort 的大概思路
- Promise 并发限制
- 省市区拼接查字段，要求 O(n) 内解出
- 中台的理解
- 项目的复盘优化
- 说下业务上最复杂的点
- node 限流算法
- 最有效的性能优化方法
- 你提到性能指标，能说说都是怎么计算的吗？比如 LCP，FID
- 算法题：**数组全排列**
- 中台业务讨论
- input type 都有哪些类型，还记得其他 attrs 呢
- css 的伪类和伪元素有哪些？有什么区别？
- 在一个未知宽度的父元素内如何创建一个等边正方形
- 异步加载 js 会阻塞什么
- 数组所有方法都有哪些？findIndex 的参数说明
- vue 和 react 的异同
- 如何优化 vue 框架，注意是优化框架
- vue 和 react 的 jsx 使用
- id key 真的能使列表比对更高效吗？举个反例？
- webpack 优化的手段
- tree-shaking 怎么配置，如何 **避免** tree-shaking？
- electron 和小程序遇到什么坑？
- 说下微信自动化测试
- es2015 到 es2020 的新特性，你最常用什么，给你收益最大的。
- weakMap 和 Map 的区别，weakMap 原理，为什么能被 GC？
- 如何干扰 GC ？
- webpack import 动态加载原理
- 知道 webpack 中的 devTool 吗？
- 如何进行错误定位和数据上报，线上异常的处理
- 为什么有时候配置了 webpack caching，chunk 还是更新了？
- 讲讲浏览器和 node 的 eventloop
- 微任务后面还有哪些？requestAnimationFrame 是怎么调用的？requestAnimationFrame 帧内总是有任务吗？分情况说下。
- 帧数怎么计算？
- 了解网络安全吗？
- 如何避免数据被 iframe 截获
- 说下状态码
- 说下 304，什么情况会 304？协商缓存的头部字段？
- 工程化实践的看法
- 项目是如何收集问题的，用户量如何？
- 性能问题如何排查，你们项目的指标，具体数据、截图发给我看看……
- 模块化是怎么实施的？
- 目录结构讲下
- 一些功能是自研还是使用第三方工具，叫什么名字，怎么使用 ？
- 疯狂问测试相关的内容，单元测试和组件测试是怎么做的、代码覆盖率多少，如何权衡测试原则，系统测试相关的内容，一些细节上的问题怎么处理，等等，要说出个 1、2、3 来 ？
- 项目亮点/难点，怎么解决 ？
- 复盘，整个项目总结，让你重新设计这套系统你会怎么做 ？
- 工程化实践和深入的一个点
- 团队氛围，有什么好的点可以说下，有什么不好的点也说下……
- 中台具体集成了什么功能 ？你都做了什么 ？
- webpack 提高构建速度的方式
- loader 输入什么产出什么 ？
- webpack 原理
- webpack 动态加载的原理
- webpack 热更新
- 如何写一个 webpack plugin
- AST 的应用
- 如何解析一个 html 文本，还是考 AST
- babel 原理，怎么写 babel 插件
- 小程序的 API 做了什么处理，能够做到全局变量的隐藏，如果是你，怎么设计 ？
- 基础题考闭包的，我讲对了思路，结果没做对。
- 实现颜色转换 'rgb(255, 255, 255)' -> '#FFFFFF' 的多种思路。
- 提供一个数字 n，生成一组 0~n-1 的整数，打乱顺序组成数组，打乱几次，如何能够看起来平衡，说出你能想到的所有方法。
- **leetcode 239**[2]
- 业务，业务，还是业务，项目复盘有没有更好的解决方案。
- 如何处理一个重大事故 bug
- 监控体系
- webpack 的缺点，让你设计一个新的构建打包工具，你会怎么设计？
- 在线文档编辑，如何处理两人的冲突，如何展示，考虑各种场景
- excel 文档冲突高级处理，文章冲突呢？是上个问题的深化。
- 看源码，整理 Vue 与 React 框架的所有横向对比，包括渲染原理、虚拟 dom、diff、patch、fiber、批量更新，手写响应式，框架用到的模式、设计思想，性能优化，相关生态技术等等。
- webpack 原理、热更新原理、动态加载原理、常见 plugins、loader、常见优化，怎么打包、怎么分 chunk，怎么写一个 plugins，生命周期，微内核源码等内容，以及 rollup、gulp 的使用、应用场景。（我记得有一面一个考官对我说，你对整个研发流程都很清楚，但都并不深入，比如一个 webpack 打包分包的依据怎么判定……emmmm，我倒是会，你也不问我啊！）
- 跨端框架的研究，工程化的梳理，使用的技术栈的坑，移动端的一些实践，面试时额外准备的项目复盘，竞品调查，对方产品的资料，测试系列，还有很多如微前端、中台、serverless、可视化、Wasm 等就不举例了。
- css 兼容性有哪几种处理方案，
- css3 新属性有哪些
- 怎么理解 margin 越界的问题
- js 的继承方式有哪些
- 深拷贝怎么实现
- js 的事件轮询机制有了解吗
- 说说 call,apply,bind
- 为什么要用 async，await
- vue 生命周期
- vue 双向数据绑定原理
- vue 的异步更新，以及 nexttick
- vue 路由有哪几种方式，是如何实现的,以及注意事项
- vuex 的使用，及其原理
- http 与 https 的区别
- 从输入 URL 到页面展示发生了什么
- 项目中遇到过什么问题
- 有没有封装过组件，插件
- webpack 怎么进行打包的
- 项目中是怎么优化的
- xss 怎么处理的
- 算法：实现 36 进制转换
- 简述 https 原理，以及与 http 的区别
- 操作系统中进程和线程怎么通信
- node 中 cluster 是怎样开启多进程的，并且一个端口可以被多个进程监听吗
- 实现原生 ajax
- vue-router 源码
- vue-router 主要提到了 hashchange 事件等，顺便跟面试官聊了一下 h5 的 historyAPI。
- vue 原理（手写代码，实现数据劫持）
- 算法：树的遍历有几种方式，实现下层次遍历
- 算法：判断对称二叉树
- Object.defineProperty 除了 set get 外还有什么属性，我回答了 configurable enumerable。
- 介绍一下项目中的难点
- 你知道哪些 http 头部
- 怎么与服务端保持连接
- http 请求跨域问题，你都知道哪些解决跨域的方法
- webpack 怎么优化
- 你了解哪些请求方法，分别有哪些作用和不同
- 你觉得 typescript 和 javascript 有什么区别
- typescript 你都用过哪些类型
- typescript 中 type 和 interface 的区别
- 算法题：合并乱序区间
- 你了解 node 多进程吗
- node 进程中怎么通信
- node 可以开启多线程吗
- 算法题：老师分饼干，每个孩子只能得到一块饼干，但每个孩子想要的饼干大小不尽相同。目标是尽量让更多的孩子满意。如孩子的要求是 1, 3, 5, 4, 2，饼干是 1, 1，最多能让 1 个孩子满足。如孩子的要求是 10, 9, 8, 7, 6，饼干是 7, 6, 5，最多能让 2 个孩子满足。
- 算法题：给定一个正整数数列 a, 对于其每个区间, 我们都可以计算一个 X 值;X 值的定义如下: 对于任意区间, 其 X 值等于区间内最小的那个数乘上区间内所有数和;现在需要你找出数列 a 的所有区间中, X 值最大的那个区间;如数列 a 为: 3 1 6 4 5 2; 则 X 值最大的区间为 6, 4, 5, X = 4 \* (6+4+5) = 60;
- https 与 http 有什么区别(一面刚好也被问到)
- cookie 有哪些属性
- cookie,session,localstorage,sessionstorage 有什么区别
- 怎么禁止 js 访问 cookie
- 你知道哪些状态码
- options 请求方法有什么用
- less,sass 它们的作用是什么
- 写一个 LRU 缓存函数
- 你们服务是怎么部署的？Node Agent 做了什么工作？
- Grpc 的优缺点？
- http2 的相关特性？
- viewport 和移动端布局方案
- 实现一个 compose 函数
- 开发中有遇到过比较难定位的问题吗？Node 内存泄露有遇到过吗？
- 有没有做过同构组件？服务端和客户端怎么同步状态的？
- render 和 renderToString 的底层实现上的区别？
- 客户端怎么处理 JS 事件失效的问题？客户端不重新加载 JS 的情况下怎么实现？
- 做服务端渲染的时候有没有遇到过比较难的点？
- 服务回滚是怎么做的？上线流程是怎样的？k8s 回滚、拉取以前的镜像
- webpack plugin 的原理是什么？
- plugin 中有异步请求会阻塞后面的 plugin 吗？
- 做过哪些 webpack 的性能优化？
- hard-source-webpack-plugin 是怎么做缓存的？修改文件后会怎么样？
- parallel 的原理是什么？多个子进程怎么通信？
- 你们 webpack 是怎么做拆包的？
- 服务端监控是怎么做的？服务有上报过什么指标？
- Node 服务怎么去定位 CPU 占用暴涨的情况？怎么去定位内存泄露？
- 编写 grpc 服务和 http 服务的区别？
- 前端的监控是怎么做的？除了 sentry 还做了其他异常处理吗？
- 讲一下你做的比较复杂的项目？以及你在项目中担当了什么角色？
- 你是怎么看待现在各种造轮子的？
- 有一个一亿长度的字符串，怎么存储设计可以让它更好去查询、修改？
- 怎么优化 H5 让它可以在 300ms 之内打开？
- 你们 WebView 加载一般耗时多久？
- 你们为什么从 Python 重构到 Node？好处是什么？
- 你是怎么看待做后台管理系统的？很多人觉得它没有难点，你觉得呢？（问这个问题是因为我现在在做后台管理系统）
- 做过离线包吗？H5 离线包的原理？客户端根据什么拦截静态资源请求？
- JS Bridge 的原理？你们这套方案的 s 优缺点？
- 怎么判断 webview 是否加载完成？
- 怎么实现 App 头部和页面的背景渐变？
- PC 端做过比较有意义的项目？
- 微前端子应用之间怎么通信？有没有了解过业界的一些方案？
- 你们部署的 Jenkins 是怎么做的？
- JS Bridge 原理？有没有安全漏洞？
- 有没有做过和安全相关的？waf 主要做了什么？
- 有没有做过埋点和性能上报相关？
- 如果你们用一个第三方的上报库，但页面加载这个 JS 失败了，还想上报该怎么办？
- 实现 DOM 字符串转虚拟 DOM 对象（不能用 DOM 相关的 api）
- 有木有做过你觉得比较困难的项目？
- 管理系统都做了哪些业务？有没有做一些提高开发效率的东西？
- 常用的组件是哪个？解决了什么问题？
- 平时 Node 都用来做什么？怎么实现的？
- SSR 的实现原理是什么？
- 项目中遇到的技术难点有哪些？
- 你觉得你们比 lazada 做得更好是哪些原因？
- 有用过代码规范相关的吗？Eslint 和 Prettier 冲突怎么解决？
- 实现一个数组转树形结构的函数
- 说几个你觉得足够复杂的项目？
- 有没有做过性能优化相关的？
- 实现一个深拷贝
- 实现一个二叉搜索树转链表的方法
- 在工作中，主要是做什么内容？
- 有用过 lerna 吗？多个项目之间共用的东西怎么共享？
- 讲一讲微前端是怎么做的？怎么独立部署？子应用通信怎么做？
- webpack 构建流程是怎样的？
- webpack loader 和 plugin 的原理和区别？
- webpack 热更新原理？
- webpack 怎么做分包？
- 做过 webpack 性能优化吗？有用过 rollup 吗？
- 什么是 TS 泛型？
- 从输入 url 到页面展示经过了哪些步骤？
- 知道 BFC 吗？使用场景有哪些？
- 怎么判断是否为数组？
- 页面卡顿怎么去定位？
- 数组有 10 万个数据，取第一个和取第 10 万个的耗时多久？
- 有用过 canvas 相关的吗？
- JS 垃圾回收机制？怎么定位 Node 内存泄露问题？
- tcp 和 udp 的区别和使用场景？
- quic 基于 udp 怎么保证可靠性？
- 讲一下同源策略和跨域方案？CORS 的几个头部是什么？
- 讲一下 react fiber？
- vue 双向绑定原理？
- 实现一个 bind 函数
- 求数组里面最大连续项的和
- event loop
- 怎么优化 h5 的加载速度？
- 离线包怎么更新？怎么知道需要打开哪个离线包？
- js bridge 通信原理？
- 怎么实现 h5 页面秒开？
- 明明不是同一个语言，为什么 js 和 native 可以通信？
- 怎么实现 js bridge 跨多个 app 共用？
- grpc 相比 http 的优势？
- rpc 的调用流程？前端怎么调用 grpc 的？
- 为什么要用 grpc？
- 服务发现为什么用 ip，而不用域名？
- 怎么实现移动端的布局？
- iOS 下软键盘输入框遮挡遇到过问题么？怎么解决顶不起来的问题？
- 求一个数组最大子项的和，要求这些子项在数组中的位置不是连续的
- 做过哪些公共组件？DatePicker 怎么实现的？难点在哪里？
- 组件封装有哪些原则？
- 组件数据和 UI 怎么分离？
- 有没有做过一些提高工作效率的东西？
- 有没有了解过拖拽？觉得它有哪些难点？
- 有没有做过优化相关的？webpack 做了哪些优化？
- cache-loader 和 hard-source-webpack-plugin 的区别是什么？
- 最近遇到的比较难的项目是什么？你们服务是怎么部署的？
- Puppeteer 可以用来做什么？
- Javscript 的数据类型问题，衍生到 `typeof`和 `instanceof`，然后怎么实现这两个类型判断以及写个函数如何判断所有东西。
- 如何解决异步问题，自发性扩散回答应该毕竟好，从 `callback`、`Promise`、`生成器`、`Async/Await`。
- BFC
- Webpack 性能如何优化，有过什么优化的方案和结果，说了下自己的方案啥的。
- 自己做过的项目中有那些是你值得说的，说了下给开源提供代码的事。
- 原型链，有哪几种继承。
- 总之网上很多问到的题目都问了，粘贴复制一样。。
- 56 题 合并区间，<https://leetcode-cn.com/problems/merge-intervals/>
- 如果拿到一个页面会怎么考虑优化，如何判断优化哪方面。基本上看`Google`控制台还有一些插件，包括`BFC`。
- 记不清了。。反正都挺简单的。
- js 中继承有哪几种，现在最常用的继承是什么，`Babel`转换 `Class`是转换成什么继承的方法。
- BFC, 为什么会用到，怎么样才能实现 BFC
- call, apply, bind
- 聊下`Vue`的 2.0 和现在 3.0 有啥区别
- Vite 是什么，你用过吗，他实现原理
- Webpack 的处理流程，插件和 loader 啥区别
- 如果我写的几个 ts, 怎么转换成原生 js
- vue 的实现原理，从 Proxy 劫持字段，到 Getter 和 Setter, 然后副函数渲染 patch 流程。
- vue keep-alive 是什么原理
- webpack 和 rollup 有啥区别
- 如果你开发个模块，打包的时候会打成什么 module。现在基本上都是 commonjs 和 esmodule, 分别打成两个。
- 人家要你开发模块的时候，是怎么判断用什么 module 的文件，pkg.main 对应于 commonjs, pkg.module 对应于 esmodule。
- commonjs 和 esmodule 的区别
- 前端监控 sentry 上报方式 img 标签（src 为上报地址，跨域，gif），navigator.sendBeacon
- CSRF 攻击
- 浏览器强缓存和协商缓存
- 你说你项目中有做过错误监控，这东西有啥存在的意义。我以为是后端老哥来面我的，我还详细介绍了下使用场景和方案。但是老哥听不懂，就过了。
- commonjs 和 esmodule 的区别，现在你最常用什么形式。
- Babel 的处理流程。
- Babel 能转换一些新版本 js 没有的方法嘛。基本上靠的是 Babel 的插件来处理，也就是垫片 ployfill。
- 现在最常用的方案，你是怎么做的。基本上 preset-env + corejs
- Webpack 的垫片是做什么的，这道题没答出来，有点奇怪我后面也没查出来，希望老哥们能在评论区里帮帮我。
- Vue 实现原理
- Vue3 的 Compisition API 是怎么实现的
- http 多路复用是什么，
- https 和 http 的区别
- 设计模式的基本原则，有用过哪些设计模式。
- 作为前端你认为什么最重要
- 开发流程一般都是怎么做的
- 对于 angular vue react 的理解
- BFC
- 输入网址后发生了什么
- 继承和原型链的各种问题
- 浏览器事件循环
- Symbol 有了解吗，迭代器有了解吗，哪些是可迭代的
- vue 实现原理
- 问了个设计题目，比如说你在写点餐业务的时候，有好几个人扫码点餐，怎么处理。基本上是通过 webSocket 来联系多端，比如说 a 加了个毛肚， 发送添加数据至 b 和 c。最后下单时，再次验证购物车是否一样，最后提交。
- 浏览器的渲染过程，以及缓存
- http1/2/3 都有啥区别
- 每次并发请求只有 5 个，怎么增加更多的请求。
- vue 是如何保证父组件重新渲染不导致子级重新渲染的
- vue-loader
- 对 Vite 的理解
- webpack 和 Vite 和 Rollup 有啥区别
- 组件设计原则
- graphql
- webpack-bundle-analyzer (next.js) -> <https://github.com/vercel/next.js/blob/canary/packages/next/build/webpack-config.ts>
  css -> cssnano
  gzip/brotli
  webp
  picture
  width/height
  懒加载
  Image Component -> next.js
  imagemin-webpack-plugin (sharp)
  loading.lazy
  lazy/suspense
  react/react-dom
  lodash
  echarts
  split-chunks (http cache) -> next.js
  路由懒加载
  image
  prefetch -> import('') Webpack 魔法注释
  compressWebpackPlugin
  minify
- 微前端描述下
- 两个请求并行发送，如果其中一个请求出错，就用默认值代替，怎么实现
- 页面有两个相同的请求怎么复用
- 跨域通信有哪些
- http 缓存
- 懒加载
- commonjs 和 es module 区别
- tree sharking 原理
- loader 会 plugins 区别
- 了解哪些新技术
- 介绍一下微前端
- 说一下 npm 包管理机制
- A 插件依赖 D 插件版本是 1.0.1，B 插件依赖 D 插件版本是 1.0.2，C 插件依赖 D 插件 1.1.0，那么 npm i 之后，下载了几个版本的 D 插件
- HTTP 常见的状态码 ，401 403 分别是什么， 常见的请求头响应头有哪些
- 说一下 webpack 配置，常用的 loader、plugin
- 介绍微前端
- 乾坤框架怎么实现的沙盒机制
- 手写一个单例模式
- 手写一个发布订阅模式
- 手写一个组合继承
- 垃圾回收机制了解么，介绍一下
- 自定义 hooks 和函数有什么区别
- 事件循环输出顺序问题
- 实现函数异步请求成功后就返回，失败后重试 max 次
- 前端怎么埋点监控
- hooks 为什么不能写在 if 语句里面
- useCallback 的实现原理
- 怎么画 1px 像素线，逻辑像素,物理像素的概念
- 自己写的 mock 服务是怎么实现的，为什么不在 webpack 里用相关插件
- 介绍下项目
- 说一下微前端实现
- 写一个发布订阅模式
- 一道 setTimeout 事件循环的题目
- 手写题实现电话号码隔位显示（3 4 4）
- 介绍下项目亮点
- 说一下 redux 如何使用
- redux 源码介绍下
- 你说你 angular, vue, react 都使用过，说一下三者的区别
- 了解缓存么 大概讲一下
- 解释下 https
- 介绍几个 git 常见的操作命令
- 介绍项目亮点
- react 通信是怎么样的
- react-redux 中 connect 怎么连接组件的
- 介绍一下微前端
- 乾坤框架源码看过么
- 数组去重方法越多越好
- 写一个匹配邮箱的正则
- 实现函数
  function repeat(s, count) {}
  repeat('s', 3) // 输出 ‘sss’
- 函数实现
  // 正则匹配标签名 输出 div p span
   <div>
       <p>
         <span></span>
       </p>
       <span>
       </span>
   </div>
- 实现一个深拷贝
- 实现函数统计字符串里面出现次数最多的字符
- 有做过什么优化么
- 介绍下微前端
- 写一个三列等距布局，越多越好
- 写一个公共组件需要注意哪些
- 写一个表单生成组件
- 你 ts 用的多么，说几个高级用法
- 介绍下 interface 和 type 的区别
- 你觉得 AI 智能给前端带来的变化
- 介绍下微前端实现方式，以及你们是怎么做的
- 乾坤框架源码看过没
- commonjs 和 es module 区别

  ```javascript
  1：

  // a.js
  module.exports = {};

  exports = {
      name: 'json'
  };

  // b.js
  const a = require('./a.js'); // 输出什么

  2:
  // a.js
  module.exports = function a() {}

  // b.js
  // 在b中用es6 module语法怎么引入
  ```

- 介绍下浏览器缓存机制
- webpack 打包原理是怎么样的
- webpack 插件写过没，介绍下原理
- webpack5 介绍下
- 看你用过 react 介绍下 fiber 架构
- esbuild 知道么介绍下
- 你用过 vue，现在出了 vue3.0 介绍下
- vue 现在出了一个打包工具 vite，介绍下为什么会比其他的打包工具快
- 介绍下 https 加密过程
- 第三方登录，如果让你去设计，你会怎么考虑
- 介绍下浏览器和 node 的事件循环
- 做了一道原型链输出问题
- 做了一道 setTimeout 输出问题
- 做了一道 this.setState 输出问题（异步和合并）
- 实现一下 promise.race
- 实现一下 task().eat().sleep(2000).eat().sleep(2000)函数
- 判断链表有环但是空间复杂度是 O(1)
- 实现 sum(1)(2, 3)(4)柯里化
- 实现一个非树状结构转树状结构函数
- 一个查找最长子字符串算法
- 介绍下项目
- 微前端实现
- 乾坤框架如何做到隔离
- 实现一个 String.prototype.\_trim 函数
- 实现一个 reduce
- 实现一个多个请求，并行和串行的函数
- ES6
  Object.create(null) / {}
  Array.isArray
  .toString.call
  Map 和 WeakMap 的区别
  Promise.race 及用途(timeout) ...
  如何拍平数组 (.flat)
  如何判断一个值是数组
  Object.create
- CommonJS/UMD/ESM
- 如何创建一个数组大小为 100，每个值都为 0 的数组 <https://q.shanyue.tech/fe/js/520.html>
- JavaScript 基础
- Css 以及优化
- vue 或 react 框架相关
- 前端打包等工程化
- 浏览器及常见安全问题相关
- 跨平台技术
- 网络相关
- 少量算法
- JavaScript 实现对上传图片的压缩？
  答：读取用户上传的 File 对象，读写到画布（canvas）上，利用 Canvas 的 API 进行压缩，完成压缩之后再转成 File（Blob） 对象，上传到远程图片服务器；不过有时候我们也需要将一个 base64 字符串压缩之后再变为 base64 字符串传入到远程数据库或者再转成 File（Blob） 对象。
  思路就是 File + Canvas 的 drawImage
  可以看看张鑫旭大佬的文章 HTML5 file API 加 canvas 实现图片前端 JS 压缩并上传
- 谈一谈 JavaScript 的异步？🌟
  答：setTimeout、MutationObserver、postMessage、Promise、async、await、generator
  从 MutationObserver、postMessage 会牵扯到 vue 的 $nextTick
  从 generator 会聊到 co.js 实现，代码不长，意思也好理解，但让我写还真没写出来，建议兄弟们好好看一遍！
  从 Promise 和 setTimeout 会聊到下面要说的**事件循环**
- 浏览器和 nodejs 事件循环？🌟
  答：执行栈，promise 是 microTask，setTimeout 是 tas
  其中很多的阶段，可以从这里看到完整的模型介绍：html.spec.whatwg.org/multipage/w…
  需要说出来的点：首先 setTimeout 并没有特殊，也是一个 task。另外每次的执行过 task 和 大量的 microtask（不一定在一次循环全执行完）后，会进行 renderUi 阶段，虽然不是每次事件循环都进行 renderUi ，但每次间隔，也就是传说中 **60hz** 的一帧 **16ms**。
  nodejs 事件循环略有不同...多了 process.nextTick 等
- 手写 bind 函数
- service worker 使用
  答：缓存，渐进式应用，拦截处理
  聊到 **worker** 可能还会聊到 **web worker， shared worder** 等等，如果有自信，或者工作对这方面有深入理解，可以秀一下。能体现出自己的优势...
- 严格模式
  答：this 的 undefined，禁止 with，arguments 不允许更改，给只读对象赋值抛异常，变量需要先声明，call，apply 第一个参数不会被转换...
- 原型链以及继承
  答：很常问，但随便找个赞数高的讲解，看一遍就懂了，记住常考点即可。
- 正则表达式匹配规则？
  答：这个真没办法，只能是对正则表达式的规则进行系统学习，当然常考的可能是 **邮箱，url** 匹配。
- flex 布局 🌟
  答：阮一峰老师的 flex 文章，清晰易懂。
  常用的 api 和两列、三列布局等等，对于我来说稍微有点难度。之前项目对兼容性高，基本没怎么用过 flex 布局。没用过的建议用一用，几个小时就会常见布局了。
- 优化长列表滚动效果
  没答上来，说了几个 js 的方案没答对点上。
  面试官答曰：transition 优化动画效果，分层渲染
  后面分析了一下，可以用 transform 进行强制分层，第二种可以用 content-visibility 将看不见的元素不渲染，设置值为 `auto` 即可。第三个是对于某些动画效果，可以用 `will-change` 作用在父元素上进行 gpu 加速，使用后删掉。
- 响应式布局 🌟
  答：可能会涉及 css 函数，rem/em 区别，媒体查询...
- 什么是 BFC？
  答：块级格式化上下文，我布局总用！
  问：什么会形成 BFC？它的作用是什么？
  答：

  - body 根元素
  - 浮动元素：float 除 none 以外的值
  - 绝对定位元素：position (absolute、fixed)
  - display 为 inline-block、table-cells、flex
  - overflow 除了 visible 以外的值 (hidden、auto、scroll)

- vue 响应式原理以及双向绑定实现代码 ? 🌟
- vue3 响应式原理，有什么不同？
- vue 的 diff 算法思路，怎么对比节点？
- vue 的 compile 实现？🌟
- vue 如何自定义指令？具体的 api 写法？
- vue3 对于 vue2 在性能上的优化（从 compile 和 runtime 两方面）？
- 用过 TypeScript 吗？有什么优点，为什么用？具体的场景，使用 TypeScript 进行类型定义。
- vue 的 keep-alive 使用场景，以及原理？🌟
- webpack 和 rollup 使用？
- tree-shaking 原理？🌟
- webpack loader 和 plugin 怎么写？
- 你对 vite 熟悉，和 webpack 区别？
- 如何统一对错误进行捕获的？vue 的异步错误如何捕获？
- 浏览器页面加载过程，越详细越好 🌟
- 浏览器缓存 🌟
- 跨域问题及处理 🌟
- v8 快数组慢数组，hidden class 或者其他模块？
- xss 和 csrc 的意思？如何防范？🌟
- electron 使用，如何实现小托盘功能？
- flutter 的 widget stateFullWidget stateLessWidget 区别？
- js Bridge 的原理 ？🌟
- flutter 的渲染引擎？
- Oauth2.0 和 jwt 单点登录等
- http/https 区别？为什么 https 更安全一点？https 为什么也不是十分安全？
- http1.x 和 http2.0 的区别？http2.0 优点，以及某些情况会比 1.x 速度更慢？
- https 加密原理？
- http2.0 压缩头，以及并行请求原理？
- tcp 的连接方式？
- 回文串，中心扩散法
- 冒泡，快排 🌟
- 二分查找 🌟
- graphql
  1.  graphql-codegen
  2.  /graphql?UserFriends
  3.  hash string
  4.  模板字符串
  5.  gql
  6.  POST
  7.  GET
  8.  POST 缓存优化 ❎
  9.  N+1 Query
  10. /graphql 调试 ❎
  11. apollo-server/apollo-client
- 虚拟滚动 -> elementui
- 小图增加阿里图片压缩后缀
  picture ❎
  后缀/转格式/宽高
  webp/avif/jpegxl
  Image -> width/height/quality/webp
- 文件过大出现卡顿
  标注
  缩略图
  虚拟滚动
  pdf.js
- 切片上传
  blob.slice
  断点续传
- 网页截屏
- setTimeout 为什么最小只能设置 4ms，怎么实现一个 0ms 的 setTimeout?
- 看你简历上有写到 rem 和 vw，能讲讲吗？为什么你选择使用 rem 而不是 vw？
  当时回答是 rem 兼容性更好，且 px 转 rem 后可以避免过长小数。
- 浏览器对于小数单位是怎么计算的？
  当时没答上来，只说了句四舍五入，后续查阅相关资料得知不同浏览器策略不同，有的会四舍五入，有的会直接取整。不管什么单位，浏览器最后都会 Computed 为 px 后再进行渲染。
- interface 和 type 的区别是什么？你日常工作中是用 interface 还是 type？
- ts 的逆变和协变有没有了解过？
- 能不能讲讲小程序的原理？
  网上很多相关文章，把双线程讲出来就行。
- 看你之前有做过 Taro，能不能讲讲 React 是怎么跑在小程序里面的？
  大概把 Taro3 的原理讲了一遍，主要是 jsx->vdom->json->wxml，具体可以看这里 **Taro 预渲染**\[10] 和 **Remax 实现原理**\[11] ，之前写过 demo，所以对这块还是比较了解。
- 你刚才讲到 json->wxml 这一步可以有两种方式(template 递归和自定义组件递归)，能不能讲讲两种方式的优劣？
  简单讲了一下，template 递归是纯视图层的操作，性能肯定更好，但是由于微信小程序 wxml 编译器的限制，template 不能递归调用自己(支付宝小程序无此限制)，所以 Taro 在微信环境中把同一个 template 写了 n 份，只有 id 不同，就是为了递归渲染。
  而自定义组件递归还要涉及到逻辑层，例如生命周期等，性能会差一些，同时还有 Shadow DOM 引起的样式问题，目前 kbone 使用的是自定义组件递归。
- 小程序有没有 HMR，能不能讲讲 HMR 的原理？
  小程序没有 HMR，当时只讲出来了保存代码小程序是怎么刷新的，HMR 没有讲出来。
- 讲讲 z-index
- 实现一个 ts Include
- 实现一个 useInterval
- js event loop 执行顺序
- options 请求是什么？有什么作用？
- cdn 的原理是什么，是在网络哪一层起的作用？
- 项目性能是如何做优化的？
  我主要从网络，缓存，js，css，接口合并等几个方面讲的，该题比较宽泛，可自行发挥。
- 动态创建 script 标签并插入到页面上，说执行时机
- 给你一个“A2B3”这样的字符串，输出“AABBB”
- 接上题“C4(A(A3B)2)2”，带嵌套的，这两题都不是原题，但是类似
- 写一个 curry，要求 add(1)(2)(3)(4) 打印 10
  一开始我洗的 add(1)(2)(3)(4)()，面试官问我能不能把最后的()去掉，最后寻求提示，他说 console.log 是怎么打印函数的，豁然开朗，复写 toString 即可。
- loader 和 plugin 的区别是什么？
- webpack 打包优化，我还提到了 vite，顺便讲了下 vite
- 小程序原理，以及 Taro 原理
- xss 和 csrf
- http2
- Tree Shaking 原理
- 最长回文子串
- 聊了很多工程化相关的问题，主要是项目从开发到上线这一整套流程，聊完之后他也指出了我说的这一套流程有什么不完善的地方。
- http2
- Tree Shaking 原理
- 项目优化和网络优化
- 股票最大收益
- 如何解决跨域问题
- es6 之后的新特性
- 数组扁平化如何做
- ts interface 和 type 的区别
- ts ?? 用法
- es 6 对象和数组解构时需要注意什么
- webpack 做过哪些优化，打包速度、打包体积方面的
- webpack thread-loader 原理、配置
- 首屏渲染优化
- 原型链
- 闭包
- 继承的几种方式
- webpack 5 介绍下
- 项目相关 - 如果实现大文件上传；文件校验等等；json scheme ，如何优化等
- 项目相关- 秒杀活动如何实现；
- 有看过哪些源码
- webpack 做过哪些优化
- 谈一谈你的项目，说到了如果同时很多人观看直播，发送弹幕，前端要怎么处理
- 如何使用异步 add 来实现一个 sum 函数
  请实现以下 sum 函数，只能调用 add 进行实现

  ```javascript
  /*
        请实现一个 sum 函数，接收一个数组 arr 进行累加，并且只能使用add异步方法
  
        add 函数已实现，模拟异步请求后端返回一个相加后的值
      */
  function add(a, b) {
    return Promise.resolve(a + b)
  }

  function sum(arr) {}
  ```

  **「追加问题：如何控制 add 异步请求的并发次数」**
  **【Q088】如何实现 promise.map，限制 promise 并发数**
  **【Q643】如何实现 chunk 函数，数组进行分组**

  以下为答案：

  ```javascript
  // 先来一个串行的写法：

  function sum(arr) {
    if (arr.length === 1) return arr[0]
    return arr.reduce((x, y) => Promise.resolve(x).then((x) => x + y))
  }

  // 接下来是并行的写法：

  function add(x, y) {
    return Promise.resolve(x + y)
  }

  function chunk(list, size) {
    const l = []
    for (let i = 0; i < list.length; i++) {
      const index = Math.floor(i / size)
      l[index] ??= []
      l[index].push(list[i])
    }
    return l
  }

  async function sum(arr) {
    if (arr.length === 1) return arr[0]
    const promises = chunk(arr, 2).map(([x, y]) => (y === undefined ? x : add(x, y)))
    return Promise.all(promises).then((list) => sum(list))
  }

  // 如果需要控制并发数，则可以先实现一个 `pMap` 用以控制并发

  function pMap(list, mapper, concurrency = Infinity) {
    return new Promise((resolve, reject) => {
      let currentIndex = 0
      let result = []
      let resolveCount = 0
      let len = list.length
      function next() {
        const index = currentIndex++
        Promise.resolve(list[index])
          .then((o) => mapper(o, index))
          .then((o) => {
            result[index] = o
            if (++resolveCount === len) {
              resolve(result)
            }
            if (currentIndex < len) {
              next()
            }
          })
      }
      for (let i = 0; i < concurrency && i < len; i++) {
        next()
      }
    })
  }

  async function sum(arr, concurrency) {
    if (arr.length === 1) return arr[0]
    return pMap(
      chunk(arr, 2),
      ([x, y]) => {
        return y === undefined ? x : add(x, y)
      },
      concurrency
    ).then((list) => sum(list, concurrency))
  }
  ```

  - 某银行前端一年半经验进字节面经:<https://juejin.cn/post/6959364219162607630>
  - 【Q088】如何实现 promise.map，限制 promise 并发数:<https://github.com/shfshanyue/Daily-Question/issues/89>
  - 【Q643】如何实现 chunk 函数，数组进行分组:<https://github.com/shfshanyue/Daily-Question/issues/661>

- 单向链表输出倒数第 K 个元素
- 看代码输出结果（考察变量、函数提升）
- 看代码输出结果（考察异步代码先后顺序）
- 手写 instanceof 关键字
- 说下输入一个 url 地址的全过程。
- http 的缓存策略。
- 说下 https，证书是如何校验的？
- 说下 http2，你觉得阻碍 http2 发展的问题是什么？（这题后面的问题挺有意思，可以网上搜下答案）
- 场景题：提交表单，常用的方法有哪些？应用层，通信层发生了哪些过程？
- post 和 get 的区别，列举一下
- http 常见的响应码，拒绝服务资源是哪个（403）
- 说一说这个系统是如何判断机制的（前端鉴权）
- 你刚才说了三方 OAuth，讲一讲内在原理吧
- 说说 https 的内在原理，ssl 握手过程
- 为什么要用非对称密钥，pms 呢？公钥怎么了？
- 说一说响应式布局吧？
- 响应式背后的浏览器原理你知道吗？（不太知道）
- 旋转动画 css，怎么去做？（animation+rotate）
- dom 树和 cssom 树原理也说一下吧
- 为什么 link 要在前，script 标签要在后面呢？原理
- 场景题：保证浏览器不受脚本的恶意攻击，（xss 攻击，解决方法）
- 假如说你的富文本编辑器内部要显示脚本，该怎么办呢？（不太清楚，我就尽可能说）
- 说说 async 和 await 的 es5 实现（我尽可能地说了一点）
- 场景题：这里有 cat 和 animal 子类和父类，如何进行 es5 继承，至少说出 5 种。
- 说说你项目做的 Vue spa 首屏优化吧（按需引入，懒加载路由，gzip 压缩，关闭一些插件...）
- 说说 webpack 打包构建在实际项目中的优化
- 算法场景题：数型系统，包含字符串关键词，如何对其作出效率很好的搜索？（balabala 说了自己的一些看法，lz77 算法，后来翻了翻算法书，应该结合 B 树来说）
- 编程题：请使用 js 函数写出 markdown 转 html 的文本编辑器。（2 个小时）
- 算法题：在一个字符串中，找到最大不连续子字符串的长度。
- 说说你 element-ui 的按需引入吧
- 说说 webpack 打包优化具体干了什么？为什么要这么做呢？（Dllplugin，happypack）
- prerender-spa-plugin 插件你用过？具体说一说吧
- SEO 优化你做了？具体讲一讲吧
- 追问：你 seo 排名怎么样了？（没有进展 😂）
- 我记得 NUXT.js 也可以做渲染和 seo 吧？了解 SSR 吗
- 小程序有碰到过复杂一点的业务场景吗？（说了数据列表懒加载处理 setData 优化问题）
- 小程序的框架你有了解吗？要不说说几个？
- 你了解过的前沿技术来说一说？（Vue3.0，Flutter，Serverless，Typescript）
- 说说 Vue3.0 和 2.x 的双向数据绑定（object.definePorperty 和 Proxy）
- 说说你最感兴趣的前端方向（跨端解决方案 Flutter、React Native...）
- 一面面试官说你还可以，那我就不再问你基础问题了，你还有什么要问我的吗？
- 说说你的个人博客和你做的小程序吧
- 你刚才只说了技术层面的，功能层面没有什么创新吗？
- 你现在还有开展什么新项目吗？
- 我不管技术层面，还是来到功能层面，除了这一个功能就没有创新了吗？（顿时语塞。。）
- 有这么一个功能场景，老师随机点名，上堂课没来的同学被抽到的概率会大幅增加，怎么去做？
- 还有一个功能场景，你的博客系统如何分享文章？
- 还有一个功能场景，你可不可以做一个在线提交作业的平台，让老师不仅可以收到作业，还可以在平台上对作业进行批改？说说具体技术实现。。。
- 我的问题问完了，你现在还有面其他的部门吗？balabala
- 详细地讲讲 Vue 的首屏优化，具体的技术点
- 优化有过量化评级吗？说说具体为多少？怎么去做的？
- 有一个问题，你如何去确定哪一种方式是对整个首屏渲染优化起到最关键作用的？
- 我们现在回过头来，你可不可以按照软件开发的流程模块再来详细地说说博客的整体优化？各个方面的性能优化？（设计，编码，打包部署，上线体验。。。说了一部分）
- 预渲染 prerender-spa-plugin 能详细讲讲？
- 你了解了原理，那么你引入这个 prerender 插件对于整个项目的架构产生了什么样的特别影响？（讲了路由冲突）
- 对于上线后的用户体验，你打算怎么做改进？
- 功能层面是这样，技术层面可以来说说？
- 数据列表的懒加载这个说的好，那有这么一个场景，你提交了新的文章，由用户在刷你的博客，你怎么让用户通过一定的事件=来查看你的新文章，不要通过页面整体刷新，还是以动态引入的方式？
- 我们再次回到刚才项目的性能优化这个点上？在你解决首屏的时候，在网络通信的每个阶段，哪个阶段是性能开销的最大的地方，优化后有何变化？如何解决？
- SEO 怎么做的，讲一讲技术细节
- 你有对你的用户群体做过数据的量化统计吗？说说你有什么样的思路，如何去利用好这些数据？
- 这边有个问题，如果单纯地通过前端来分析用户的行为，开销会非常大，你有什么好办法？说说思路
- 如果过了很长时间，有人问你，一个高性能的博客页面该如何搭建，你会按照什么样的逻辑取来跟他分析这些零碎繁杂的性能优化？
- 好了，博客项目只是你个人对于技术的探索，你还有没有学校里真正拥有用户的实际项目呢？说说看
- 功能描述的很详细，这里有个问题，总所周知，二维码有一定的时效性，可传播性，如何防范那些没来同学也扫到二维码了？说说方法
- 没来的学生，你们就会采取这种单一的方案吗？还有没有别的？
- 说说你们项目组的团队，如何分工的？
- 在这个团队对于项目的功能构建中，你起到了什么作用呢？
- 你刚才说到了前后端分离，讲讲你和后台同学如何落实好前后端分离的？
- 对于后台的数据接口，经常会发生一些分歧，你们团队是怎么化解这种分歧的，有没有一种方式增进团队之间的沟通？
- 这小程序现在的用户量怎么样呢？日活又如何？
- 同样的，再说说这个小程序性能优化做了哪些呢？
- 你对于前端未来的开发？以及你以后的职业规划？
- 你希望阿里能给到你什么样的经历？在阿里希望能学到什么？
- 这边在杭州，之后方便过来对吧？
- 说说你最有成就感的项目
- 你的博客网站，难道没有分析过用户的行为吗？对于用户量很大的情况下，难道没有做过性能分析吗？
- 详细地讲一讲你做了哪些性能优化？
- 就这么多吗？对于效果你有做过量化的评测吗？
- 对于首屏中的 FP，FCP，FMP，TTI 你又分别去做量化的考虑吗？
- 对了，你如何通过代码来分析首屏的 FCP 时间？
- 除了这些，难道就没有进一步优化吗？
- prerender 预渲染是什么原理呀？
- 这样的一种插件引入，为整个性能提升又带来了多少量化的参考呢？你有去研究过吗？
- 说说你拥有的实际用户量的项目吧？
- 这个小程序已经上线对吧？你们团队有没有对这个小程序做过用户行为的调研呢？
- 我想要知道的是在程序里面有代码去自动去分析用户的行为吗？
- 我看你懂 Vue，React 有学过一些吗？系统地说一说两者的区别
- Vue 如何解析 template 模板，diff 算法两者的不同是什么？？
- 详细地说说前端的动画种类？
- canvas 有了解过吗？它适用于什么样的场景？
- 你对于前端前沿技术的看法？
- 你刚刚讲了 flutter，Dart 语言能不能说说看？
- 我看你做过的项目还蛮多的，用户量也还很可以，真厉害，你能跟我仔细的说说嘛？
- 博客的话，做过哪些方面的优化呢？
- 首屏渲染优化还如何去排查性能呢？
- Vue 的预渲染这个插件，具体是怎么去做的？
- Vue 的双向数据绑定说一下吧
- Vue 的子组件与子组件之间的通信讲讲吧
- 父子组件的通信和子父组件的通信是不是也可以实现呢？
- 说说你对 Vue 的总体看法，以及与其他框架的不同的地方
- 小程序的话，你做了哪些优化？说说吧
- 二维数组具体用 setData 怎么去更改呢？
- 场景题：现在手机 QQ 要做个成语接龙，你怎么去做，说说思路吧
- 你有什么较好的算法可以尽量减少成语库的数量吗？
- 有没有想过前端如何去检测用户输入的是不是成语？
- 你刚才说了缓存，讲一讲 cookie 吧
- 还有什么种类的缓存，有什么样的不同呢？说说
- 肯定遇到过跨域吧，说说跨域吧（CORS,JSONP）
  CORS 相关的响应头如下：
  • Access-Control-Allow-Origin：允许的域名，该字段是必须的，可以设置为特定的前台项目的地址，如 http://localhost：8080，表示只允许此地址发送跨域请求；也可以设置为\*，表示允许任意域名的跨域请求。
  • Access-Control-Allow-Credentials：该字段可选。它的值是一个布尔值，表示是否允许发送 Cookie。在默认情况下，Cookie 不包括在 CORS 请求中。
  • Access-Control-Expose-Headers：该字段可选。进行 CORS 请求时，XMLHttpRequest 对象的 getResponseHeader()方法只能获取六个基本字段：Cache-Control、Content-Language、Content-Type、Expires、Last-Modified、Pragma。如果想获取其他字段，就必须在 Access-Control-Expose-Headers 里面指定。
- 好吧，我的问题就问这么多，顺便了解一下，你家人同意你来深圳吗？
- 您对我有什么样的评价？我觉得你项目大的挺好的，但是基础的话，我觉得你答的还有点疏漏，回去再好好想想，好吧？
- 后面要是有面试会在一周之内，通知你。
- 说说博客的优化点在什么地方
- 双向数据绑定的原理
- 追问：3.0 会有改进吗？传统的 2.0 数据绑定怎么解决数组问题
- 响应式你是怎么做的？说说
- 场景题：假如你的博客被脚本注入了？你该怎么去防御？
- 追问：escapeHTML 怎么转译呢？
- 你博客有做过鉴权吗？说一说
- 假如说某链接获取到你的敏感信息，发送奇怪请求到服务器，你怎么去防御？
- 追问：你刚才提到了双向 cookie？双向 cookie 什么机制？
- 讲一讲 cookie 是怎么发送到服务端，具体过程，尽量详细
- 追问：TCP 的三次握手
- 追问：TCP 的超时重传
- 追问：TCP 为什么是三次握手呢？
- 小程序具体做了哪些功能呢？说说看吧
- 懒加载数据列表二维数组怎么实现呢？
- 说说快速排序吧
- 追问：时间复杂度说说，解释一下
- 智力题：试探玻璃杯破碎的楼层（感觉答得不好）
- 说说在大学里做的项目
- Vue 的 spa 首屏优化怎么做的，说具体思路
- SEO 怎么做的，说说技术细节
- 预渲染 prerender 怎么做的，说说技术细节
- 算法题：大量数据的数组，怎么找出排名前 n 个数（说了分治思路）
- 网络安全攻击，都系统地说说吧
- 说说你最近正在做的一个项目，有什么样比较难的技术细节
- 讲讲 Vue 的生命周期吧，尽量详细
- Vue 有个 nexttick，请问发生在 vue 实例的哪个生命周期
- Vue 的双向数据绑定说一下
- 讲一讲你的个人网站吧，IP 地址是怎么来的？
- 说说首屏渲染优化做了哪些吧
- 你的小程序的课堂在线点名可以详细地说说吗？
- 你的动画遇到了溢出，掉帧问题，你具体怎么解决呢？
- 你的小程序的人员分工我很想了解了解，用户量怎样？
- 顺便问一下，你们学校经常搞工程类比赛吗？
- 你小程序的二维数组如何做懒加载的呢？
- 说说你了解的 http 响应码吧
- 说说 get 和 post 的差异吧
- 我看你简历写使用过性能检测工具，能具体说说使用过哪些点吗？
- 你了解过火焰图吗？排查过函数堆栈内部的变化吗？
- js 的浅拷贝和深拷贝说说看
- 说说你最近做过的最难的一个项目
- 说说你博客 Vue spa 的首屏优化
- UI 库组件如何按需引入呢？
- webpack 打包如何优化的？说说看，还有更好的方法吗？
- 你有给你的博客网站做过埋点吗？处理过用户的数据吗？
- Vue 的源码你有去读吗？说说你了解的
- 我问你些基础知识吧，讲讲浏览器如何渲染出 html 页面的，原理
- Node.js、PM2 这块只是会用的程度是吗？
- 你对于前端未来的一些看法，说说了解哪些前沿知识
- 可不可以讲讲 Flutter 的渲染机制？（不会）
- Dart 语言可以跟我系统地说说看嘛？（不会）
- 有没有去做过一些前端国际化的东西呢？
- 读过 js 底层的一些源码吗？
- 对于你的项目，你有没有什么在技术方面更好的改进点的？
- 我这边的问题问完了，你有什么问题？
- 对我的评价：我这边感觉蛮好的，但你以后的学习过程中，需要不断地去深入，要拥有自己的垂直领域 balabala...
- 我听同事说你已经拿到了腾讯的 offer，我现在来问个问题，你觉得腾讯和阿里的前端氛围有什么样的区别？可以随便说说
- 我前两个下属问过你很多基础问题了，我就不问了，我来提这么一个问题，你是黑客，你如何去 XSS 攻击？绕开网站的防御
- 说说你博客网站你做过的最难的一个技术点，说说解决的详细流程
- 你觉得你的博客还有什么可以改进优化的点吗？
- 说说你小程序的主要功能吧
- 场景题：那些没来的学生也拿到了二维码，你怎么去排查到他们？说说方法
- 除了地图定位还有别的方法吗？再思考思考
- 你对于前端未来有没有什么展望？学习路线说说看
- 你在学校里应该有技术团队吧，如何处理关系的？
- 平时有关注过一些大牛的动态吗？说一说
- 你有你未来对前端技术的看法？
- 性能优化
- http 缓存
- 做过的有特点的项目
- 遇到的问题与解决方案
- toB 和 toC 的区别
- 现场面对客户的经历
- 前端安全相关(着重中间人劫持)
- 项目开发流程
- 对 vuex 的看法
- vue 从 data 改变到页面渲染的过程
- 介绍状态机
- 组件设计原则
- 怎么看待组件层级嵌套很多层
- 前端安全防范措施
- 介绍 oauth
- 怎么看待 virtual dom
- 对 flutter 的了解
- weex 和 rn 原理
- 大屏用的技术
- 大屏数据来源与管理
- websocket 的使用场景
- pwa 的使用
- 对 http2 的了解
- 对新技术的了解
- 性能优化
- 对 MVC MVP MVVM 的了解
- 对 SEO 的了解
- 做了道逻辑题
- 国内前端行业的发展
- 你的优点
- 你的缺点
- 你还能提高的地方
- 三年内的职业规划
- 其他的日常聊天
- 有什么问我的
- 部门在 XXG 以至公司的定位（相比于公司其他方向的部门，我们的特点是？ 相比于同方向其他公司的部门，我们的特点是？）
- 设计师、产品、研发之间的合作
- 部门对公司或对行业最大的贡献是？
- 换肤都做过什么处理，有没有处理过可能改变尺寸的换肤
- i18n 在团队内部都做了哪些实践
- webpack 迁移 vite 遇到了哪些问题
- CI/CD 做了哪些实践
- 鉴权有了解么，jwt 如何实现踢人，session 和 jwt 鉴权的区别
- TCP 三次握手 http1.0，1.1，2 都有哪些区别
- https，为什么 https 可以防中间人攻击
- 冒泡排序
- 给你一个已经升序排列的数组，给一个数字，找一下这个数字在这个数组里出现了几次
- 洗牌算法，如何验证这个洗牌算法可以把牌洗得足够乱
- node stream 去取一个超大数据量的日志，由于内存限制每次只能取一部分，现在希望在全部日志中随机取一万条，如何做
- 介绍一下项目 有哪些是由你主导提出的方案做的事情
- esmodule 介绍一下，它和 commonjs 的区别，主要的优势是什么
- 介绍一下 vite 的原理，它会去编译你的代码吗，vite 引用 commonjs 的包的时候怎么处理
- 如何转成 esm vue3 的组合式 API 有了解吗，它有哪些优势
- 介绍 https cors 介绍一下
- 微前端有了解吗
- 为什么你们移动端 h5 用 vue，pc 管理端用 react？
- git 对象上的操作有了解过吗？git reset、rebase 这些操作用过吗 ？
- 你们小程序是用的 taro，对 taro 原理有了解吗
- 你们 cms 系统的架构是怎样的
- 你有了解过 webpack 现在也支持 esm 了吗？
- 你们的组件库是全公司公用的还是团队内自己的，是从 0 开发还是参考其他开源组件库在别人的基础上搞的？
- 有用 vue3 吗，为什么团队没有上 vue3？
- 你们 react 用的是什么语法？fiber 原理有-
- 怎么理解 vue 单向数据流的
- Vue 组件之间的通信方式都有哪些，用过 eventbus 么，eventbus 的思想是什么
- 写个自定义 v-modal
- 和 listener 有了解吗
- Vue 生命周期有哪些，都是做什么的，updated 什么情况下会触发，beforeCreate 的时候能拿到 Vue 实例么，组件销毁的时候调用的是哪个 API
- 什么情况下会触发组件销毁，销毁的时候会卸载自定义事件和原生事件么
- 自定义指令写过么，自定义指令都有哪些钩子
- 传统前端开发和框架开发的区别是什么
- Vue2 的数据响应式有两个缺陷，你知道是哪两个缺陷么，为什么会有这样的缺陷，如何解决
- Vue 如何实现的数组的监听，为什么 Vue 没有对数组下标修改做劫持
- 用 Set 获取两个数组的交集，如何做
- animation 和 transition 有什么区别
- 写个动画，一个盒子，开始时缩放是 0，50%时是 1，100%时是 0，开始结束都是慢速，持续 2 秒，延迟 2 秒，结束后固定在结束的效果
- 聊一下最复杂的项目
- 在无障碍的项目中做过哪些
- 做黑夜模式有没有考虑过用户设置了定时切换手机黑夜模式的情况
- 你们开发的 h5 项目依赖的安卓和苹果的 webview 的内核分别都是什么
- Lottie 动画上做过哪些优化，有考虑在低端机上用 CSS 动画做么
- 如果让你做一个动画，一个地球本身在自转，外面有个飞机围着它转，飞机的螺旋桨自己也在转，有哪些需要考虑的点
- CI/CD 上做过哪些
- webpack 迁移 Vite 遇到过哪些问题，之前 webpack 慢是为什么，有过优化么
- 业务内的公共工具提炼了哪些
- 自己做着玩的这些项目介绍一下，主要都是做什么的
- 这次找工作主要看重什么
- CSS 实现一个扇形
- 问输出

  ```javascript
  async function async1() {
    console.log('async1 start')
    await async2()
    console.log('async1 end')
  }
  async function async2() {
    console.log('async2')
  }
  console.log('script start')
  setTimeout(() => {
    console.log('setTimeout')
  }, 0)
  async1()
  new Promise((resolve) => {
    console.log('promise1')
    resolve()
  }).then(() => {
    console.log('promise2')
  })
  console.log('script end')
  ```

- Vue 的 nextTick 是做什么的？8.React 的合成事件和原生事件了解吗？
- webpack 和 vite 的区别是什么，切 Vite 的动力是什么
- 之前的开发模式是怎样的，是一个人负责一个模块还是按照需求排期分配
- 微前端有了解么
- 之前做过哪些工具
- 移动端兼容性问题遇到过哪些
- 如何限制 Promise 请求并发数
- 实现这个 pipe
  const fn = pipe(addOne, addTwo, addThree, addFour); // 传入 pipe 的四个函数都是已实现的
  fn(1); // 1 + 1 + 2 + 3 + 4 = 11，输出 11
- 了解过 Vue3 么，为什么还没有上 Vue3，了解 Proxy 么，它和 defineProperty 的区别是什么，性能上有什么区别么
- Vue 如果想做模板的复用，应该怎么做
- 有做过骨架屏么，是怎么做的
- 有做过懒加载么
- MySQL 优化有了解过么
- 如果实现一个三栏布局，需要三栏占同样的宽度，放多个元素时会自动换行，有哪些做法
- 移动端适配是用 rem 还是 vw？分别的原理是什么？你们用什么方案？
- ES6 语法用过哪些，都有哪些常用的特性
- 实现一个 node 异步函数的 promisify
- Vue 生命周期都有哪些
- keep-alive 的原理是什么，如果不用它的话怎么自己实现类似的效果
- v-if 和 v-show 的区别
- 介绍一下之前做的项目
- 如果需要你实现一个全文翻译功能，富文本的标签部分你是如何处理的，翻译之后数据如何回填
- typescript 实现一个字符串类型去左侧空格
  type A = " Hello world! ";
  type B = LeftTrim<a>; // 'Hello world! '
- 如果需要你实现一个弹幕的组件，你需要如何设计这个组件的 props 和 state，内部如何实现，有哪些地方可以优化
- 介绍一个有挑战性的项目
- 无障碍方面你了哪些优化
- i18n 方面你都做过哪些
- 你们做的是一个怎么样的产品
- const data1 = { "a.b.c": 1, "a.b.d": 2 };
  const data2 = { "a.b.e": 3, "a.b.f": 4 };
  // 把如上两个对象合并成一个 JSON，其中的.需要处理成对应的层级
- 你对 serverless 的理解是什么样的
- 之前做过 SSR 是哪种服务端渲染，是同构么
- 介绍一些上一份工作主要都负责哪些事情
- 介绍一下单例模式和它在前端的应用
- 介绍一下原型链
- 介绍一下前端的继承方式
- HTTP，TCP，七层网络结构，讲一下
- chrome 浏览器最多同时加载多少个资源，那如果想同时加载更多资源应该怎么办
- http2 的多路复用是什么原理
- 实现一个改变 this 指向的 call 方法，介绍一下原理
- 求斐波那契数列第 N 项
- 跨端有了解过么，Taro，uniapp 有写过么
- 有 Devops 相关的经验么
- Docker 和 k8s 有相关经验么
- 了解 JSON Web Token 么，它和其他的鉴权方式有什么区别
- 网络安全有了解么，CSRF 如何防御，SameSite 有哪几个值
- 之前的工作在每个阶段给你带来了哪些成长
- 你之前做过的比较有亮点的项目
- 如果你还在之前的部门的话，你有哪些事情是还想做的
- 对 TDD 的看法是怎样的
- 移动端一套代码适配多端是如何做的
- 介绍一个比较难的项目
- 如果用户希望自己定义一个颜色生成对应的皮肤，应该怎么制定方案
- webpack 迁移 Vite 遇到过哪些问题
- Vue 和 React 的区别
- Vue 和 React 的 Diff 算法有哪些区别
- 编写一个方法，判断一个字符串是否是合法的 XML
  const str1 = "<html><div>123</div></html>"; // true
  const str2 = "<div><div>123</div><div></div></div>"; // true
  const str2 = "<html><div>123</html></div>"; // false
- 在一个矩阵中查找一个字符串，可以上下左右移动，但是不能回头，如果能找到这个字符串返回 true

  ```javascript
  const str = 'abcde'
  const matrix = [
    ['0', '0', '0', '0', '0', '0'],
    ['0', '0', 'a', 'b', '0', '0'],
    ['0', '0', '0', 'c', 'd', '0'],
    ['0', '0', '0', '0', 'e', '0']
  ]
  ```

- 浏览器缓存机制
- HTTPS 介绍一下
- 事件循环介绍一下
- 输出结果

  ```javascript
  async function async1() {
    console.log('async1 start')
    await async2()
    console.log('async1 end')
  }
  async function async2() {
    console.log('async2')
  }
  console.log('script start')
  setTimeout(() => {
    console.log('setTimeout')
  }, 0)
  async1()
  new Promise((resolve) => {
    console.log('promise1')
    resolve()
  }).then(() => {
    console.log('promise2')
  })
  console.log('script end')
  ```

- v-for 为什么会有 key
- diff 算法介绍一下
- webpack 和 Vite 的区别，迁移过程是怎么样的
- 前端工程化你是怎么理解的
- 在之前公司业务和技术上主要都负责哪些
- 技术选型和技术架构都是怎样的
- 研发流程上有做效率工具么
- node 的框架用的是哪个，内存监控是怎么做的，你了解过哪些 node 的框架
- vue 和 react 都看过哪些部分源码，v-model 的原理是什么，虚拟 dom 的优缺点是什么
- typescript 相比 JavaScript 的优点是什么
- export 和 module.exports 的区别
- node 的内存泄露是如何监控的
- node 读取文件的时候，fs.readFile 和 stream 有什么区别
- 你的优势和劣势是什么
- 介绍有难点的项目
- 使用 Vite 遇到过哪些问题
- esbuild 有了解吗
- 当你们把体量很大的项目拆分后，有没有遇到拆分之前没有的问题
- 组内工具包你们是如何保证向下兼容的
- 写个二叉树遍历，深度优先广度优先
- Typescript 类型了解过吗，infer 是做什么的，实现一个 Pick 和一个 Omit
- SSR 和 CSR 的区别，Nuxt 这类的 SSR 方案和直接渲染 ejs 这类方案有什么本质的区别
- Vue 和 React 使用的比重是怎样的，这两者各自的优劣介绍一下
- PureComponent 会引入什么问题，什么情况下会需要用到它
- Vue 的单文件开发模式，这个解析 vue-loader 是如何实现的。
- 如果 template 语言换掉的话，会如何处理。
- script 的部分会如何处理，由于 babel-loader 是只能针对 js 类型的文件进行转化，那.vue 文件中的 script 标签是如何被 babel-loader 读取的。
- vue scoped 是怎么实现的，dom 上的哈希是如何和 style 中的哈希对应起来的，又是如何保证每次生成的哈希不变的
- babel.config.js 和.babelrc 有什么区别，应该在什么场景使用，同时使用的话会出现什么现象
- Vue 调用 render 函数的时机是在什么时机被触发的，后续状态变更导致 render 又是谁触发的
- Vue 和 React 在数据更新上的差异，Vue 这种数据劫持的方式会不会带来额外的问题，Vue3 在这些问题上有优化么
- 和 forceupdate 都做了哪些事
- 异步更新 DOM 这个操作，Vue 和 React 都是如何实现的，Vue 的异步处理还有其他方式可以做么，除了 MessageChannel 还有其他和他用法类似的 API 么
- 公用的代码如何做提取，如何判断一个资源是否应该被提取
- Portal 除了做了把组件提到对应的 DOM 下之外，还做了哪些事
- 用什么方式发请求，axios 是个同构的工具，它是如何实现区分 Node 和浏览器环境的
- axios 内部如何把 xhr 的 callback 转换为 promise 的，如何处理请求异常的
- 实现 ob 和 watch 方法，希望当方法传入 watch 函数时会执行一次，之后每次修改 data 上的属性时，会触发对应的 console

  ```javascript
  const data = ob({ count: 0, foo: 'test' })

  watch(() => {
    console.log('watch-count', data.count)
  })
  watch(() => {
    console.log('watch-foo', data.foo)
  })

  data.count += 1
  console.log('showcount', data.count)
  delete data.count
  data.foo = 'test2'
  ```

- 输入一个字符串，遇到方括号则对方括号内的字符串重复 n 次，n 是方括号前面的数字，如果没有数字则为 1 次，可能存在嵌套

  ```javascript
  const test1 = 'a2[b]a2[b2[c]]'
  // abbabccbcc
  const test2 = '2[3[c]]a2a'
  // cccccca2a
  const test3 = '[abc][d]3[e2]4'
  // abcde2e2e24
  ```

- Vue2 和 3 的区别，依赖收集和派发更新都是如何做的，vue 是如何保证父组件重新渲染不导致子级重新渲染的
- webpack 异步加载和分包的原理是什么
- Vite 依赖与预构建是把所有的用到的依赖都合并到一起还是每个都是单独的包，一个包安装了多个版本问题如何处理？
- node 的进程管理了解过么？多进程都有哪些方案？
  4.1 worker 挂了如何能监测到？
  4.2 IPC 通信是什么？
  4.3 如果用 cluster 启动多进程后，子进程是多个端口还是一个端口？
  4.4 一个 worker 是一个进程吗？它有独立的 pid 么？
  5.5 进程之间数据通信如何做
- node 内存泄露是如何监控的？原理是什么？内存是监控进程的还是监控 docker 的？
- webpack 打 polyfill 都有哪几种方式
- http2 都有哪些应用，多路复用和 1.1 版本 keep-alive 有什么区别和联系，如果 http1.1 服务端需要按顺序处理请求，那为什么有的时候在一个页面里看图片，有时下面的图片会先出来，http pipeline 有了解吗，http 流传输有了解吗
- 前端的工程化都做了哪些事情？git CI/CD 都做了哪些事？比如 lint，安全检查，圈复杂度都有关注吗？lint 的规则是你们业务自己定制的吗？组件测试和自动化测试有做吗？上线的流水线有配过吗？小流量上线是如何做测试的？
- Taro 多平台的兼容是怎样做的，Taro 是怎么把 react 代码编译成运行时，运行时是什么样的代码，又是如何让它在原生小程序的 DSL 中执行的
- 前端监控报警是怎么做的，都有哪些监控指标，报警的策略是怎样的，关注哪些指标和维度，白屏如何监控
- 都做过哪些优化，动画的剪包如何做，FPS 是如何监控的
- 主要做过哪些项目
- Vue 兄弟组件传值方式都有哪些
- 介绍一下 Vuex
- 介绍一下 diff 算法
- Websocket 介绍一下，它和 http 有什么关系
- 介绍一下 https
- 用三个正面的词和三个负面的词评论一下你自己
- 介绍一下你最近读过的一本书
- 有没有做过哪些和代码没关系的但是比较精通的事情
- 你对下一份工作的期望是怎样的
- 对上家公司的感受，自己的成长，不满的地方
- 之前的团队规模是怎样的
- 之前的业务是怎样的
- 对下一份工作有怎么样的期望，你对这个规划做过哪些努力
- 介绍一个有难点的工作
- 为什么之前要把项目从 SSR 迁移到 CSR
- 实现一下 koa 中间件原理，如何判断调用了多次 next 并抛出错误
- 事件循环介绍一下，Node 事件循环中如果在 Poll 阶段不停地产生新的事件会怎样
- Node 中如果要对很大的字符串做 JSON.parse 应该怎样处理
- 介绍一下浏览器的合成层
- 如果一个页面需要同时适配 PC 端和移动端，应该怎么做，rem 和 vw 方案有什么区别
- typescript 定义一个对象应该如何定义，如果定义对象的 key 必须是字符串，应该如何定义
- Vue 的响应式原理介绍一下，Watcher 的 cleanDeps 是做什么的
- computed 和 watch 是什么原理
- 如果 data 里有一个对象，不希望它被深层监听，需要怎么做
- 给定任意二维数组，输出所有的排列组合项。比如 `[['A','B'], ['a','b'], ['1', '2']]`，输出 `['Aa1','Aa2','Ab1','Ab2','Ba1','Ba2','Bb1','Bb2']`
- 给出任意一个二维数组，要求输出数组元素的所有排列组合。如`[['A', 'B', 'C'],[ 'A1', 'B1', 'C1'],[ 'A2', 'B2']]`，输出`["AA1A2", "BA1A2", "CA1A2", "AB1A2", "BB1A2", "CB1A2", "AC1A2", "BC1A2", "CC1A2", "AA1B2", "BA1B2", "CA1B2", "AB1B2", "BB1B2", "CB1B2", "AC1B2", "BC1B2", "CC1B2"]`
- Node 服务迁移到轻服务主要都做了什么
- 你们的 RPC 用的哪个框架，grpc 和 thrift 的区别有了解么，protobuf 有了解吗
- serverless 有多少了解，它适合做什么，都用它写过什么
- 客户端提供 API 版本不一致这类兼容性问题你是如何做的处理
- webpack 迁移 Vite 有遇到什么问题，snowpack 有了解过么，它和 vite 有什么区别
- 性能优化都做过哪些
- 一个页面的性能指标都有哪些，你是如何做监控的，如何监控 node 服务的性能监控
- 实现一个二叉树中序遍历的迭代器，时间复杂度最好是多少，最差是多少，空间复杂度是多少
- 实现一个函数，传入一个数组，数组中每一项代表一个线段的起止位置，计算所有线段覆盖的长度总量，并编写测试用例

  ```javascript
  lineCoverage([
    [0, 1],
    [2, 3]
  ]) // 2
  lineCoverage([
    [0, 2],
    [2, 3],
    [3, 4]
  ]) // 4
  lineCoverage([
    [0, 2],
    [1, 3],
    [2, 4]
  ]) // 4
  lineCoverage([
    [0, 5],
    [1, 3],
    [2, 4]
  ]) // 5
  lineCoverage([
    [0, 6],
    [2, 6],
    [6, 7]
  ]) // 7
  ```

- 计算一个矩阵内，所有 1 覆盖的区域（岛屿问题） 力扣

  ```ts
  howManyDots(canvas:number[][]): number
  // 上下左右相邻视为一起
  [[0,0,0],
  [0,1,0],
  [0,0,0]]
  =>1

  [[1,1,0,1],
  [0,0,1,0],
  [0,1,1,0]]
  =>3

  [[1,1,1,1],
  [0,0,0,1],
  [1,0,0,1],
  [1,1,1,1]]
  =>1
  ```

- Vue 从修改属性到渲染到页面上都经历了什么

```javascript
/**

- 目标:
- 实现一个简单的观察者模式(或发布-订阅模式)
  */

const shop = {
  apple: 5, // 苹果 5 元
  potato: 2, // 马铃薯 2 元
  tomato: 3, // 西红柿 3 元
  orange: 7 // 橙子 7 元
}

/**
 * 现在我们有一个便利店的实例对象，目标是需要增加对商品价格的监听，当商品价格发生变化时，触发对应的事件。
 * 1、小明关注苹果价格变化
 * 2、小刚关注橙子价格变化
 * 3、当价格变化时，自动触发对应的事件
 */

class Pubsub {
  constructor() {}

  list = {}

  // 监听方法，添加监听者，监听对象，和监听事件的方法，
  // 提示，可以将移除方法作为监听方法的返回值
  listen = (key, listener, callback) => {}

  // 发布消息的方法
  publish = (key, price) => {
    /** 该如何定义 发布方法？ **/
  }
}
// 定于一个Pubsub的实例对象
const pubsub = new Pubsub()

const event1 = pubsub.listen('apple', '小明', (listener, price) => {
  console.log(`${listener}关注的apple的最新价格是${price}元`)
})

const event2 = pubsub.listen('apple', '小强', (listener, price) => {
  console.log(`${listener}关注的apple的最新价格是${price}元`)
})

const event3 = pubsub.listen('orange', '小刚', (listener, price) => {
  console.log(`${listener}关注的orange的最新价格是${price}元`)
})

const event4 = pubsub.listen('orange', '小强', (listener, price) => {
  console.log(`${listener}关注的orange的最新价格是${price}元`)
})

/**
 * 应该补充怎样的逻辑能够使得我们能够监听shop中的属性值变化呢？
 * 提示：vue中双向绑定是怎么实现的呢？
 * vue2.0或vue3.0的实现方式都是可以的
 */

/** 我们设置一个观察者方法，让 shop这个实例对象便成为可观察对象 **/
const observable = () => {}

const newShop = observable(shop)

newShop.apple = 6
/** 小明关注了苹果的价格，苹果价格变更将会触发事件
 ** console.log将会输出:  小明关注的apple的最新价格是6元
 **/

newShop.tomato = 10
/** 无人关注西红柿价格，不会触发事件 **/

newShop.orange = 11
/** 小刚关注了橙子的价格，橙子价格变更将会触发事件
 ** console.log将会输出:  小刚关注的orange的最新价格是11元
 **/

console.log(newShop)
/**
 ** 输入出newShop
 **/

console.log(newShop.apple)
/**
 ** 输入出newShop的apple新值
 **/
```

- 如果需要你实现扫码登录、单点登录，有什么方案
- 为什么之前用 SSR，为什么又从 SSR 迁移成 CSR
- 离线包的原理是什么
- 有做过哪些性能优化
- vite 的原理是什么，迁移 vite 有遇到什么问题么
- serverless 有什么了解，它背后的实现原理是什么，你用它做过哪些东西
- 一个字符串的全排列 问题基本都答上来了，题也都写出来了，但是不知道为啥挂了
- Vue 新版本特性有了解么
- 在工作中有用到什么设计模式么
- typescript 装饰器有了解么，类装饰器的 this 是如何处理的
- 有用过抽象类么
- 举例一下 Map 和 object 的区别，如果需要一个字典的需求，都是 key: value 的形式，那应该怎么选择这两个呢
- Map 和 WeakMap 有什么区别
- js 垃圾回收机制有了解吗
- 二分查找的时间复杂度是多少，简要描述一下过程，O(logN)是怎么算出来的，TopK 的时间复杂度是多少，快排的时间复杂度是多少
- ES5 的继承都有哪几种，主要介绍一下组合寄生
- 输入一个二叉树和两个 node，输出这两个 node 的最近公共祖先
- 如果让你实现一个计算器，都需要考虑哪些问题 比较开放的一个题，边说边写
- 接触过哪些排序算法，归并排序的思路是什么，一个数组做归并排序的话，一共经历了多少次合并
- 前端缓存策略，last-modified 和 etag 有什么区别，分别的适用场景是什么
- 对一个树形结构遍历，输出所有叶子节点
- 换肤方案你们具体是如何实现的
- 国际化方案是如何做的
- 页面间同步状态一般都有哪些方案，分别的应用场景都是哪些
- localstorage 的会不会出现不同项目的 key 覆盖别人的 key 的问题，如何解决
- 写一个发布订阅模式的 on/emit/off
  7.1 如果需要把订阅者执行成功和失败的方法分开，需要怎么做
  7.2 如果希望失败的可追溯，找到是哪个订阅者的报错，需要怎么做
  7.3 实现一下 before 和 after 方法，可以添加一些前置的和后置的订阅者
  7.4 现在希望给所有的订阅者加打点上报的功能，并且提供全局的开关，需要如何设计
  7.5 如果需要给某一个订阅者单独加一个打点，需要如何设计
- 如果想给一个对象上的所有方法在执行时加一些打点上报的功能，如何做
- 主要都负责哪些业务，工作的 C 端和 B 端的占比是怎样的
- 如果希望 DOM 中的一个值和 js 中的变量双向绑定，使用原生 js 可以怎么做，React 和 Vue 分别又都是怎么做的
- proxy 和 defineProperty 的区别是什么，各自的优势和缺点是什么
- 浏览器发请求和 node 发请求都有什么区别，浏览器都为发请求做了哪些默认行为
- 如何理解线程和进程
- 为什么 Vite 比 webpack 快很多，ESM 和 commonJS 的区别是什么，为什么 ESM 加载会更快，如何理解 ESM 的静态
- 都做过哪些打包的优化
- 在 CI/CD 中都需要做哪些事情可以把流程做得更好
- 组件库你们是如何做的，你在里面是什么角色，组件与组件之间的调用关系如何处理
- 刘海屏你们如何适配的
- 有对小程序做过从打开到完全展现这个流程的监控么
- 讲讲对 TDD 的理解
- 提升开发效率你们有做过什么么
- 性能上优化有做过哪些事情
- 解释一下事件循环
- 对 B 端和 C 端在技术开发上侧重点都有哪些
- 请写一个抽奖程序 ，已有参与抽奖的员工工号组成的数组 staffIds。
  规则 1：同一员工不可重复中奖。
  规则 2：每轮执行抽奖程序，入参是本轮要抽取的中奖人数 n，将中奖人工号打印出来
- webpack 迁移到 Vite 有什么优势，遇到过什么问题，迁移后如何测试
- 怎么理解 SSR，在项目中如何应用
- B 端都做过哪些内容，架构是怎样的
- 浏览器请求头和响应头都能记起哪些，都是做什么的
- 协商缓存与强缓存
- 响应头和跨域相关都有哪些，之前都是如何解决跨域的
- Access-Control-Allow-Origin 用 \* 和指定域名的区别是什么
- 跨域是否允许携带 cookie，如果希望携带 cookie 需要如何做，如果 a.com 是我的域名，向 b.com 发请求，带的是哪个域名的 cookie
- 请求头的 host，origin，refer 的区别是什么
- 在什么场景下会发起 options 请求
- !important 在什么场景用，css 选择器权重是如何计算的
- 盒模型的边距叠加，如何解决盒子塌陷，如何创建 BFC
- ==和===的区别，a==1&&a==2 有什么方式让它返回 true
- Object.create(null)和直接创建一个{}有什么区别
- new 一个函数做了哪些事
- 对事件循环的理解
- Vue 和 React 源码读过哪些部分，印象最深刻的是哪些
- 简单介绍以下 Vue-router 的原理
- diff 算法简单介绍一下
- 前端工程化做过哪些
- 如何做到的逐步减少项目中的 typescript 报错
- 写过 webpack 插件么
- babel 转换的原理是什么
- 性能优化做过哪些
- 离线存储是如何做的
- 都用过哪些设计模式
- 对线上各类异常如何处理，对线上的静态资源加载失败如何捕获
- node 多进程间通信是如何做的
- koa 中间件原理实现是如何做的
- 如何界定一个依赖包的安全性
- node 做过哪些性能优化
- 在 git CI 做过哪些事，做的动机是什么
- 业务上，前端和后端的工作占比是怎样的
- 有升级到 Vue3 么，觉得 Vue 的优点是怎样的
- 脚手架用的是什么，有自己做过脚手架么，Vite 的原理是什么，如何区分环境
- 为什么要把 SSR 迁移到 CSR
- 离线包的原理是什么，有做离线包增量更新么
- bridge 原理有了解么
- 对页面的异常监控有了解吗
- 性能优化都做过哪些
- 写一个 EventBus，包含 emit/on/off
- 介绍一下盒模型，怪异模式和标准模式有什么区别
- 如何做 CSS 屏幕适配
- 移动端有没有遇到过滑动穿透的问题
- 有没有遇到过移动端浏览器兼容问题
- js 的数据类型都有哪些，有什么区别，为什么基本数据类型存到栈但是引用数据类型存到堆
- 数据类型常用的判断方式都有哪些
- await 和 promise 的关系，分别的应用场景有哪些
- esmodule 和 commonjs 区别是什么，还接触过其他的模块化方案么
- 浏览器都有过哪些了解，内核都有哪些，chrome 浏览器开启一个页签时开启了多少个进程，对应开启了哪些线程
- 异步加载 js 的方式都有哪些
- 加载 css 和 js 时会阻塞 dom 渲染么
- 强缓存和协商缓存谁的优先级谁高，区别是什么，强缓存和服务器有通讯么，没有通讯的话有状态码么，状态码是谁返回的，缓存是存到了哪里
- cookie 都有哪些属性
- samesite 作用是什么
- cookie 和 storage 的区别是什么
- http 都有哪些版本，1.1 有什么不好的地方么，队头阻塞是什么引起的，2.0 有没有完全解决了队头阻塞问题
- get 和 post 有什么区别
- Vue 和 React 的区别
- SSR 和 CSR 的区别是什么，分别的适用场景是什么，什么叫同构，除了 SSR 还有什么方案可以解决首屏渲染问题
- 有写过 webpack 插件么
- babel 配置过么，preset 和 plugin 谁的优先级高
- 项目代码规范是如何做的，如何避免有人本地跳过代码规范
- git commit 的有限制么
- eslint 和 prettier 的冲突是如何解决的
- CI 和 CD 的区别，除了 gitlab 的 CI/CD 之外还接触过哪些
- Vue3 和之前版本的差异在哪儿
- Node 了解过哪些，之前的 SSR 都是如何做的
- wasm 之前有哪些了解
- 屏幕内有一个矩形，有一条对角线，如果在矩形上点击，如何判断点击的位置是在对角线上方，还是下方，还是点到了对角线上
- 如果想给这个矩形画个对角线，可以有哪些方式
- 之前的数据可视化是如何做的
- 有没有一些技术沉淀的东西，比如在技术社区的交流或者写一些文章
- 除了编码以外，有没有做过管理方面的事情
- serverless 有哪些了解
- 前端工程化都做了哪些
- SSR 迁移到 CSR 的背景是怎样的，各自的优势是什么，为什么服务端渲染页面会比客户端快
- 首屏性能优化都有哪些
- 都有用到过哪些协议
- 遇到的无障碍的挑战是哪些，屏幕阅读器功能是如何实现的了解吗
- 国际化做过哪些
- 都做过哪些方面的重构，重构都做了哪些优化
- webpack 迁移 vite 遇到了哪些问题
- 对 serverless 有哪些了解，都用它做了哪些事情
- 测试驱动开发是怎么样的流程，有什么方案可以提高 TDD 的效率
- 前端安全都遇到过哪些问题
- https 讲一下
- 常见的 HTTP 状态码都有哪些
- 浏览器进程模型有了解吗
- 浏览器渲染流程是怎样的
- 事件循环介绍一下
- Vue 的插槽的实现原理是什么
- 都做过哪些性能优化
- Vue 的组合式 API 的优势是什么
- Vue2 的重复逻辑封装一般都有哪些方式
- 如果是需要通过调用 API 显示 UI 组件，这种需要如何实现（比如 Toast、Dialog）
- useCallback 和 useMemo 的区别和使用场景
- 对一个公共组件或者工具做打包，一般都需要产出哪些范式的文件
- commonjs 和 esm 的模块引入和加载执行的区别是什么
- node 调用 RPC 是怎么做的，对 thrift 有哪些了解
- SSR 和 CSR 的优势分别是什么
- 如果页面中有大量的 DOM 更新，导致页面变卡，有哪些方案可以优化
- 换肤方案是如何做的
- 如果在 js 中执行 location.href = url，这个行为有可能会有哪些安全问题
- CSRF 原理，整体的攻击链路是怎样的，都有哪些解决方案
- XSS 都有哪些方式，如果过滤都需要过滤哪些内容
- Vue 和 React 的区别，项目是如何做选型的
- 介绍一个之前重构的项目
- 有没有经历过需求无法实现或实现难度较大的情况，这种情况如何处理呢
- 之前做过最有挑战的问题
- 实现一个类似微信聊天列表页的布局，有如下需求
  有一个吸顶的栏，内部的内容不需要实现
  一个吸底部的按钮栏，内部有四个按钮，按钮功能不需要做，只需要实现布局
  中间的列表可滚动
  // 多说一下，这个其实考察的是画页面的基本能力和细节，比如假如使用 fixed 布局，滚动条会是全屏的
  // 但是如果使用 absolute，限制屏幕高度 100%，中间局部滚动就可以把滚动条限制到中间部分，甚至可以隐藏滚动条
  // 面试考画页面的话，一定要多注意这类细节，还有比如 BEM 命名、1px 边框等问题是否有意识，这些都要考虑
- 最长连续递增子序列
- SSR 为什么要迁移到 CSR，如果不迁移的话如何能做到 CSR 离线包的效果
- 搜索旋转排序数组 力扣
- Vue 和 React 的区别
- Vue 数据双向绑定原理
- 页面第一次加载会触发哪些 Vue 的生命周期
- Vue 的 filter 原理有了解吗，如果需要你实现一个 filter，可以实现把一个字符串首字母大写的功能，你要如何做（最开始问原理，导致我后面理解错了，我以为是让我实现一下 Vue 的 filter 功能了，然而人家其实要的是'abc' => 'Abc'的一个方法，但是面试官对我的实现持肯定态度）
- 用 css 实现一个 Tooltip：界面上有一个 Button，鼠标 hover 上去后会在 Button 上方显示一个 tooltip，这个 tooltip 有圆角，下方有一个小三角形
- 对闭包的理解，闭包的适用场景和缺点
- 从输入 URL 到页面渲染都发生了什么
- 无障碍都做过哪些
- 合并两个有序数组
- 合并多个有序数组（这题里我解答完之后自认为时间复杂度是 O(n2)，循环中用到了 shift 这个方法，面试官问我这个的时间复杂度是多少，我说是 O(n)，面试官说有什么办法可以解决这个么，我说可以基于原有的方式倒着循环，这样就可以用 pop 代替 shift 了，面试官问我为什么 pop 时间复杂度是 O(1)，我说不知道，面试官让我有时间可以去了解一下均摊算法）
- SSR 迁移 CSR 的原因，遇到过哪些问题
- LRU 算法 力扣 （这个题我最开始用 Map 做的，面试官跟我说如果不用 Map，如何实现每次查询和删除都能做到 O(1)，我没思路，面试官问我查询 O(1)用什么，我说用哈希，问我插入删除 O(1)用什么，我说用链表，可我不知道怎么结合到一起，面试官提示我可以用双向链表，然后我才做出来的）
- 在追求极致体验方面做过哪些
- 都会关注哪些指标，如何做检测
- 有没有做过自动化测试方案，对于兼容性如何做自动化测试
- 对于 UX 还原度，应该如何高效测试
- 一个 PC 页面，如果需要适配手机屏幕，都有哪些需要注意的，可能需要解决哪些问题，需要如何去测试
- SSR 迁移到 CSR 是基于什么考虑
- 项目的体量大概都有多大
- 项目优化或者重构后，一般从哪些方面评判效果好还是不好呢
- bridge 的原理有了解么，有遇到过什么问题么，在一些没有 bridge 的场景里有没有做过特殊处理
- 做过唤起 app 么，有遇到过什么问题吗，如何判断唤起是否成功
- 国际化采用的什么方案
- 换肤方案是如何做的
- 小程序和 H5 都有哪些区别，有看过小程序底层如何实现的么
- 为什么要做 Vite 迁移，迁移有遇到了什么问题
- 写一个 React Hooks，用来倒计时，传入时间，返回 start、pause、restart、isRunning
- 实现一个方法，传入一个 url 的数组和一个数字，对 url 进行请求，并根据数字限制最大请求数
- 对下一份工作有什么期望
- Vue 和 React 的区别
- proxy 和 defineproperty 的在 Vue 中区别是什么
- Vue-router 原理
- Vite 为什么会比 webpack 快
- Rollup 和 webpack 打包结果有什么异同
- 问输出，解释一下函数调用栈和作用域链的关系

  ```javascript
  function bar() {
    console.log(project)
  }

  function foo() {
    var project = 'foo'
    bar()
  }

  var project = 'global'
  foo()
  ```

- 对 js 的异步是如何理解的
- 如何理解闭包
- 判断一个对象是否是循环引用对象
- 团队内部 eslint 的规范是如何指定的
- 从输入 url 到渲染页面，都发生了什么
- 换肤方案是如何做的
- 国际化方案是如何做的，都做了哪些语种
- 离线包的方案原理是什么
- node 主要都做了哪些
- 安全问题遇到过哪些，CSRF 的加签名是如何做的
- 单向链表反转
- 快速排序
- 幂等与非幂等的区别
- get 请求是否可以传图片
- 有没有遇到过前端安全问题
- 简述 Vue 的生存周期（创建，挂载，更新，销毁）
- 你用过 Bootstrap 写过库吗？让你用 Bootstrap 设计一个系统，怎么设计？（这问题我现在都不知道怎么答）
- Express 和 Koa 框架的区别、优缺点
- Node.js 的优缺点（擅长 I/O 密集、不擅长计算密集……）
- 系统优化方案？简述一下 CDN 加速服务？
- 简述事件委托机制（事件捕获、冒泡，父元素监听）
- HTTP 里的 304 状态码了解吗？
- 简述 ES2017 里的 async 和 await
- 谈谈你印象最深的一个项目（照实说）
- 你觉得要怎样成为一名优秀的前端工程师？（快速学习、善于沟通）
- HTTP 、 HTTPS 、 HTTP2 的区别？
- 列举数组的用法（建议分类列举，栈、队列、映射、删除等）
- 数组去重（直接倒进集合再倒出来）
- 跨域（图像 ping， JSONP ， CORS ， webSocket 等）
- 本地存储（ cookie ， localStorage ， sessionStorage 等）
- HTTP ， TCP ， UDP ， IP （参看计算机网络教材）
- 进程通信，有名和匿名管道
- 你有什么要问我的吗？（见后文小结里的 HR 相关文章）
- 简述 CSRF （跨站请求伪造）的攻击和防御措施
- 在线写代码，给定一个数组和一个正整数 N，求一个和小于 N 的最长连续子数组（我两层 for 循环暴力解了，在面试官引导下做出了一定的优化）
- 在线写代码， CSS 的单行和多行截断？（ overflow ， text-overflow ）
- Vue 的双向绑定原理（事件监听， getter 和 setter ）
- 在线写代码，给定一个二叉树，求根节点到叶子节点的路径上所有节点值之和（DFS，先序遍历，递归）
- 在线写代码，两栏布局，左边定宽右边自适应，等高（ flex ， grid ， float ， position ，方法很多随便说几个）
- 简述自定义事件实现方法（参看红宝书）
- 简述 getter 和 setter 写法（参看红宝书）
- TCP 三次握手和四次挥手，拥塞控制（参看计算机网络教材）
- 跨域方式（ JSONP , webSocket 等，但原理要搞懂）
- Web 本地存储（ Cookie ， localStorage ， sessionStorage 等）
- Cookie 相关的头字段和格式（ Set-Cookie：name1=value1, expires='...',expires='...' ）
- document.cookie 的格式，写一个封装后的函数（格式同上，函数就是花式处理字符串）
- session 原理（基于 Cookie ，或查询字符串，或 ETag ）
- 手写代码，不产生新数组，删除数组里的重复元素（排序， splice() ）
- 6 道基本技术问题，居中、闭包、块级元素和行内元素等（答案略）
- 某个项目的页面布局方式，缓存的设计和优化方式（本地存储和协议相关的）
- ajax 的原生写法（创建 XHR 对象， open() ， setRequestHeader() ， send() ， onreadystatechange ）

  ```javascript
  // 关于 ajax ,我再强调以下方面。
  const xhr = new XMLHttpRequest()

  //open()接受 3 个参数：请求类型、 URL 和是否异步的布尔值
  //GET 方式通常这样发：
  xhr.open('get', 'example.php?name1=value1&name2=value2', true)

  //可以设定请求头，包括自定义请求头，比方说这样：
  xhr.setRequestHeader('MyHeader', 'MyValue')

  //可以这样取得一个包含所有头部信息的长字符串：
  var myHeader = xhr.getResponseHeader('MyHeader')
  var allHeaders = xhr.getAllResponseHeaders()

  //POST 方式有这几个地方要改：
  //请求头要重设，数据会以 key1=value1&key2=value2 的方式发送到服务器
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
  //获取表单
  var form = document.getElementById('user-info')
  //序列化表单，发送的内容传入 send()
  xhr.send(serialize(form))

  //也可以这样传值：
  var data = new FormData(form)
  //再传一点别的
  data.append('name', 'Nicholas')
  xhr.send(data)
  ```

- vue-router 的原理（ hash ， HTML5 新增的 pushState ）
- CSS 三栏布局，左右定宽，中间自适应（ flex ， grid 等）
- 解释构造函数、对象、原型链之间的关系（看红宝书）
- 手写代码，实现原型式继承（看红宝书）
- 手写代码，实现借用构造函数（看红宝书）
- Vue 双向绑定原理（事件监听， getter 和 setter ）
- Virtual DOM 和 diff 算法（ DOM 树，分层比较， key ， DocumentFragment ）
- jQuery 链式调用的原理
- 最近碰到的技术难题，不一定是前端（我答了 B 站的爬虫与反爬虫）
  关于反爬虫，请求头中的这两个字段要修改。
  - Host ：发出请求的页面所在的域。
  - Referer ：发出请求的页面的 URI 。注意， HTTP 规范将这个头部字段拼写错了，而为保证与规范一致，也只能将错就错了（这个英文单词的正确拼法应该是 referrer ）。
- 列举块级元素和行内元素（ div 等， span 等）
- absolute 依据的定位元素是？（非 static 的祖先元素）
- 几道 js 基础题（多去牛客网刷题）
- parseInt() 和 array 的 map 方法的参数？（看红宝书）
  ```javascript
  const result = ['1', '2', '3'].map(parseInt) // parseInt(item,index,arr)
  console.log(result)
  ```
- webpack 用过吗？如何处理图片、 CSS 文件？（各种 loader ）
- 使用 flex 布局写移动端布局（注意 flex-direction 要改）
- jQuery 的 delegate 原理（事件冒泡与捕获）
- z-index 的蜜汁用法（这是一个“拼爹”的属性）
- CORS 跨域文件共享的请求头（询问允许的方法和域）
- 获取页面滚动高度（ window.pageYOffset ）
- 闭包、异步（老生常谈，参见上文）
- 高阶函数（呃……我真不太清楚这是啥，听起来挺像闭包的）
- 求 N 的阶乘末尾有多少个 0，在线码代码或讲思路（求因数，统计 2、5、10 的个数）
- 给一个小于一百万的数，求和它最接近的 Fibo 数（我的思路是简单地求数列然后求差，面试官说 Fibo 数超过 34 个以后就超过一百万，可以把 34 个数都求出来然后研究状态转换……）
- CSS 布局（ Grid 和 flex 都考且考察细致）
- 数组的随机排序（我蒙了个答案，好像还算对。**打乱数组**[21]）
- JSON 对象的深度克隆（遍历递归，或者序列化和反序列化）
- 简述动画写法（ setTimeout ， requestAnimationFrame ， CSS3 ……）
- 列举“传统”的异步（……这题啥意思？不会）
- Node 的多线程，高并发，安全（我都不会……问后端大佬吧）
- 听说过 PWA 吗？（没听说过，不会……）
- 解释 event loop （听过，不太会）
- 服务端渲染，计算首屏和白屏时间（不太会……**首屏白屏**[22]
- 服务器如何强制更新后的文件替代客户端缓存的文件（不太会……好像和 MD5 有关？）
- 执行代码求输出，并说明为什么，严格模式下输出有变化吗，为什么

  ```javascript
  var a = function () {
    this.b = 3
  }
  var c = new a()
  a.prototype.b = 9
  var b = 7
  a()

  console.log(b)
  console.log(c.b)
  ```

- 请实现以下的函数，可以批量请求数据，所有的 URL 地址在 urls 参数中，同时可以通过 max 参数控制请求的并发度，当所有请求结束之后，需要执行 callback 回调函数。发请求的函数可以直接使用 fetch 即可
- 实现一个字符串反转：输入：[www.toutiao.com.cn](http://www.toutiao.com.cn) 输出：cn.com.toutiao.www
  要求：1.不使用字符串处理函数 2.空间复杂度尽可能小
- 观察者模式与发布订阅者区别，并写出其模型
- vue 事件机制是如何实现的 (<https://juejin.im/post/59ca5e975188257a8908959b>)
- vue 的组件通信方式有哪些
- vue 响应式数据原理(vue2/vue3/依赖收集/发布订阅/watcher 消息队列控制/Vue.set 实现)
- vue 转小程序怎么实现(ast/生命周期对齐/跨平台模块兼容/兼容细节点实现过程)
- 性能指标，如何理解 TTI，如何统计，与 FID 有什么区别，如何实现统计，还聊了很多性能的东西
- 说说你所了解的安全问题及防护方法（[Web 安全总结(面试必备良药)](http://mp.weixin.qq.com/s?__biz=MzI0MzIyMDM5Ng==&mid=2649825865&idx=1&sn=a049c26b3f81d8657a6066b8e11a7f05&chksm=f175e88ac602619cd82cca9716d7054007470ac77ba1a2d5b23d667cd0e7af73ebeba62ce835&scene=21#wechat_redirect)）
- 说说你知道的设计模式，并举个对应的模式例子
- 打包结果优化，具体做了哪些优化
- vue 中 beforeCreate 和 created 的区别
- vue 中用过哪些修饰器？
  事件修饰符
  .stop
  .prevent
  .capture
  .self
  .once
  .passive

  按键修饰符
  .enter
  .tab
  .delete (捕获“删除”和“退格”键)
  .esc
  .space
  .up
  .down
  .left
  .right

  其他常用的修饰符
  .trim
  .number
  .lazy
  .sync

- vue 中 computed 和 watch 的区别
  - computed 一般用于简化模板中变量的调用
  - watch 一般用于监听数据的变化，做一些逻辑处理或者异步处理，可以深度监听、立即执行
  - computed 和 watch 在源码里都是通过 Watcher 类创建出来的
  - 初始化时，先创建 computed 再创建 watch 。数据改变时，先执行 computed 再执行 watch
- vue 中 key 的作用是什么？
  Key 的作用：
  主要用来在虚拟 DOM 的 diff 算法中，在新旧节点的对比时辨别 vnode ，使用 key 时，Vue 会基于 key 的变化重新排列元素顺序，尽可能的复用页面元素，只找出必须更新的 DOM，最终可以减少 DOM 操作。常见的列子是结合 v-for 来进行列表渲染，或者用于强制替换元素/组件。
  设置 Key 的好处：
  （1）数据更新时，可以尽可能的减少 DOM 操作；
  （2）列表渲染时，可以提高列表渲染的效率，提高页面的性能；
- 比如，在 v-for 时写了 key ，将第二个元素和第三个元素交换了顺序，实际的 diff 算法怎样的
- 有没有做过组件的抽离和组件库的开发？具体做了什么工作
- 内部组件库，怎么本地开发和调试？怎么上线？本地调试有哪些方式
- 聊一聊浏览器的渲染机制，浏览器是怎么解析和渲染 html 的？
- js 异步加载的方式？defer 和 async 的区别？
  （1）defer 是在 HTML 解析完之后才会执行，如果是多个，按照加载的顺序依次执行
  （2）async 是在加载完之后立即执行，如果是多个，执行顺序和加载顺序无关
- 重定向的状态码有哪些？它们的区别是什么？【描述】【举例】
- https 相较 http ，是怎么体现安全性的？【描述】
  http: 超文本传输协议(Hypertext Transfer Protocol)，是互联网上应用最为广泛的一种网络协议，是一个客户端和服务器端请求和应答的标准（TCP），它是一个在计算机世界里专门在两点之间传输文字、图片、音频、视频等超文本数据的约定和规范。
  https 的全称是 Hypertext Transfer Protocol Secure , 它用来在计算机网络上的两个端系统之间进行安全的交换信息(secure communication). HTTPS 是 HTTP 协议的一种扩展，它本身并不保证传输的安全性，那么谁来保证安全性呢？在 HTTPS 中，使用传输层安全性(TLS)或安全套接字层(SSL)对通信协议进行加密。也就是 HTTP + SSL(TLS) = HTTPS。
  （TLS(Transport Layer Security) 是 SSL(Secure Socket Layer) 的后续版本，它们是用于在互联网两台计算机之间用于身份验证和加密的一种协议。）
- http 和 https 的区别
  https 协议需要 ca 证书，费用较高
  http 数据信息是明文传输，https 则是具有安全性的 ssl 加密传输协议。
  使用不同的链接方式，端口也不同，一般而言，http 协议的端口为 80 , https 的端口为 443
  http 的连接很简单，是无状态的；https 协议是由 http + ssl 协议构建的可进行加密传输、身份认证的网络协议，比 http 协议安全
- https 证书的作用是什么？
  CA 的全称是 Certificate Authority，证书认证机构，你必须让 CA 颁布具有认证过的公钥，才能解决公钥的信任问题。
  存在一个数字签名的认证问题。因为私钥是自己的，公钥是谁都可以发布，所以必须发布经过认证的公钥，才能解决公钥的信任问题。
- 讲一下 js 原型链【描述】
- 由构造函数创建的实例对象，和构造函数本身，他们的原型链有什么区别？【描述】
- 讲一下闭包？实际开发中有什么应用？【描述】【举例】
- flex 布局相关都有哪些属性？含义是什么？flex 属性对应哪几个属性【描述】
- flex-grow 和 flex-shrink 代表什么含义【描述】
  flex-grow 属性定义项目的放大比例，默认为 0，即如果存在剩余空间，也不放大。
  flex-shrink 属性定义了项目的缩小比例，默认为 1，即如果空间不足，该项目将缩小。
- CommonJS 与 ESModule 的区别【描述】
- Tree-shaking 原理【描述】
- ESModule 模块化是怎么解决循环引用的问题的【描述】 <https://es6.ruanyifeng.com/#docs/module-loader#%E5%BE%AA%E7%8E%AF%E5%8A%A0%E8%BD%BD>
- 最近在学习什么新技术？Vue3.0 做了哪些优化【描述】
- 说一个你做过印象最深刻的项目【描述】
- 对于首屏加速，你有哪些方案【描述】
- 路由懒加载有哪些方式【描述】
- 说一下你对模块化的理解，CommonJS 和 ESModule 有什么区别？【描述】
  CommonJS 模块输出的是一个值的拷贝，ES6 模块输出的是值的引用。
  CommonJS 模块是运行时加载，ES6 模块是编译时输出接口。
  CommonJS 模块的 require() 是同步加载模块，ES6 模块的 import 命令是异步加载，有一个独立的模块依赖的解析阶段。
- 打包结果里面出现重复包的情况，怎么解决【描述】
- 有哪些手段可以加快 webpack 打包速度【描述】
  使用高版本的 webpack (使用 webpack4)
  多线程/多实例构建：HappyPack(不维护了) thread-loader
  缩小打包作用域
  充分利用缓存提升二次构建速度
  DLLPlugin 提前打包、分包，避免反复编译浪费时间
- 移动端开发，是怎么适配的？有没有办法在打包时将 px 转换为 rem【描述】
- 描述一下 Vue 中 template 模板编译的过程【描述】
- 说下 vue-router 的实现原理【描述】
- 有没有方案，当 history.pushState 改变了浏览器地址栏后，监听到地址改变【描述】
  利用观察者模式
  重写 history 方法，并添加 window.addHistoryListener 事件机制
- 你觉得怎样才算是一个高标准的组件库【描述】
- 组件库的文档是怎么开发的？【描述】
  手工维护方案：建工程手动引用组件，书写示例和说明
  elementUI 方案：示例和说明按照一定规则写在 md 文件中，调用 md-loader 将 md 文件转成相应的页面
  Storybook 方案：Storybook 是 UI 组件的开发环境。它允许您浏览组件库，查看每个组件的不同状态，以及交互式开发和测试组件。
- 组件库怎么进行本地开发调试？【描述】
  （1）本地写 demo
  （2）本地编译，拷贝到业务系统，替换 node_module 下的静态资源进行测试
- 求实现：有个请求，10 秒内可以重试 3 次，如果 3 次都失败，就抛出异常【伪代码】
  利用 setTimeout 和 Promise.race 实现
- flex 布局以及其他的布局方式
- 讲一讲原型链
- 浏览器渲染过程
- Vue 的特性
- Vue-loader
- Eslint 的使用及原理(原理没答上来，他建议我去了解一下计算机的基础编译原理)
- 手撕事件发送和接收(裂开了，讲了思路,没有撕出来)
- 闭包
- extends
- 实现 extends 的思路
- 手写一个继承
- http2.0 http1.1 http1.0 之间的区别
- Vue 的虚拟 DOM 和 diff 算法
- 小程序和 Vue 的异同
- 项目优化的点 做过哪些
- http 缓存 304 状态码
- 你觉得你还擅长什么 比如我没问到什么 讲了跨域 websocket 和 node 其他一时想不起来了
- webpack 使用过吗？讲讲使用 webpack 的过程
- 博客是怎么优化 vue 首屏加载的 我提到了 SSR 有使用过吗？
- Date 对象使用过吗？两个 date 对象 如何判断是否在同一天
- CDN 了解过吗
- https 的工作原理
- node 的单线程
- 多线程和多进程的区别
- 在修改一个对象的属性后，如何实时在网页上更新对应的值
- CSRF 了解过吗
- XSS 攻击
- 如果一个页面突然出现了一段广告，可能是什么原因，怎么解决
- 框架带来的好处 又有什么问题
- 除了无法检测增删之外还有什么问题
- 数组的那些方法是如何写到 vue 中的
- 如何检测一个对象的类型 instanceof 的原理
- 讲一下原型链
- vue2.x 的数据劫持怎么做的(没答上来，让猜测)
- 改变数组下标的方式去修改 vue 中没有变化，如何解决？
- 虚拟 DOM 和 diff 算法
- vue-router 的两种模式 原理的差异
- 问简历上的第二个项目
- 对图像渲染的了解 echarts svg canvans 的关系 对他们的理解
- token 的原理 解决了什么问题 jwt
- TCP 四次挥手 为什么断开四次连接三次
- 专业课哪个学的好 讲讲
- 自己实现的 pid 算法的原理
- 做题，实现一个 diff，如何检测两个数组的增删改
- 假设要优化我的表单组件，要求在配置数组中控制表单的布局，怎么实现:我答的是通过添加一个字段判断属于那种类型，然后将其渲染到对应的位置，后来仔细想想感觉没有 get 到面试官的点
- 追问第一个项目路由的设计，如何实现的
- 对单页面应用的认识这里我简单讲了一下，然后提到了单页面应用的缺陷，首屏加载时间会比较长，然后谈到了优化方案，讲了现在的优化方案，以及正在调研的 SSR，讲了一下应用思路
- 追问第一个项目提到的按需加载是如何实现的
- 问项目 webpack 打包的配置
- 有没有考虑把项目打包的时候进行分离，打包成多个项目的形式我说这个项目没有考虑，其他项目有考虑过，然后讲了团队的其他几个项目，说在调研微前端进行集成，之前考虑单点登录，后面调研微前端
- 问团队的情况
- 我主要擅长 vue，他们主要使用 react，问我的看法是什么以及对 react 的认识
- 问简历上第二个项目的基本情况，分工等等
- 介绍一下简历上的第一个项目，追问了项目上的细节，分别对用户和对开发人员而言
- 第一个项目的优化
- 做第一个项目遇到的最大的问题
- 第一个项目是如何发布的
- 优化的时候我提到了 SSR(给自己挖坑了)，一直追问这方面 对 SSR 的理解 什么时候用最好 解决了什么问题 (后面反问环节说我这里答到点了，最主要的是 SEO)
- 有没有对项目打包做过优化
- 对 Vue 的认识，Vue 相较于三剑客时代，对于开发人员来说，优化了什么
- Vue 有哪些特性
- 描述一下 vue-loader 的实现原理，如果让你来实现，你会怎么实现
- SSR 和正常的渲染的区别，服务端和前端需要怎么做
- 用户访问你们的系统，渲染过程是什么样子(我答了从 URL 到渲染的过程，继续追问，服务器给用户返回资源 后，怎么渲染)
- SSR 会返回什么？在服务端怎么实现？
- 讲一讲事件代理
- 闭包和作用域问题(这是我回答的最好的问题)
- react 的了解？
- 有没有用 node 写过一些中间件(我说写过一个 token 的中间件用来鉴权，他说不算，他说的是中台那种框架中 间件)
- 移动端了解过吗？(我说媒体查询适配过，小程序了解过)
- 拉回到项目，对第二个开源项目比较感兴趣，问了很多细节，实现了什么功能，从用户出发到使用场景进行分析并提出疑问，跟我探讨，帮我总结 二十多分钟又过去了
- 第一个项目，你觉得你遇到最大的挑战是什么？
- 你觉得你带团队的时候，带实验室和带团队，区别是什么，挑战是什么，遇到过什么问题？
- 为什么选择 CBU 了解我们的业务吗 我说了之后跟我讲了下团队做的一些东西以及我后面在团队可以去发展哪些方面
- 讲一下你花时间最多的项目吧
- 你们团队遇到技术问题怎么解决呢？一般会怎么沟通
- 给你出个情景题吧，如果要你实现一个类似百度的项目，你会从什么角度来考虑，然后进行技术选型
- 你自己对前端哪些发展方向比较感兴趣呢？讲了中后台和跨端
- 你对业务这块怎么看待呢？有没有兴趣？
- 了解哪些阿里的技术栈呢？
- 项目里面遇到的最大的挑战是什么？
- 之前的面试环节遇到的没有回答好的问题有没有？
- 商业型项目规模，怎么谈的？
- 在项目里面承担的角色是什么？
- 做这么多东西学到了什么？
- 在这些管理的过程中，遇到的难题有吗？
- 有没有面试其他公司？
- 怎么考虑的？利弊是什么？
- 讲一讲对你影响很大的人
- 讲一讲你导师对你的建议
- 对个人未来发展的看法
- 网络协议七层(我说我不太熟悉，比较熟悉协议)
- http1.0 http1.1 http2.0 https tcp 和 udp 区别 （都答出来了）
- 哪些情况用 TCP 哪些情况用 UDP 直播用哪个
- 对 Vue 的认识 特性
- 双向绑定 虚拟 dom diff 算法
- CORS 跨域
- 一道题 36 匹马 6 个赛道 如何快速决出前三名
- 手撕 JSON.stringify()，自己实现一个，给了个链接写代码
- 确认毕业时间
- 简历上第二个项目细节
- 带团队的时候 code review 怎么节约时间提高效率，怎么做
- 表单输入的时候会涉及什么安全问题
- 如何上传文件很大应该怎么解决
- 讲一个项目难点
- 讲一下垃圾回收和内存泄露的情况
- 你们实验室的情况
- 一个逻辑题 100 枚硬币 两个人 一次拿 1-5 枚 第一个人第一次拿多少 一定能拿到最后一枚（4 枚）
- 过往项目或者比赛中，收获最大的一次是什么？收获了什么？
- 当初怎么接触到前端的呢？
- 还面试了哪里？如何选择
- 对前面三位面试官的评价
- 假如你在后面发现做过的项目有缺陷，你会怎么做？
- `eventloop`机制，`promise`的实现和静态方法、`async`实现。
- `Event Loop` 是什么？\*\*
  `JavaScript`的事件分两种，宏任务(`macro-task`)和微任务(`micro-task`)
  - **宏任务**：包括整体代码`script，setTimeout，setInterval`
  - **微任务**：`Promise.then(非new Promise)`，`process.nextTick(node中)`
  - 事件的执行顺序，是先执行宏任务，然后执行微任务，这个是基础，任务可以有同步任务和异步任务，同步的进入主线程，异步的进入`Event Table`并注册函数，异步事件完成后，会将回调函数放入`Event Queue`中(宏任务和微任务是不同的`Event Queue`)，同步任务执行完成后，会从`Event Queue`中读取事件放入主线程执行，回调函数中可能还会包含不同的任务，因此会循环执行上述操作。
- **`Promise` 的含义**
  `Promise`是一个异步编程的解决方案，简单来讲，`Promise`类似一个盒子，里面保存着在未来某个时间点才会结束的事件。
  三种状态：
  - `pending`：进行中
  - `fulfilled` ：已经成功
  - `rejected` ：已经失败 状态改变，只能从 `pending` 变成 `fulfilled` 或者 `rejected`，状态不可逆。
- `async`实现和常用方法
  **`async` 函数的实现原理，就是将 `Generator` 函数和自动执行器，包装在一个函数里。**
  `Generator` 函数是协程在 ES6 的实现，最大特点就是可以交出函数的执行权（即暂停执行）。
  **协程是一种用户态的轻量级线程，**协程的调度完全由用户控制。协程拥有自己的寄存器上下文和栈。协程调度切换时，将寄存器上下文和栈保存到其他地方，在切回来的时候，恢复先前保存的寄存器上下文和栈，直接操作栈则基本没有内核切换的开销，可以不加锁的访问全局变量，所以上下文的切换非常快。
- `Vue` 和 `React` 之间的区别

  1. Vue 的表单可以使用 `v-model` 支持双向绑定，相比于 React 来说开发上更加方便，当然了 `v-model` 其实就是个语法糖，本质上和 React 写表单的方式没什么区别。
  2. 改变数据方式不同，Vue 修改状态相比来说要简单许多，React 需要使用 `setState` 来改变状态，并且使用这个 API 也有一些坑点。并且 Vue 的底层使用了依赖追踪，页面更新渲染已经是最优的了，但是 React 还是需要用户手动去优化这方面的问题。
  3. React 16 以后，有些钩子函数会执行多次，这是因为引入 Fiber 的原因，这在后续的章节中会讲到。
  4. React 需要使用 JSX，有一定的上手成本，并且需要一整套的工具链支持，但是完全可以通过 JS 来控制页面，更加的灵活。Vue 使用了模板语法，相比于 JSX 来说没有那么灵活，但是完全可以脱离工具链，通过直接编写 `render` 函数就能在浏览器中运行。
  5. 在生态上来说，两者其实没多大的差距，当然 React 的用户是远远高于 Vue 的。
  6. 在上手成本上来说，Vue 一开始的定位就是尽可能的降低前端开发的门槛，然而 React 更多的是去改变用户去接受它的概念和思想，相较于 Vue 来说上手成本略高。

- `Vue3.0`都有哪些重要新特性？
  建议往 Composition API 和 Tree-shaking 方面答，对应比较`React Hooks`和`webpack` 的`Tree-shaking`
- `Vue3.0` 对比`Vue2.0`的优势在哪？
- `Vue3.0`是如何实现代码逻辑复用的？
  可以先对比`Composition API`和`mixin`的差异，并凸显出`Vue2.0`那种代码上下反复横跳的缺点。
- 讲一讲强缓存和协议缓存？
- `HTTP/2.0` 都有哪些特性？头部压缩的原理？
- `TCP`三次握手和四次挥手？以其存在意义。
- 状态码。`302.304.301.401.403`的区别？
- 状态码。`204`和`304`分别有什么作用？
- `HTTP`和`HTTPS`握手差异？
- `CSRF` 跨站请求伪造和`XSS` 跨站脚本攻击是什么？
- 你是如何解决跨域的？都有几种？
- `nginx` 了解吗？你都用来做什么？
- 有了【`Last-Modified，If-Modified-Since`】为何还要有【`ETag、If-None-Match`】
  ![图片](https://mmbiz.qpic.cn/mmbiz_jpg/icnrNBicEhkVW1cB9GKLR79AZ7pWcRCJshjFfJ3Gk8vBz3ibWNHZSibjrt8qur84JlKpaXZXocXtFia8K1mwSiaPkjrQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
- 弹性盒子中 `flex: 0 1 auto` 表示什么意思？
- 聊聊`this`的指向问题。
- 聊一聊原型链。
- 垃圾回收中的堆和栈的区别。
- `TypeScript`用过吗？聊聊你对`TypeScript`的理解？
- `call、apply`和`bind`方法的用法以及区别
- `Webpack`原理，以及常用插件
- 项目中遇到的难点，以及解决思路。
- 你是如何做`Web`性能优化的？首屏渲染如何处理？
  这个问题很大，我有个简略版，回答思路引自专栏《 浏览器工作原理与实践》：
  主要围绕着两个阶段：加载阶段 和 交互阶段
  **加载阶段：**
  1.  减少关键资源的个数和大小（`Webpack`拆/合包，懒加载等）
  2.  减少关键资源`RTT`的时间（`Gzip`压缩，边缘节点`CDN`）
      **交互阶段：**
  3.  `JS`代码不可占用主线程太久，与首屏无关的脚本加上延后处理（`aysnc/defer`）属性，与`DOM`无关的交给`Web Worker`。
  4.  `CSS`用对选择器（尽可能绑定`Class`或`Id`）,否则会遍历多次。
  5.  首屏渲染中如果有动画，加上`will-change`属性，浏览器会开辟新的层处理（触发合成机制）
  6.  避免强制同步布局，避免布局抖动。
  7.  图片懒加载（有四种方式）
- 埋点数据上报的方案做过吗？
- 前端架构思考，你是如何考量部门的技术栈的？
- 前端重构思考，老项目在新业务紧急与重构技术债务间如何衡量轻重？
- 单元测试做过吗？你是怎么做的?
- `docker` 准备流程？
- `DevOps`平台关键功能点？
- 自动化测试，`CI/CD` 的关键核心都有哪些？
- 如何保障`DevOps`推动？
- 接口如何做优化？`Mock`平台搭建方案？
- 高阶组件是什么？你设计这么一个水印组件，为什么用高阶组件。组件设计思路。\
- 说一下水印组件的业务场景。如果有人要在控制台里通过删除 dom 的方式去除水印，怎么防范？（监听键盘事件 F12 禁止打开控制台）假设用户在控制台中通过 disable js 来禁用 js，监听事件无效了，又该怎么防范？（说了一下思路，比如点击 disable js 这个动作本身是可以监听到的，那么可以监听这个动作并且拦截，然后可以做一些自定义的操作，比如直接关闭掉页面）
- Dvajs 和 umijs 区别。
- this 指向问题（箭头函数定义时确定，普通函数执行时确定）

  ```javascript
  class Student {
    constructor(name) {
      this.name = 'Tom'
    }

    getInfo() {
      return {
        name: 'Jerry',
        getName() {
          return this.name
        }
      }
    }
  }
  let s = new Student()
  console.log(s.getInfo().getName()) // Jerry
  // 如何打印出 Tom，只能修改 class 中代码
  //（箭头函数，展开说一下 this 指向的问题）
  ```

- obj 实例化，修改属性和重新实例化的指针问题

  ```javascript
  function changeObjProperty(o) {
    o.siteUrl = '<http://a.com>'
    o = new Object()
    o.siteUrl = '<http://b.com>'
  }

  let s = new Object()
  changeObjProperty(s)
  console.log(s.siteUrl)
  ```

- 0.1 + 0.2 !== 0.3(精度丢失问题：IEEE 754。如何解决？比如按小数点拆分整数部分与小数部分，分别按位相加，注意进位处理。)
- 简述一下 SPA 与前端路由（扩展讲一下 ajax -> pjax -> history api 的 pushState, popState, replaceState。浏览器 url 的出栈入栈与这些 api 的关系，路由映射管理与组件渲染。）
- 编码：
  ```javascript
  /*
  实现一个 randomString 函数，返回一个数组，
  该数组内有一千个字符串，
  每串字符串为 6 位数 0-9 的随机验证码，不可重复。
  */
  function randomString() {
    // write your code here
  }
  ```
- 编码:

  ```javascript
  /*
  实现一个 sum 函数，接收一个 arr，
  累加 arr 的项，只能使用 add 方法，
  该方法接收两个数，
  模拟异步请求后端返回一个相加后的值
  */
  function add(a, b) {
    return Promise.resolve(a + b)
  }

  function sum(arr) {
    // 思路可以二分，切成两部分 beforeSum, afterSum。
  }

  /*
  变种：如果后端设置了并发限制，
  一次不能请求超过三个，怎么办？
  */
  ```

- css 题：实现一个 chrome 浏览器的后退按钮，鼠标移入有深色的圆形背景，内部是一个 90 度的角。
- 需求题：假设有 A 页面有一些 query 参数 点击打开 B 页面 要把 A 的参数带过去 然后 B 页面跳转到 C 页面 如果是 B 页面本身带的参数 就带到 C 页面 如果 B 页面的参数是 A 页面带过来的 那么就不带到 C 页面。（这一题基本花去了大部分时间，和面试官讨论了可行的思路，然后进行编码。主要是 query 参数的 merge 处理，跳转拦截之类的实现。）
- 常规题：把 123456789，变成金钱模式，即：12,345,678（思路有很多，比如 reverse 之后利用模除手动插入逗号...）
- 编码题：

  ```javascript
  /*
  请实现抽奖函数 rand，保证随机性
  输入为表示对象数组，对象有属性 n 表示人名，w 表示权重
  随机返回一个中奖人名，中奖概率和 w 成正比
  */
  let peoples = [
    { n: 'p1', w: 100 },
    { n: 'p2', w: 200 },
    { n: 'p3', w: 1 }
  ]
  let rand = function (p) {}
  ```

- 开放题：一个 html 引入一个超大 JS，js 中是一个乱序数字数组(长度巨大)，从中找到最大值显示出来，遇到这种需求你该怎么做？
- 讲一下线程和进程的区别
- Vue2 中使用的 Object.defineProperty 和 Vue3 中使用的 Object.proxy 的区别
- 介绍一下 CDN
- 手写原生 call
- CDN 介绍，回源是什么？CDN 的原理是什么？
- v-model 的实现原理
- vue 数据拦截是怎么实现的？patch 的实现原理是怎么样的？
- 如何实现 vue 组件的异步加载？
- MVVM 框架和 MVC 框架的差别
- 算法题：版本号数组排序
- 算法题：链表转反链表
- es6、es7 这些后来的版本在 es5 的基础上新增了那些东西，罗列一下
- 闭包是什么？简单介绍一下
  （ps：这里回答的时候结合了作用域链的概念介绍了闭包的形成，然后说了一下闭包的用途还有要注意的地方）
- http 请求是怎么组成的，你对 option 请求有什么了解？这个请求在跨域的时候一定会发出吗？
- 介绍一下 flex 的各个属性，以及原理
- 对于工程化你有什么了解？怎么实现代码向下兼容？babel 为什么没实现所有代码的向下兼容？
- 介绍一下 vue 的 nextTick 是怎么实现得？
- 介绍一下你在平时业务中使用过的优化方案？
- 介绍一下浏览器的页面缓存机制？
- 算法题：判断字符串的括号正常闭合，写完之后面试官还会要求你对源代码进行优化
- React 和 Vue 的差别，为什么你的项目使用 Vue 去开发？
- vue 怎么实现数据双向绑定？data 中不定义相关字段，直接使用 v-model 可以吗？
- vue2 和 vue3 数据拦截的区别？为什么 proxy 不能向下兼容？
- vue 的 data 为什么要用函数返回一个对象？
- 无感刷新 token 是怎么实现的？
- git 操作相关
- https 数据传输流程
- CSRF 的了解
- 301、302 和 304 代表什么意思？浏览器缓存是怎么回事？
- 简单说下栈和队列？如何用栈实现队列？
- 如何判断链表是否有环？不用快慢指针的话有什么方法？
- 介绍一下浏览器从输入 URL 到解析到页面的过程？
- 介绍一下前端的盒模型？
- 介绍一下事件循环机制？
- 介绍一下前端的继承方式有哪些？
- 介绍一下 new 的过程中，有哪些步骤？
- Vue 的 diff 方法是怎么样的？Key 在其中有什么作用？
- 为什么 Vue 的 data 要返回对象？不返回有啥问题？
- 介绍一下浏览器的页面缓存机制？
- CSRF 攻击的原理，如何防范？
- MVVM 框架和 MVC 框架的差别？
- 算法题：实现树的广度优先遍历
- 算法题：实现树的深度优先遍历
- 实现广告曝光率的统计，要求如下：
  区分为资源没加载的情况下流失的用户
  统计用户累计在广告位浏览时间
  统计广告位展示比例不同的情况下的用户比例
- 如何监听线上页面内存溢出？
- 页面报错监听，考虑异步的情况（其实就是设计一套通用的报错监控方案）
- CSRF 攻击的原理，如何防范？
- MVVM 框架和 MVC 框架的差别
- 简单介绍一下装饰器模式
- 400,401,300,302 是什么意思
- font-size 和 border 可以被继承吗
- Object.defineProperty 和 Object.proxy 的区别，前者怎么使用
- 怎么捕获异步事件的报错，try catch 可以吗？
- 两道小题目

  ```javascript
  function A() {
    this.name = 'a'
  }
  function B() {
    this.name = 'b'
  }
  A.prototype.getName = function () {
    return this.name
  }
  B.prototype.getName = function () {
    return this.name
  }
  A.prototype = new B()
  const c = new A()
  c.getName()
  console.log(x)
  x = 1
  console.log(x)
  console.log(test('abc'))
  function test(p) {
    return p
  }
  var x
  ```

- 说一下浏览器缓存
  浏览器缓存分为**强缓存**和**协商缓存**，强缓存会直接从浏览器里面拿数据，协商缓存会先访问服务器看缓存是否过期，再决定是否从浏览器里面拿数据。
  控制强缓存的字段有：Expires 和 Cache-Control，Expires 和 Cache-Control。
  控制协商缓存的字段是：Last-Modified / If-Modified-Since 和 Etag / If-None-Match，其中 Etag / If-None-Match 的优先级比 Last-Modified / If-Modified-Since 高。
- cookie 与 session 的区别
  Session 是在服务端保存的一个数据结构，用来跟踪用户的状态，这个数据可以保存在集群、数据库、文件中；Cookie 是客户端保存用户信息的一种机制，用来记录用户的一些信息，也是实现 Session 的一种方式。
- 浏览器如何做到 session 的功能的。
  其实就是考察 http 怎么处理无状态是怎么处理的，具体可见 COOKIE 和 SESSION 有什么区别？里面的答案。
- 解释一下：csrf 和 xss
  XSS：恶意攻击者往 Web 页面里插入恶意 Script 代码，当用户浏览该页之时，嵌入其中 Web 里面的 Script 代码会被执行，从而达到恶意攻击用户的目的。
  CSRF：CSRF 攻击是攻击者借助受害者的 Cookie 骗取服务器的信任，可以在受害者毫不知情的情况下以受害者名义伪造请求发送给受攻击服务器，从而在并未授权的情况下执行在权限保护之下的操作。
- 怎么防止 csrf 和 xss
- 跨域的处理方案有哪些
  常用的：jsonp、CORS、nginx 代理，完整的大概是九种，可见：九种跨域方式实现原理（完整版）
- CORS 是如何做的？
  服务端设置 Access-Control-Allow-Origin 就可以开启 CORS。
- 对于 CORS ，Get 和 POST 有区别吗？
  其实想考察的就是什么时候会有**预检请求(option 请求)**。
- 了解 HTTPS 的过程吗？
  推荐浪浪的 深入理解 HTTPS 工作原理
- webpack 如何做性能优化
  webpack 做性能优化主要是考虑打包体积和打包速度。
  体积分析用 `webpack-bundle-analyzer` 插件，速度分析用：`speed-measure-webpack-plugin` 插件。
  打包速度优化瓶子君的：玩转 webpack，使你的打包速度提升 90%。
- es module 和 commonjs 的区别
  高频题，考察 ES6 模块和 CommonJS 模块 的区别。关键点：1. 前者是值的引用，后者是值的拷贝。2.前者编译时输出接口，后者运行时加载。
  推荐文章：前端模块化：CommonJS,AMD,CMD,ES6
- 动态加载的原理是啥，就是 webpack 编译出来的代码
  讲道理 webpack 动态加载就两种方式：`import()`和 `require.ensure`，不过他们实现原理是相同的。
  我觉得这道题的重点在于动态的创建 script 标签，以及通过 `jsonp` 去请求 **chunk**，推荐的文章是：webpack 是如何实现动态导入的
- 笔试题：页面结构包括页头（永远在顶部）、主体内容、页脚，页脚永远在页面底部（不是窗口底部），即内容高度不够时，页脚也要保证在页面底部
- 笔试题：写 new 的执行过程
  new 的执行过程大致如下：
  创建一个对象
  将对象的 \_ \*proto\_\* 指向 构造函数的 prototype
  将这个对象作为构造函数的 this
  返回该对象。

  ```javascript
  function myNew(Con, ...args) {
    let obj = Object.create(Con.prototype)
    let result = Con.apply(obj, args)
    return typeof obj === 'object' ? result : obj
  }
  ```

- 笔试题：写一个处理加法可能产生精度的函数，比如 0.1 + 0.2 = 0.3
  思路：对于浮点数在底层处理是有问题的，所以目的就是想办法将所以的浮点数转化为整数进行处理，同时乘以一个倍数(A)，然后加起来后再除以这个倍数(A)，这个倍数应该是两个数中最小的那个数的倍数，比如 0.1 + 0.02 ,那么应该同时乘以 100，变为 10 + 2，然后再将值除以 100。
- 写一个 es6 的继承过程
- 写一个大数相乘的解决方案。传两个字符串进来，返回一个字符串
- 算法题: https://leetcode.cn/problems/bu-ke-pai-zhong-de-shun-zi-lcof/description/
- webpack 原理
  1.  初始化参数：从配置文件和 Shell 语句中读取与合并参数，得出最终的参数；
  2.  开始编译：用上一步得到的参数初始化 Compiler 对象，加载所有配置的插件，执行对象的 run 方法开始执行编译；
  3.  确定入口：根据配置中的 entry 找出所有的入口文件；
  4.  编译模块：从入口文件出发，调用所有配置的 Loader 对模块进行翻译，再找出该模块依赖的模块，再递归本步骤直到所有入口依赖的文件都经过了本步骤的处理；
  5.  完成模块编译：在经过第 4 步使用 Loader 翻译完所有模块后，得到了每个模块被翻译后的最终内容以及它们之间的依赖关系；
  6.  输出资源：根据入口和模块之间的依赖关系，组装成一个个包含多个模块的 Chunk，再把每个 Chunk 转换成一个单独的文件加入到输出列表，这步是可以修改输出内容的最后机会；
  7.  输出完成：在确定好输出内容后，根据配置确定输出的路径和文件名，把文件内容写入到文件系统。
      在以上过程中，Webpack 会在特定的时间点广播出特定的事件，插件在监听到感兴趣的事件后会执行特定的逻辑，并且插件可以调用 Webpack 提供的 API 改变 Webpack 的运行结果。
- babel 原理
  babel 的转译过程分为三个阶段：**parsing、transforming、generating**，以 ES6 代码转译为 ES5 代码为例，babel 转译的具体过程如下：
  1.  ES6 代码输入
  2.  babylon 进行解析得到 AST
  3.  plugin 用 babel-traverse 对 AST 树进行遍历转译,得到新的 AST 树
  4.  用 babel-generator 通过 AST 树生成 ES5 代码
- 项目里如何做的性能优化
- 写过 webpack loader 或者插件吗
- 讲讲你写的 babel 插件
- 了解多端的原理吗？
- http 与 tcp 的关系
- tcp 可以建立多个连接吗？
- 介绍一下为什么要有 三次握手，四次挥手
- 写过 babel 插件吗？用来干啥的？怎么写的 babel 插件
- 知道怎么转化成 AST 的吗？
- 说一下你的项目有哪些复杂的点，以及怎么解决的
- 你们的业务组件库有多少个，是什么样的组件
- 权限组件是怎么设计的
- 介绍一下你对中间件的理解
- 怎么保证后端服务稳定性，怎么做容灾
  1.  多个服务器部署
  2.  降级处理，服务挂了，从缓存里面取。
- 怎么让数据库查询更快
  1.  索引
  2.  如果数据量太多了可以拆表，分多个数据库
- 数据库是用的什么？
  mysql
- 为什么用 mysql
- vue3 的 类似 hooks 的原理是怎么样的
- 组件升级怎么让使用这个组件的人都知道。
- 如果让你设计项目自动设计组件升级，并且安全，你会怎么去设计
- flutter 有了解过吗？为什么说它的性能可以媲美原生？它有什么缺点吗？
- 如果一个项目要用移动端跨平台框架开发，你会选择哪个？
- 反转单向链表怎么做？需要几个指针？都有什么作用？
- Vue 和 React 的区别是什么？你觉得哪个好？
- 说下 crsf 和 xss，分别举例说明，各有什么解决办法？
- Cookie 的同源策略是怎么样的，跨域情况下如何携带 Cookie（这里主要考察了 SameSite 问题，因为我 crsf 问题没答到这点）
- 假设有一个非常复杂耗时的逻辑，代码逻辑已经最优了前提下要你优化，你有哪些办法？（这题其实是考察 WebWorker）
- 说下浏览器的进程、线程模型，chrome 浏览器有多少个进程？线程模型中的每个线程都是干嘛用的？
- 说下 js 的内存泄漏，什么情况容易出现内存泄漏？怎么解决？垃圾回收机制是怎么样的？
- 自己的项目做了哪些性能优化？除了 webpack 打包之类的优化外，http 层面有做了哪些优化？gzip 如何开启？gzip 有多少个级别？
- 用二分法移除掉一个字符串中所有的字母字符。
- 随机生成 100w 正负整数存储下来，记录时间 t1；然后把这 100w 数据中的负数全去掉，记录时间 t2；然后记录总共耗时 t3 = t2 - t1。
- 在耗时 t3 的基础上优化下，使 t4 的耗时只有 t3 的 70%; 在 t4 的耗时基础下再优化，使 t5 的耗时只有 t4 的 70%...
- 说一下输入一个 url 地址后的全过程？dom 渲染那块描述过于简单，能否说的更详细点？react 中的 diff 算法的原理？传统的 diff 算法是怎么实现的？
- 你们的前端项目主要用的是 ES 版本是多少？说出 ES7 中的 3 个性特性并说出应用场景？说出 ES8 中的三个新特性并说出应用场景？
- WebWorker 有了解过吗？它有什么应用场景？刚刚的算法题可以用这个进行再次优化吗？
- 为什么说 https 是安全的？https 的证书校验过程是怎么样的？（这里一定要说的非常非常详细）证书校验用到了哪些算法？
- https 一定是安全的吗？（考察 https 中间人劫持），有什么解决办法？
- 说出 http2 中至少三个新特性？你们有在实际中用过吗？
- 要你设计一个前端监控方案，你打算怎么做。
- rem, 计算出 375 的屏幕，1rem,单位出现小数怎么处理
- 数组插入几种做法
- 数组中 删除一个元素
- Taro 的技术实现原理是什么
- 有没有了解过 Remax，它和 Taro 有何不同
- 如何评价 Flutter
- 数组替换做法
- 输入 url 到页面做了哪些事
- css 树和 html dom 树构建先后顺序
- 你关于性能优化是否只知道 js 文件摆放顺序、减少请求、雪碧图等等，却连衡量指标 window\.performance.timing 都不清楚是干什么的？
- 请你描述下一个网页是如何渲染出来的，dom 树和 css 树是如何合并的，浏览器的运行机制是什么，什么是否会造成渲染阻塞？
- 请简述下 js 引擎的工作原理，js 是怎样处理事件的 eventloop，宏任务源 tasks 和微任务源 jobs 分别有哪些？js 是如何构造抽象语法书（AST）的？
- 你是否考虑全面你编写的整个函数，或者整个功能的容错性与扩展性？怎样构建一个组件是最合理最科学的，对于错误的处理是否有统一的方式方法？
- 浏览器缓存的基本策略，什么时候该缓存什么时候不该缓存，以及对于控制缓存的字段的相关设置是否清楚？
- 你是否可以利用面向对象的思维去抽象你的功能，你会构建一个 class（ES6）吗？你对于前端架构的理解？
- 你会用 VUE，你会用 React，你读得懂这两个架构的源码吗？你懂他俩的基本设计模式吗？让你去构建一个类似的框架你如何下手？
- 你会用 less，那么让你去写一个 loader 你可以吗？
- webpack 你也会用，你了解其中原理吗？你知道分析打包依赖的过程吗？你知道 tree-shakeing 是如何干掉无用重复的代码的吗？
- 你可以用 js 去实现一个单向、双向、循环链表吗？你可以实现查找、插入、删除操作吗？
- 你了解基本常见算法吗？快速排序写一个？要是限制空间利用你该如何写？
- 你是如何理解前端架构的？你了解持续集成吗？
- 你了解基本的设计模式吗？举例单例模式、策略模式、代理模式、迭代模式、发布订阅模式。。。？
- 写一个事件监听函数呗？实现 once、on、remove、emit 功能
- node.js 的实现层是什么？
- node 的事件循环机制是怎样的？
- node 的 child_process 模块有几个 api,分别的作用是什么？
- http1.0 与 1.1 协议的区别？
- node 是如何实现 http 模块的？
- nginx 相关配置了解过吗？1、你关于性能优化是否只知道 js 文件摆放顺序、减少请求、雪碧图等等，却连衡量指标 window\.performance.timing 都不清楚是干什么的？
- js 的 async 和 defer 区别
- 一个 js 体积过大，如何加载
- 跨域的几种方式
- 线上跨域的解决办法
- cors 跨域理解
- 什么是简单请求，什么是复杂请求
- vue 和 react 区别
- tree-shaking
- babel-import-plugin 原理
- 为什么 rollup 打包体积小
- 如何实现浏览器间的兼容
- babel-polyfill 是什么，如何实现 babel-polyfill 按需加载
- javascript 精度问题的原因
- axios 用途
- http 状态 301，302， 304,缓存相关字段
- cookie、ws 是否跨域
- 触发 bfc 的方式
- rem 和 vw 的使用场景
- 说说 TS 和 ES 的区别，以及 TS 带来的好处？
- 你说你学习能力强，那你毕业这一年多来，你都是怎么熟悉业务和项目的？有系统的看完过哪本书？
- 对小程序有了解吗？（我只写过 demo）
- 对打包工具有了解吗？
- 除了 react，你还用过哪些框架？
- 求契波那切数列的第 N 项
- 获取到契波那切数列的前 N 项
- 求一个对象的层级数（我写完后，又问如果不用递归，只用循环实现呢）
- 实现下面这道题中的 machine 函数
  ![图片](https://mmbiz.qpic.cn/mmbiz_png/VgnGRVJVoHGRwjNljTztZkr75TyFTX8SZ4H4l8sld6Ud2jjibp1KIUpEdLh6s7cqd41gPvfUUzSItRCbky8vTsQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
- 介绍一下你们那边的业务？那你们业务都是在 app 里面吗？（安卓、IOS、H5 甚至小程序和快应用都有，基本上都是 webview 套 h5 做的）
- 你最近有比较感兴趣的、主要研究的技术吗？为什么感兴趣？
- 我看了你的 github，上面 star 了一个 react.backbone，这个是什么？
- 我看你的 github 里面有个 mobx-jquery，这个是做什么的？
- 这个 mobx-jquery 里面的 observer 你是怎么实现的？（封装的 autorun）那么 autorun 的原理是什么？
- 你对团队的要求是怎么样的？你毕业这一年多收获最大的是什么？
- 看到你写了 TS，那么 TS 的优势是什么呢？你说修改字段后其他还用原字段的地方会报错，那么是怎么跟踪到是否修改的呢？vscode 里面是怎么实现根据类型文件来给一个方法添加类型的呢？
- 看到你的简历里面写着维护一个老项目，这个 lizard 是什么框架？（基于 backbone 封装的一个 Hybrid 框架 xxxxx）
- 那来做道题吧。实现一个函数，可以按顺序获取到一个 DOM 节点下面所有的文本。
- 你有什么想问我的吗？（你平时在公司的一天都是在做什么呢？）
- vuex 是什么？怎么使⽤？哪种功能场景使⽤它？

  - 只⽤来读取的状态集中放在 store 中；改变状态的⽅式是提交 mutations，这是个同步的事物；异步逻辑应该封装在 action 中。
  - 在 main.js 引⼊ store，注⼊。新建了⼀个⽬录 store，…export 。
  - 场景有：单⻚应⽤中，组件之间的状态、⾳乐播放、登录状态、加⼊购物⻋
  - state：Vuex 使⽤单⼀状态树,即每个应⽤将仅仅包含⼀个 store 实例，但单⼀状态树和模块化并不冲突。存放的数据状态，不可以直接修改⾥⾯的数据。
  - mutations：mutations 定义的⽅法动态修改 Vuex 的 store 中的状态或数据
  - getters：类似 vue 的计算属性，主要⽤来过滤⼀些数据。
  - action：actions 可以理解为通过将 mutations ⾥⾯处⾥数据的⽅法变成可异步的处理数据的⽅法，简单的说就是异步操作数据。view 层通过 store.dispath 来分发 action。
    modules：项⽬特别复杂的时候，可以让每⼀个模块拥有⾃⼰的 state、mutation、action、getters，使得结构⾮常清晰，⽅便管理

- 关于响应式数据绑定，双向绑定机制：Object.defineProperty()

  vue 实现数据双向绑定主要是：采⽤数据劫持结合发布者-订阅者模式的⽅式，通过`Object.defineProperty()`来劫持各个属性的`setter`，`getter`，在数据变动时发布消息给订阅者，触发相应监听回调。当把⼀个普通`Javascript`对象传给 Vue 实例来作为它的`data`选项时,`Vue`将遍历它的属性，⽤`Object.defineProperty()`将它们转为`getter/setter`。⽤户看不到`getter/setter`，但是在内部它们让`Vue`追踪依赖，在属性被访问和修改时通知变化。

  `vue`的数据双向绑定将`MVVM`作为数据绑定的⼊⼝，整合`Observer`，`Compile`和`Watcher`三者，通过`Observer`来监听⾃⼰的`model`的数据变化，通过`Compile`来解析编译模板指令（`vue`中是⽤来解析`{{}}`），最终利⽤`watcher`搭起`observer`和`Compile`之间的通信桥梁，达到数据变化—>视图更新；视图交互变化（`input`）—>数据`model`变更双向绑定效果。

-「数据劫持」\*\*：Vue 内部使⽤了 Object.defineProperty()来实现双向绑定，通过这个函数可以监听到 set 和 get 的事件。

```javascript
var data = { name: 'yck' }
observe(data)
let name = data.name // -> get value
data.name = 'yyy' // -> change value
function observe(obj) {
  // 判断类型
  if (!obj || typeof obj !== 'object') {
    return
  }
  //Object.keys(obj)将对象转为数组
  Object.keys(obj).forEach((key) => {
    defineReactive(obj, key, obj[key])
  })
}
function defineReactive(obj, key, val) {
  // 递归⼦属性
  observe(val)
  Object.defineProperty(obj, key, {
    enumerable: true,
    configurable: true,
    get: function reactiveGetter() {
      console.log('get value')
      return val
    },
    set: function reactiveSetter(newVal) {
      console.log('change value')
      val = newVal
    }
  })
}
```

-「Proxy 与 Object.defineProperty 对⽐」\*\*

Object.defineProperty 虽然已经能够实现双向绑定了，但是他还是有缺陷的 .

- 只能对属性进⾏数据劫持，所以需要深度遍历整个对象 对于数组不能监听到数据的变化
- 虽然 Vue 中确实能检测到数组数据的变化，但是其实是使⽤了 hack 的办法，并且也是有缺陷的。

-「web 网站中常见攻击手法和原理」\*\*

- 跨站脚本攻击(`xss`)：恶意攻击者通过往`web`页面中插入恶意`html`代码，当用户浏览该页面时，嵌入`web`里面的`html`代码会被执行，从而达到恶意攻击用户的特殊目的。
- `sql`注入：`sql`注入就是把`sql`命令插入到`web`表单进行提交，或输入域名，或页面请求的查询字符串，最终达到欺骗服务器执行恶意`sql`命令的目的。具体而言，就是利用现有应用程序，将恶意的`sql`命令注入到后台数据库引擎中进行执行。
- `cookie`攻击：通过 js 很容易访问到当前网站的`cookie`，你可以打开任何网站，然后在浏览器地址栏输入`javascript:alert(doucment.cookie)`，立刻可以看到当前站点的 cookie，攻击者可以利用这个特性取得用户的关键信息。假设这个网站仅依赖 cookie 进行用户身份验证，那么攻击者就可以假冒你的身份来做一些事情。现在多数浏览器都支持在`cookie`上打上`HttpOnly`的标记，但凡有这个标记的`cookie`就无法通过`js`来获取，如果能够在关键`cookie`上打上标记，就可增强`cookie`的安全性。
- `HTTP Headers`攻击：凡是用浏览器查看任何 web 网站，无论你的 web 网站采用何种技术和框架，都用到了`http`协议。`http`协议在`Response header`和`content`之间，有一个空行，即两组`CRLF(0x0D 0A)`字符这个空行标志着`headers`的结束和`content`的开始。攻击者利用这一点，只要攻击者有办法将任意字符注入到`headers`中，这种攻击就可以发生。
- 文件上传攻击：文件上传漏洞就是利用对用户上传的文件类型判断不完善，导致攻击者上传非法类型的文件，从而对网站进行攻击。比如可以上传一个网页木马，如果存放文件的目录刚好有执行脚本的权限，那么攻击者就可以得到一个`webshell`。

-「Vue 中 diff 原理」\*\*
要知道渲染真实 DOM 的开销是很大的，比如有时候我们修改了某个数据，如果直接渲染到真实 dom 上会引起整个 dom 树的重绘和重排。有没有可能我们只更新我们修改的那一小块 dom 而不要更新整个 dom 呢？diff 算法能够帮助我们

-「diff 算法包括一下几个步骤：」\*\*

- 用`JavaScript`对象结构表示`DOM`树的结构；然后用这个树构建一个真正的`DOM`树，插到文档当中
- 当状态变更的时候，重新构造一棵新的对象树。然后用新的树和旧的树进行比较(`diff`)，记录两棵树差异
- 把 2 所记录的差异应用到步骤 1 所构建的真正的`DOM`树上(`patch`)，视图就更新了

diff 算法是通过**「同层的树节点」**进行比较而非对树进行逐层搜索遍历的方式，所以时间复杂度只有 O(n)，是一种相当高效的算法![图片](https://mmbiz.qpic.cn/mmbiz_png/83d3vL8fIicY94owPia4iaoyicxZ6HP2AccTY5EN1WtW0nQCWrNgmRV02OibmU0youFh4UH2y3pPRt47w9frzxLv94A/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)逐个遍历 newVdom 的节点，找到它在 oldVdom 中的位置，如果找到了就移动对应的 DOM 元素，如果没找到说明是新增节点，则新建一个节点插入。遍历完成之后如果 oldVdom 中还有没处理过的节点，则说明这些节点在 newVdom 中被删除了，删除它们即可。

-「vue 模板编译原理」\*\*
模板转换成视图的过程整个过程：

- Vue.js 通过编译将 template 模板转换成渲染函数(render ) ，执行渲染函数就可以得到一个虚拟节点树
- 在对 Model 进行操作的时候，会触发对应 Dep 中的 Watcher 对象。Watcher 对象会调用对应的 update 来修改视图。这个过程主要是将新旧虚拟节点进行差异对比，然后根据对比结果进行 DOM 操作来更新视图。![图片](https://mmbiz.qpic.cn/mmbiz_png/83d3vL8fIicY94owPia4iaoyicxZ6HP2AccTB5QKn5qibmv5M94OhjIDU0DFNVuZ7X5Eymg0DmmLNSfQp1LQch5S0ag/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)我们对上图几个概念加以解释:
- 渲染函数：渲染函数是用来生成`Virtual DOM`的。`Vue`推荐使用模板来构建我们的应用界面，在底层实现中`Vue`会将模板编译成渲染函数，当然我们也可以不写模板，直接写渲染函数，以获得更好的控制。
- `VNode`虚拟节点：它可以代表一个真实的`dom`节点。通过`createElement`方法能将`VNode`渲染成`dom`节点。简单地说，`vnode`可以理解成节点描述对象，它描述了应该怎样去创建真实的`DOM`节点。
- `patch`(也叫做`patching`算法)：虚拟`DOM`最核心的部分，它可以将`vnode`渲染成真实的`DOM`，这个过程是对比新旧虚拟节点之间有哪些不同，然后根据对比结果找出需要更新的的节点进行更新。这点我们从单词含义就可以看出，`patch`本身就有补丁、修补的意思，其实际作用是在现有`DOM`上进行修改来实现更新视图的目的。`Vue`的`Virtual DOM Patching`算法是基于`Snabbdom`的实现，并在些基础上作了很多的调整和改进。

- 「介绍下你了解 Webpack 多少知识」\*\*
  基本概念：

  - 入口（Entry）:指示 webpack 应该使用哪个模块，来构建其内部依赖图的开始。
  - 加载器（Loader）:webpack 默认处理 js 和 json 文件，loader 配置 webpack 去处理其他类型的文件，将其转为有效模块给应用程序使用，并添加到依赖图中。
  - 插件（Plugins）:loader 用于转换某些类型的模块，而插件用于执行范围更广的任务。比如：打包优化、资源管理、注入环境变量等。
  - 模式（Mode）:设置当前配置文件在开发和生产环境下的优化行为，默认为生产环境。
  - 输出（Output）:指示 webpack 应该在哪输出它创建的 bundle，以及如何命名文件。入口文件可以有多个，但是出口文件只能有一个。

- Loader 和 Plugin 的区别：

  - **「Loader」**在`module.rules`中配置，也就是说他作为模块的解析规则而存在。类型为数组，每一项都是一个`Object`，里面描述了对于什么类型的文件（`test`），使用什么加载(`loader`)和使用的参数（`options`）。
  - **「Plugin」**在`plugins`中单独配置。类型为数组，每一项是一个`plugin`的实例，参数都通过构造函数传入。

  在我的个人理解中，plugin 更像是对 loader 的补充，两者进行相辅相成，loader 大多是固定的配置，而 plugin 能够处理更加灵活的设置。
  核心作用：

  - 打包压缩：在进行开发时，项目文件是千姿百态的，此时可以使用 Webpack 将不同模块有序进行打包整合，根据业务进行进行划分模块，使得结构清晰可读。整个项目在开发过程中，代码和文件是比较庞大的，如果进行项目部署时，会占用很大的内存，因此可以进行压缩，将原先几十 M 降低成几 M，甚至几百 K。
  - 编译兼容：相信在实际开发中，由于历史的原因各种浏览器遗留下很多兼容性问题，一方面我们积极学习浏览器的新性能，另一方面又要兼顾旧浏览器的问题。通过 Webpack 进行按需加载器的机制，可以实现在配置 bebel-loader 时，对预定义的环境进行配置，将其对新旧浏览器进行兼容。与此同时，由于浏览器只能读取 html、js 等文件，因此可以通过 webpack 将非 js 文件模块转为可读 js 文件模块。
  - 能力拓展：通过`webpack`的`Plugin`机制，我们在实现模块化打包和编译兼容的基础上，可以进一步实现诸如按需加载，代码压缩等一系列功能，帮助我们进一步提高自动化程度，工程效率以及打包输出的质量。

- 千分位格式化数字

  用 js 实现如下功能，将给定的数字转化成千分位的格式，如把`12345678`转化成`12,345,678`。
  这题目相对是比较简单了，能够用来解决的问题的方法也有很多，最简单的可以用正则化进行处理。

  - 正则化

  ```javascript
  let num = 12345678
  let str = num.toString()
  let newStr = str.replace(/(\d)(?=(?:\d{3})+`$)/g, '$`1,')
  ```

  - 将字符串拆分拼接

  思路：将数字转换为字符串(toString())再打散成数组(split)，如果直接数字转换为数组，就是一整个放进去了，不能单独取到每一位。然后通过循环，逐个倒着把数组中的元素插入到新数组的开头(unshift)，第三次或三的倍数次，插入逗号，最后把新数组拼接成一个字符串。

  ```javascript
  let num = 12345678
  function Thousands(num) {
    //将数字转换为字符串后进行切分为数组
    let numArr = num.toString().split('')
    let arr = []
    let count = 0 //用于计数
    for (let i = numArr.length - 1; i >= 0; i--) {
      count++
      //从numArr末尾取出数字后插入arr中，其实就是对齐进行倒序
      arr.unshift(numArr[i])
      //当count每到三位数字，则进行追加逗号。i!=0即取到第1位的时候，前面不用加逗号。
      if (!(count % 3) && i !== 0) arr.unshift(',')
    }
    //将数组拼接为字符串
    return arr.join('')
  }
  Thousands(num)
  ```

  缺点：一位一位的加进去，性能差，且还要先转换成字符串再转换成数组。

  - 用 charAt()获取子字符串，主要用到字符串拼接

  思路：不先转为数组，直接获取字符串的每一个字符进行拼接。

  ```javascript
  let num = 12345678
  function Thousands(num) {
    //将数字转换为字符串
    let str = num.toString()
    let res = '' //用于接收拼接后的新字符串
    let count = 0 //用于计数
    for (let i = str.length - 1; i >= 0; i--) {
      count++
      //从numArr末尾取出数字后插入arr中，其实就是对齐进行倒序
      res = str.charAt(i) + res
      //当count每到三位数字，则进行追加逗号。i!=0即取到第1位的时候，前面不用加逗号。
      if (!(count % 3) && i !== 0) res = ',' + res
    }
    //将数组拼接为字符串
    return res
  }
  Thousands(num)
  ```

  缺点：依旧需要进行一一分割拼接。

  - 每截取三位进行拼接

  思路：每次取末三位子字符串放到一个新的空字符串里并拼接上之前的末三位，原本数组不断截掉后三位直到长度小于三个，最后把剥完的原数组拼接上新的不断被填充的数组。

  ```javascript
  let num = 123345678
  function Thousands(num) {
    //将数字转换为字符串
    let str = num.toString()
    let res = '' //用于接收拼接后的新字符串
    while (str.length > 3) {
      res = ',' + str.slice(-3) + res
      str = str.slice(0, str.length - 3)
    }
    if (str) return str + res
  }
  Thousands(num)
  ```

- 比较两个对象的属性和值是否相同

  题目描述：

  ```javascript
  obj1 = { name: 'wenbo', age: 12, score: [120, 121, 113] }
  obj2 = { age: 12, name: 'wenbo', score: [120, 121, 113] }
  ```

  - 遍历进行比较

  思路：对两个对象进行遍历取值进行比较

  ```javascript
  function fun(obj1, obj2) {
    //判断obj1、obj2是否为Object类型
    let o1 = obj1 instanceof Object
    let o2 = obj2 instanceof Object
    //如果两者有不是对象类型的，既可以直接进行等值比较
    if (!o1 || !o2) return obj1 === obj2
    //如果两个是对象类型，且两者的键值对个数不同
    if (Object.keys(obj1).length !== Object.keys(obj2).length) return false
    //当以上情况均不是，则进行遍历比较
    for (let key in obj1) {
      //需要判断两个对象的此key对应的值是否为对象类型
      let flag1 = obj1[key] instanceof Object
      let flag2 = obj2[key] instanceof Object
      if (flag1 && flag2) {
        fun(obj1[key], obj2[key])
      } else if (obj1[key] !== obj2[key]) {
        return false
      }
    }
    return true
  }
  let obj1 = { name: 'wenbo', age: 12, score: [120, 121, 113] }
  let obj2 = { age: 12, name: 'wenbo', score: [120, 121, 113] }
  fun(obj1, obj2)
  ```

  亦或：

  ```javascript
  function fun(obj1, obj2) {
    //判断obj1、obj2是否为Object类型
    let o1 = obj1 instanceof Object
    let o2 = obj2 instanceof Object
    //如果两者有不是对象类型的，既可以直接进行等值比较
    if (!o1 || !o2) return obj1 === obj2
    //如果两个是对象类型，且两者的键值对个数不同
    if (Object.keys(obj1).length !== Object.keys(obj2).length) return false
    //取对象obj1和obj2的属性名
    let obj1Props = Object.getOwnPropertyNames(obj1)
    //循环取出属性名，再判断属性值是否一致
    for (let i = 0; i < obj1Props.length; i++) {
      let propName = obj1Props[i]
      //需要判断两个对象的此key对应的值是否为对象类型
      let flag1 = obj1[propName] instanceof Object
      let flag2 = obj2[propName] instanceof Object
      if (flag1 && flag2) {
        fun(obj1[propName], obj2[propName])
      } else if (obj1[propName] !== obj2[propName]) {
        return false
      }
    }
    return true
  }
  let obj1 = { name: 'wenbo', age: 12, score: [120, 121, 113] }
  let obj2 = { age: 12, name: 'wenbo', score: [120, 121, 113] }
  console.log(fun(obj1, obj2))
  ```

  - 需要考虑的问题

  当对象遍历过程中，遇到对象的属性时 Object 类型，且指向的是该对象，那么需要考虑的是以上代码还能运行成功吗？如：

  ```javascript
  let obj1 = { name: 'wenbo', age: 12, score: [120, 121, 113] }
  obj1.temp = obj1
  let obj2 = { age: 12, name: 'wenbo', score: [120, 121, 113] }
  obj2.temp = obj1
  ```

  思路：新建一个数组，将 obj1 遍历过的键值存储在数组中，再下一次进行遍历时发现一样的值，直接跳过进行比较。

- 伪代码实现下懒加载

- 代码题

  ```javascript
  if (!('a' in window)) {
    var a = 1
  }
  console.log(a)
  var a = {}
  var b = {}
  var c = {}
  console.log(a === b)
  console.log(b === c)
  console.log(a === c)

  var d = (e = f = {})
  f = {}
  e = f
  d = e

  console.log(d === e)
  console.log(d === f)
  console.log(e === f)
  ```

- http 状态 301，302， 304,缓存相关字段
- cookie、ws 是否跨域
- 触发 bfc 的方式
- rem 和 vw 的使用场景
- 伪代码实现下懒加载
- 实现一下 some, every
- flatten 实现
- 函数组件怎么阻止重复渲染
- AST 作用 or babel 实现原理
- 实现自定义 hooks,usePrevious。setcount(count => count + 1)后输出上一次 count 的值
- 不同域名共享 cookie
- on, emit, 实现
- 输入 url 到页面返回结果
- 缓存的实现方式
- webpack 分包
- Webpack 插件，生命周期
- umi 约定式路由怎么实现的
- babel 实现远原理
- React ref
- fib 实现，如何优化
- 说出你最擅长的部分，追问
- webpack 拆包的依据。1.被多个模块使用，cache 起来 2.资源过大
- canvas 点击线段事件。重合区域怎么处理
- webWorker 的使用：为什么不在 worker 里面发出请求，做数据转换呢？
- generate 函数和 async 区别
- webpack 插件实现
- Vue， React 使用情况
- 父子组件的 mounted 调用顺序
- $nextTick 实现原理
- 子元素水平垂直居中
- 斐波那契数列如何优化
- 业务题：封装一个全局的弹窗，在任何组件内都可以调用。追加：如何同时打开 5 个弹窗，关闭顺序又如何
- 封装 Vue 插件
- $nextTick 原理
- 兄弟组件通信
- vuex 模块化怎么做
- 不同域名如何共享 cookie
- 性能优化的点，webpack 分包，首页资源大小，请求优化，gzip 之前还是之后，React 重新渲染
- 国际化站点，cdn, 在页面什么阶段加载国际化文件，如果有 20 多个语言该怎么做
- ssr 有没有用过
- 项目中 websocket 是解决了什么问题
- DOM, BOM, js 的关系
- React dom 绑定事件，与原生事件有什么区别
- http2 多路复用
- 有使用过 vue 吗？说说你对 vue 的理解?
- 说说你对 SPA 单页面的理解，它的优缺点分别是什么？如何实现 SPA 应用呢?
- 什么是双向绑定？原理是什么?
- 请描述下你对 vue 生命周期的理解？在 created 和 mounted 这两个生命周期中请求数据有什么区别呢？
- Vue 组件之间的通信方式都有哪些？
- v-show 和 v-if 有什么区别？使用场景分别是什么？
- v-if 和 v-for 的优先级是什么？如果这两个同时出现时，那应该怎么优化才能得到更好的性能？
- SPA 首屏加载速度慢的怎么解决？
- Vue 中组件和插件有什么区别？
- 为什么 data 属性是一个函数而不是一个对象？
- 动态给 vue 的 data 添加一个新的属性时会发生什么？怎样解决？
- Vue 实例挂载的过程是什么？
- Vue 中的 $nextTick 有什么作用？
- 说说你对 vue 的 mixin 的理解，有什么应用场景？
- 说说你对 slot 的理解？slot 使用场景有哪些？
- Vue.observable 你有了解过吗？说说看
- 你知道 vue 中 key 的原理吗？说说你对它的理解
- 怎么缓存当前的组件？缓存后怎么更新？说说你对 keep-alive 的理解是什么？
- Vue 常用的修饰符有哪些？有什么应用场景？
- 你有写过自定义指令吗？自定义指令的应用场景有哪些？
- Vue 中的过滤器了解吗？过滤器的应用场景有哪些？
- 什么是虚拟 DOM？如何实现一个虚拟 DOM？说说你的思路
- 你了解 vue 的 diff 算法吗？说说看
- Vue 项目中有封装过 axios 吗？主要是封装哪方面的？
- 你了解 axios 的原理吗？有看过它的源码吗？
- SSR 解决了什么问题？有做过 SSR 吗？你是怎么做的？
- 使用 vue 开发过程你是怎么做接口管理的？
- 说下你的 vue 项目的目录结构，如果是大型项目你该怎么划分结构和划分组件呢？
- vue 要做权限管理该怎么做？如果控制到按钮级别的权限怎么做？
- Vue 项目中你是如何解决跨域的呢？
- vue 项目本地开发完成后部署到服务器后报 404 是什么原因呢？
- 你是怎么处理 vue 项目中的错误的？
- Vue3 有了解过吗？能说说跟 Vue2 的区别吗？
- 算法：实现 36 进制转换
- 简述 https 原理，以及与 http 的区别
- 操作系统中进程和线程怎么通信
- node 中 cluster 是怎样开启多进程的，并且一个端口可以被多个进程监听吗
- 实现原生 ajax
- vue-router 源码
- vue 原理（手写代码，实现数据劫持）
- 算法：树的遍历有几种方式，实现下层次遍历
- 介绍一下项目中的难点
- 你知道哪些 http 头部
- 怎么与服务端保持连接
- http 请求跨域问题，你都知道哪些解决跨域的方法
- webpack 怎么优化
- 你了解哪些请求方法，分别有哪些作用和不同
- 你觉得 typescript 和 javascript 有什么区别
- typescript 你都用过哪些类型
- typescript 中 type 和 interface 的区别
- 算法题：合并乱序区间
- 你了解 node 多进程吗
- node 进程中怎么通信
- node 可以开启多线程吗
- 算法题：老师分饼干，每个孩子只能得到一块饼干，但每个孩子想要的饼干大小不尽相同。
  - 目标是尽量让更多的孩子满意。如孩子的要求是 1, 3, 5, 4, 2，饼干是 1, 1，
  - 最多能让 1 个孩子满足。如孩子的要求是 10, 9, 8, 7, 6，饼干是 7, 6, 5，最多能
  - 让 2 个孩子满足。
- 算法题：给定一个正整数数列 a, 对于其每个区间, 我们都可以计算一个 X 值;
  - X 值的定义如下: 对于任意区间, 其 X 值等于区间内最小的那个数乘上区间内所有数和;
  - 现在需要你找出数列 a 的所有区间中, X 值最大的那个区间;
  - 如数列 a 为: 3 1 6 4 5 2; 则 X 值最大的区间为 6, 4, 5, X = 4 \* (6+4+5) = 60;
- https 与 http 有什么区别(一面刚好也被问到)
- cookie 有哪些属性
- cookie,session,localstorage,sessionstorage 有什么区别
- 怎么禁止 js 访问 cookie
- 你知道哪些状态码
- options 请求方法有什么用
- less,sass 它们的作用是什么
- 项目中生成 PDF 的会占用 CPU 很多吧，如果大量访问怎么处理
- 有什么通知用户的方法
- HTTPS 原理
- 浏览器的同源策略，不做限制会造成什么影响
- XSS
- CSRF
- GET 和 POST 的区别
- HTTP OPTIONS 请求
- 304 状态码
- HTTP/2 有什么新特性
- 前端性能优化都有哪些方法
- 平时用到的数据结构和算法有哪些
- 哈希的原理
- 二叉搜索树的原理
- 给定两个文本文件，找出他们中相同的行都有哪些
- 对 JS 单线程的理解
- 事件循环
- 页面间共享数据的方法有哪些
- 点击链接到打开页面之间发生了什么
- 大文本文件排序用什么算法好
- 三次握手和四次挥手详细介绍
- TCP 有哪些手段保证可靠交付
- URL 从输入到页面渲染全流程
- 如何预防中间人攻击
- ES6 的 Set 内部实现
- 如何应对流量劫持
- 跨域
- webpack 的 plugins 和 loaders 的实现原理
- vue 和 react 谈谈区别和选型考虑
- webpack 如何优化编译速度
- 事件循环机制，node 和浏览器的事件循环机制区别
- 单元测试编写有哪些原则
- 一个大型项目如何分配前端开发的工作
- typescript 有什么好处
- vue 项目中如何约束 rxjs 数据的类型
- JWT 优缺点
- 选择器优先级
- nginx 负载均衡配置
- 前端性能优化手段
- 301 302 307 308 401 403
- vue 组件间通信
- 谈谈 XSS 防御，以及 Content-Security-Policy 细节
- 场景题：一个气球从右上角移动到中间，然后抖动，如何实现
- 场景题：一个关于外边距合并的高度计算
- 算法：实现 setter(obj, 'a.b.c' ,val)
- 手写冒泡排序
- JWT 细节，适用场景
- 跨域
- 方案题：不同前端技术栈的项目，如何实现一套通用组件方案？
- ES6 特性
- 闭包和 this 一起谈谈
- postcss 配置
- Promise 内部实现原理
- vuex, mobx, redux 各自的特点和区别
- 各方面谈谈性能优化
- serviceworker 如何保证离线缓存资源更新
- virtual dom 有哪些好处
- Vue3 proxy 解决了哪些问题？
- Vue 响应式原理
- 发布订阅模式和观察者模式的异同
- css 垂直居中
- CI/CD 流程
- 谈谈性能优化
- canvas 优化绘制性能
- webpack 性能优化手段
- 事件循环
- 如何解决同步调用代码耗时太高的问题
- 场景题：如何实现登录功能
- vue 组件间通信
- 性能优化
- vuex 数据流动过程
- 谈谈 css 预处理器机制
- 算法：Promise 串行
- CI/CD 整体流程
- 性能优化
- SSR 对性能优化的提升在哪里
- vue 组件间通信
- react 和 vue 更新机制的区别
- Vue3 proxy 的优劣
- 性能优化
- 深拷贝
- 跨域
- rem, 计算出 375 的屏幕，1rem,单位出现小数怎么处理
- javascript 精度问题的原因
- axios 用途
- 性能优化的点，webpack 分包，首页资源大小，请求优化，gzip 之前还是之后，React 重新渲染
- 国际化站点，cdn, 在页面什么阶段加载国际化文件，如果有 20 多个语言该怎么做
- ssr 有没有用过
- 项目中 websocket 是解决了什么问题
- DOM, BOM, js 的关系
- React dom 绑定事件，与原生事件有什么区别
- http2 多路复用
- vue 和 react 选型和比较
- ssr 优缺点
- 贝塞尔曲线
- Vue3 proxy 优缺点
- ES6 特性
- Vue 组件间通信
- ssr 性能优化，node 中间层细节处理
- 如何编写 loaders 和 plugins
- 性能优化
- webpack 热更新原理
- vue 和 react 组件通信
- 说下你常用的几种布局方式，集中往盒模型、flex 布局说(至于 grid 布局，这个我看过没有用到过)
- 实现水平居中的几种方法？
- animate 和 translate 有没有用过，一些常见的属性说下？
- CSS 实现宽度自适应 100%，宽高 16:9 的比例的矩形。
- 如何实现左边两栏一定比例，左栏高度随右栏高度自适应？
- 说一下对闭包的理解，以及你在什么场景下会用到闭包？
- 说一下你对原型与原型链的了解度，有几种方式可以实现继承，用原型实现继承有什么缺点，怎么解决？
- iframe 的缺点有哪些？
- Ajax 的原生写法
- 为什么会有同源策略？
- 前端处理跨域有没有遇到过，处理跨域的方式有哪几种方式去解决
- 怎么判断两个对象是否相等
- 代码实现一个对象的深拷贝
- 从发送一个 url 地址到返回页面，中间发生了什么
- 说下工作中你做过的一些性能优化处理
- HTML5 新特性，语义化
- 浏览器的标准模式和怪异模式
- xhtml 和 html 的区别
- 使用 data-的好处
- meta 标签
- canvas
- HTML 废弃的标签
- css js 放置位置和原因
- 什么是渐进式渲染
- html 模板语言
- meta viewport 原理-
- 盒模型，box-sizing
- CSS3 新特性，伪类，伪元素，锚伪类
- CSS 实现隐藏页面的方式
- 如何实现水平居中和垂直居中。
- 说说 display
- 请解释{box-sizing\:border-box;}的作用，并说明使用它的好处
- 浮动元素引起的问题和解决办法？绝对定位和相对定位，元素浮动后的 display 值
- 解释一下 css3 的 flexbox，以及适用场景
- inline 和 inline-block 的区别
- 哪些是块级元素那些是行级元素，各有什么特点
- grid 布局
- table 布局的作用
- 实现两栏布局有哪些方法？
- css dpi
- 你知道 attribute 和 property 的区别么
- css 布局问题？css 实现三列布局怎么做？如果中间是自适应又怎么做？
- 流式布局如何实现，响应式布局如何实现
- 移动端布局方案
- 实现三栏布局（圣杯布局，双飞翼布局，flex 布局）
- 清除浮动的原理
- overflow:hidden 有什么缺点？
- padding 百分比是相对于父级宽度还是自身的宽度
- css3 动画，transition 和 animation 的区别，animation 的属性，加速度，重力的模拟实现
- CSS 3 如何实现旋转图片（transform: rotate）
- sass less
- 对移动端开发了解多少？（响应式设计、Zepto；@media、viewport、JavaScript 正则表达式判断平台。）
- 什么是 bfc，如何创建 bfc？解决什么问题？
- CSS 中的长度单位（px,pt,rem,em,ex,vw,vh,vh,vmin,vmax）
- CSS 选择器的优先级是怎样的？
- 媒体查询的原理是什么？
- CSS 的加载是异步的吗？表现在什么地方？
- 常遇到的浏览器兼容性问题有哪些？常用的 hack 的技巧
- 外边距合并
- JS 常见的 dom 操作 api
- 解释一下事件冒泡和事件捕获
- 事件委托（手写例子），事件冒泡和捕获，如何阻止冒泡？如何组织默认事件？
- 对闭包的理解？什么时候构成闭包？闭包的实现方法？闭包的优缺点？
- call，apply，bind
- 显示原型和隐式原型，手绘原型链，原型链是什么？为什么要有原型链
- 创建对象的多种方式
- 实现继承的多种方式和优缺点
- new 一个对象具体做了什么
- 手写 Ajax，XMLHttpRequest
- 举例说明一个匿名函数的典型用例
- 指出 JS 的宿主对象和原生对象的区别，为什么扩展 JS 内置对象不是好的做法？有哪些内置对象和内置函数？
- attribute 和 property 的区别
- 什么是“use strict”,好处和坏处
- 函数的作用域是什么？js 的作用域有几种？
- JS 如何实现重载和多态
- 原生事件绑定（跨浏览器），dom0 和 dom2 的区别？
- 给定一个元素获取它相对于视图窗口的坐标
- 如何实现图片滚动懒加载
- js 的字符串类型有哪些方法？ 正则表达式的函数怎么使用？
- 深拷贝
- 编写一个通用的事件监听函数
- web 端 cookie 的设置和获取
- JavaScript 的事件流模型都有什么？
- navigator 对象，location 和 history
- js 的垃圾回收机制
- 内存泄漏的原因和场景
- DOM 事件的绑定的几种方式
- DOM 事件中 target 和 currentTarget 的区别
- js 动画和 css3 动画比较
- JavaScript 倒计时（setTimeout）
- js 处理异常
- js 的设计模式知道那些
- 轮播图的实现，以及轮播图组件开发，轮播 10000 张图片过程
- websocket 的工作原理和机制。
- 手指点击可以触控的屏幕时，是什么事件？ 什么是函数柯里化？以及说一下 JS 的 API 有哪些应用到了函数柯里化的实现？(函数柯里化一些了解，以及在函数式编程的应用，- 最后说了一下 JS 中 bind 函数和数组的 reduce 方法用到了函数柯里化。)
- 所有的 ES6 特性你都知道吗？如果遇到一个东西不知道是 ES6 还是 ES5, 你该怎么区分它
- es6 的继承和 es5 的继承有什么区别
- promise 封装 ajax
- es6 generator 是什么，async/await 实现原理
- ES6 和 node 的 commonjs 模块化规范区别
- HTTP 协议头含有哪些重要的部分，HTTP 状态码
- 网络 url 输入到输出怎么做？
- 性能优化为什么要减少 HTTP 访问次数？
- Http 请求的过程与原理
- https（对是 https）有几次握手和挥手？https 的原理。
- http 有几次挥手和握手？TLS 的中文名？TLS 在哪一网络层？
- TCP 连接的特点，TCP 连接如何保证安全可靠的？
- 为什么 TCP 连接需要三次握手，两次不可以吗，为什么
- 为什么 tcp 要三次握手四次挥手？
- tcp 的三次握手和四次挥手画图（当场画写 ack 和 seq 的值）？
- tcp 与 udp 的区别
- get 和 post 的区别？什么情况下用到？
- http2 与 http1 的区别？
- websocket
- 什么是 tcp 流，什么是 http 流
- babel 是如何将 es6 代码编译成 es5 的
- http2 的持久连接和管线化
- 域名解析时是 tcp 还是 udp
- 域名发散和域名收敛
- Post 一个 file 的时候 file 放在哪的？
- HTTP Response 的 Header 里面都有些啥？-
- 跨域，为什么 JS 会对跨域做出限制
- 前端安全：xss，csrf…
- 浏览器怎么加载页面的？script 脚本阻塞有什么解决方法？defer 和 async 的区别？
- 浏览器强缓存和协商缓存
- 浏览器的全局变量有哪些
- 浏览器同一时间能够从一个域名下载多少资源
- 按需加载，不同页面的元素判断标准
- web 存储、cookies、localstroge 等的使用和区别
- 浏览器的内核
- 如何实现缓存机制？（从 200 缓存，到 cache 到 etag 再到）
- 说一下 200 和 304 的理解和区别
- 什么是预加载、懒加载
- 一个 XMLHttpRequest 实例有多少种状态？
- 服务器如何知道你？
- 浏览器渲染过程
- ie 的某些兼容性问题
- session
- 拖拽实现
- 拆解 url-
- 对 webpack,gulp，grunt 等有没有了解?对比。
- webpack 的入口文件怎么配置，多个入口怎么分割。
- webpack 的 loader 和 plugins 的区别
- gulp 的具体使用。
- 前端工程化的理解、如何自己实现一个文件打包，比如一个 JS 文件里同时又 ES5 和 ES6 写的代码，如何编译兼容他们-
- 对 AMD,CMD,CommonJS 有没有了解?
- 为什么要模块化？不用的时候和用 RequireJs 的时候代码大概怎么写？
- 说说有哪些模块化的库，有了解过模块化的发展的历史吗？
- 分别说说同步和异步模块化的应用场景，说下 AMD 异步模块化实现的原理？
- 如何将项目里面的所有的 require 的模块语法换成 import 的 ES6 的语法？
- 使用模块化加载时，模块加载的顺序是怎样的，如果不知道，根据已有的知识，你觉得顺序应该是-
- 使用过哪些框架？
- zepto 和 jquery 是什么关系，有什么联系么？
- jquery 源码如何实现选择器的，为什么\$取得的对象要设计成数组的形式，这样设计的目的是什么
- jquery 如何绑定事件，有几种类型和区别
- 什么是 MVVM，MVC，MVP
- Vue 和 Angular 的双向数据绑定原理
- Vue，Angular 组件间通信以及路由原理
- react 和 vue 的生命周期
- react 和 vue 的虚拟 dom 以及 diff 算法
- vue 的 observer，watcher，compile
- react 和 angular 分别用在什么样的业务吗？性能方面和 MVC 层面上的区别
- jQuery 对象和 JS 的 Element 有什么区别
- jQuery 对象是怎么实现的
- jQuery 除了它封装了一些方法外，还有什么值得我们去学习和使用的？
- jQuery 的\$(‘xxx’)做了什么事情
- 介绍一下 bootstrap 的栅格系统是如何实现的-
- 对 nodejs 有没有了解
- Express 和 koa 有什么关系，有什么区别？
- nodejs 适合做什么样的业务？
- nodejs 与 php，java 有什么区别
- Nodejs 中的 Stream 和 Buffer 有什么区别？
- node 的异步问题是如何解决的？
- node 是如何实现高并发的？
- 说一下 Nodejs 的 event loop 的原理-
- 8 种排序算法，原理，以及适用场景和复杂度
- 说出越多越好的费波拉切数列的实现方法？-
- cdn 的用法是什么？什么时候用到？
- 浏览器的页面优化？
- 如何优化 DOM 操作的性能
- 单页面应用有什么 SEO 方案？
- 单页面应用首屏显示比较慢，原因是什么？有什么解决方案？-
- 正则表达式
- 前端渲染和后端渲染的优缺点
- 数据库的四大特性，什么是原子性，表的关系
- 你觉得前端体系应该是怎样的？
- 一个静态资源要上线，里面有各种资源依赖，你如何平稳上线
- 如果要你去实现一个前端模板引擎，你会怎么做
- 知道流媒体查询吗？
- SEO
- mysql 和 mongoDB 有什么区别？
- restful 的 method 解释
- 数据库知识、操作系统知识
- click 在 ios 上有 300ms 延迟，原因及如何解决
- 移动端的适配，rem+媒体查询/meta 头设置
- 移动端的手势和事件；
- unicode，utf8，gbk 编码的了解，乱码的解决-
- 你都看过什么书？最近在看什么书？
- 用过什么框架？有没有看过什么框架的代码？
- 有没有学过设计模式？
- 说一说观察者模式吧！能不能写出来？
- 你最大的优点是什么？那你最大的缺点呢？
- 你除了写博客还有什么输出？
- 现在你的领导给你了一份工作，要求你一个星期完成，但你看了需求以后估计需要 3 周才能完成，你该怎么办？
- 平时关注的前端技术
- 如何规划自己的职业生涯
- 项目过程中，有遇到什么问题吗？怎么解决的？
- 最近在研究哪方面的东西？
- 请介绍一项你最热爱、最擅长的专业领域，并且介绍的学习规划。
- 请介绍你参与的印象最深刻的一个项目，为什么？并且介绍你在项目中的角色和发挥的作用。-
- http、https、以及 websocket 的区别
- http 常见的状态码，400,401,403 状态码分别代表什么？
- 协商缓存和强缓存的区别
- 说下计算机网络的相关协议？
- 简单阐述一下 vue 的生命周期
- 如何实现一个自定义组件，不同组件之间如何通信的？
- 父子组件如何通信的？
- 前端路由有没有用过，你在项目中怎么实现路由的嵌套？
- nextTick 和 Vuex 两个有没有用过，分为什么情况下用到？
- Vue 的响应式原理你知道是怎么实现的吗？你觉得订阅者-发布者模式和观察者模式有区别吗？有的话，说一下它们的区别。
- CSS 常见两列布局、三列布局
- CSS 水平垂直居中
- 闭包，JS 没有闭包的话会怎么样
- js 的原型链，继承
- js 的 bind、apply、call 有什么区别
- new 操作符原理（手动实现 new 给出思路）
- promise.all 应用场景
- promise 和 async/await 的区别
- vue 的生命周期（我说我 React 比较熟）
- react 的生命周期（React16）
- react 性能优化
- react 的 diff 算法
- react 的 Fiber 架构
- 状态码 304（强缓存和协商缓存）
- MVC MVP MVVM 架构了解吗，他们的使用场景
- 怎么理解前后端分离思想
- 网络安全
- 看你用过 nginx，聊聊 nginx 吧
- docker 也用过？（不是很熟还是别往简历上写给自己挖坑啦..）
- 圣杯布局、双飞翼布局
- CSS 媒体查询
- CSS 动画、CSS 对网页性能优化
- 浏览器渲染原理
- JS 单线程、EventLoop、宏队列、微队列
- Ajax 和 Fetch
- 怎么同时让多个异步请求并行
- 跨域
- xss 和 csrf （聊到跨域基本都会聊跨域安全问题，所以这两个知识点可以一起准备
- session 和 cookie
- 服务器怎么知道 session 过期？
- 怎么设置 cookie 过期时间
- sessionStorage 和 localStorage
- 强缓存和协商缓存
- promise、generator、async/await
- PureComponent 知道吗
- JS 垃圾回收
- JS EventLoop
- 知道装饰器吗
- 数组方法 map、filter、reduce
- babel 的编译原理
- webpack 工作流程和原理，怎么写一个插件
- TCP ？UDP ？区别是什么，你说 TCP 头部很大，具体有哪些报文信息呢？
- 页面渲染 重绘与重排 页面加载如何优化
- http1.1 / http2.0 / https
- 最短路径算法能简单聊聊实现吗 （迪杰斯特拉算法）
- 树的深度优先遍历、广度优先遍历实现和区别
- 一棵二叉树要用数组存储，这棵树要具备哪种条件？（完全二叉树）
- 实现括号匹配用数据结构怎么做？说说思路 （栈）
- 快速排序原理
- 小程序的富文本为什么选用 wxParse，富文本原理
- 图片有哪些格式，知道 WebP 格式的图片吗，图片的一些优化手段
- 跨域
- 前端常见攻击方式
- 状态码
- 强缓存和协商缓存
- Node 的优势
- Express 和 Koa 区别
- react 路由原理
- react hooks
- redux 异步中间件实现原理
- Vue MVVM 原理
- 服务端渲染原理
- nginx 的配置，反向代理、负载均衡原理
- 知道 PWA 吗
- hybrid 技术
- Flutter 了解吗
- 看过源码吗
- 使用框架踩到坑时，有没有去看过源码？
- 在做项目时，有没有从架构层面考虑过
- 我现在有个需求，需要实现一个 web 端的微信，你想想该怎么实
- 怎么看待前后端分离思想，以及服务端渲染技
- 写过脚手架吗
- 了解过设计模式吗？
- 后端的技术栈有了解吗？
- 平时是怎么学习的，学习习惯，为什么学前端？
- 性能优化
- http 缓存
- 做过的有特点的项目
- 遇到的问题与解决方案
- toB 和 toC 的区别
- 前端安全相关(着重中间人劫持)
- 对 vuex 的看法
- vue 从 data 改变到页面渲染的过程
- 介绍状态机
- 组件设计原则
- 怎么看待组件层级嵌套很多层
- 前端安全防范措施
- 介绍 oauth
- 怎么看待 virtual dom
- 对 flutter 的了解
- weex 和 rn 原理
- 大屏用的技术
- 大屏数据来源与管理
- websocket 的使用场景
- pwa 的使用
- 对 http2 的了解
- 对新技术的了解
- 介绍项目特色与难点
- 对 MVC MVP MVVM 的了解
- 对 SEO 的了解
- 实现 F12 开发者工具的检查（inspect）功能
- 实现 把一个盒子从一个区域拖放到另一个指定区域中
  盒子一部分在区域内，一部分在区域外，该如何处理
  简述几个封装好的关键方法
- 开发完的项目，在微信浏览器上白屏，该如何排查
- 如何统计一个页面上哪些区域用户点击次数最多
- 如何根据按钮级别的粒度，设计用户权限，例如：A 可以访问按钮，B 不可以
- 如何对一个网页内容进行自动化截屏，如何解决登录限制
- http 状态 301，302， 304,缓存相关字段
- cookie、ws 是否跨域
- 触发 bfc 的方式
- rem 和 vw 的使用场景
- 伪代码实现下懒加载
- 实现一下 some, every
- flatten 实现
- 函数组件怎么阻止重复渲染
- AST 作用 or babel 实现原理
- 实现自定义 hooks,usePrevious。setcount(count => count + 1)后输出上一次 count 的值
- 不同域名共享 cookie
- on, emit, 实现
- 输入 url 到页面返回结果
- 缓存的实现方式
- webpack 分包
- Webpack 插件，生命周期
- umi 约定式路由怎么实现的
- babel 实现远原理
- webpack 拆包的依据。1.被多个模块使用，cache 起来 2.资源过大
- canvas 点击线段事件。重合区域怎么处理
- webWorker 的使用：为什么不在 worker 里面发出请求，做数据转换呢？
- generate 函数和 async 区别
- webpack 插件实现
- 父子组件的 mounted 调用顺序
- $nextTick 实现原理
- 子元素水平垂直居中
- 斐波那契数列如何优化
- 业务题：封装一个全局的弹窗，在任何组件内都可以调用。追加：如何同时打开 5 个弹窗，关闭顺序又如何
- 封装 Vue 插件
- 5 个弹窗
- 手机号码分割 150-7602-7889
- 最大字符串数， “abcdabcda” 求最长的不重复字符串
- 不同域名如何共享 cookie
- 前端工程化，webpack, babel, Node 等。
- 精通框架源码
- 可视化，3D 方向
- 流媒体，音视频
- Koa 的中间件原理，介绍一下 compose 函数
- 介绍 NodeJS 的 EventLoop 机制，process.nextTick() 的作用
- NodeJS 是单线程还是多线程，都有哪些线程，JS 为什么是单线程的
- CommonJS 的实现原理
- NodeJS 中存在哪些流，怎么理解 pipe() 及其优点
- require 的解析规则
- 介绍一下负载均衡，NodeJS 的 cluster 和 child_process 是什么
- webpack 是如何进行打包的
- webpack 动态 import 是如何实现的
- 如何编写自己的 loader 和 plugin
- 简述 webpack 配置文件中的 externals，UMD 了解吗
- HTTP 首部（Header）和实体（Body）的分隔符是什么，用正则如何匹配
- HTTPS 的详细过程，什么是数字证书，消息摘要，非对称加密，Hash 算法
- 如何实现 Tab（标签）页之间，客户端与服务器的实时通讯
- HTTP 状态码：301、302、307 的区别
- 简述浏览器的垃圾回收机制，什么是强引用、弱引用、循环引用
- 简述 requestAnimationFrame 和 requestIdleCallback 的作用
- CSS 选择器的解析顺序是从右到左，还是从左到右，为什么
- click 事件在移动端有什么问题，如何解决，你在移动端还遇到那些坑
- 简述 JWT 的生成过程和优缺点，怎么主动注销 JWT 和续签 JWT
- 通过什么检测网站的性能，有哪些指标
- 如何查看网站的 Ajax 请求是由哪行代码发出的，一个元素都绑定了哪些事件，Chrome 调试面板 F8,F10,F11 各代表什么
- 说说你对 jpg、gif、jpeg、png、webp、base64 URL 的了解
- 实现 F12 开发者工具的检查（inspect）功能
- 实现 把一个盒子从一个区域拖放到另一个指定区域中
- 盒子一部分在区域内，一部分在区域外，该如何处理
- 开发完的项目，在微信浏览器上白屏，该如何排查
- 如何统计一个页面上哪些区域用户点击次数最多
- 如何根据按钮级别的粒度，设计用户权限，例如：A 可以访问按钮，B 不可以
- 如何对一个网页内容进行自动化截屏，如何解决登录限制
- Koa 的中间件原理，介绍一下 compose 函数
- 介绍 NodeJS 的 EventLoop 机制，process.nextTick() 的作用
- NodeJS 是单线程还是多线程，都有哪些线程，JS 为什么是单线程的
- CommonJS 的实现原理
- NodeJS 中存在哪些流，怎么理解 pipe() 及其优点
- require 的解析规则
- 介绍一下负载均衡，NodeJS 的 cluster 和 child_process 是什么
- webpack 是如何进行打包的
- webpack 动态 import 是如何实现的
- 如何编写自己的 loader 和 plugin
- 简述 webpack 配置文件中的 externals，UMD 了解吗
- HTTP 首部（Header）和实体（Body）的分隔符是什么，用正则如何匹配
- HTTPS 的详细过程，什么是数字证书，消息摘要，非对称加密，Hash 算法
- 如何实现 Tab（标签）页之间，客户端与服务器的实时通讯
- HTTP 状态码：301、302、307 的区别
- 简述浏览器的垃圾回收机制，什么是强引用、弱引用、循环引用
- 简述 requestAnimationFrame 和 requestIdleCallback 的作用
- CSS 选择器的解析顺序是从右到左，还是从左到右，为什么
- click 事件在移动端有什么问题，如何解决，你在移动端还遇到那些坑
- 简述 JWT 的生成过程和优缺点，怎么主动注销 JWT 和续签 JWT
- 通过什么检测网站的性能，有哪些指标
- 如何查看网站的 Ajax 请求是由哪行代码发出的，一个元素都绑定了哪些事件，Chrome 调试面板 F8,F10,F11 各代表什么
- 说说你对 jpg、gif、jpeg、png、webp、base64 URL 的了解
- webpack 如何拆分大文件？
- webpack 打包的过程?
- webpack 的基本配置？
- 手写冒泡排序？
- 给定两组数，分别以链表方式存储，求和？注意进位
- 数组去重？
- 解释 TCP/IP 的三次握手和四次挥手？
- 解释跨域问题以及前端常用的解决方案？
- CORS 的细节，哪些是简单请求？哪些是非简单请求？
- 浏览器的渲染原理是一定会被问到的？
- 浏览器输入一个 url 之后的过程，以及过程中应用了哪些缓存，如何优化？
- script 标签和 link 标签的先后顺序对页面加载的影响？
- async 和 defer 的区别？
- 输入 url 到页面展示
- 浏览器存储
- 如何实现继承
- 跨域，常用哪个，解释一下
- 缓存
- 如果列表组件要新增一些内容，例如标题，简介等，你会怎么对代码进行修改（容器组件 -> 展示组件）
- csrf 和 xss
- flex
- 判断是否为数组
- typeof arr === 'object'
- 浏览器事件循环，node 事件循环
- webpack 流程，插件
- koa 源码
- koa 洋葱模型
- mobx 原理
- 首屏优化
- async/await Promise
- 盒模型
- babel 原理
- Taro 原理
- react 中 props 和 state 的区别
- 组件怎么拿到 redux 的数据
- 水平垂直居中
- 给你一个 DOM 元素，用 CSS 的方式让他呈现两色的效果，只能有一个 DOM 元素
- 一个数组只有 1 和 2，排序，1 在前面，2 在后面
- JS 的事件模型，捕获和冒泡，阻止冒泡
- preventDefault 和 stopPropagation 区别
- http 缓存
- https
- 跨域
- 前端有哪些优化
- 浏览器兼容性
- react 的事件绑定和原生的有什么区别
- 一个数组，有很多数字存在两次，只有一个数字存在一次，怎么找出这个数字，我说异或，他问我如果有两个不同的怎么办？
- 关于前端性能优化有什么相关的经验或者知识吗
- reflow 和 repaint 有什么区别
- 关于前端跨域请求通常是怎么做的
- 关于 iframe 内部和外部变量的读取是怎么进行的
- xss 和 csrf 了解吗
- 能介绍下常用的排序算法和他们的区别吗
- 能在刚才页面实现个 javascript 的冒泡排序吗
- 如果让你设计一些测试输入来验证这个排序函数 你会怎么设计
- 前端防连击 throttle 和 debounce
- 继承
- HTTP 缓存
- 输入 URL 到页面发生了什么
- prototype、_proto_、constructor 的区别
- 拼接数组
- 判断数组
- 复制数组
- JSONP
- Ajax 原理
- 水平垂直居中
- 左侧定宽、右侧自适应的两栏布局
- BFC 特性
- HTTPS
- ES6 generator、async、await 了解吗
- 盒模型，bfc
- float，清除浮动
- 请解释一下 CSS3 的 Flexbox（弹性盒布局模型）,以及适用场景？
- JavaScript 原型，原型链 ? 有什么特点？
- Javascript 如何实现继承？ 构造函数继承，非构造函数继承
- Javascript 作用链域?
- 什么是闭包（closure），为什么要用它？
- .call() 和 .apply() 的含义和区别？
- 实现一个 bind
- 什么是跨域，如何解决？ jsonp cors ，jsonp 原理
- promise 的原理和事件循环
- amd，cmd 规范
- 用户页面打开很慢，有哪些优化方式？
- react 的虚拟 dom 了解多少？这种类型的框架和传统的 jq 操作 dom 的优势？ diff 算法？说了一下虚拟 dom 如何实现，diff 算法做了什么优化
- 请求头包含哪些部分
- 服务端渲染？ 答，个人认为服务端渲染的好处在与首屏加载速度和利于 seo，但是目前网络环境下，首屏加载速度没有太多差别，hybrid App 首页一般都是原生的，很少会有白屏，客户端渲染还可以减少服务端的压力
- webpack 打包？ 讲了一下打包过程，loader，和 plugin 如何起作用的
- 盒模型
- 垂直居中方法
- 三栏布局
- 选择器权重计算方式
- 清除浮动的方法
- flex
- 什么是 BFC、可以解决哪些问题
- 如何实现一个自适应的正方形
- 如何用 css 实现一个三角形
- 深拷贝
- 数组去重、数组乱序
- 手写 call、apply、bind
- 继承（ES5/ES6）
- 实现 promise.retry
- 将一个同步 callback 包装成 promise 形式
- 写一个函数，可以控制最大并发数
- jsonp 的实现
- eventEmitter(emit,on,off,once)
- 实现 new
- 实现数组 flat、filter 等方法
- lazyMan
- 函数 currying
- 变量的结构赋值
- promise、async await、Generator 的区别
- ES6 的继承与 ES5 相比有什么不同
- js 模块化（commonjs/AMD/CMD/ES6）
- 从输入 URL 到呈现页面过程
- 强缓存、协商缓存、CDN 缓存
- HTTP2
- HTTP 状态码
- 三次握手与四次挥手
- 跨域（JSONP/CORS）
- 跨域时如何处理 cookie
- 垃圾回收机制
- https
- 什么是 xss，如何预防
- 什么是 csrf，如何预防
- 为什么会造成 csrf 攻击
- watch 与 computed 的区别
- vue 生命周期及对应的行为
- vue 父子组件生命周期执行顺序
- 组件间通讯方法
- 如何实现一个指令
- vue.nextTick 实现原理
- diff 算法
- 如何做到的双向绑定
- 如何设计一个组件
- 用过哪些 loader 和 plugin
- loader 的执行顺序为什么是后写的先执行
- webpack 配置优化
- webpack 打包优化（happypack、dll）
- plugin 与 loader 的区别
- webpack 执行的过程
- 如何编写一个 loader、plugin
- tree-shaking 作用，如何才能生效
- 首屏加载如何优化
- 一个网页从请求到呈现花了很长时间，如何排查### **CSS**
- 盒模型
- 垂直居中方法
- 三栏布局
- 选择器权重计算方式
- 清除浮动的方法
- flex
- 什么是 BFC、可以解决哪些问题
- 如何实现一个自适应的正方形
- 如何用 css 实现一个三角形
- 深拷贝
- 数组去重、数组乱序
- 手写 call、apply、bind
- 继承（ES5/ES6）
- 实现 promise.retry
- 将一个同步 callback 包装成 promise 形式
- 写一个函数，可以控制最大并发数
- jsonp 的实现
- eventEmitter(emit,on,off,once)
- 实现 new
- 实现数组 flat、filter 等方法
- lazyMan
- 函数 currying
- promise、async await、Generator 的区别
- ES6 的继承与 ES5 相比有什么不同
- js 模块化（commonjs/AMD/CMD/ES6）
- 从输入 URL 到呈现页面过程
- 强缓存、协商缓存、CDN 缓存
- HTTP2
- HTTP 状态码
- 三次握手与四次挥手
- 跨域（JSONP/CORS）
- 跨域时如何处理 cookie
- 垃圾回收机制
- https
- 什么是 xss，如何预防
- 什么是 csrf，如何预防
- 为什么会造成 csrf 攻击
- 事件循环
  事件循环绝对是一个必考题。其中涉及到宏任务、微任务、UI 渲染等的执行顺序，浏览器端的必须要掌握，node 端的有精力的最好也能掌握。
- watch 与 computed 的区别
- vue 生命周期及对应的行为
- vue 父子组件生命周期执行顺序
- 组件间通讯方法
- 如何实现一个指令
- vue.nextTick 实现原理
- diff 算法
- 如何做到的双向绑定
- 虚拟 dom 为什么快
- 如何设计一个组件
- 用过哪些 loader 和 plugin
- loader 的执行顺序为什么是后写的先执行
- webpack 配置优化
- webpack 打包优化（happypack、dll）
- plugin 与 loader 的区别
- webpack 执行的过程
- 如何编写一个 loader、plugin
- tree-shaking 作用，如何才能生效
- 首屏加载如何优化
- 一个网页从请求到呈现花了很长时间，如何排查
- CSS 动画和 Js 动画的区别
- 如何实现精确的 setInterval?
- 讲讲对函数式编程的理解
- 页面发了个请求，请求没返回用户就切去另一个页面了，这会有什么影响，怎么处理？fetch 请求怎么取消？
- 讲讲 ES6 的 Reflect 特性
- 讲讲 Promise 和 Rxjs 的区别
- switchMap 运算符是做什么的
- 如何实现一个全局单例(答工厂模式，又问工厂模式和全局直接挂载对象有什么区别，当时没想到，工厂模式是第一次用时才生成实例的)
- Vue 里数组是怎么实现响应式的
- vue 计算属性原理和特点，问怎么实现的缓存避免重复计算的(卡壳了，我说是 computedWatcher 被通知更新时可能可以查看依赖，后来面试官告诉我是依赖时候更新时会修改标记位，响应式的重点是【被动】)
- this 的是如何确定指向的
- call，apply, bind 的区别
- bind 怎么实现 call
- VUE 双向绑定原理 eventloop 原理 原型链原理
- VueRouter 的原理你能不能说一下呢？(两种路由方式说了一下)
- 对于 History 路由而言，你觉得在服务端是如何做路由分发的呢？(愣住，面试官接下来跟我解释了一波)
- 你说你看过 Vue 源码，能不能介绍一下 Vuex 的 Mutation 和 Action 的区别吗？(mutation 做同步操作，action 一般用于异步)
- 为什么要设计出 Mutation 和 Action 这两个东西？(我开始不是很清楚，扯到 Redux，和面试官交流后，一致同意 Action 作为业务逻辑的封装更合适，提供了更大的自由度)
- 进程和线程的区别(解释了一波，顺便把 Chrome 为什么从单进程转成多进程架构说了一下)
- 知道哪些进程间通信(IPC)的方式？ (主从式、会话式、消息-邮箱机制、管道、共享内存、Unix Domain Socket，然后跟他讲我看过 Chromium IPC 的源码，内核里面把以前的 ChannelPosix 换成了 ChannelMojo，从而达到线程安全的目的，顺便解释了下线程安全，面试官表示很欣赏，说这个都看过，看来你学了不少)
- ES5 写一个数组去重(刚开始写了一个 O(n^2)时间的) 能不能优化？ (我问能不能用新空间，他说可以，然后写了一个 O(n)时间的)
- 能不能区别开数字和字符串？(想了想，最后还是用 indexOf 方式，最优的没想出来，面完猛然想出来了，当时脑子有点乱)
- 讲一讲 HTTPS 加密(对称加密有 AES + CHACHA20, 分组模式以前有 CBC、CTR，TLS1.3 中只剩下 GCM，非对称加密 RSA、ECDHE)
- 怎么握手的呢？(讲了三个版本：传统 RSA、TLS1.2、TLS1.3, 后面也讲了 TLS1.3 的 Session ID、Session Ticket 以及 PSK)
- HTTPS 如何保证数据是否被篡改？(说了下有签名的过程)
- 签名是什么原理(私钥加密，公钥解密，比对哈希摘要)
- 你知道哪些哈希摘要算法(Sha256, Sha384)
- 你能不能介绍一下你的项目(说了下项目遇到的挑战，说了这几点: 1. 怎么解决闭包陷阱。2. 通过 EventLoop 解决 transform 失效的问题)
- 能不能说说你对 EventLoop 的理解(宏任务-微任务-UI 渲染)
- 如果要在 UI 渲染之前做一些事情你会怎么办？(我会启动微任务执行吧)
- requestAnimationFrame 在 EventLoop 中是一个什么位置？(给他解释显示器和浏览器的 Vsync 信号，然后 rAF 首先执行，他貌似不满意，我请教了他一下，给我解释实际上 rAF 会在 UI 渲染之前)
- 分离图层做动画有什么好处呢？(给他讲了分层的原理，通过设置 CSS 的 will-change 可以转换为一个图层，调用 GPU 加速)
- 分离图层会发生重绘吗？(会)那既然重绘，它的好处在哪里？(不会影响其他的图层)
- 你觉得你哪些技术比较厉害？(Vue 源码，浏览器，服务端渲染)
- 你说你看过 Vue 的源码，能不能说说 computed 属性为什么能够在依赖改变的时候，自己发生变化？(我说 computed 和 watch 公用一个 Watcher 类，在 computed 的情况下有一个 dep 收集依赖，从而达到更新 computed 属性的效果，顺便跟他讲了 computed Watcher 如何跟渲染 Watcher 关联，以及 Vue 在二次收集依赖时用 cleanupDeps 卸载一些无用的 dep)
- 你觉得你的优势是什么？(1.深度思考的能力 2.善于分享 3.社区影响力)
- 你对 webpack 了解多少？(我说了下 webpack 的一些优化手段，打包时间方面，预编译、缓存、缩小构建目标，说了大概十个插件，然后打包体积上，JS 和 CSS 的 Tree-Shaking 怎么配置)
- 你觉得 CommonJS 为什么不能做 Tree-Shaking ?
- ESModule 既然是编译时加载，那它可以做到运行时加载吗，想过这个问题吗？(愣了一会，说 webpack 有动态 import 的方式)
- 写过 loader 和 plugin 吗？(实话实说，没有)那你知道两者有什么差异吗？(先 loader 后 plugin)
- 你对未来的发展是如何规划的？(谈了谈我对五级工程师的看法，我的阶段目标是到达最低的第五级)
- 你觉得你在专业上的目标是怎样的？(成为领域前 20%)- ES5 写一个数组去重(刚开始写了一个 O(n^2)时间的)
- 浏览器兼容性问题
  **因为我的工作主要还在专注在 web 端，所以浏览器兼容性的问题没有少碰到过，因主要是兼容 IE8 以上以及其他各个浏览器，这个就当做总结一下吧(在被问到这一块的时候其实我是有加分的，因为回答的比较多 2333)**
  - 使用 meta 标签来调节浏览器的渲染方式，告诉浏览器用哪种内核渲染，360 双核浏览器就是在 ie 和 chrome 之间来回切换，现在使用 meta 标签来强制使用最新的内核渲染页面
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  - rgba 不支持 IE8 **解决：用 opacity**
  - CSS3 前缀
    -webkit- webkit 渲染引擎 chrome/safari
    -moz gecko 引擎 firefox
    -ms- trident 渲染引擎 IE
    -o- opeck 渲染引擎 opera
  - 过渡不兼容 IE8，可以用 JS 动画实现
  - background-size 不支持 IE8，可以用 img
  - 使用 PIE.htc 让 IE6/7/8 支持 CSS3 部分属性，像 CSS3 的 border-radius，box-shadow，css backgrounds(-pie-background),Gradients,RGBA 属性
    .border-radius {border-radius: 10px;-webkit-border-radius: 10px;-moz-border-radius: 10px;background: #abcdef;behavior: url(css/PIE.htc);}
  - 用 css hack
    IE6: \_IE7/7: \*IE7/Firefox: !importantIE7: \*+IE6/7/8: 9IE8:
  - \:IE 浮动 margin 产生的双倍距离,通常使用 float\:left 来实现，浏览器存在兼容性问题，导致图片与 后面的内容存在 margin 不一致的问题，解决方法就是给图片添加 diaplay\:inline 即可
  - ie8 不支持 nth-child，但支持 first-child 和 last-child，可以通过转化写法来处理问题，span\:nth-child(2)可以转换为 span\:first-child+span,可以使 ie8 显示该内容，last-child 可以自定义一个 class 类兼容 ie8 写法
  - IE8 下不支持 HTML5 属性 placeholder，解决问题的 js 插件挺多的，常用的使用 jquery.JPlaceholder.js 插件处理问题
  - 识别 HTML5 元素，IE 中可能无法识别 nav/footer，使用 html5shiv
  - 火狐下表单阻止表单默认提交事件：在 form 中添加 action="javascript:",秒杀上述所有默认行为;
  - 始终为按钮 button 添加 type 属性，IE 下的默认类型是 button，其他浏览器下的默认类型是 submit
  - IE 下删除所有不必要的 console 语句，IE 下当遇到 console 时不识别之后报错，代码不会执行，或者全局自定义一个 window\.console 方法
  - IE 浏览器下由于参数过长导致通过 GET 请求下载文件方法报错，解决改为 POST 请求
  - IE 浏览器下 iframe 弹窗中输入框光标丢失（无法输入）问题，解决清一下 frame
  - 兼容 IE8 new Date()返回 NaN 问题，解决自定义方法
    function parseISO8601(dateStringInRange) {var isoExp = /^s\*(d{4})-(dd)-(dd)s\*\$/, date = new Date(NaN), month, parts = isoExp.exec(dateStringInRange);if(parts) { month = +parts\[2]; date.setFullYear(parts\[1], month - 1, parts\[3]); if(month != date.getMonth() + 1) { date.setTime(NaN); }}return date;}
- 跨端的原理？我讲了几个例子：taro、uni-app，顺便提了 flutter、react native、小程序等的架构，具体怎么设计的。
- 动态表单能够运用在什么场景？我举了 7、8 个例子。
- 移动端适配相关的问题，应用场景。
- react 与 vue 的技术栈对比，说下区别
- B 端遇到的最复杂的数据结构是什么
- 数据展示的优化、数据截取和处理
- 实际场景中，哪些地方应用到了堆、链表、多叉树结构
- es6 及 es6+ 的能力集，你最常用的，这其中最有用的，都解决了什么问题。
- GC 相关问题：es6+ ，eventloop 中涉及 GC 的部分。
- 数组 flat 展开的各种解法，数组 map 应用
- 讲下 V8 sort 的大概思路
- Promise 并发限制
- 省市区拼接查字段，要求 O(n) 内解出
- 中台的理解
- node 限流算法
- 你提到性能指标，能说说都是怎么计算的吗？比如 LCP，FID
- input type 都有哪些类型，还记得其他 attrs 呢
- css 的伪类和伪元素有哪些？有什么区别？
- 在一个未知宽度的父元素内如何创建一个等边正方形
- 异步加载 js 会阻塞什么
- vue 和 react 的异同
- 如何优化 vue 框架，注意是优化框架
- id key 真的能使列表比对更高效吗？举个反例？
- webpack 优化的手段
- tree-shaking 怎么配置，如何 **避免** tree-shaking？
- electron 和小程序遇到什么坑？
- 说下微信自动化测试
- es2015 到 es2020 的新特性，你最常用什么，给你收益最大的。
- weakMap 和 Map 的区别，weakMap 原理，为什么能被 GC？
- 如何干扰 GC ？
- webpack import 动态加载原理
- 知道 webpack 中的 devTool 吗？
- 如何进行错误定位和数据上报，线上异常的处理
- 为什么有时候配置了 webpack caching，chunk 还是更新了？
- 讲讲浏览器和 node 的 eventloop
- 微任务后面还有哪些？requestAnimationFrame 是怎么调用的？requestAnimationFrame 帧内总是有任务吗？分情况说下。
- 帧数怎么计算？
- 了解网络安全吗？
- 如何避免数据被 iframe 截获
- 说下状态码
- 说下 304，什么情况会 304？协商缓存的头部字段？
- 工程化实践的看法
- 项目是如何收集问题的，用户量如何？
- 性能问题如何排查，你们项目的指标，具体数据、截图发给我看看……
- 模块化是怎么实施的？
- 目录结构讲下
- 一些功能是自研还是使用第三方工具，叫什么名字，怎么使用 ？
- 疯狂问测试相关的内容，单元测试和组件测试是怎么做的、代码覆盖率多少，如何权衡测试原则，系统测试相关的内容，一些细节上的问题怎么处理，等等，要说出个 1、2、3 来 ？
- 项目亮点/难点，怎么解决 ？
- 复盘，整个项目总结，让你重新设计这套系统你会怎么做 ？
- 工程化实践和深入的一个点
- 团队氛围，有什么好的点可以说下，有什么不好的点也说下……
- 中台具体集成了什么功能 ？你都做了什么 ？
- 你是如何进行技术突破的，又是如何学习的 ？
- webpack 提高构建速度的方式
- loader 输入什么产出什么 ？
- webpack 原理
- webpack 动态加载的原理
- webpack 热更新
- 如何写一个 webpack plugin
- AST 的应用
- 如何解析一个 html 文本，还是考 AST
- babel 原理，怎么写 babel 插件
- 小程序的 API 做了什么处理，能够做到全局变量的隐藏，如果是你，怎么设计 ？
- 基础题考闭包的，我讲对了思路，结果没做对。
- 实现颜色转换 'rgb(255, 255, 255)' -> '#FFFFFF' 的多种思路。
- 提供一个数字 n，生成一组 0\~n-1 的整数，打乱顺序组成数组，打乱几次，如何能够看起来平衡，说出你能想到的所有方法。
- 监控体系
- 虚拟 dom 有什么好的地方？框架为什么要设计虚拟 dom？
- webpack 的缺点，让你设计一个新的构建打包工具，你会怎么设计？
- 在线文档编辑，如何处理两人的冲突，如何展示，考虑各种场景
- excel 文档冲突高级处理，文章冲突呢？是上个问题的深化。
- 了解哪些排序算法，说说冒泡排序和快排的区别
- 背包问题
- 浏览器缓存
- 输入一串 url 到浏览器，会发生什么？
- vm.$set 原理
- 深拷贝如何解决循环引用
- http 缓存头部字段
- vue 和 react 的区别
- 讲讲前端路由
- 一道查找路径的场景题
- 一道如何优雅处理异步的场景题
- webpack 工作流
- webpack 是如何解决两次引入的
- 讲讲 http 三次握手，为什么需要三次握手
- 讲讲 http 四次挥手，为什么需要四次而不是三次
- 如何看待 toc tob 端业务
- 对于新技术如何看待
- 小程序有了解过吗
- 在小组担任的位置
- 说说你工作中遇到有挑战的项目
- 数据库范式
- 布局的几种方式
- rem vw 的区别
- rem em 的区别
- webpack 你是如何做优化的
- 浏览器缓存
- vue 如何做权限检验
- 讲讲 http2.0
- 单元测试如何测试，代码覆盖率如何
- Koa 中间件原理
- Koa 如何实现监控处理
- commonjs 的实现原理
- 讲讲垃圾回收机制
- Vue 和 React 的区别
- 函数式编程 如何理解纯函数
- Node 原生 api 错误处理有了解吗
- 说说浏览器渲染流程
- 说说那些属性可以直接避免重绘和重排
- treeshaking 原理
- 按需加载的原理
- 讲讲原型链
- 了解过那些前端构建工具 分别介绍他 webpack rollup gulp
- 双向数据绑定原理
- 说 vue 如何收集依赖的
- 组件库设计有什么原则？
- 组件库是自己从 0 开始搭的吗，说说有哪些特点
- 如何实现组件库按需加载
- 讲讲 http2.0
- 讲讲 ts 中 type 和 interface 的区别
- 说说 http
- 说说 vue 双向绑定
- diff 算法
- http 缓存
- 讲讲 http2.0
- 说说状态逻辑复用问题
- 介绍下项目的亮点
- 介绍下 es6 新增了哪些特性
- Reflect 的用途？
- 域名切片
- 为什么 vue 或者 react 要求 key 值唯一
- MVVM 实现
- data 里面为什么是函数
- UDP TCP 区别
- vuex 应用场景
- 说说 XSS 攻击
- 说说 vue 的模板编译
- 说说你项目的亮点
- new 原理实现
- 状态码 403 404 503 304 说说
- diff 算法
- 说说事件循环
- 浏览器缓存
- nextTick 原理
- 说说你的 vuex 持久化插件
- 内联元素与块级元素
- dom 操作有哪些 api
- 数组去重有哪几种方式
- 柯里化问题
- 数字转金额的问题
- 判断变量的几种方式，有哪些不同
- 块级作用域和函数作用域
- call bind new 实现原理
- vue 双向绑定原理
- LRU 算法
- http2.0 的有哪些内容
- http 缓存
- rem vw 区别
- 移动 1px 问题
- 函数柯里化
- diff 算法
- nextTick 原理
- 事件循环
- 如何解决移动端 click300ms 延迟？
- vue 有哪些全局组件
- 移动端如何完成拖拽功能？
- 一道逻辑题：有 5L 的桶和 3L 的桶，如何拿到 4L 的水
- 居中的几种方案
- 事件循环
- 移动 1px
- setTimeout 与 rAF
- flex:1
- 介绍下你写的库
- 发布订阅和观察者的区别
- 单例模式
- 发布订阅和观察者的区别
- JSONP 实现原理
- 移动端点击延迟怎么处理
- git flow 工作流介绍
- 性能监控如何做
- 跨域解决方案
- 简单请求和复杂请求
- 多路复用
- git flow 工作流介绍
- 如何进行 code review
- 平时怎么学习
- 组件库相关问题
- 项目自己搭的？如何支持 treeshaking
- 如何做版本号管理
- less 样式如何做按需加载
- webpack 项目如何优化
- ts 泛型
- 怎么通过实例拿到构造函数
- extend 原理
- Object.create 原理
- 虚拟列表原理
- 浏览器缓存原理
- 什么 csrf 攻击
- csrftoken 怎么获取，存到哪里
- 并发调度手写题
- 权限页面的细节：
  - 各个模块、按钮怎么设计权限；
  - 分角色、分地域怎么设计？
  - 要加个表头，还要控制展示的顺序，在各个浏览器表现一致，怎么设计？说出所有方案，想到什么自由发挥了……
  - 聊到本地存储，问：localStorage 在各浏览器、移动端浏览器的 size 一致吗？
    其他：
  - 这一段是我简历的项目，略过……
  - 继续聊阿里的产品，简单使用后，请提出几个可以优化的地方？
  - 啥也没透露，让你预测下这款产品的接下来的方向，如果是你，你会着手哪个方向，并且凭啥让你来干，说下你擅长的……
  - 正式讨论产品，大家都在做什么，团队协作的情况，公布接下来的迭代方向，针对的人群，目标……
- 题一
  - 1.计算多个区间的交集
  - 区间用长度为 2 的数字数组表示，如[2, 5]表示区间 2 到 5（包括 2 和 5）；
  - 区间不限定方向，如[5, 2]等同于[2, 5]；
  - 实现`getIntersection 函数`
  - 可接收多个区间，并返回所有区间的交集（用区间表示），如空集用 null 表示
  - 示例：
  - getIntersection([5, 2], [4, 9], [3, 6]); // [4, 5]
  - getIntersection([1, 7], [8, 9]); // null
- 题二：

  - 2.DOM 的体积过大会影响页面性能，假如你想在用户关闭页面时统计（计算并反馈给服务器）
    当前页面中元素节点的数量总和、元素节点的最大嵌套深度以及最大子元素个数，请用 JS 配合
    原生 DOM API 实现该需求（不用考虑陈旧浏览器以及在现代浏览器中的兼容性，可以使用任意
    浏览器的最新特性；不用考虑 shadow DOM）。比如在如下页面中运行后：
    ```html
    <html>
      &lt;head&gt;&lt;/head&gt; &lt;body&gt;
      <div>
        <span>f</span>
        <span>o</span>
        <span>o</span>
      </div>
      &lt;/body&gt;
    </html>
    // 会输出：
    ```

  {
  totalElementsCount: 7,
  maxDOMTreeDepth: 4,
  maxChildrenCount: 3
  }

  ```

  ```

- 题三
  // 3.请使用原生代码实现一个 Events 模块，可以实现自定义事件的订阅、触发、移除功能
  const fn1 = (... args)=>console.log('I want sleep1', ... args)
  const fn2 = (... args)=>console.log('I want sleep2', ... args)
  const event = new Events();
  event.on('sleep', fn1, 1, 2, 3);
  event.on('sleep', fn2, 1, 2, 3);
  event.fire('sleep', 4, 5, 6);
  // I want sleep1 1 2 3 4 5 6
  // I want sleep2 1 2 3 4 5 6
  event.off('sleep', fn1);
  event.once('sleep', ()=>console.log('I want sleep));
  event.fire('sleep');
- 跨端的原理？我讲了几个例子：taro、uni-app，顺便提了 flutter、react native、小程序等的架构，具体怎么设计的。
- 动态表单能够运用在什么场景？我举了 7、8 个例子。
- 移动端适配相关的问题，应用场景。
- 我公司的业务讨论，是否了解过竞品等等，这里略过。
- 对于你项目的竞品有了解吗？说一下
- 你的项目与竞品相比，好在哪里，有什么优势？
- 下班后都在做什么，问的都是过往经历，问的太详细了，让人不舒服。
- 如果与同事发生了意见的不一致，你会如何解决呢
- 现在针对我们的业务，急需增加一个新的模块位置，你会怎么设计？数据怎么展示……
- react 与 vue 的技术栈对比，说下区别
- B 端遇到的最复杂的数据结构是什么
- 快速实现 [1, 2, ...100]，所有你能想到的解
- 数据展示的优化、数据截取和处理
- 实际场景中，哪些地方应用到了堆、链表、多叉树结构
- es6 及 es6+ 的能力集，你最常用的，这其中最有用的，都解决了什么问题。
- GC 相关问题：es6+ ，eventloop 中涉及 GC 的部分。
- 数组 flat 展开的各种解法，数组 map 应用
- 讲下 V8 sort 的大概思路
- Promise 并发限制
- 省市区拼接查字段，要求 O(n) 内解出
- node 限流算法
- 你提到性能指标，能说说都是怎么计算的吗？比如 LCP，FID
- 算法题：**数组全排列**[1]
- 中台业务讨论
- input type 都有哪些类型，还记得其他 attrs 呢
- css 的伪类和伪元素有哪些？有什么区别？
- 在一个未知宽度的父元素内如何创建一个等边正方形
- 异步加载 js 会阻塞什么
- vue 和 react 的异同
- 如何优化 vue 框架，注意是优化框架
- vue 和 react 的 jsx 使用
- id key 真的能使列表比对更高效吗？举个反例？
- webpack 优化的手段
- tree-shaking 怎么配置，如何 **避免** tree-shaking？
- electron 和小程序遇到什么坑？
- 说下微信自动化测试
- es2015 到 es2020 的新特性，你最常用什么，给你收益最大的。
- weakMap 和 Map 的区别，weakMap 原理，为什么能被 GC？
- 如何干扰 GC ？
- webpack import 动态加载原理
- 知道 webpack 中的 devTool 吗？
- 如何进行错误定位和数据上报，线上异常的处理
- 为什么有时候配置了 webpack caching，chunk 还是更新了？
- 讲讲浏览器和 node 的 eventloop
- 微任务后面还有哪些？requestAnimationFrame 是怎么调用的？requestAnimationFrame 帧内总是有任务吗？分情况说下。
- 帧数怎么计算？
- 了解网络安全吗？
- 如何避免数据被 iframe 截获
- 说下状态码
- 说下 304，什么情况会 304？协商缓存的头部字段？
- 工程化实践的看法
- 项目是如何收集问题的，用户量如何？
- 性能问题如何排查，你们项目的指标，具体数据、截图发给我看看……
- 模块化是怎么实施的？
- 目录结构讲下
- 一些功能是自研还是使用第三方工具，叫什么名字，怎么使用 ？
- 疯狂问测试相关的内容，单元测试和组件测试是怎么做的、代码覆盖率多少，如何权衡测试原则，系统测试相关的内容，一些细节上的问题怎么处理，等等，要说出个 1、2、3 来 ？
- 项目亮点/难点，怎么解决 ？
- 复盘，整个项目总结，让你重新设计这套系统你会怎么做 ？
- 工程化实践和深入的一个点
- 团队氛围，有什么好的点可以说下，有什么不好的点也说下……
- 中台具体集成了什么功能 ？你都做了什么 ？
- 你是如何进行技术突破的，又是如何学习的 ？
- 对未来的规划
- 有什么问题想问？我随便问了几个问题过渡，然后抛出最重要的一个，厚着脸皮让大佬指出我的问题（PS：这是我面试的目的之一，当时几个面试进度属猎豹最快了。别人眼中的我，在前端方面具体是怎样的感官 ？我一直很好奇。不是每个人都有一个对自己清晰的认识的，既然自己想不出来，那就通过面试吧）。
- webpack 提高构建速度的方式
- loader 输入什么产出什么 ？
- webpack 原理
- webpack 动态加载的原理
- webpack 热更新
- 如何写一个 webpack plugin
- AST 的应用
- 如何解析一个 html 文本，还是考 AST
- babel 原理，怎么写 babel 插件
- 小程序的 API 做了什么处理，能够做到全局变量的隐藏，如果是你，怎么设计 ？
- 基础题考闭包的，我讲对了思路，结果没做对。
- 实现颜色转换 'rgb(255, 255, 255)' -> '#FFFFFF' 的多种思路。
- 提供一个数字 n，生成一组 0\~n-1 的整数，打乱顺序组成数组，打乱几次，如何能够看起来平衡，说出你能想到的所有方法。
- **leetcode 239**
- 监控体系
- 虚拟 dom 有什么好的地方？框架为什么要设计虚拟 dom？
- webpack 的缺点，让你设计一个新的构建打包工具，你会怎么设计？
- 在线文档编辑，如何处理两人的冲突，如何展示，考虑各种场景
- excel 文档冲突高级处理，文章冲突呢？是上个问题的深化。
- 你这个文章是富文本编辑好直接放在数据库对吧？如果文章里面有不安全的标签，显示出来比较危险，你有没有做一个处理？
  1.  过滤用户输入
  2.  markdown 区域内不渲染 html 标签
- 除了标签还有什么别的安全问题？
  我答了：XSS 注入，主要是 script 标签。
- 你这个没有实现登录这一套是吧？如果我要设置登录一个月的选项，如何实现这个功能？
- cookie 和 token 的区别是什么？
- 父容器和三个子容器：ABC，B 为固定宽度，AC 宽度随父容器宽度变化。
  flex 布局：ac 设置 flex1
  float：abc 浮动，使用 calc 计算宽度，中间盒子设置 margin
- 浏览器地址栏中输入网址键入回车，会有哪些事情？
- 有个问题：你说来了 script 代码会停止渲染，其实，这个中间有三种方式，不一定都会停止，你了解这三种方式吗？

  > 浅谈 script 标签中的 async 和 defer
  >
  > 推荐的应用场景
  >
  > defer: 如果你的脚本代码依赖于页面中的 DOM 元素（文档是否解析完毕），或者被其他脚本文件依赖。
  >
  > \*\*例：\*\*评论框、代码语法高亮、polyfill.js
  >
  > async: 如果你的脚本并不关心页面中的 DOM 元素（文档是否解析完毕），并且也不会产生其他脚本需要的数据。
  >
  > \*\*例：\*\*百度统计
  >
  > 如果不太能确定的话，用 defer 总是会比 async 稳定。

  \14. 它为什么会有这三种模式？

  > 为了让开发者自己选择，可以让页面渲染更快。

  \15. 渲染是如何构造出渲染树的，做了哪些工作可以说一下吗？

  > 大概说了 DOM 树，树的结构，然后 CSS 树，把 css 的属性合成到 DOM 树上，就变成渲染树，这个树上的节点有 style 属性，根据 style 属性浏览器会对它们重排（也叫回流）和重绘，根据层级关系渲染在页面上。

  \16. 有没有有了解过流行的框架？比如 vue、react

  \17. 框架里面有一个 diff 算法，它如何去优化这个渲染的计算或者优化效率的？

  > 详解 vue 的 diff 算法，我回答成了集中读 dom，集中写 dom。

  \18. 如何尽快地定位到被改变的节点？（开放性题目）

  > diff 算法的做法是：只比较同层级的节点。
  >
  > 我回答的做法：给每个节点以数组或者哈希的形式编号，根据索引去找变化的节点，拿一些空间换时间。

  \19. 有没有试过，同样一个域名，同时的并发请求最多能到多少？

  \20. 有这些数据我们能做哪些事情？

  \21. 现在有一个变量，我想在一个方法里面去用它，但是我不想外面能够去改变它的值，比如第一次加载页面可以读到这个变量，但是这个变量之后不再被外面的业务逻辑去改动。我想一直访问，但是值一直是最初那个值，不受外界干扰。

  > const 不行，对象内的值可以修改。函数内可以修改，但是外面无法修改到里面的值。

  \22. 有没有了解过 Webpack 打包这一块？

  \23. 有没有了解过页面的首屏优化？你的 DEMO 是如何优化的？

  > 1.  缩小图片体积，放到外链引用
  >
  > 2.  不操作 dom 的 js 就使用 defer 或者 async
  >
  > 3.  使用 cdn 加速 js 加载
  >
  > 4.  使用骨架图，类似于 youtube 和知乎

  \24. 有没有抓包过？你如何跟踪某一个特定的请求？比如一个特定的 URL，你如何把有关这部分的 url 数据提取出来？

  > 计网实验课使用 wireshark 抓过包，URL、端口、IP 都应该是可以通过 filter 过滤出来的。

  \25. 有多个 Tab 标签页，都打开腾讯视频，出了问题你如何定位哪一 tab 的数据？

  > 用 Chrome 的开发者工具 Network 抓

  \26. 如果不是 HTTP 的请求报文呢？比如 FTP、WebSocket，如何在抓包的时候过滤到想要的数据？

  > 没有录自己的声音，也忘了自己在说什么。。应该是根据协议或者端口过滤吧。

  \27. TCP 如何保证数据的完整性？它有一个确认的机制，如何完成这个机制？

  > 提到了流量窗口，但是流量窗口和这个问题无关。
  >
  > 1.  数据有可能丢失：使用超时重传。
  > 2.  对数据进行编号：需要按编号接收到所有数据。
  > 3.  最后对数据使用校验和

  \28. 对于校验和有没有更深入的理解？比如它是怎么做的？

  \29. 你说的滑动窗口是用于解决什么问题的？

  > 实现可靠传输（数据按序到达）、流量控制（限速）

  \30. TCP 和 UDP 的区别是什么？

  \31. 谁的包会大一点，通常情况下？

  > 回答了 tcp，因为 udp 不保证可靠传输，再结合它的应用场景（实时直播、会议等），它发送的包应该要小一点。
  >
  > 下来查的：通常情况下不能保证说哪一个大或者小，因为业务场景不同。
  >
  > TCP 一个报文最长 65536 字节，但是一般双方会通过 MSS 最大报文长度限制，TCP 和 UDP 都要通过 IP 层。一般又通过 MTU(IP 层)进行限制。

  \32. 设计一套聊天系统，保证聊天内容有序不丢包，然后离线的时候还要能正常收发，我是采用 TCP 还是 UDP？

  > 这个问题要结合 TCP 和 UDP 的特点来答，哪些该用 UDP？哪些该用 TCP？
  >
  > 只用 TCP 会不会有性能问题？

  \33. 算法题：二分查找 2：查找指定元素的第一个和最后一个位置，给定一个按照升序排列的整数数组 nums，和一个目标值 target，找出给定目标值在数组中的开始位置和结束位置。

  > 这道题当时没跑出来，但是大致思路应该是对的，后续我有时间写一下这个题的题解（又给自己挖坑）（逃）

  \34. 有没有了解过 http2.0？3.0 呢？你觉得 2.0 有什么缺陷吗？1.1 有什么缺陷？

  \35. 了解过 quic 吗？

  > 谷歌制定的一套基于 UDP 的协议。

  \2. 你是自己写的还是网上找的框架？

  > 使用原生 JS 实现

  \3. 博客内容也是你自己写的？

  > 是的，在文章。

  \4. 你这个没有路由吗？

  > 没有，只是单纯的 display\:show 和 none

  \5. 有没有遇到什么比较难的问题吗？

  > 讲了自己使用网上的富文本 js 插件。

  \6. 你除了列表里面的这几篇文章，还写过什么别的其他的博客吗？

  > 见我的文章列表。

  \7. 看到你也去美团面试过，如果这面过了的话你会怎么选？

  > 1.  腾讯成立时间将近是美团的两倍，它平台资源也很丰富，能给我提供更好的发展机会。

  \9. 对 TCP 和 UDP 了解吗？比如具体的区别是什么？

  \10. TCP 如何保证数据可达？

  > 确认收到和超时重传。
  >
  > 它还配套了流量窗口、拥塞避免这样的协议算法。

  \11. 服务端收到了，回 ACK 包的时候客户端没收到，客户端又发了一个包，它不会重复吗？

  > 服务端拿到这个包什么也不处理，只是把之前的确认重新发送一次。

  \12. 那它怎么知道这个包是同一个包呢？

  > TCP 有对数据进行编号，从 0 到 4gb，我们假设某一个包中发送了 10 到 50 长度为 40 的数据，接收方可以比较已收到的内容 的序号和 刚刚到达的包数据的序号来判断是不是重复。

  \13. 你听说过黏包吗？

  > 没有。网络编程中的黏包现象

  \14. 有没有看过源码方面的东西？比如框架的源码之类的

  > 目前还没有看过，框架的话，我目前还只是想尽可能去熟练掌握运用的这个阶段，我觉得先把它熟练掌握再看源码是一个比较良好的过程。

  \15. 上学有学过 c++或者其他方面的吗？

  > 大一 c++，大二 java。

  \16. java 垃圾回收机制了解吗？

  > 了解一些 js 的垃圾回收机制，您问的是 java 的吧？

  \17. 那你介绍 js 的吧。

  > 1.  引用计数，这种不能清除循环引用的对象。引出了标记清除。
  > 2.  标记清除。

- 能不能说说浏览器的缓存(灵魂之问，一时想不起来了，尴尬，寻求提示)

- - cache-control 有哪些字段？设置 max-age: 0 跟浏览器缓不缓存有关系吗？s-max-age 的作用？
  - 强缓存和协商缓存的顺序

- 能不能说说 Cookie 有哪些字段？(我说了 domain、path、httpOnly、sameSite 的三种取值)

- - 还有吗？关于 https 的一个字段(擦，不知道，过吧)

- TCP 三次握手

- 你应该对 React 原理很了解吗？(我打断了，React 原理不熟，问我 Vue 吧，后来问了一个 diff 就完事了)

- - 怎么进行优化？(说了一种批量操作，别的好像忘了，他提示我 DOM 离线操作也可以)
  - 重绘和回流了解吗？

- 有没有了解过前端一些前沿的方向(说了 flutter，dart，看过你们团队的 serverless 文章)

- - 了解过 WebAssembly 吗？(没有啊)
  - 了解过 PWA ?(我个人觉得要凉，然后问我 PWA 原理是怎么样的呢？说了下大概 Service Worker 吧，不太熟)

- 介绍一下你的项目(我说了一下技术栈，遇到的挑战和解决方案)

- 你觉得 React 和 Vue 有什么共通之处？

- 说一下浏览器渲染过程(说的很详细，面试官说可以，细节把握的很 professional)

- 说一下对于前端技术的发展过程(从刀耕火种的年代说起，到后来的 jq，angular，react，vue 三大框架，gulp、grunt、rollup、webpack 打包工具，然后到未来的一些方向，比如 PWA, 跨端，serverless，微前端，webassemblely，加入了我自己的理解)

- 你觉得前端除了完成页面交互稿之外，还能做其他的什么事情？(首先是性能优化，其次是处理数据，然后是工程化)

- - 你觉得工程化的理解是怎样的？(从代码的角度，编译、压缩、规范，从人的角度，团队协作、统一产出标准)

- 你觉得你选择阿里云或者淘宝，你选择的标准的什么？

- 还有什么想问我的吗？(问了一些转正和部门相关的事情)

- HTTPS 的握手过程讲一讲。(讲了很久很细，面试官知道我理解，喊停了)

- - HTTPS 和 HTTP 的缓存有什么区别？(懵了)

- DOM API 掌握怎么样？(不是很熟)

- - Element 和 Node 的区别(假装想了一会，不知道)

- XSS 攻击 Cookie 相关的字段(HttpOnly, 解释了一下作用)

- CSRF 攻击，解释一下 Cookie 的 SameSite 字段 (说了下，觉得可以，过)

- - chrome 最新的 xxx 特性是如何防范 CSRF 攻击 (这个真没听说过)

- fetch 和 xhr 有什么区别？(fetch 不熟)

- - 好，解释一下 xhr 的 cors 过程(简单请求，非简单请求两种情况，说了下)

- React 闭包陷阱有什么好的解决办法吗？(说实话，简历上写了，实际上理解不深，只说了一种)

- - useReducer 可以解决你知道吗？(当时真的不清楚，主要忘了闭包陷阱的表单场景，尴尬)

- 看了你的小册子，能不能讲讲 React.memo 和 JS 的 memorize 函数的区别(memorize 函数当时不知道，以为是什么高深的算法，后来才发现就是 cache 函数，换了个名字而已。反正当时说不会)

- - 特意考了一题对 React.memo 的理解(擦，还是考 React.memo, 三个场景，中间一个场景答错了，非常减分。这道题出的还是很有水平)

- WeakMap 和 Map 的性能有什么差别?(前者对 GC 更加友好，保持弱引用)

- - 换个说法吧，如果这个立即执行函数中有递归函数，两者性能有区别吗？(没 GET 到面试官的点啊，过了吧这题)
  - 如果是在立即执行函数中，两者的性能有区别吗？(楞了一会，说强弱引用还是会有 GC 的区别，没影响)

- 能不能说说 AMD 和 ESModule 有什么区别？(AMD 不熟，说 ESModule，介绍了 import、export 以及导出引用的特点)

- 那么你能不能告诉我 ESModule 对于 Tree-Shaking 有什么优势呢？(会做一些编译阶段的优化吧)

- async await 经过编译后和 generator 有啥联系？(问了两遍，还是不知道问的啥，直接说了 async await 原理，他说你讲了太深，问的不是这个，过吧过吧)
- HTTP 的 GET 和 POST 请求有什么区别？(我说了 4 个区别)
- 说一说 CSRF 和 XSS 攻击？(说了一堆，他说你讲的太细了，是不是最近看过之类的文章，我说没有)
- HTTP 缓存能不能说一下？(强缓存，协商缓存，中间扯到代理了，讲了一堆，他说可以了)
- 你知道 JS 的语言标准是如何制定的吗？(确实不熟，说下去自己查查)
- 你用过哪些 ES 最新的语法，越新越好
- 你对 babel 了解吗？能不能说说几个 stage 代表什么意思？
- Vue 的响应式对数组是如何处理的？(重写数组方法，手动派发更新)
  - Object 为什么可以自动派发更新？
- 假如我在一个 for 循环中改变当前组件依赖的数据，改变一万次，会有什么效果？(讲到批量更新和 nextTick 原理，他表示可以)
- 假如让你设计一个适配 PC、手机和平板的项目，你有哪些布局方案？(首先是 vh、vw，然后用淘宝出品的 lib-flexible 库进行 rem 适配，还有一种 flex + px 的适配方式)
- CSS 当中以 @ 开头的属性有哪些？(我说了@media, @keyframes，后来提醒我还有@import，我补充这个是串行加载 CSS)
- 了解过前端当前的发展趋势吗，比如一些新的技术方向。(说了对 PWA 的看法，为什么会凉，flutter、electron、微前端，serverless)
- 了解过云计算吗？能不能讲一讲云计算的发展方向和前景？(没了解过)
- 说说你对前端架构的认识，如何设计出一个架构方案(说实话，我顶不住，没研究过)
- 在一个大型项目中，如何定位发生内存泄露的代码？(没有实践过)
- Last-Modified 和 Etag 有什么区别？
- Cache-Control 和 Last-Modified 的区别
- 说说 String, StringBuilder 和 StringBuffer 的区别
- 跨域有哪些方案？

  1.  浏览器和 nodejs 事件循环？🌟

  答：执行栈，promise 是 microTask，setTimeout 是 task

  其中很多的阶段，可以从这里看到完整的模型介绍：html.spec.whatwg.org/multipage/w…

  需要说出来的点：首先 setTimeout 并没有特殊，也是一个 task。另外每次的执行过 task 和 大量的 microtask（不一定在一次循环全执行完）后，会进行 renderUi 阶段，虽然不是每次事件循环都进行 renderUi ，但每次间隔，也就是传说中 **60hz** 的一帧 **16ms**。

  nodejs 事件循环略有不同...多了 process.nextTick 等

  1.  手写 bind 函数

  答：同上。

  1.  service worker 使用

  答：缓存，渐进式应用，拦截处理

  聊到 **worker** 可能还会聊到 **web worker， shared worder** 等等，如果有自信，或者工作对这方面有深入理解，可以秀一下。能体现出自己的优势...

  1.  严格模式

  答：this 的 undefined，禁止 with，arguments 不允许更改，给只读对象赋值抛异常，变量需要先声明，call，apply 第一个参数不会被转换...

  能答出来一些就行。

  1.  原型链以及继承

  答：很常问，但随便找个赞数高的讲解，看一遍就懂了，记住常考点即可。

  1.  正则表达式匹配规则？

  答：这个真没办法，只能是对正则表达式的规则进行系统学习，当然常考的可能是 **邮箱，url** 匹配。

  ### css 以及优化

  1.  flex 布局 🌟

  答：阮一峰老师的 flex 文章，清晰易懂。

  常用的 api 和两列、三列布局等等，对于我来说稍微有点难度。之前项目对兼容性高，基本没怎么用过 flex 布局。没用过的建议用一用，几个小时就会常见布局了。

  1.  优化长列表滚动效果

  没答上来，说了几个 js 的方案没答对点上。

  面试官答曰：transition 优化动画效果，分层渲染

  后面分析了一下，可以用 transform 进行强制分层，第二种可以用 content-visibility 将看不见的元素不渲染，设置值为 `auto` 即可。第三个是对于某些动画效果，可以用 `will-change` 作用在父元素上进行 gpu 加速，使用后删掉。

  1.  响应式布局 🌟

  答：可能会涉及 css 函数，rem/em 区别，媒体查询...

  1.  什么是 BFC？

  答：块级格式化上下文，我布局总用！

  问：什么会形成 BFC？它的作用是什么？

  答：

  - body 根元素
  - 浮动元素：float 除 none 以外的值
  - 绝对定位元素：position (absolute、fixed)
  - display 为 inline-block、table-cells、flex
  - overflow 除了 visible 以外的值 (hidden、auto、scroll)

  作用嘛，为了布局 😂（千万别这么答哈，具体可以看下面文章）

  推荐一篇 BFC 文章

  ### vue 或 react 框架相关

  1.  vue 响应式原理以及双向绑定实现代码 ? 🌟
  2.  vue3 响应式原理，有什么不同？
  3.  vue 的 diff 算法思路，怎么对比节点？
  4.  vue 的 compile 实现？🌟
  5.  vue 如何自定义指令？具体的 api 写法？
  6.  vue3 对于 vue2 在性能上的优化（从 compile 和 runtime 两方面）？
  7.  react 有什么不同？了解 hooks 吗？

  答：（虽然我不会，但我可以说点别的，比如 vue3 也有 hooks，它的使用和一些优点？）

  1.  用过 TypeScript 吗？有什么优点，为什么用？具体的场景，使用 TypeScript 进行类型定义。

  答：vue 项目多， ts 用的少，也用过，写前端监控 sdk 时，对接口进行类型校验，它像一个文档，每一个接口都有定义，后面再翻看瞬间理解意思。（强类型好处还有很多，但是个人觉得写起来超级麻烦，当然有人很喜欢很爽。）

  1.  vue 的 keep-alive 使用场景，以及原理？🌟

  ### 前端打包等工程化

  1.  webpack 和 rollup 使用？

  2.  tree-shaking 原理？🌟

  3.  webpack loader 和 plugin 怎么写？

  4.  你对 vite 熟悉，和 webpack 区别？

  5.  给 vite 做的贡献和在实际项目的使用？

  - vite-electron-quick Git 地址

  - 代码被 merge 的 pr 历史

  1.  如何统一对错误进行捕获的？vue 的异步错误如何捕获？

  - 自己写的 JS 错误捕获 SDK Git 地址

  顺便求个 git 小 🌟🌟

  ![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/H8M5QJDxMHrFWJIUTubbI1xZS9ntOIm9iaXPDlEqjgfeIxFPw0HasYmsdNVnxdJI6eqx5uklLba7yibcRJR6oZ2g/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

  ### 浏览器及常见安全问题相关

  1.  浏览器页面加载过程，越详细越好 🌟
  2.  浏览器缓存 🌟
  3.  跨域问题及处理 🌟
  4.  v8 快数组慢数组，hidden class 或者其他模块？
  5.  xss 和 csrc 的意思？如何防范？🌟

  答：美团的两篇文章摆出来，面试官直接问下一题！

  - xss 防范
  - csrf 防范

  ### 跨平台技术

  1.  electron 使用，如何实现小托盘功能？
  2.  flutter 的 widget stateFullWidget stateLessWidget 区别？
  3.  js Bridge 的原理 ？🌟
  4.  flutter 的渲染引擎？

  ### 网络相关

  2.  Oauth2.0 和 jwt 单点登录等
  3.  http/https 区别？为什么 https 更安全一点？https 为什么也不是十分安全？
  4.  http1.x 和 http2.0 的区别？http2.0 优点，以及某些情况会比 1.x 速度更慢？
  5.  https 加密原理？
  6.  http2.0 压缩头，以及并行请求原理？
  7.  tcp 的连接方式？

  ### 少量算法

  - 回文串，中心扩散法
  - 冒泡，快排 🌟
  - 二分查找 🌟

  ## 面试中的项目题

  大概就是让你去设计一个系统的技术选型，或者是如何设计组件库，设计一个系统。个人猜测对于渣渣的我，这种题就是看看有没有 owner 意识，而且也可以看一下我对哪些技术更感兴趣？

  除了系统，还有某些场景的设计方案，比如如何用鉴权控制登陆时间设计**保持七天登录状态**。

  因为我简历中几乎没有涉及 nodejs 服务端的东西，但面试官总想问一问...

  只能说做过自己博客的服务端...

  服务端代码 Git 地址

  但是很简陋...只能说开发过 😂

  ## 总结

  - 对于框架原理只能说个大概，真的深入某一部分具体的代码和实现方式就只能写出一个框架，许多细节注意不到。
  - 算法方面还是很薄弱，好在面试官都很和蔼可亲，擅长发现人的美哈哈哈...（最好多刷一刷，不然影响你的工资和成功率 😯）
  - 在投递简历之前，最好通过各种渠道找到公司内部的人，先提前了解业务，也可以帮助后期优秀 offer 的决策。
  - 要勇于说不，对于某些 offer 待遇不满意、业务不喜欢，应该相信自己，不要因为当下没有更好的 offer 而投降，一份工作短则一年长则 N 年，为了幸福生活要慎重选择！！！

  ### 第一个场景问题

  比如直播的场景，你应该知道吧，你需要实现一个这样子的场景，比如某个老师点击某个地方，比如 U 盘，你这个时候需要展示 U 盘的动画效果，比如这个时候，老师点击这个电脑屏幕，你需要展示一个小电脑的动画效果，向上述这样子，**「需要在特定的时间点，完成特定的动画效果」**。

  - 嗯，这个问题，我的想法是，动画是例外加上去的，如果说是直接后期处理的话，那应该跟我们前端的关系不大了，所以我们接下来的问题，就是如何去处理，时间同步的问题，怎么在具体的时间点，开始展示动画呢
  - 第二个问题，假设我们可以获取到某个时间点的动画，那么接下来，小哥哥，给我们提出了一个新的问题，就是当你的网络拥塞时，比如有延迟的时候，这个时候，出现卡顿的效果，原本需要 5 秒播放完的，可能需要 7 秒，那么你是如何去解决动画同步的？

  嗯，我没有做过这种类似的问题，所以回答起来感觉很吃力，有了解的小伙伴可以评论留下你们的答案，我虚心学习。

- 有一个场景，在一个输入框输入内容，怎么更加高效的去提示用户你输入的信息，举个例子，你输入天猫，那么对应的提示信息是天猫商城，天猫集团，这个信息如何最快的获取，有没有不需要发请求的方式来实现？

  ### 第三个场景问题

  Git 版本工具你使用过吧，那你能不能实现一个这样子的效果，完成 Git Diff 算法，比较两个文件的不同，然后说一说具体的思路，这个过程怎么去比较的？两个文件不同的位置如何标注出来，如何找出这个不同，具体说一说思路。

  - 一开始我想的是 diff 算法，比如是 vue 中的虚拟 dom 算法，但是感觉不对啊，diff 是做了优化的，这里很明显不合理，于是这个方法就不合理了。
  - 那么两个文件，该如何快速的找到对应的两者文件的差别呢？这个问题想了好久，嗯，当时自己好像是口胡了一些思路，比如去逐行逐行的比较，这样子的话，其实也不是很合理的，仔细想一想不行
  - 小哥哥提示了我，我们是不是要去找`最长的公共子串`，这个是时候，我应该想起来这个是两个串的`LCS`,应该就是经典的`动态规划`问题,最后一个问题，确实没有想到这个，可能就是很久没有接触这类动态规划问题了。
  - 核心应该是动态规划解决 LCS，以及后续的处理，可以去看看有些文章，写的很不错，我这里就不张开啦。

  Git 是怎样生成 diff 的：Myers 算法

  嗯,三面的话，考察的是你思考问题，以及结合问题是如何分析，可能也考了算法吧，嗯，害，挺难的。

- localstroge sessionstoge 区别 应用场景
- vue 组件间通信
  好几次面试都问了这个问题，这个问题我是这么看待的，取决于你平时项目中经常使用的方式是哪些，所以我每次都会答三种方式，反而网上 8 种组件间通信的方式，我记不住，也觉得了解一下即可，跟面试官交流一下，你在项目种是如何使用的即可。
- 遍历对象方法
  for in 遍历的也可以，不过对于非继承的属性名称也会获取到，通过 hasOwnproperty 判断
  Object.keys() 可枚举属性和方法名
  Object.getOwnPropertyNames() 可以获取数组内包括自身拥有的枚举或不可枚举属性名称字符串，如果是数组的话，还有可能获取到`length`属性
- 数组去重
  常规题，讲清楚思路，最后小哥哥提示能不能使用 O(n)，我给出了两者方案
  - Set
  - 用对象特性，我觉得他就是想考这个，给你们贴一个代码吧?
    ```javascript
    let unique = (arr) => {
      let obj = {}
      return arr.filter((ele) => {
        return obj.hasOwnProperty(typeof ele + ele) ? false : (obj[typeof ele + ele] = true)
      })
    }
    ```
- 深度遍历
- 链表的相加问题?
- 前端性能优化

  - 构建请求行
  - 查缓存 （重点说一说）
  - tcp http （比如减少请求次数，嗯，应该还有其他优化吧，cdn？）
  - 浏览器渲染过程 （这里面就有优化了，比如常见的如何避免回流和重绘）
  - webpack 打包优化也可以说一说，前提你得有自信

- 原型
- 闭包
- 作用域
- 输入 url 过程整个过程
- https 区别，TLS 握手
- 浏览器缓存
- https 如何保证安全，TLS 握手的过程聊一聊
- vue 通信方式
- vue 数据响应式的原理，数组是怎么重写的
- rem, 计算出 375 的屏幕，1rem,单位出现小数怎么处理
- javascript 精度问题的原因
- axios 用途
- 性能优化的点，webpack 分包，首页资源大小，请求优化，gzip 之前还是之后，React 重新渲染
- 国际化站点，cdn, 在页面什么阶段加载国际化文件，如果有 20 多个语言该怎么做
- ssr 有没有用过
- 项目中 websocket 是解决了什么问题
- http2 多路复用

```javascript
if (!('a' in window)) {
  var a = 1
}
console.log(a)
var a = {}
var b = {}
var c = {}
console.log(a === b)
console.log(b === c)
console.log(a === c)

var d = (e = f = {})
f = {}
e = f
d = e

console.log(d === e)
console.log(d === f)
console.log(e === f)
```

- http 状态 301，302， 304,缓存相关字段
- cookie、ws 是否跨域
- 触发 bfc 的方式
- rem 和 vw 的使用场景
- 伪代码实现下懒加载
- 实现一下 some, every
- flatten 实现
- 函数组件怎么阻止重复渲染
- AST 作用 or babel 实现原理
- 不同域名共享 cookie
- on, emit, 实现
- 输入 url 到页面返回结果
- 缓存的实现方式
- webpack 分包
- Webpack 插件，生命周期
- umi 约定式路由怎么实现的
- babel 实现远原理
- 说出你最擅长的部分，追问
- webpack 拆包的依据。1.被多个模块使用，cache 起来 2.资源过大
- canvas 点击线段事件。重合区域怎么处理
- webWorker 的使用：为什么不在 worker 里面发出请求，做数据转换呢？
- generate 函数和 async 区别
- webpack 插件实现
- Vue， React 使用情况
- 父子组件的 mounted 调用顺序
- $nextTick 实现原理
- 子元素水平垂直居中
- 斐波那契数列如何优化
- 业务题：封装一个全局的弹窗，在任何组件内都可以调用。追加：如何同时打开 5 个弹窗，关闭顺序又如何
- 前端工程化，webpack, babel, Node 等。
- 精通框架源码
- 可视化，3D 方向
- 流媒体，音视频
- 数组交集，编写一个函数，输入两个数组，输出它们的交集。输出数组中不含重复的元素，元素排列顺序可随意。
- 二叉树的搜索，输入一个普通二叉树的根节点，实现一个调度器，调用调度器的 next()方法，将返回二叉树中下一个最小的数；调用迭代器的 hasNext()方法，将返回是否存在下一个数。二叉树节点是整数，无序。
- 三角形个数，输入一个非负整数的数组，如果将数组元素选作三角形的边长，编写一个函数，输出这个数组可构成的三角形数量。
- 数组切分问题，输入一个正序排列的整型数组，如果它可以被切分为 1 个或多个子序列，输出 True，反之 False。子序列需为连续的整型数组，并且长度至少为 3。
  例 1：
  输入： [1,2,3,3,4,5]
  输出：True
  解释：可以切分为 2 个各自连续的子序列：
  1, 2, 3
  3, 4, 5
  例 2：
  输入： [1,2,3,3,4,4,5,5]
  输出：True
  解释：可以切分为 2 个各自连续的子序列：
  1, 2, 3, 4, 5
  3, 4, 5
  例 3：
  输入： [1,2,3,4,4,5]
  输出：False
  解释：无法切分出长度至少为 3 的子序列。

- 事件循环(浏览器/node/版本差异)
- setTimeout 实现原理
- react 和 vue 的区别
- 前端错误监控及容灾
- 谈谈 node 的内存泄漏
- 浏览器的渲染机制是怎样的
- SSR 作用及优缺点
- 如何进行状态管理
- webpack 及浏览器的技术分享目的是什么，分享了什么，怎么做的分享
- 如何进行项目重构
- 进程与线程的区别
- 说说知道的设计模式

## 2 常规基础题

**「2.1 vuex 是什么？怎么使⽤？哪种功能场景使⽤它？」**

- 只⽤来读取的状态集中放在 store 中；改变状态的⽅式是提交 mutations，这是个同步的事物；异步逻辑应该封装在 action 中。
- 在 main.js 引⼊ store，注⼊。新建了⼀个⽬录 store，…export 。
- 场景有：单⻚应⽤中，组件之间的状态、⾳乐播放、登录状态、加⼊购物⻋
- state：Vuex 使⽤单⼀状态树,即每个应⽤将仅仅包含⼀个 store 实例，但单⼀状态树和模块化并不冲突。存放的数据状态，不可以直接修改⾥⾯的数据。
- mutations：mutations 定义的⽅法动态修改 Vuex 的 store 中的状态或数据
- getters：类似 vue 的计算属性，主要⽤来过滤⼀些数据。
- action：actions 可以理解为通过将 mutations ⾥⾯处⾥数据的⽅法变成可异步的处理数据的⽅法，简单的说就是异步操作数据。view 层通过 store.dispath 来分发 action。

modules：项⽬特别复杂的时候，可以让每⼀个模块拥有⾃⼰的 state、mutation、action、getters，使得结构⾮常清晰，⽅便管理

**「2.2 关于响应式数据绑定，双向绑定机制：Object.defineProperty()」**

vue 实现数据双向绑定主要是：采⽤数据劫持结合发布者-订阅者模式的⽅式，通过`Object.defineProperty()`来劫持各个属性的`setter`，`getter`，在数据变动时发布消息给订阅者，触发相应监听回调。当把⼀个普通`Javascript`对象传给 Vue 实例来作为它的`data`选项时,`Vue`将遍历它的属性，⽤`Object.defineProperty()`将它们转为`getter/setter`。⽤户看不到`getter/setter`，但是在内部它们让`Vue`追踪依赖，在属性被访问和修改时通知变化。

`vue`的数据双向绑定将`MVVM`作为数据绑定的⼊⼝，整合`Observer`，`Compile`和`Watcher`三者，通过`Observer`来监听⾃⼰的`model`的数据变化，通过`Compile`来解析编译模板指令（`vue`中是⽤来解析`{{}}`），最终利⽤`watcher`搭起`observer`和`Compile`之间的通信桥梁，达到数据变化—>视图更新；视图交互变化（`input`）—>数据`model`变更双向绑定效果。

**「数据劫持」**：Vue 内部使⽤了 Object.defineProperty()来实现双向绑定，通过这个函数可以监听到 set 和 get 的事件。

    var data = { name: 'yck' }
    observe(data)
    let name = data.name // -> get value
    data.name = 'yyy' // -> change value
    function observe(obj) {
        // 判断类型
        if (!obj || typeof obj !== 'object') {
        	return
        }
        //Object.keys(obj)将对象转为数组
        Object.keys(obj).forEach(key => {
        	defineReactive(obj, key, obj[key])
        })
    }
    function defineReactive(obj, key, val) {
        // 递归⼦属性
        observe(val)
        Object.defineProperty(obj, key, {
            enumerable: true,
            configurable: true,
            get: function reactiveGetter() {
                console.log('get value')
                return val
            },
            set: function reactiveSetter(newVal) {
                console.log('change value')
                val = newVal
            }
        })
    }

**「Proxy 与 Object.defineProperty 对⽐」**

Object.defineProperty 虽然已经能够实现双向绑定了，但是他还是有缺陷的 .

- 只能对属性进⾏数据劫持，所以需要深度遍历整个对象 对于数组不能监听到数据的变化
- 虽然 Vue 中确实能检测到数组数据的变化，但是其实是使⽤了 hack 的办法，并且也是有缺陷的。

**「web 网站中常见攻击手法和原理」**

- 跨站脚本攻击(`xss`)：恶意攻击者通过往`web`页面中插入恶意`html`代码，当用户浏览该页面时，嵌入`web`里面的`html`代码会被执行，从而达到恶意攻击用户的特殊目的。
- `sql`注入：`sql`注入就是把`sql`命令插入到`web`表单进行提交，或输入域名，或页面请求的查询字符串，最终达到欺骗服务器执行恶意`sql`命令的目的。具体而言，就是利用现有应用程序，将恶意的`sql`命令注入到后台数据库引擎中进行执行。
- `cookie`攻击：通过 js 很容易访问到当前网站的`cookie`，你可以打开任何网站，然后在浏览器地址栏输入`javascript:alert(doucment.cookie)`，立刻可以看到当前站点的 cookie，攻击者可以利用这个特性取得用户的关键信息。假设这个网站仅依赖 cookie 进行用户身份验证，那么攻击者就可以假冒你的身份来做一些事情。现在多数浏览器都支持在`cookie`上打上`HttpOnly`的标记，但凡有这个标记的`cookie`就无法通过`js`来获取，如果能够在关键`cookie`上打上标记，就可增强`cookie`的安全性。
- `HTTP Headers`攻击：凡是用浏览器查看任何 web 网站，无论你的 web 网站采用何种技术和框架，都用到了`http`协议。`http`协议在`Response header`和`content`之间，有一个空行，即两组`CRLF(0x0D 0A)`字符这个空行标志着`headers`的结束和`content`的开始。攻击者利用这一点，只要攻击者有办法将任意字符注入到`headers`中，这种攻击就可以发生。
- 文件上传攻击：文件上传漏洞就是利用对用户上传的文件类型判断不完善，导致攻击者上传非法类型的文件，从而对网站进行攻击。比如可以上传一个网页木马，如果存放文件的目录刚好有执行脚本的权限，那么攻击者就可以得到一个`webshell`。

**「Vue 中 diff 原理」**

要知道渲染真实 DOM 的开销是很大的，比如有时候我们修改了某个数据，如果直接渲染到真实 dom 上会引起整个 dom 树的重绘和重排。有没有可能我们只更新我们修改的那一小块 dom 而不要更新整个 dom 呢？diff 算法能够帮助我们

**「diff 算法包括一下几个步骤：」**

- 用`JavaScript`对象结构表示`DOM`树的结构；然后用这个树构建一个真正的`DOM`树，插到文档当中
- 当状态变更的时候，重新构造一棵新的对象树。然后用新的树和旧的树进行比较(`diff`)，记录两棵树差异
- 把 2 所记录的差异应用到步骤 1 所构建的真正的`DOM`树上(`patch`)，视图就更新了

diff 算法是通过\*\*「同层的树节点」\*\*进行比较而非对树进行逐层搜索遍历的方式，所以时间复杂度只有 O(n)，是一种相当高效的算法 ![图片](https://mmbiz.qpic.cn/mmbiz_png/WOeOmUjdHrv58We4uLlugZuuXRUnvdG44ibgIzsdvt7xP0OTckSmfAIurhLvz99U3uldcnucP9TzkEhd7ib1ibvEA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1) 逐个遍历 newVdom 的节点，找到它在 oldVdom 中的位置，如果找到了就移动对应的 DOM 元素，如果没找到说明是新增节点，则新建一个节点插入。遍历完成之后如果 oldVdom 中还有没处理过的节点，则说明这些节点在 newVdom 中被删除了，删除它们即可。

**「vue 模板编译原理」**

模板转换成视图的过程整个过程：

- Vue.js 通过编译将 template 模板转换成渲染函数(render ) ，执行渲染函数就可以得到一个虚拟节点树
- 在对 Model 进行操作的时候，会触发对应 Dep 中的 Watcher 对象。Watcher 对象会调用对应的 update 来修改视图。这个过程主要是将新旧虚拟节点进行差异对比，然后根据对比结果进行 DOM 操作来更新视图。![图片](https://mmbiz.qpic.cn/mmbiz_png/WOeOmUjdHrv58We4uLlugZuuXRUnvdG4YIBEr2iauMe9yCLEwtV4QsLjygG4HsgNsaMUXzQQEuIZYezQzvgfqPg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1) 我们对上图几个概念加以解释:
- 渲染函数：渲染函数是用来生成`Virtual DOM`的。`Vue`推荐使用模板来构建我们的应用界面，在底层实现中`Vue`会将模板编译成渲染函数，当然我们也可以不写模板，直接写渲染函数，以获得更好的控制。
- `VNode`虚拟节点：它可以代表一个真实的`dom`节点。通过`createElement`方法能将`VNode`渲染成`dom`节点。简单地说，`vnode`可以理解成节点描述对象，它描述了应该怎样去创建真实的`DOM`节点。
- `patch`(也叫做`patching`算法)：虚拟`DOM`最核心的部分，它可以将`vnode`渲染成真实的`DOM`，这个过程是对比新旧虚拟节点之间有哪些不同，然后根据对比结果找出需要更新的的节点进行更新。这点我们从单词含义就可以看出，`patch`本身就有补丁、修补的意思，其实际作用是在现有`DOM`上进行修改来实现更新视图的目的。`Vue`的`Virtual DOM Patching`算法是基于`Snabbdom`的实现，并在些基础上作了很多的调整和改进。

**「介绍下你了解 Webpack 多少知识」**

基本概念：

- 入口（Entry）:_指示 webpack 应该使用哪个模块，来构建其内部依赖图的开始。_
- 加载器（Loader）:_webpack 默认处理 js 和 json 文件，loader 配置 webpack 去处理其他类型的文件，将其转为有效模块给应用程序使用，并添加到依赖图中。_
- 插件（Plugins）:_loader 用于转换某些类型的模块，而插件用于执行范围更广的任务。比如：打包优化、资源管理、注入环境变量等。_
- 模式（Mode）:_设置当前配置文件在开发和生产环境下的优化行为，默认为生产环境。_
- 输出（Output）:_指示 webpack 应该在哪输出它创建的 bundle，以及如何命名文件。入口文件可以有多个，但是出口文件只能有一个。_

Loader 和 Plugin 的区别：

- \*\*「Loader」\*\*在`module.rules`中配置，也就是说他作为模块的解析规则而存在。类型为数组，每一项都是一个`Object`，里面描述了对于什么类型的文件（`test`），使用什么加载(`loader`)和使用的参数（`options`）。
- \*\*「Plugin」\*\*在`plugins`中单独配置。类型为数组，每一项是一个`plugin`的实例，参数都通过构造函数传入。

在我的个人理解中，plugin 更像是对 loader 的补充，两者进行相辅相成，loader 大多是固定的配置，而 plugin 能够处理更加灵活的设置。

核心作用：

- 打包压缩：在进行开发时，项目文件是千姿百态的，此时可以使用 Webpack 将不同模块有序进行打包整合，根据业务进行进行划分模块，使得结构清晰可读。整个项目在开发过程中，代码和文件是比较庞大的，如果进行项目部署时，会占用很大的内存，因此可以进行压缩，将原先几十 M 降低成几 M，甚至几百 K。
- 编译兼容：相信在实际开发中，由于历史的原因各种浏览器遗留下很多兼容性问题，一方面我们积极学习浏览器的新性能，另一方面又要兼顾旧浏览器的问题。通过 Webpack 进行按需加载器的机制，可以实现在配置 bebel-loader 时，对预定义的环境进行配置，将其对新旧浏览器进行兼容。与此同时，由于浏览器只能读取 html、js 等文件，因此可以通过 webpack 将非 js 文件模块转为可读 js 文件模块。
- 能力拓展：通过`webpack`的`Plugin`机制，我们在实现模块化打包和编译兼容的基础上，可以进一步实现诸如按需加载，代码压缩等一系列功能，帮助我们进一步提高自动化程度，工程效率以及打包输出的质量。

## 3 手撕代码题

### 3.1 千分位格式化数字

用 js 实现如下功能，将给定的数字转化成千分位的格式，如把`12345678`转化成`12,345,678`。

这题目相对是比较简单了，能够用来解决的问题的方法也有很多，最简单的可以用正则化进行处理。

- 正则化

  let num = 12345678;
  let str = num.toString();
  let newStr = str.replace(/(\d)(?=(?:\d{3})+`$)/g,"$`1,");

- 将字符串拆分拼接

思路：将数字转换为字符串(toString())再打散成数组(split)，如果直接数字转换为数组，就是一整个放进去了，不能单独取到每一位。然后通过循环，逐个倒着把数组中的元素插入到新数组的开头(unshift)，第三次或三的倍数次，插入逗号，最后把新数组拼接成一个字符串。

    let num = 12345678;
    function Thousands(num){
      //将数字转换为字符串后进行切分为数组
      let numArr = num.toString().split("");
      let arr = [];
      let count = 0;//用于计数
      for(let i = numArr.length-1;i>=0;i--){
        count++;
        //从numArr末尾取出数字后插入arr中，其实就是对齐进行倒序
        arr.unshift(numArr[i]);
        //当count每到三位数字，则进行追加逗号。i!=0即取到第1位的时候，前面不用加逗号。
        if(!(count%3)&&i!==0) arr.unshift(",");
      }
      //将数组拼接为字符串
      return arr.join("");
    }
    Thousands(num);

缺点：一位一位的加进去，性能差，且还要先转换成字符串再转换成数组。

- 用 charAt()获取子字符串，主要用到字符串拼接

思路：不先转为数组，直接获取字符串的每一个字符进行拼接。

    let num = 12345678;
    function Thousands(num){
      //将数字转换为字符串
      let str = num.toString();
      let res = "";//用于接收拼接后的新字符串
      let count = 0;//用于计数
      for(let i = str.length-1;i>=0;i--){
        count++;
        //从numArr末尾取出数字后插入arr中，其实就是对齐进行倒序
        res = str.charAt(i) + res;
        //当count每到三位数字，则进行追加逗号。i!=0即取到第1位的时候，前面不用加逗号。
        if(!(count%3)&&i!==0) res = ',' + res;
      }
      //将数组拼接为字符串
      return res;
    }
    Thousands(num);

缺点：依旧需要进行一一分割拼接。

- 每截取三位进行拼接

思路：每次取末三位子字符串放到一个新的空字符串里并拼接上之前的末三位，原本数组不断截掉后三位直到长度小于三个，最后把剥完的原数组拼接上新的不断被填充的数组。

    let num=123345678;
    function Thousands(num){
        //将数字转换为字符串
        let str = num.toString();
        let res = "";//用于接收拼接后的新字符串
        while(str.length>3){
            res = "," + str.slice(-3) + res;
            str = str.slice(0,str.length-3)
        }
        if(str) return str + res;
    };
    Thousands(num);

### 3.2 比较两个对象的属性和值是否相同

题目描述：

    obj1 = {name:"wenbo",age:12,score:[120,121,113]};
    obj2 = {age:12,name:"wenbo",score:[120,121,113]};

- 遍历进行比较

思路：对两个对象进行遍历取值进行比较

    function fun(obj1,obj2){
      //判断obj1、obj2是否为Object类型
      let o1 = obj1 instanceof Object;
      let o2 = obj2 instanceof Object;
      //如果两者有不是对象类型的，既可以直接进行等值比较
      if(!o1 || !o2) return obj1 === obj2;
      //如果两个是对象类型，且两者的键值对个数不同
      if(Object.keys(obj1).length!==Object.keys(obj2).length) return false;
      //当以上情况均不是，则进行遍历比较
      for(let key in obj1){
        //需要判断两个对象的此key对应的值是否为对象类型
        let flag1 = obj1[key] instanceof Object;
        let flag2 = obj2[key] instanceof Object;
        if(flag1 && flag2){
          fun(obj1[key],obj2[key])
        }else if(obj1[key] !== obj2[key]){
          return false;
        }
      }
      return true;
    }
    let obj1 = {name:"wenbo",age:12,score:[120,121,113]};
    let obj2 = {age:12,name:"wenbo",score:[120,121,113]};
    fun(obj1,obj2);

亦或：

    function fun(obj1,obj2){
      //判断obj1、obj2是否为Object类型
      let o1 = obj1 instanceof Object;
      let o2 = obj2 instanceof Object;
      //如果两者有不是对象类型的，既可以直接进行等值比较
      if(!o1 || !o2) return obj1 === obj2;
      //如果两个是对象类型，且两者的键值对个数不同
      if(Object.keys(obj1).length!==Object.keys(obj2).length) return false;
      //取对象obj1和obj2的属性名
      let obj1Props = Object.getOwnPropertyNames(obj1);
      //循环取出属性名，再判断属性值是否一致
      for (let i = 0; i < obj1Props.length; i++) {
        let propName = obj1Props[i];
        //需要判断两个对象的此key对应的值是否为对象类型
        let flag1 = obj1[propName] instanceof Object;
        let flag2 = obj2[propName] instanceof Object;
        if(flag1 && flag2){
          fun(obj1[propName],obj2[propName])
        }else if(obj1[propName] !== obj2[propName]){
          return false;
        }
      }
      return true;
    }
    let obj1 = {name:"wenbo",age:12,score:[120,121,113]};
    let obj2 = {age:12,name:"wenbo",score:[120,121,113]};
    console.log(fun(obj1,obj2));;

- 需要考虑的问题

当对象遍历过程中，遇到对象的属性时 Object 类型，且指向的是该对象，那么需要考虑的是以上代码还能运行成功吗？如：

    let obj1 = {name:"wenbo",age:12,score:[120,121,113]};
    obj1.temp = obj1;
    let obj2 = {age:12,name:"wenbo",score:[120,121,113};
    obj2.temp = obj1;

思路：新建一个数组，将 obj1 遍历过的键值存储在数组中，再下一次进行遍历时发现一样的值，直接跳过进行比较。

1.  编写函数`convert(money)` ，传入金额，将金额转换为千分位表示法。例如：12345.6 => 12,345.6
2.  实现对象的深拷贝,输出：新的对象
3.  请完成 React 组件封装，能够实现长度展示功能封装，并且不失 input 原生组件能力。

- 进程线程的区别 [event loop 事件循环 ]
- 聊一聊缓存 [浏览器缓存+http 缓存]
- 如果浏览器关闭了再打开, 请求还是 from cache 吗?
- Service Worker 了解过么?
- 聊一下常见的前端安全问题.
- 你的网站是怎么阻止 csrf 攻击的?
- 为什么用 token 就可以防止 csrf 攻击?
- token 的刷新机制是怎么样的， 为什么这么设置？
- 讲一下 跨域
- 如何处理项目的异常.
- script error 怎么捕获
- 脚手架做了什么功能.
- webpack 做了什么优化
- webpack 原理
- 维护的公共组件需要发布大更新, 如何做?
- 聊一下高阶组件 hoc
- 聊一聊组件设计, 领域模型
- 项目的最大难点是什么? 怎么解决?
- 聊一下 node 的事件循环.
- node 架构中容灾
- pm2 的原理.
- 有没有读过 egg 源码.
- 了解过 grahql 么
- 聊一下微服务
- 小程序跟 h5 的区别是什么? [小程序底层实现]
- 讲一下 taro 小程序的底层原理，跟 mpvue 的区别 [AST, babel]
- SPA 项目如何监控 pv, uv 值
- 如何在用户刷新、跳转、关闭浏览器时向服务端发送统计的数据？
- 错误日志上报遇到的问题.

```markdown
前端日志上报可以很简单

对业务逻辑的执行收集了日志数据之后可以参数的形式构造一个 url，再通过一个 Image 请求发送到到服务器就完成了日志的上报。

(new Image).src = `/r.png?page=${location.href}&param1=${param1}...`;

这样一行代码就搞定了日志的上报，然鹅，在生产环境中，日志上报所延伸的问题要复杂很多。

日志上报带来的问题

日志上报最终是为了服务业务，监控业务的运行状态，一般而言前端运行的场景中开发者最期望监控的不外乎页面&API 请求是否正常响应和页面 js 逻辑是否正常执行。

为了覆盖这两个监控目标，需要通过很多类型的日志来覆盖，还有一些特殊场景下，开发者还希望能与具体业务灵活结合，实现自定义上报。所以常见的日志类型如下

– 页面&API 请求是否正常响应

– API 调用日志 – API 调用成功与否及其耗时

– 页面性能日志 – 页面连接耗时、首次渲染时间、资源加载耗时等

– 访问统计日志 – PV/UV，短时间内断崖式的量变化很容易反应问题

– 页面 js 逻辑是否正常执行

– 页面稳定性日志 – 页面加载和页面交互产生的 js error 信息

– 业务相关日志

– 自定义上报 – 某些业务逻辑的结果、速度、统计值等自定义内容
```

- 规范 [eslint, prettier, git commit hook]
- 如何制定规范？
- 可视化表单了解过么?
- 聊一下 axios .有什么优点, 跟 fetch, ajax 对比
- axios 为什么既可以在浏览器发请求,又可以在 node 层发请求?
- 跨域
- 执行上下文/作用域链/闭包
- 事件循环
- 安全
- 缓存
- 模块化
- 深拷贝浅拷贝
- 异步处理 async await promise
- http 请求头, http2 http 相关知识
- webpack 热更新的原理
- loader 和 plugin 的区别
- 手写一个 plugin
- webpack 底层 Tapable 原理
- webpack 做的性能优化
- tree-shaking
- webpack 的构建流程
- 多页面打包怎么做?
- 文件指纹
- webpack 如何实现异步加载
- koa 中间件原理
- 介绍下 stream
- babel
- transform-runtime, stage-2 说一下他们的作用
- babel 如何将字符串解析成 AST ?
- 讲一下 AST 语法树
- babel-runtime 和 babel-polyfill
- npm package.json
- npx
  - 说一下对 package.json 的理解,它都有哪些作用

3.  什么是事件冒泡和事件捕获，区别是什么。

4.  什么是跨域，如何处理跨域

    **跨域**

    协议，域名，端口，三者有一不一样，就是跨域

    **如何解决跨域**

    目前有两种最常见的解决方案：

5.  1.  CORS，在服务器端设置几个响应头
    2.  Reverse Proxy，在 nginx/traefik/haproxy 等反向代理服务器中设置为同一域名

6.  浏览器缓存原理

7.  当输入 URL 时，整个过程是什么样的

8.  关于模块分包的几个细节

9.  有没有接触过 node，你认为 node 怎么样

10. node 引入一个模块的过程是什么

11. https 有什么用，原理是什么

12. https 如何保证证书是可信任的

13. amd 和 cmd 的区别，commonjs，esmodule

14. 什么是函数柯力化

15. virtual DOM 是什么，如何实现

16. dom diff 是什么

17. get 和 post 请求

18. 你们持续集成的流水线有什么

19. Accept 头部的作用什么，如果服务器不支持怎么办

关于技术面试，大部分属于基础，在网络上都能够找到答案，所以面试大厂基础一定要牢固！

## **笔试题**

- 实现 printf 函数，具备以下功能

let str = 'My name is `${name}, I am from ${city}`',

info = {

name: 'AaDerBrane',

city: 'GungZhou'

};

console.log(printf(str, info));

_// My name is AaDerBrane, I am from GuangZhou_

functionprintf(str, info) {}

- docContentLoad 和 onload 区别
- 0.5 像素的边框，怎么做
- 介绍下缓存
- 讲一下跨域
- fetch 和 ajax 的区别
- 对比过 react 和 vue 吗
- 受控组件和非受控组件的区别
- 你们 abort 机制怎么设计的，了解过原理吗
- 说一下 webrtc 的运行机制
- 假如让你使用 webrtc 和 websocket 去实现你画我猜的小游戏，怎么设计
- 项目里面有用到 webpack，请问你使用 webpack 有啥需要注意的地方呢
- 有了解过 loader 的原理吗？写过 webpack 插件吗？知道 webpack 插件的组成吗？
- babel 怎么转译的？了解过吗？
- 你的项目性能监控是怎么处理的
- node 层用什么框架？egg 解决了什么问题
- 你说 KOA 是洋葱模型，洋葱模型的架构是啥？
- 接上面一题，假如中间件 B 的 next 不执行了，最后流向哪里？
- 设计登录状态管理系统
- session 应该存在哪里
- 给定一棵树，请你输出所有从根节点到叶子节点的路径组成的数字之和

```javascript
let tree = {
  val: 1,
  left: {
    val: 2,
    left: {
      val: 4,
      left: null,
      right: null
    },
    right: {
      val: 5,
      left: null,
      right: null
    }
  },
  right: {
    val: 3,
    left: null,
    right: null
  }
}

// 例如以上的树，总共有从根节点到叶子节点的路径 3 条，分别为：1->2->4,1->2->5,1->3_
// 则计算方法为：124+125+13=262_
```

- JavaScript 的基本类型
- setTimeout、Promise、async/await 三者之间异步解决方案的区别？
- 宏任务和微任务，通常会给出一段代码，让你给出输出结果，并解释？
- 解释 JavaScript 的单线程模型，以及为什么这样设计？setTimeout 的延时为何做不到精确？
- 原型链知识的考察，形式也是给出一段代码，让你给出输出结果，并解释?
- 说说你用过的 ES6 语法的功能点，对 ES2017-9 的新增功能点是否有关注？
- 解释 JavaScript 的闭包？解释 this 指针指向的问题以及常用改变 this 指针指向的函数? apply, bind, call 三者之间的区别？
- JavaScript 继承的几种方式及优缺点？
- fetch 是否可以共享 Cookie?两个 then 分别对应着什么？
- 手写代码实现红绿灯效果，红灯 3 秒，绿灯 1 秒，黄灯 2 秒，循环重复?
- JavaScript 是如何操作 Cookie 的？
- 如何翻转 DOM？冒泡和捕获机制，实际应用有哪些？
- 冒泡和捕获机制，以及实际应用？
- 浏览器的渲染原理是一定会被问到的？
- 浏览器输入一个 url 之后的过程，以及过程中应用了哪些缓存，如何优化？
- script 标签和 link 标签的先后顺序对页面加载的影响？
- async 和 defer 的区别？
- 解释 TCP/IP 的三次握手和四次挥手？
- 解释跨域问题以及前端常用的解决方案？
- CORS 的细节，哪些是简单请求？哪些是非简单请求？
- 解释 HTTPS? 解释 HTTP/2？
- HTTP 报文的格式？
- 手写冒泡排序？
- 数组去重？
- 给定一组数，求和函数是带延时的网络请求，如何在最快的时间内计算出这组数据的和？
- webpack 如何拆分大文件？
- webpack 打包的过程?
- webpack 的基本配置？
- 买卖股票的最佳时机
- 二维矩阵
  ![图片](https://mmbiz.qpic.cn/mmbiz_png/ZWVxrQ7G0WSCs5Z45JzPQw0YVicT0JZbwd5V3ibpAdDhgWRAZ1faiaibL4WmWFhDAjQ1yOYZXwp6ySITT31nY139Xw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

### 面试题

- 集成化开发是怎么搞的

- - git hook 钩子脚本，jenkin 设置自动化构建触发方式，编写脚本..

- traivs 集成了解么？

- taro 组件化开发

- 单元测试一般你使用哪些方法？

- 快照的原理了解么？

- e2e 自动化测试是什么？

- e2e 是事件驱动吗？

- tree shaking 他是怎么实现的？

- webpack 做了什么优化

- - 体积方面的优化: 压缩啊， 动态 polyfill，分包，tree shaking，延迟加载 js ……
  - 构建速度方面的优化: 多进程打包,大型库外链,Dllplugin 将库预先编译 ,减少构建搜索或编译路径,缓存 bable-loader cache
- 分包,怎么分包,同步和异步你记得吗?
- 多进程编译？怎么实现的你了解么？
- 容灾怎么搞？ 接口级容灾，模块级容灾，页面级容灾，404，还有 cdn 处理
- 那 nginx 那块的容灾呢，了解么？
- nginx 怎么做负载均衡的
- 除了用 nginx 做过这些， 还设置过什么？
- 求最长的山脉
  输入：[2,1,4,7,3,2,5] 输出：5 解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。
  理解题目理解了很久...实际实现起来并不难，就是很难理解
  首先， 最长的山脉：指最长的 2 个坡底之间的距离。
  那么这道题的解决思路就出来了。
  - 使用双指针分别从左右两边开始平移，找到第一个 坡底 即可
  - 坡底：2 种情况，一种是左右 2 边都比它大，一种是在边界处，下一个值比它大。
- 场景题：一个页面有很多很多个数据，怎么让它不卡顿？
  - 虚拟滚动
  - 分片渲染
  - ……
- git eslint， 这些要怎么集成，写脚本？如何设置警告值，加邮件提醒？
- node 的 qps 是多少？为什么这么设置？
- 日志多的情况，如何处理？
- babel 细节
- 你了解 koa 中间件么？
- 手写一个 koa 中间件。
- 树
  二叉树的最大深度
  路径总和
  首个公共祖先
  重建二叉树
- 股票系列 买卖股票的最佳时机
- 动态规划 三角形最小路径和
- Vue 实例的生命周期讲一下, mounted 阶段真实 DOM 存在了嘛?
  `Vue`实例从创建到销毁的过程，就是生命周期。
  也就是：开始创建->初始化数据->编译模板->挂载`dom`->数据更新重新渲染虚拟 `dom`->最后销毁。这一系列的过程就是 vue 的生命周期。所以在 mounted 阶段真实的 DOM 就已经存在了。
  - beforeCreate：vue 实例的挂载元素 el 和数据对象`data`都还没有进行初始化，还是一个 `undefined`状态
  - created: 此时 vue 实例的数据对象`data`已经有了，可以访问里面的数据和方法， `el`还没有，也没有挂载`dom`
  - beforeMount: 在这里 vue 实例的元素`el`和数据对象都有了，只不过在挂载之前还是虚拟的`dom`节点
  - mounted: vue 实例已经挂在到真实的`dom`上，可以通过对 `dom`操作来获取`dom`节点
  - beforeUpdate: 响应式数据更新时调用，发生在虚拟`dom`打补丁之前，适合在更新之前访问现有的 `dom`，比如手动移除已添加的事件监听器
  - updated: 虚拟`dom`重新渲染和打补丁之后调用，组成新的 `dom`已经更新，避免在这个钩子函数中操作数据，防止死循环。
  - beforeDestory: vue 实例在销毁前调用，在这里还可以使用，通过`this`也能访问到实例，可以在这里对一些不用的定时器进行清除，解绑事件。
  - destoryed：vue 实例销毁后调用，调用后所有事件监听器会被移除，所有的子实例都会被销毁。
- Vue 中的的通信方式有几种？隔代组件的通信你用那种方式解决？
  总共有 7 种，当时是只回答了 4 种
  - props/\$emit 适用父子组件通信
  - ref 与 parent/children 适用父子组件通信
  - EventBus(事件总线) 适用于父子、隔代、兄弟组件通信
  - attrs/listeners 适用于隔代组件通信
  - provide/inject 适用于隔代组件通信
  - vuex 适用于父子、隔代、兄弟组件通信
  - slot 插槽方式
- Vue 中的常见指令有那些？？
  v-text/v-html/v-for/v-show/v-if/v-else/v-cloak/v-bind/v-on/v-model/v-slot...
- 谈谈你对 vuex 的理解？
  vuex 是一个专门为 vue.js 开发的状态管理模式，每一个 vuex 应用核心就是 store(仓库)。store 基本上就是一个容器，它包含着你的应用中大部分的 state(状态)
  - `vuex`的状态存储是响应式的，当 `vue`组件中 store 中读取状态时候，若`store`中的状态发生变化，那么相应的组件也会相应地得到高效更新。
  - 改变`store`中的状态的唯一途径就是显示 `commit`(提交)`mutation`，这样使得我们可以方便地跟踪每一个状态的变化。
    主要有以下几个模块：
  - State: 定义了应用状态的数据结构，可以在这里设置默认的初始状态
  - Getter: 允许组件从`Stroe`中获取数据， `mapGetters`辅助函数仅仅是将`store`中的`getter`映射到计算属性。
  - Mutation: 唯一更改`store`中状态的方法，且必须是同步函数。
  - Action: 用于提交`muatation`, 而不是直接变更状态，可以包含任意异步操作。
  - Module: 允许将单一的`store`拆分为多个 `sotre`且同时保存在单一的状态树中
- vuex 中`state`存储的数据如果页面刷新此时数据还会有吗?
- v-bind 和 v-model 的区别， v-model 原理知道吗？
  v-bind 用来绑定数据和属性以及表达式
  v-model 使用在表单中，实现双向数据绑定的，在表单元素外不起使用。
  v-model 原理：我们在 vue 项目中主要使用 v-model 指令在表单 input、textarea、select、等表单元素上创建双向数据绑定， v-model 本质上就是 vue 的语法糖，v-model 在内部为不同的输入元素使用不同的属性并抛出不同的事件：
  - `text`和 `textarea`元素使用 value 属性和 input 事件
  - `checkbox`和 `radio`使用`checked`属性和 change 事件
  - `slect`字段将 `value`作为`prop`并将 change 作用事件
    <input v-model="something">
    本质上相当于这样
    <input v-bind:value="something" v-on:input="something = $event.target.value">
    其实就是通过绑定一个 something 属性，通过监听 input 事件，当用户改变输入框数据的时候，
    通过事件传递过来的事件对象中的 target 找到事件源，value 属性表示事件源的值，从而实现双向数据绑定的效果
- MVC 和 MVVM 有什么区别？？
  **「MVC」**
  - M - Model：模型，是应用程序中用于处理应用程序数据逻辑的部分，通常模型对象负责在数据库中存取数据
  - V - View: 视图，是应用程序中处理数据显示的部分，通常视图是依据模型数据创建的。
  - C - Controller: 控制器, 是应用程序中处理用户交互的部分，通常控制器负责从视图读取数据，控制用户输入，并向模型发送数据。
    ![图片](https://mmbiz.qpic.cn/mmbiz/XP4dRIhZqqX2uXkcficYZicefWj6UaCf7kXZxVzn1kCZARMdeEUWr2SxfjH3VoCQucS4aTqicrTC5y4avCev1nz2Q/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
  - View 接受用户交互请求
  - View 将请求转交给 Controller 处理
  - Controller 操作 Model 进行数据更新保存
  - 数据更新保存之后，Model 会通知 View 更新
  - View 更新变化数据使用户得到反馈
    **「MVVM」**
  - M - Model，Model 代表数据模型，也可以在 Model 中定义数据修改和操作的业务逻辑
  - V - View，View 代表 UI 组件，它负责将数据模型转化为 UI 展现出来
  - VM - ViewModel，ViewModel 监听模型数据的改变和控制视图行为、处理用户交互，简单理解就是一个同步 View 和 Model 的对象，连接 Model 和 View
    ![图片](https://mmbiz.qpic.cn/mmbiz/XP4dRIhZqqX2uXkcficYZicefWj6UaCf7kAIhIPNdO7oVibYF6ZfCH81wMf0IhRrVfQOX83ejQYpT35VbTiaiaWEUlg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
  - View 接收用户交互请求
  - View 将请求转交给 ViewModel
  - ViewModel 操作 Model 数据更新
  - Model 更新完数据，通知 ViewModel 数据发生变化
  - ViewModel 更新 View 数据
    **「两者的区别」**
  - ViewModel 替换了 Controller 在 UI 层之下
  - ViewModel 向 View 暴露了它所需要的数据和指令
  - ViewModel 接收来自 Model 的数据
    > 概括起来就是，MVVM 由 MVC 发展而来，通过在 Model 之上而在 View 之下增加一个非视觉的组件将来自 Model 的数据映射到 View 中。

### 其他

1.  前端的异常处理有做过嘛？？做过哪些？

遇到这个问题我是蒙的，说实话真本地没想过面实习会问到我异常处理问题。我当时只讲了

- js 中的编码错误异常
- http 请求异常
- Promise 异常的处理

其实还有很多种，我连`window.error`来捕获运行错误都没讲

如何优雅处理前端异常？

1.  cookie、SessionStroage、LocalStroage 这三者的区别。

回答这个问题的时候我没答好，讲到最后自己都没听明白，之间自己还做过笔记(可见复习的重要性，做过的笔记一定要多看，不然也就没有意义了)

- 存储大小

Cookie4K, Stroage5M

- 存储有效期

Cookie 有有效期的限制，而 Storage 没有，sessionStorage 只在窗口关闭会消失 LocalStorage 始终有效即使浏览器关闭也有，是存储在硬盘中的。存储位置：`C:\Users\你的计算机名\AppData\Local\Google\Chrome\User Data\Default\Local Storage\leveldb`

- 作用域不同

sessionStorage 不在不同的浏览器窗口共享，即使是同一个页面，LocalStorage 在所有同源窗口中都是共享的，cookie 也是在所以同源窗口共享。

Cookie、LocalStorage 与 SessionStorage 的区别在哪里？

1.  对于 http 请求有了解过嘛？常见的状态码都有那些？405 是什么？

> HTTP 网络状态码(STATUS) 根据状态码能够清楚的反映出当前交互的结果及原因

- 200 OK 成功(最理想的状态)
- 301 Moved Permanently 永久转移（永久重定向）
- 302 Move temporarily 临时转移
- 304 Not Modified 设置缓存
- 400 Bad Request 请求参数错误
- 401 Unauthorized 无权限访问
- 404 Not Found 找不到资源(最不理想的状态)
- 405 Method Not Allowed 请求行中指定的请求方法不能被用于请求相应的资源，但是该响应必须返回一个 Allow 头信息来表示出当前资源能够接受请求方法的列表。
- 500 Internal Server Error 未知的服务器错误
- 503 Service Unavailable 服务器超负荷

> 2xx 状态码一般是前端人员的锅，5xx 一般是后台人员的锅，学会看问题出在哪里很重要，对以后工作中的甩锅有很大帮助。

1.  浏览器缓存知道吗？

浏览器缓存也就是 HTTP 缓存机制，其机制是根据 HTTP 报文的缓存标识进行的，缓存分为两种：

- 强制缓存
- 协商缓存

**「强制缓存」**

> 当浏览器向服务器发送请求的时候，服务器会将缓存规则放入 HTTP 响应的报文的 HTTP 头中和请求结果一起返回给浏览器，控制强制缓存的字段分别是 Expires 和 Cache-Control，其中 Cache-Conctrol 的优先级比 Expires 高。

**「协商缓存」**

> 协商缓存就是强制缓存失效后，浏览器携带缓存标识向服务器发起请求，由服务器根据缓存标识决定是否使用缓存的过程

强制缓存优先于协商缓存进行，若强制缓存生效则直接使用缓存，若不生效则进行协商缓存，协商缓存由服务器决定是否使用缓存，若协商缓存失效，那么代表该请求的缓存失效，重新获取请求结果，再存入浏览器缓存中；生效则返回 304，继续使用缓存

浏览器缓存机制

1.  原生 Ajax 和 axios 的区别，Ajax 怎么发送 http 请求的？

原生 Ajax 是根据 `XMLHttpRequest`发 HTTP 请求，而 axios 是根据 Ajax 进行封装的插件，其内部利用 Promise 实现，很好的解决的异步请求回调地狱的问题。

后者的问题其实就是问 Ajax 发送请求的五个步骤，这个过于基础就不讲了。

1.  get 请求和 post 请求有什么区别？？

**「GET」**

- 一般用于获取数据
- 基于 URL 地址传参，所以有个长度限制(一般在 8KB 左右)，如果超过就会被截掉
- 因为 GET 请求基于问号传参容易被劫持，所以相对不安全。
- 会产生不可控制的缓存，POST 不会

**「POST」**

- 一般用于新增数据
- 基于请求传参，理论上没有任何限制(真实项目中会自己做大小限制，防止上传过在信息导致请求迟迟完不成)
- PSOT 请求基于请求主体传参，相对来说不好被劫持，比较安全

1.  http 和 https 有什么区别？？

这个问题要回答起来能回答半个小时，每个人回答的方向不一样。

我的回答是：HTTP 为超文本传输协议，HTTPS 为安全超文本传输协议，后者是前者的升级，相对比较安全，通过数据加密传输的方式，安全系数比较高，HTTPS 也会作为网站的搜索权重指标，所以 HTTPS 的网站在排名中也更有优势。

1.  后端能删除前端设置的 cookie 吗？

我回答是不可以的，我也不知道是不是对的，百度了一圈也没有答案。。。有知道的大佬可以在评论区回答下。

1.  常见布局有几种方式？

- 弹性布局(rem/em)
- 栅格化布局
- 百分比布局
- 浮动布局
- ...

网上有很多种，可以自己去搜，这里就不多讲了。

1.  rem 和 em 有区别嘛? 1em 等于多少像素

rem 和 em 单位一样，都是一个相对单位，不同的是 em 是相对于元素的`父元素`的 font-size 进行计算，rem 是相对于 `根元素`html 的 font-size 进行计算。

> 1em 相当于当前元素父元素的 font-size

    举个栗子
    <style>
     .box {
       font-size: 18px;
     }
     .box .children {
       width: 2rem; // 相当于2 * 18 = 36px
     }
    </style>
      <div class="box">
      <span class="children">里面</span>
    </div>

1.  git 用过吧？常见的命令有哪些？如果让你来负责一个项目你怎么让管理你的仓库？

**「常用命令」**

    # 创建版本库：
    - git clone
    - git init

    # 查看配置
    git config -l // 查看全部
    git conig --global -l // 查看仓库中人员名和邮箱
    git config user.name xxx // 设置
    git config user.email xxx // 设置

    # 修改和提交
    git status
    git diff // 查看变更内容
    git add .
    git mv
    git rm
    git commmit -m

    # 查看提交历史
    git log
    git log <file> // 查看该文件每次提交的记录
    分支操作
    git branch // 查看当前分支
    git checkout -b // 添加一个新分支并切换过去

    # 远程操作
    git remote -v // 查看远程分支
    git remote add <remoteURL> // 添加远程分支

最后说了下我管理库的方式：首先我会在 gitHub 上创建一个仓库，为当前项目中每位开发人员取一个对应的分支，让其在对应的分支开发。然后 clone 我这个仓库。当队员需要向 gitHub 上传代码时，需要先将自己的代码同步到自己远程仓库对应的分支中，再切换到要本地的主分支将自己本地开发的分支代码进行合并，如果有冲突先在本地解决，最后再同步到远程的主分支 复制代码\`

### 场景题

1.  如果有一张很大的图片放到线上, 显示要很久, 你会怎么优化?

我当时只回答了这两点，其他的我也不知道。。。

- 用延迟加载技术
- 优化图片的大小

1.  如果让你对 element-ui 中的表单进行二次动态封装，你会怎么做？

对于这种题我回答的贼差，不敢误人子弟，这里分享一个错的文章 组件化页面：封装 el-form

1.  项目中遇到过那些复杂的业务场景，怎么解决的？

这个就看个人回答了，不同的项目遇到的问题也不一样。

1.  封装组件你有什么好的想法

对于这个问题我是蒙的，可能是因为我简历上写了很好的组件化开发思想吧（说实话当时的回答有点打脸)，我是从代码方面回答的。

通过 vue.extend，vue.component 注册这种方式找到项目通用的模块，指定通用部分代码，props 传值，并且通过 slot 来自由定制内容，然后创建 vue 文件。

对于这种问题网上也没有好的回答，欢迎大佬在下方评论交流。

1.  在众多表单中都需要用到点击查询按钮根据参数的不同来弹出一个查询框，里面有个小列表,查到数据后点一行再回显， 你怎么封装这个组件? (就是多个页面中需要查询显示数据列表)

我说下我的大概思路，首先分析需求：需要什么？

- 一个 form 表单，一个 table，分页
- n 个条件框，查询按钮、重置按钮、其他功能按钮。。

需要实现的功能

- 查询
- 点击分页后查询数据
- 重置
- 选中一行后拿到数据
- 其他功能的触发

最后确定那些数据是需要外部传入就 ok 了。

- HTML5 有哪些新特性？
- Doctype 作⽤? 严格模式与混杂模式如何区分？它们有何意义?
- 如何实现浏览器内多个标签页之间的通信？
- ⾏内元素有哪些？块级元素有哪些？空(void)元素有哪些？⾏内元 素和块级元素有什么区别？
- 简述⼀下 src 与 href 的区别？
- cookies,sessionStorage,localStorage 的区别？
- HTML5 的离线储存的使用和原理？
- 怎样处理 移动端 1px 被 渲染成 2px 问题？
- 浏览器是如何渲染页面的？
- iframe 的优缺点？
- Canvas 和 SVG 图形的区别是什么？
- 谈一谈 meta 标签？
- 请你讲一讲 CSS 的权重和优先级
- 介绍 Flex 布局，flex 是什么属性的缩写：
- CSS 怎么画一个大小为父元素宽度一半的正方形？
- CSS 实现自适应正方形、等宽高比矩形
- 实现两栏布局的方式
- 实现三列布局的方式
- CSS 动画有哪些？
- 用 css2 和 css3 分别写一下垂直居中和水平居中
- visibility 和 display 的差别（还有 opacity)
- opacity 可以有过渡效果嘛？
- BFC 与 IFC 区别
- BFC 会与 float 元素相互覆盖吗？为什么？举例说明
- 了解 box-sizing 吗？
- 什么是 BFC
- 了解盒模型吗？
- 清除浮动有哪些方法？
- 写代码：实现函数能够深度克隆基本类型
- 事件流
- 事件是如何实现的？
- new 一个函数发生了什么
- new 一个构造函数，如果函数返回 `return {}` 、 `return null` ， `return 1` ， `return true` 会发生什么情况？
- 闭包是什么？
- 闭包产生的本质
- 一般如何产生闭包
- 闭包的应用场景
- 什么是作用域？
- 什么是作用域链？
- JS 隐式转换，显示转换
- 了解 this 嘛，bind，call，apply 具体指什么
- 手写 bind、apply、call
- setTimeout(fn, 0)多久才执行，Event Loop
- js 脚本加载问题，async、defer 问题
- 如何判断一个对象是不是空对象？
- <script src=’xxx’ ’xxx’/>外部 js 文件先加载还是 onload 先执行，为什么？
- 怎么加事件监听
- 事件传播机制（事件流）
- 说一下原型链和原型链的继承吧
- 说下对 JS 的了解吧
- 如何判断数组类型
- 函数中的 arguments 是数组吗？类数组转数组的方法了解一下？
- 用过 TypeScript 吗？它的作用是什么？
- PWA 使用过吗？serviceWorker 的使用原理是啥？
- ES6 之前使用 prototype 实现继承
- 如果一个构造函数，bind 了一个对象，用这个构造函数创建出的实例会继承这个对象的属性吗？为什么？
- 知道 ES6 的 Class 嘛？Static 关键字有了解嘛
- 事件循环机制 （Event Loop）
- 手写题：数组扁平化
- 手写题：实现柯里化
- 手写题：数组去重
- let 闭包
- instance 如何使用
- active-class 是哪个组件的属性？嵌套路由怎么定义？
- 怎么定义 vue-router 的动态路由？怎么获取传过来的动态参数？
- vue-router 有哪几种导航钩子？
- scss 是什么？在 vue.cli 中的安装使用步骤是？有哪几大特性？
- v-model 是什么？怎么使用？vue 中标签怎么绑定事件？
- axios 是什么？怎么使用？描述使用它实现登录功能的流程？
- axios+tp5 进阶中，调用 axios.post(‘api/user’)是进行的什么操作？axios.put(‘api/user/8′)呢？
- 什么是 RESTful API？怎么使用?
- vuex 是什么？怎么使用？哪种功能场景使用它？
- mvvm 框架是什么？它和其它框架（jquery）的区别是什么？哪些场景适合？
- 自定义指令（v-check、v-focus）的方法有哪些？它有哪些钩子函数？还有哪些钩子函数参数？
- 说出至少 4 种 vue 当中的指令和它的用法？
- vue-router 是什么？它有哪些组件？
- 导航钩子有哪些？它们有哪些参数？
- Vue 的双向数据绑定原理是什么？
- 请详细说下你对 vue 生命周期的理解？
- 请说下封装 vue 组件的过程？
- 你是怎么认识 vuex 的？
- vue-loader 是什么？使用它的用途有哪些？
- 请说出 vue.cli 项目中 src 目录每个文件夹和文件的用法？
- vue.cli 中怎样使用自定义的组件？有遇到过哪些问题吗？
- 聊聊你对 Vue.js 的 template 编译的理解？
- Vuex 是什么？为什么使用 Vuex？
- vuejs 与 angularjs 的区别？
- vue 为什么不直接操作 dom？
- 你怎么理解 vue 是一个渐进式的框架？
- Vue 声明组件的 state 是用 data 方法，那为什么 data 是通过一个 function 来返回一个对象，而不是直接写一个对象呢？
- 说下 vue 组件之间的通信？
- vue 中 mixin 与 extend 区别？
- HTTP 缓存
- HTTP 常用的状态码及使用场景？
- 你知道 302 状态码是什么嘛？你平时浏览网页的过程中遇到过哪些 302 的场景？
- HTTP 常用的请求方式，区别和用途？
- 你对计算机网络的认识怎么样
- HTTPS 是什么？具体流程
- 三次握手和四次挥手
- 在交互过程中如果数据传送完了，还不想断开连接怎么办，怎么维持？
- 你对 TCP 滑动窗口有了解嘛？
- WebSocket 与 Ajax 的区别
- 了解 WebSocket 嘛？
- HTTP 如何实现长连接？在什么时候会超时？
- Fetch API 与传统 Request 的区别
- POST 一般可以发送什么类型的文件，数据处理的问题
- TCP 如何保证有效传输及拥塞控制原理。
- http 知道嘛？哪一层的协议？（应用层）
- OSI 七层模型和 TCP/IP 四层模型
- TCP 协议怎么保证可靠的，UDP 为什么不可靠？
- HTTP 2 改进
- DDOS 攻击
- 算法
  **链表**
  - 前序遍历判断回文链表
  - 合并 K 个升序链表
  - K 个一组翻转链表
  - 环形链表
  - 排序链表
  - 相交链表
    **字符串**
  - 【面试真题】最长回文子串【双指针】
  - 最长公共前缀【双指针】
  - 无重复字符的最长子串【双指针】
  - 【面试真题】最小覆盖子串【滑动窗口】
    **数组问题**
  - 【面试真题】俄罗斯套娃信封问题【排序+最长上升子序列】
  - 最长连续递增序列【快慢指针】
  - 最长连续序列 【哈希表】
  - 寻找两个正序数组的中位数【双指针】
  - 删除有序数组中的重复项【快慢指针】
  - 和为 K 的子数组【哈希表】
  - 跳跃游戏【贪心算法】
    **二叉树**
  - 二叉树的最近公共祖先
  - 二叉搜索树中的搜索
  - 删除二叉搜索树中的节点
  - 完全二叉树的节点个数
  - 二叉树的锯齿形层序遍历
    **排序算法**
  - 用最少数量的箭引爆气球
  - 合并区间【排序算法+区间问题】
    **二分查找**
  - 判断子序列【二分查找】
  - 在排序数组中查找元素的第一个和最后一个位置【二分搜索】
  - 最长递增子序列
  - 【面试真题】 零钱兑换
  - 【面试真题】 最长公共子序列
  - 编辑距离
  - 【面试真题】最长回文子序列
  - 【面试真题】最大子序和
  - 【面试真题】 买卖股票的最佳时机
    **BFS**
  - 打开转盘锁
  - 二叉树的最小深度
    **栈**
  - 最小栈【栈】
  - 下一个更大元素
  - 【面试真题】有效的括号
  - 简化路径
    **DFS**
  - 岛屿的最大面积
  - 相同的树
    **回溯算法**
  - N 皇后
  - 全排列
  - 括号生成
  - 复原 IP 地址
  - 子集
- 不用 sort 实现排序，比如输入 [3,2,6,9,1,4,8] 返回排序后的数组
- 请 js 实现一个 permute 函数，输入数字 123， 打印出这三个数字的全排列
- 平时设计过组件吗
  这个考察组件化的知识，vue 和 react 都是组件化最热门的框架，我们如果能抽离框架，展示组件化的思想，就是满分答案 我们用很常见的评级 rate 组件举例
  "★★★★★☆☆☆☆☆".slice(5 - rate, 10 - rate);
- 谈一下你对 SPA 的理解
- webpack
  - cdn
  - publicPath
  - nginx
  - 由 nginx 进行维护
  - server
  - location
  - vue-cli 自己的
  - 自己修改的？
- 权限
- 协商缓存和强缓存
  - last-modified
  - etag
- 防盗链
  - referer
  - 原理: **<https://q.shanyue.tech/fe/%E5%89%8D%E7%AB%AF%E5%B7%A5%E7%A8%8B%E5%8C%96/257.html>**
- cors
- 怎么查看请求方的 IP 地址 ❎
- - **<https://q.shanyue.tech/base/http/285.html>**
  - IP
  - TCP

- CSP ❎

- - 内容安全策略

- Data URL

- - base64? ❎
  - dataurl 不一定是 base64 的

- HSTS ❎

- - **<https://q.shanyue.tech/base/http/604.html>**

- postman

- - 接口调试

-

-

-

- 1.  CICD 优化，从八分钟到二分钟

  2.  1.  为什么变快
      2.  pnpm 更快一些 ✅
      3.  多进程
      4.  限制范围 -> 增量打包
      5.  webpack5 cache ✅
      6.  node_modules

  3.  1.  四个 JOB？
      2.  并行 Pipeline
      3.  缓存加速 npm i -> Gitlab CI
      4.  私有仓库
      5.  build
      6.  npm -> yarn
      7.  rancher
      8.  Docker 构建前端的优化

  4.  脚手架

  5.  1.  eslint/prettier/style-lint
      2.  代码风格统一

  6.  hooks

  7.  1.  与直接使用 lodash.debounce 的区别 ✅
      2.  useUpdate
      3.  useLocalstorage
      4.  useFix -> IphoneXFix ?
      5.  useCountdown
      6.  useDebouce
      7.  useScoll
      8.  useMount

  8.  JSSDK

  9.  1.  数据平台
      2.  xhr/image/sendBeacon 上报
      3.  前端错误的上报
      4.  往哪里上报？

  10. koa

  11. 白屏时间过长

  12. 1.  OSS
      2.  阿里内网？
      3.  CDN 上的 JSON 数据

  13. 院校列表卡顿

  14. 1.  虚拟列表优化

  15. 打印 PDF 的分页问题

  16. 1.  page-break-before

  17. webpack 个性化配置及优化

  18. 1.  作用域提升

  19. 项目水印功能

  20. 1.  canvas
      2.  mutation observer

  21.

# 一道 JS 基础编程题（闭包）

题目：

    var foo = function(...args) {
        // 要求实现函数体
    }

    var f1 = foo(1,2,3); f1.getValue();
    // 6 输出是参数的和

    var f2 = foo(1)(2,3); f2.getValue();
    // 6

    var f3 = foo(1)(2)(3)(4); f3.getValue();
    // 10

解答：

    function foo(...args) {
      const target = (...arg1s) => foo(...[...args, ...arg1s])
      target.getValue = () => args.reduce((p, n) => p+ n, 0)
      return target
    }

题目：前端在后台管理系统经常会用到目录树，求下面目录 tree 的高度。

得出 depth 即为树的高度得出 depth 即为树

    const tree = {
      name: 'root',
      children: [
        { name: '叶子1-1' },
        { name: '叶子1-2' },
        {
          name: '叶子2-1',
          children: [{
            name: '叶子3-1',
            children: [{
              name: '叶子4-1'
            }]
          }]
        }
      ]
    }

    function getDepth(tree) {
      let depth = 0

      if (tree) {
        let arr = [tree]
        let temp = arr
        while (temp.length) {
          arr = temp
          temp = []
          for (let i = 0; i < arr.length; i++) {
            if (arr[i].children && arr[i].children.length) {
              for (let j = 0; j < arr[i].children.length; j++) {
                temp.push(arr[i].children[j])
              }
            }
          }
          depth++
        }
      }
      return depth
    }console.log(getDepth(tree)); //输出4

1.  定义变量 depth 为 0 得出 depth 即为树的高度得出 depth 即为树

2.  定义一个空数组 temp,然后遍历 tree，如果 tree 有 children，就 push 到 temp 里面

3.  开始 while 循环，如果 temp 长度不为 0，depth++；如果 temp 长度为 0，停止

如果还有更好的解法，欢迎评论区留言。

### 思路：

得出 depth 即为树的高度得出 depth 即为树

1.  定义变量 depth 为 0
2.  定义一个空数组 temp,然后遍历 tree，如果 tree 有 children，就 push 到 temp 里面
3.  开始 while 循环，如果 temp 长度不为 0，depth++；如果 temp 长度为 0，停止
4.  得出 depth 即为树的高度

每日算法：删除字符串中出现次数 >= 2 次的相邻字符

    输入："abbbaca"
    输出："ca"
    解释："abbbaca" => "aaca"=>"ca"

#### 解答

    /**
     * 删除字符串中出现次数 >= 2 次的相邻字符
     * @param {string}s
     */
    function removeDuplicate(s) {
      const stack = [] // Space: O(n)
      let top
      let next
      let i = 0
      while (i < s.length) { // Time: O(n)
        top = stack[stack.length - 1]
        next = s[i]
        if (next === top) {
          // 字符串中出现了相邻字符
          // 1. 移除栈顶字符
          // 2. 移动指针, 指向下一个不同的字符
          stack.pop()
          while (s[i] === top) i += 1
        } else {
          stack.push(next)
          i += 1
        }
      }

      return stack.join('')  // Time: O(n)
    }

- 时间复杂度: O(n), n 为字符的个数
- 空间复杂度: O(n), 栈所用的空间

前端工程化专栏: **<https://q.shanyue.tech/engineering/>**
面试题库: **<https://q.shanyue.tech/>**

- 手动打包上传服务器

- - node_modules/.bin
  - package.json ✅
  - bin
  - prepare
  - postinstall
  - rsync/scp
  - npm run dist -> scp
  - oss?
  - 如何自动去做？npm script hook
  - npm run build: webpack

- package-lock.json/yarn.lock

- - 锁定版本
  - 如何只保留一个存在？

- 组件库

- - npm publish 之前忘记了 npm run build 怎么办？
  - iview/elementui 二次封装
  - 根据组件路径单独引入
  - dist/ ❎

- umd

- - **<https://cdn.jsdelivr.net/npm/vuetify@latest/>**
  - **<https://npm.devtool.tech/vuetify>**
  - **<https://cdn.jsdelivr.net/npm/element-plus@latest/>**
  - 可支持打 esm/umd 多份
  - 可在 npm.devtool.tech 查看 treeshaking 支持的徽章
  - 模块化方案: **<https://q.shanyue.tech/engineering/475.html>**
  - commonjs/window
  - tree shaking 友好？
  - rollup
  - 一些更好打包方案的组件库

- npm publish 的过程

- - prepare
  - 如何发包: **<https://q.shanyue.tech/engineering/754.html>**
  - semver: **<https://q.shanyue.tech/engineering/534.html>**
  - npm version patch/minor/major
  - 如何修改 version ❎
  - npm publish 之前忘记了 npm run build 怎么办？

-

-

-

-

- http cache

  2.  1.  etag
      2.  last-modified
      3.  etag 与 last-modified 的区别
      4.  `stat .`
      5.  版本 ❎
      6.  file system (操作系统)
      7.  强缓存
      8.  协商缓存

- http status code -> **<https://developer.mozilla.org/en-US/docs/Web/HTTP/Status>**
  200 300 304 400 402 (Payment) 403 404 500
- HTTP2
- connection: keep-alive -> http1.1 multiplex

  10. 1.  data-src -> src
      2.  Astro -> 300k->30k 极致的首屏优化

- 路由懒加载 (import)
- 服务器时间差值
- Promisify
- 判断是否为数组

  18. vue3/vite/webpack

  19. vite

  20. 1.  esm
      2.  HMR
      3.  如何支持 commonjs

  21. webpack ()

  22. 1.  commonjs -> bundle

  23. tree-shaking

  24. 1.  预编译

  25. vue3

  26. 1.  Proxy
      2.  虚拟 DOM 优化 -> static node?

  27. 工具

  28. 1.  DataURL 预览: **<https://devtool.tech/dataurl>**

## 第一场

- CSS

- - 左侧固定，右侧自适应 flex
  - grid `300px 1fr`

- css specifity

- css +/\~ ❎

- 表格单行/双行

- - `:nth-child(2n)`

- 长宽比 `2:1` ✅

- - padding-bottom (无法放 content)
  - aspect-ratio

- 伪类与微元素的区别

- - \::before
  - \::selection ❎

- 跨域

- - webpack-dev-server
  - nginx
  - jsonp
  - cors
  - proxy

- data url

- - base64
  - svg ❎

- prefetch/preload ✅

- cjs/esm

- package.json

- - vue3
  - ^1.2.3
  - \~1.2.3
  - main
  - exports ❎
  - version/semver ✅
  - devDep
  - peerDep ✅

- webpack

- - cache
  - thread
  - swc-loader
  - 提升构建速度

- js 压缩代码

- - 空格
  - 变量名缩短
  - 预计算
  - terser

- tree shaking

- - { a: 3, b: 4 }
  - vite
  - ESM
  - commonjs -> esm ✅
  - json tree shaking

- http

- - 304
  - 206
  - 204
  - 201
  - 401
  - 405
  - 429 -> Rate Limit ❎

- http2

- - ws 的区别
  - header
  - 多路复用
  - Frame/Stream/Message
  - Server Push (index.html) ❎

- ws

- koa / node->stream

- - /api/users/\:userId -> 正则
  - path-to-regexp -> 前缀树
  - Content-Type
  - cors
  - body-parser ❎
  - router

- webpack 体积优化

- - webpack-bundle-analyzer
  - terser
  - gzip/brotli -> not webpack

- vue3

- - Proxy/define

- ES6 Proxy

- - 代理
  - 不可变数据 -> immer.js

## 未录到的一场

- 跨域
  - CORS
  - JSONP
  - Proxy
- CSS
  - class/attribute
  - CSS Scope
  - BEM
  - attribute
  - calc(100%/3)
  - flex: 1
  - grid
  - 布局三等分
  - 如何避免样式冲突
  - 优先级 ❎
- webpack
  - commonjs
  - esm ->
  - umd
- package.json
  - main
  - module
  - exports -> q.shanyue.tech/engineering/535.html
- http
  - 404
  - 403
  - 304
  - 204
  - 201 Created ❎
  - 401
  - 406 ❎
  - 429
  - cache
  - status code
- webpack 压缩 Javascript 体积
  - express-static
  - accept-encoding
  - terser
  - tree shaking
  - gzip (nginx)
  - css
  - webpack-bundle-analyzer
  - polyfill -> preset-env
- webpack 加载 css
  - css-loader
  - style-loader
  - extract css -> webpack5 目前已经支持
- webpack 减小打包体积
  - babel-loader -> swc
  - tsloader -> type check
  - cache
  - 多进程
- semver
  - ^1.2.3
  - \~1.2.3
- 幽灵依赖 ❎ - 重复依赖 -> pnpm
- pnpm 是如何处理 ❎
- nodejs/koa/洋葱模型
  - 中间件
  - body-parser/stream/raw-body ❎
  - cors vary
- CICD
- Github Action (免费)
  - COS
  - Github 管理项目
  - 前端在哪里部署？
- 持续交付
- 版本管理/Tag/Release
- 质量检查 (PR)

  - husky (git hooks) ❎
  - ci 的时机
  - sync
  - `.git/hooks/precommit`
  - lint-staged -> Stage
  - git index/stage/head
  - git hooks 是如何工作的
  - \[open、sync\_\*\*]
  - N 个分支走到 dev 环境是否无法上线
  - PR/feature/xxx 新功能分支
  - dev 测试环境
  - staging 预发布环境
  - master 会做吗？❎
  - on: pull_request and feature/\*\*
  - lint
  - test
  - prettier
  - commit-msg
  - 多个阶段
  - 自动关掉 PR
  - Approving + CI Success 才能进行合并 ❎
  - 为什么这么做？(当 CI 失败时自动关掉)
  - WIP:
  - CI 失败: -> 策略

- Code Review

- - 两个人合并

- Preview/Review App ❎

- - k8s/Deployment
  - docker-compose/service name

- - environment
  - Docker/Label/docker-compose/service ❎

- Integration

- - 企业微信

- ChangeLog

- Artifact

- 如何自动部署

- - only_files

- 如何回滚

- 如何跳过 git hooks

- - 干掉 eslint 插件 ❎
  - `git commit --no-verify` ❎

- 如何回滚

- - 生产环境与测试环境隔离开 ❎

- - bucket
  - 目录以分支命名
  - 仅仅备份 index.html/public

- changelog

- - CI？
  - release-it

- 性能优化

- - 时间
  - 体积
  - 分包
  - 运行时

- - 不需要再前端去做 gzip

- - imagemin-webpack
  - 懒加载

- - Image\[width=600]
  - CDN 实现一个 Image 组件
  - next.js/Image
  - gatsby/Image

- - 更快
  - 六个 ❎

- - 节点服务器/region

- - 域名分片
  - http2/stream/

- - 编译期预计算 / 自动会做 ❎
  - `const day = 365 * 24 * 3600`
  - `function sum(); const s = sum(x, y)`

- - `const day = 65xxxx`

- - `const s = 10`

- - JS/CSS -> terser/cssnano
  - CDN ?
  - 图片
  - gzip ❎

- - initial/async(import())

- - minChunks
  - runtimeChunk -> webpack

- - webpack 魔法注释

- - prefetch
  - preload

- - import()
  - splitChunks/分包策略
  - chunks: 'all' 是什么意思

- - lighthouse

- - 构建优化

- 主题色插件开发

- - emotion
  - style components
  - vanilla-extract

- - shade

- - elementUI
  - css-in-ts

1.  ESM

2.  1.  browserslist
    2.  \[].at -> corejs -> 垫片
    3.  **<https://github.com/Fyrd/caniuse#readme>**
    4.  caniuse-lite
    5.  caniuse-db 数据库所在
    6.  **<https://q.shanyue.tech/engineering/734.html>**
    7.  ?.
    8.  a?.b?.c -> a
    9.  **<https://babeljs.io/repl>**
    10. IIFE
    11. webpack
    12. 二者区别: **<https://q.shanyue.tech/engineering/475.html>**
    13. import/export
    14. importmap
    15. rollup 与 webpack 打包后的区别: **<https://q.shanyue.tech/engineering/729.html>**
    16. 打包后的模块化方案
    17. babel
    18. 满足谷歌浏览器的最近五个版本

3.  pinia/vuex

4.  vite

5.  1.  依赖预构建: **<https://cn.vitejs.dev/guide/dep-pre-bundling.html>**
    2.  xxx -> esm
    3.  性能: lodash-es 有 600 多个模块，将会发送 600 多个请求，可预编译打包为一个
    4.  esm
    5.  热更新为什么特别快
    6.  预编译?

6.  http 2.0 新特性

7.  1.  frame 格式(**「字节问过」**): **<https://httpwg.org/specs/rfc7540.html#rfc.section.4.1>**
    2.  ws
    3.  十种 (**「字节问过」**)
    4.  frame 类型: **<https://httpwg.org/specs/rfc7540.html#FrameTypes>**
    5.  streamid
    6.  多路复用
    7.  二进制帧的格式
    8.  stream

8.  pnpm

9.  1.  pnpm 的优势: **<https://q.shanyue.tech/engineering/751.html>**
    2.  如何解决体积过大的问题
    3.  幽灵依赖问题

业务介绍

- 用户:角色:菜单
- 审批流程
- toB/内部使用？

验证码的验证流程

- key: 随机数 -> 随 cookie 先传到前端
- value: 验证码
- blob
- content-type\:application/octet-stream
- octet-stream 是什么?: **<https://q.shanyue.tech/base/http/134.html>**
- 验证码图片的渲染流程？
- 验证码的验证过程 redis
  如何把二进制搞成 blob 的
- **<https://github.com/axios/axios>**
- responseType: 'blob', // default ❎
- **<https://developer.mozilla.org/en-US/docs/Web/API/Blob/Blob>**: new Blob(\[new Uint8Array(buffer, byteOffset, length)]);
- content-type\:application/octet-stream
- 二进制流响应是什么 ？
- arrayBuffer -> Blob 如何转化 ❎
- Response API -> res.json()
- TypedArray/Uint8Array ❎

对前端登录数据进行基础校验以及 base64 加密

- guid
- jwt

base64

- 编码后会边长还是变短？❎

- 工作原理: **<https://devtool.tech/base64>**

- PC Web

- - 系统级应用开发
  - 架构如何:
  - **<https://www.electronjs.org/blog/webview2>**
  - **<https://tauri.studio/docs/about/architecture>**
  - **<https://github.com/tauri-apps/tauri#comparison-between-tauri-and-electron>**

- - 微信 h5
  - electron
  - electron 开发与后台管理开发有何不一样
  - uniapp
  - 跨端得以实现的原理

- nuxt

- nest
  - SSG/SSR: **<https://nuxtjs.org/docs/concepts/server-side-rendering>**
- 前端工程化流程，从开发到部署

- webpack/rollup(gulp)

- - 业务用 webpack
  - 库用 rollup，好处: 生成无模板代码，esm 友好，可打多份

- vite/webpack

- - lodash
  - 预构建做了什么: **<https://cn.vitejs.dev/guide/dep-pre-bundling.html>**
  - vite 依赖预构建

- 公共组件开发

- - 基于第三方封装
  - 私有服务器
  - eslint 封装

- - 开闭原则: 添加一个新的功能，应该通过在已有代码的基础上进行扩展来实现，而不是修改已有代码。

- 智能⽹关过滤器代码

- 如何设计组件

- - Swith
  - sass 控制变量
  - 什么是 headless component ?
  - tippyjs: **<https://github.com/atomiks/tippyjs-react>**
  - headlessui: **<https://headlessui.dev/>**
  - 好处逻辑行为与 UI 分离 **<https://freesgen.hashnode.dev/headless-components-in-vue>**
  - 示例
  - 通用性
  - 样式

- 如何动态加载组件

- - import()

- nest 依赖注入和控制反转的实现

- nest 的生命周期

- - **<https://docs.nestjs.cn/8/fundamentals?id=%e7%94%9f%e5%91%bd%e5%91%a8%e6%9c%9f%e4%ba%8b%e4%bb%b6>**

- 每日算法：给定两个数组，编写一个函数来计算它们的交集

```javascript
const intersection = function (nums1, nums2) {
  return [...new Set(nums1.filter((item) => nums2.includes(item)))]
}
```

来源：<https://github.com/sisterAn/JavaScript-Algorithms>

- 场景题：提交表单，常用的方法有哪些？应用层，通信层发生了哪些过程？
- post 和 get 的区别，列举一下
- http 常见的响应码，拒绝服务资源是哪个（403）
- 说一说这个系统是如何判断机制的（前端鉴权）
- 你刚才说了三方 OAuth，讲一讲内在原理吧
- 说说 https 的内在原理，ssl 握手过程
- 为什么要用非对称密钥，pms 呢？公钥怎么了？
- 说一说响应式布局吧？
- 响应式背后的浏览器原理你知道吗？（不太知道）
- 旋转动画 css，怎么去做？（animation+rotate）
- dom 树和 cssom 树原理也说一下吧
- 为什么 link 要在前，script 标签要在后面呢？原理
- 场景题：保证浏览器不受脚本的恶意攻击，（xss 攻击，解决方法）
- 假如说你的富文本编辑器内部要显示脚本，该怎么办呢？（不太清楚，我就尽可能说）
- 说说 async 和 await 的 es5 实现（我尽可能地说了一点）
- 场景题：这里有 cat 和 animal 子类和父类，如何进行 es5 继承，至少说出 5 种。
- 说说你项目做的 Vue spa 首屏优化吧（按需引入，懒加载路由，gzip 压缩，关闭一些插件...）
- 说说 webpack 打包构建在实际项目中的优化算法
- 场景题：数型系统，包含字符串关键词，如何对其作出效率很好的搜索？（balabala 说了自己的一些看法，lz77 算法，后来翻了翻算法书，应该结合 B 树来说）
- 编程题：请使用 js 函数写出 markdown 转 html 的文本编辑器。（2 个小时）
- 算法题：在一个字符串中，找到最大不连续子字符串的长度。
- 说说你 element-ui 的按需引入吧
- 说说 webpack 打包优化具体干了什么？为什么要这么做呢？（Dllplugin，happypack）
- prerender-spa-plugin 插件你用过？具体说一说吧
- SEO 优化你做了？具体讲一讲吧 追问：你 seo 排名怎么样了？（没有进展）
- 我记得 NUXT.js 也可以做渲染和 seo 吧？了解 SSR 吗
- 小程序有碰到过复杂一点的业务场景吗？（说了数据列表懒加载处理 setData 优化问题）
- 小程序的框架你有了解吗？要不说说几个？
- 你了解过的前沿技术来说一说？（Vue3.0，Flutter，Serverless，Typescript）
- 说说 Vue3.0 和 2.x 的双向数据绑定（object.definePorperty 和 Proxy）
- 说说你最感兴趣的前端方向（跨端解决方案 Flutter、React Native...）
- 有这么一个功能场景，老师随机点名，上堂课没来的同学被抽到的概率会大幅增加，怎么去做？
- 还有一个功能场景，你的博客系统如何分享文章？
- 还有一个功能场景，你可不可以做一个在线提交作业的平台，让老师不仅可以收到作业，还可以在平台上对作业进行批改？说说具体技术实现。。。
- 详细地讲讲 Vue 的首屏优化，具体的技术点
- 优化有过量化评级吗？说说具体为多少？怎么去做的？
- 有一个问题，你如何去确定哪一种方式是对整个首屏渲染优化起到最关键作用的？
- 我们现在回过头来，你可不可以按照软件开发的流程模块再来详细地说说博客的整体优化？各个方面的性能优化？（设计，编码，打包部署，上线体验。。。说了一部分）
- 预渲染 prerender-spa-plugin 能详细讲讲？
- 你了解了原理，那么你引入这个 prerender 插件对于整个项目的架构产生了什么样的特别影响？（讲了路由冲突）
- 对于上线后的用户体验，你打算怎么做改进？
- 功能层面是这样，技术层面可以来说说？
- 数据列表的懒加载这个说的好，那有这么一个场景，你提交了新的文章，由用户在刷你的博客，你怎么让用户通过一定的事件=来查看你的新文章，不要通过页面整体刷新，还是以动态引入的方式？
- 我们再次回到刚才项目的性能优化这个点上？在你解决首屏的时候，在网络通信的每个阶段，哪个阶段是性能开销的最大的地方，优化后有何变化？如何解决？
- SEO 怎么做的，讲一讲技术细节
- 你有对你的用户群体做过数据的量化统计吗？说说你有什么样的思路，如何去利用好这些数据？
- 这边有个问题，如果单纯地通过前端来分析用户的行为，开销会非常大，你有什么好办法？说说思路
- 如果过了很长时间，有人问你，一个高性能的博客页面该如何搭建，你会按照什么样的逻辑取来跟他分析这些零碎繁杂的性能优化？
- 好了，博客项目只是你个人对于技术的探索，你还有没有学校里真正拥有用户的实际项目呢？说说看
- 功能描述的很详细，这里有个问题，总所周知，二维码有一定的时效性，可传播性，如何防范那些没来同学也扫到二维码了？说说方法
- 没来的学生，你们就会采取这种单一的方案吗？还有没有别的？
- 在这个团队对于项目的功能构建中，你起到了什么作用呢？
- 你刚才说到了前后端分离，讲讲你和后台同学如何落实好前后端分离的？
- 对于后台的数据接口，经常会发生一些分歧，你们团队是怎么化解这种分歧的，有没有一种方式增进团队之间的沟通？
- 你的博客网站，难道没有分析过用户的行为吗？对于用户量很大的情况下，难道没有做过性能分析吗？
- 对于首屏中的 FP，FCP，FMP，TTI 你又分别去做量化的考虑吗？
- 对了，你如何通过代码来分析首屏的 FCP 时间？
- 除了这些，难道就没有进一步优化吗？
- prerender 预渲染是什么原理呀？
- 这样的一种插件引入，为整个性能提升又带来了多少量化的参考呢？你有去研究过吗？
- 说说你拥有的实际用户量的项目吧？
- 这个小程序已经上线对吧？你们团队有没有对这个小程序做过用户行为的调研呢？
- 我想要知道的是在程序里面有代码去自动去分析用户的行为吗？
- 我看你懂 Vue，React 有学过一些吗？系统地说一说两者的区别
- Vue 如何解析 template 模板，diff 算法两者的不同是什么？？
- 详细地说说前端的动画种类？
- canvas 有了解过吗？它适用于什么样的场景？
- 谈一谈 `css` 盒模型
- 多种方式实现上面 `100px` 下面自适应的布局
- `display` 都有哪些属性
- 块元素和行内元素、行内块元素的区别
- `js` 原型和原型链
- `Person.prototype.constructor` 是什么
- 函数有没有 `__ proto __` 属性
- 如何判断数据类型的多种方式，有什么区别，适用场景
- `Promise` 如何一次进行多个异步请求
- 如果想要其中一个请求出错了但是不返回结果怎么办
- `webpack` 打包优化知道多少
- 大前端了解吗
- `koa` 如何启动一个服务器
- `new koa` 都做了什么
- `koa` 洋葱圈模型原理
- `koa` 洋葱圈和 `express` 中间件有什么区别
- 长列表优化，一万条数据不用分页和懒加载，如何提升性能
- 数据请求从发起到接收数据之间发生了什么
- 前端安全了解吗
- `csrf` 和 `xss` 是什么，如何避免
- 前端怎样对用户的数据进行加密传输
- 基于 `md5` 提升安全性
- 谈一谈 `css` 盒模型 【面试题解】CSS 盒子模型与 margin 负值
- 多种方式实现上面 `100px` 下面自适应的布局
  - `flex` 布局
  - `gird` 布局
  - `margin-top + calc`
  - `定位 + calc`
- `display` 都有哪些属性
  | 值 | 描述 |
  | :--------------: | :--------------------------------------------------: |
  | **none** | 此元素不会被显示。 |
  | **block** | 此元素将显示为块级元素，此元素前后会带有换行符。 |
  | **inline** | 默认。此元素会被显示为内联元素，元素前后没有换行符。 |
  | **inline-block** | 行内块元素。 |
  | **table** | 此元素会作为块级表格来显示，表格前后带有换行符。 |
  | **inherit** | 规定应该从父元素继承 display 属性的值。 |
  | **flex** | 弹性盒模型。 |
  | **grid** | 网格布局。 |
- 块元素和行内元素、行内块元素的区别
- 块级元素
  **（1）常见的块元素有哪些？**
  常见的块元素有`<h1>~<h6>、<p>、<div>、<ul>、<ol>、<li>`等，其中 `<div>` 标签是最典型的块元素。
  **（2）块级元素有什么特点？**
  - 自己独占一行
  - 高度，宽度、外边距以及内边距都可以控制。
  - 宽度默认是容器（父级宽度）的 `100%`
  - 是一个容器及盒子，里面可以放行内或者块级元素
    **（3）注意问题：**
    只有文字才能组成段落，因此 `p` 标签里面不能放块级元素，特别是 `p` 标签不能放 `div`。同理还有这些标签`h1,h2,h3,h4,h5,h6,dt` ，他们都是文字类块级标签，里面不能放其他块级元素。
- 行内元素
  **（1）常见行内元素有哪些？**
  常见的行内元素有 `<a>、<strong>、<b>、<em>、<i>、<del>、<s>、<ins>、<u>、<span>` 等，其中 `<span>` 标签最典型的行内元素，也称内联元素。
  **（2）行内元素有哪些特点？**
  - 相邻行内元素在一行上，一行可以显示多个
  - 高、宽直接设置是无效的
  - 只可以设置水平方向的外边距
  - 默认宽度就是它本身内容的宽度
  - 行内元素只能容纳文本或则其他行内元素
    **（3）注意问题：**
    链接里面不能再放链接。
    特殊情况 `a` 里面可以放块级元素，但是给 `a` 转换一下块级模式最安全。
- 行内块元素
  **（1）常见行内块儿元素有哪些？**
  在行内元素中有几个特殊的标签 `<img />、<input />、<td>`，可以对它们设置宽高和对齐属性，有些资料可能会称它们为行内块元素。
  **（2）行内块元素有什么特点？**
  - 和相邻行内元素（行内块）在一行上,但是之间会有空白缝隙，一行可以显示多个。
  - 默认宽度就是它本身内容的宽度。
  - 高度，行高、外边距以及内边距都可以控制。
- 块级元素、行内元素和行内块元素的区别
  | **元素模式** | **元素排列** | **设置样式** | **默认宽度** | **包含** |
  | :----------: | :--------------------: | :--------------------: | :--------------: | :----------------------: |
  | 块级元素 | 一行只能放一个块级元素 | 可以设置宽度高度 | 容器的 100% | 容器级可以包含任何标签 |
  | 行内元素 | 一行可以放多个行内元素 | 不可以直接设置宽度高度 | 它本身内容的宽度 | 容纳文本或则其他行内元素 |
  | 行内块元素 | 一行放多个行内块元素 | 可以设置宽度和高度 | 它本身内容的宽度 | |
- 块级元素、行内元素和行内块元素互转
  - 块转行内：`display:inline`;
  - 行内转块：`display:block`;
  - 块、行内元素转换为行内块：`display: inline-block`;
- `js` 原型和原型链 深入 JavaScript 系列（六）：原型与原型链
- `Person.prototype.constructor` 是什么
  Person.prototype.constructor === Person // true
- 函数有没有 `__ proto __` 属性
  ```javascript
  let fn = function () {}
  // 函数（包括原生构造函数）的原型对象为Function.prototype
  fn.__proto__ === Function.prototype // true
  ```
  函数都是由 `Function` 原生构造函数创建的，所以函数的 `__proto__` 属性指向 `Function` 的 `prototype` 属性。
- `Promise` 如何一次进行多个异步请求
  答：利用 `Promise.all` 。
- `Promise.all` 的返回机制是什么
  除了 `Promise.all` ，还有其他几个原型方法也要知道。
  👉👉 **看了就会，手写 Promise 原理，最通俗易懂的版本！！！**
- 如果想要其中一个请求出错了但是不返回结果怎么办
  答：使用 `Promise.allSelectd` 。
- `webpack` 打包优化知道多少 玩转 webpack，使你的打包速度提升 90%
- `koa` 如何启动一个服务器

  ```javascript
  const Koa = require('koa')
  const app = new Koa()

  app.use(async (ctx) => {
    ctx.body = 'Hello World'
  })

  app.listen(3000)
  ```

- `new koa` 都做了什么
  - 构建上下文 `ctx`
  - 构建洋葱圈模型。
- `koa` 洋葱圈模型原理 浅析 koa 的洋葱模型实现
- `koa` 洋葱圈和 `express` 中间件有什么区别
- 长列表优化，一万条数据不用分页和懒加载，如何提升性能
- 数据请求从发起到接收数据之间发生了什么
- `csrf` 和 `xss` 是什么，如何避免
- 前端怎样对用户的数据进行加密传输
  答：`md5`，我其实不太了解，只是用 `md5` 做过登录注册的密码加密，也不会别的了。
- 基于 `md5` 提升安全性
  答：`md5（md5）`，我开玩笑的，有没有大佬可以指点一下。
- 说一下 `vue` 有哪些优点和特点
- 什么是虚拟 `dom`
- `vue` 组件间传值的 `n` 种方式
- `vue` 有哪些内置指令
- `v-show` 和 `v-if` 有什么区别
- 如何让 `CSS` 只在当前组件中起作用
- 如何解决 `vue` 初始化页面闪动问题
- 什么是 `SPA`，有什么优点和缺点
- `vue` 首屏渲染优化有哪些
- `vue` 生命周期函数有哪些
- 第一次页面加载会触发哪几个钩子
- 在哪个生命周期中发起数据请求
- `vue-router` 有几种模式
- `hash` 和 `history` 有什么区别
- `vuex` 有哪些属性
- `git` 常用命令了解哪些
- 搭一个新项目的框架,需要考虑哪些问题
- 如何做权限认证
- 如何做 `mock` 数据
- 说一下 `vue` 有哪些优点和特点
  - **渐进式框架**：可以在任何项目中轻易的引入；
  - **轻量级框架**：只关注视图层，是一个构建数据的视图集合，大小只有几十 `kb` ；
  - **简单易学**：国人开发，中文文档，不存在语言障碍 ，易于理解和学习；
  - **双向数据绑定**：在数据操作方面更为简单；
  - **组件化**：很大程度上实现了逻辑的封装和重用，在构建单页面应用方面有着独特的优势；
  - **视图，数据，结构分离**：使数据的更改更为简单，不需要进行逻辑代码的修改，只需要操作数据就能完成相关操作；
- 什么是虚拟 `dom`
  `Virtual DOM` 是 `DOM` 节点在 `JavaScript` 中的一种抽象数据结构，之所以需要虚拟 `DOM`，是因为浏览器中操作 `DOM` 的代价比较昂贵，频繁操作 `DOM` 会产生性能问题。
  虚拟 `DOM` 的作用是在每一次响应式数据发生变化引起页面重渲染时，`Vue` 对比更新前后的虚拟 `DOM`，匹配找出尽可能少的需要更新的真实 `DOM`，从而达到提升性能的目的。
  虚拟 `DOM` 的实现原理主要包括以下 **3** 部分：
- 用 `JavaScript` 对象模拟真实 `DOM` 树，对真实 `DOM` 进行抽象；
- `diff` 算法 — 比较两棵虚拟 `DOM` 树的差异；
- `pach` 算法 — 将两个虚拟 `DOM` 对象的差异应用到真正的 `DOM` 树。
- `vue` 组件间传值的 `n` 种方式
  **（1）`props / $emit` 适用 父子组件通信**
  **（2）`ref` 适用 父子组件通信**
  - `ref`：如果在普通的 `DOM` 元素上使用，引用指向的就是 `DOM` 元素；如果用在子组件上，引用就指向组件实例
    **（3）`$parent` / `$children` / `$root`：访问父 / 子实例 / 根实例**
    **（4）`EventBus （$emit / $on）` 适用于 父子、隔代、兄弟组件通信**
    这种方法通过一个空的 `Vue` 实例作为中央事件总线（事件中心），用它来触发事件和监听事件，从而实现任何组件间的通信，包括父子、隔代、兄弟组件。
    **（5）`$attrs`/`$listeners` 适用于 隔代组件通信**
  - `$attrs`：包含了父作用域中不被 `prop` 所识别 (且获取) 的特性绑定 ( `class` 和 `style` 除外 )。当一个组件没有声明任何 `prop` 时，这里会包含所有父作用域的绑定 ( `class` 和 `style` 除外 )，并且可以通过 `v-bind="$attrs"` 传入内部组件。通常配合 `inheritAttrs` 选项一起使用。
  - `$listeners`：包含了父作用域中的 (不含 `.native` 修饰器的) `v-on` 事件监听器。它可以通过 `v-on="$listeners"` 传入内部组件
    **（6）`provide / inject` 适用于 隔代组件通信**
    祖先组件中通过 `provide` 来提供变量，然后在子孙组件中通过 `inject` 来注入变量。`provide / inject API` 主要解决了跨级组件间的通信问题，不过它的使用场景，主要是子组件获取上级组件的状态，跨级组件间建立了一种主动提供与依赖注入的关系。
    **（7）`Vuex` 适用于 父子、隔代、兄弟组件通信**
    `Vuex` 是一个专为 `Vue.js` 应用程序开发的状态管理模式。每一个 `Vuex` 应用的核心就是 `store`（仓库）。`store` 基本上就是一个容器，它包含着你的应用中大部分的状态 ( `state` )。
  - `Vuex` 的状态存储是响应式的。当 `Vue` 组件从 `store` 中读取状态的时候，若 `store` 中的状态发生变化，那么相应的组件也会相应地得到高效更新。
  - 改变 `store` 中的状态的唯一途径就是显式地提交 `(commit) mutation`。这样使得我们可以方便地跟踪每一个状态的变化。
    **（8）插槽**
    `Vue3` 可以通过 `usesolt` 获取插槽数据。
    **（9）`mitt.js` 适用于任意组件通信**
    Vue3`中移除了`$on`，`$off`等方法，所以 `EventBus`不再使用，相应的替换方案就是`mitt.js
- `vue` 有哪些内置指令
  ![图片](https://mmbiz.qpic.cn/sz_mmbiz/H8M5QJDxMHrs1Gic0ynJLEPic2w3wOg5I1s4xNKCZnmsC4fvPKLMbATRSZOZ63G6dq5gz6j03ic8vNG1ckKLbAyzg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1)
- `v-show` 和 `v-if` 有什么区别
- **手段**：`v-if` 是动态的向 `DOM` 树内添加或者删除 `DOM` 元素；`v-show` 是通过设置 `DOM` 元素的 `display` 样式属性控制显隐；
- **编译过程**：`v-if` 切换有一个局部编译/卸载的过程，切换过程中合适地销毁和重建内部的事件监听和子组件；`v-show` 只是简单的基于 `css` 切换；
- **编译条件**：`v-if` 是惰性的，如果初始条件为假，则什么也不做；只有在条件第一次变为真时才开始局部编译; `v-show` 是在任何条件下，无论首次条件是否为真，都被编译，然后被缓存，而且 `DOM` 元素保留；
- **性能消耗**：`v-if` 有更高的切换消耗；`v-show` 有更高的初始渲染消耗；
- **使用场景**：`v-if` 适合运营条件不大可能改变；`v-show` 适合频繁切换。
- 如何让 `CSS` 只在当前组件中起作用
  在组件中的 `style` 标签中加上 `scoped`
- 如何解决 `vue` 初始化页面闪动问题
  使用 `vue` 开发时，在 `vue` 初始化之前，由于 `div` 是不归 `vue` 管的，所以我们写的代码在还没有解析的情况下会容易出现花屏现象，看到类似于 `{{message}}` 的字样，虽然一般情况下这个时间很短暂，但是我们还是有必要让解决这个问题的。
  首先：在 `css` 里加上 `[v-cloak] { display: none; }` 。如果没有彻底解决问题，则在根元素加上 `style="display: none;" :style="{display: block }"`
- 什么是 `SPA`，有什么优点和缺点
  `SPA` 仅在 `Web` 页面初始化时加载相应的 `HTML`、`JavaScript` 和 `CSS`。一旦页面加载完成，`SPA` 不会因为用户的操作而进行页面的重新加载或跳转；取而代之的是利用路由机制实现 `HTML` 内容的变换，`UI` 与用户的交互，避免页面的重新加载。
  **优点：**
  - 用户体验好、快，内容的改变不需要重新加载整个页面，避免了不必要的跳转和重复渲染；
  - 有利于前后端职责分离，架构清晰，前端进行交互逻辑，后端负责数据处理；
    **缺点：**
  - 初次加载耗时多：为实现单页 `Web` 应用功能及显示效果，需要在加载页面的时候将 `JavaScript`、`CSS` 统一加载，部分页面按需加载；
  - 不利于 `SEO`：由于所有的内容都在一个页面中动态替换显示，所以在 `SEO` 上其有着天然的弱势。
- `vue` 首屏渲染优化有哪些
  - 图片压缩/懒加载
  - 禁止生成 `.map` 文件
  - 路由懒加载
  - `cdn` 引入公共库
  - 开启 `GZIP` 压缩
- `vue` 生命周期函数有哪些
  `Vue` 的生命周期钩子核心实现是利用发布订阅模式先把用户传入的的生命周期钩子订阅好（内部采用数组的方式存储）然后在创建组件实例的过程中会一次执行对应的钩子方法（发布）。
- `beforeCreate`：是 `new Vue()` 之后触发的第一个钩子，在当前阶段 `data`、`methods`、`computed` 以及 `watch` 上的数据和方法都不能被访问。
- `created`：在实例创建完成后发生，当前阶段已经完成了数据观测，也就是可以使用数据，更改数据，在这里更改数据不会触发 `updated` 函数。可以做一些初始数据的获取，在当前阶段无法与 `Dom` 进行交互，如果非要想，可以通过 `vm.$nextTick` 来访问 `Dom`。
- `beforeMount`：发生在挂载之前，在这之前 `template` 模板已导入渲染函数编译。而当前阶段虚拟 `Dom` 已经创建完成，即将开始渲染。在此时也可以对数据进行更改，不会触发 `updated`。
- `mounted`：在挂载完成后发生，在当前阶段，真实的 `Dom` 挂载完毕，数据完成双向绑定，可以访问到 `Dom` 节点，使用 `$refs` 属性对 `Dom` 进行操作。
- `beforeUpdate`：发生在更新之前，也就是响应式数据发生更新，虚拟 `dom` 重新渲染之前被触发，你可以在当前阶段进行更改数据，不会造成重渲染。
- `updated`：发生在更新完成之后，当前阶段组件 `Dom` 已完成更新。要注意的是避免在此期间更改数据，因为这可能会导致无限循环的更新。
- `beforeDestroy`：发生在实例销毁之前，在当前阶段实例完全可以被使用，我们可以在这时进行善后收尾工作，比如清除计时器。
- `destroyed`：发生在实例销毁之后，这个时候只剩下了 `dom` 空壳。组件已被拆解，数据绑定被卸除，监听被移出，子实例也统统被销毁。
- 第一次页面加载会触发哪几个钩子
  beforeCreate`，`created`，`beforeMount`，`mounted
- 在哪个生命周期中发起数据请求
  可以在钩子函数 `created`、`beforeMount`、`mounted` 中进行调用，因为在这三个钩子函数中，`data` 已经创建，可以将服务端端返回的数据进行赋值。
  推荐在 `created` 钩子函数中调用异步请求，有以下优点：
  - 能更快获取到服务端数据，减少页面 `loading` 时间；
  - `ssr` 不支持 `beforeMount` 、`mounted` 钩子函数，所以放在 `created` 中有助于一致性；
- `vue-router` 有几种模式
  `vue-router` 有 3 种路由模式：`hash`、`history`、`abstract`：
  - **hash**: 使用 `URL hash` 值来作路由。支持所有浏览器，包括不支持 `HTML5 History Api` 的浏览器；
  - **history** : 依赖 `HTML5 History API` 和服务器配置。
  - **abstract** : 支持所有 `JavaScript` 运行环境，如 `Node.js` 服务器端。如果发现没有浏览器的 `API`，路由会自动强制进入这个模式.
- `hash` 和 `history` 有什么区别
  **（1）hash 模式的实现原理**
  早期的前端路由的实现就是基于 `location.hash` 来实现的。其实现原理很简单，`location.hash` 的值就是 `URL` 中 `#` 后面的内容。比如下面这个网站，它的 `location.hash` 的值为 `#search`：
  https://www.word.com#search
  `hash` 路由模式的实现主要是基于下面几个特性：
  - `URL` 中 `hash` 值只是客户端的一种状态，也就是说当向服务器端发出请求时，`hash` 部分不会被发送；
  - `hash` 值的改变，都会在浏览器的访问历史中增加一个记录。因此我们能通过浏览器的回退、前进按钮控制 `hash` 的切换；
  - 可以通过 `a` 标签，并设置 `href` 属性，当用户点击这个标签后，`URL` 的 `hash` 值会发生改变；或者使用 `JavaScript` 来对 `loaction.hash` 进行赋值，改变 `URL` 的 `hash` 值；
  - 我们可以使用 `hashchange` 事件来监听 `hash` 值的变化，从而对页面进行跳转（渲染）。
    **（2）history 模式的实现原理**
    `HTML5` 提供了 `History API` 来实现 `URL` 的变化。其中做最主要的 `API` 有以下两个：`history.pushState()` 和 `history.repalceState()`。这两个 `API` 可以在不进行刷新的情况下，操作浏览器的历史纪录。唯一不同的是，前者是新增一个历史记录，后者是直接替换当前的历史记录，如下所示：
    window.history.pushState(null, null, path);
    window.history.replaceState(null, null, path);
    `history` 路由模式的实现主要基于存在下面几个特性：
  - `pushState` 和 `repalceState` 两个 `API` 来操作实现 `URL` 的变化 ；
  - 我们可以使用 `popstate` 事件来监听 `url` 的变化，从而对页面进行跳转（渲染）；
  - `history.pushState()` 或 `history.replaceState()` 不会触发 `popstate` 事件，这时我们需要手动触发页面跳转（渲染）。
- `vuex` 有哪些属性
  有五种，分别
  - **State**：定义了应用状态的数据结构，可以在这里设置默认的初始状态。
  - **Getter**：允许组件从 `Store` 中获取数据，`mapGetters` 辅助函数仅仅是将 `store` 中的 `getter` 映射到局部计算属性。
  - **Mutation**：是唯一更改 `store` 中状态的方法，且必须是同步函数。
  - **Action**：用于提交 `mutation`，而不是直接变更状态，可以包含任意异步操作。
  - **Module**：允许将单一的 `Store` 拆分为多个 `store` 且同时保存在单一的状态树中。
- `git` 常用命令了解哪些
- 搭一个新项目的框架,需要考虑哪些问题
- 如何做权限认证
  答：在路由守卫中根据 `url` 地址结合 `token` 做权限认证。
- 如何做 `mock` 数据
  答：可以使用 `mock.js`
- `css` 如何实现一个幻灯片效果
- 手写表格
- `ajax` 是什么?有什么优缺点
  `ajax` 是一种创建交互网页应用的一门技术。
  优点：
- 实现局部更新(无刷新状态下)，
- 减轻了服务器端的压力
  缺点：
- 破坏了浏览器前进和后退机制(因为 `ajax` 自动更新机制)
- `ajax` 请求多了，也会出现页面加载慢的情况。
- 搜索引擎的支持程度比较低。
- `ajax` 的安全性问题不太好(可以用数据加密解决)。
- 同步和异步的区别
  **同步：** 同步的思想是：所有的操作都做完，才返回给用户。这样用户在线等待的时间太长，给用户一种卡死了的感觉（就是系统迁移中，点击了迁移，界面就不动了，但是程序还在执行，卡死了的感觉）。这种情况下，用户不能关闭界面，如果关闭了，即迁移程序就中断了。
  **异步：** 将用户请求放入消息队列，并反馈给用户，系统迁移程序已经启动，你可以关闭浏览器了。然后程序再慢慢地去写入数据库去。这就是异步。但是用户没有卡死的感觉，会告诉你，你的请求系统已经响应了。你可以关闭界面了。
- `WEB` 应用从服务器主动推送 `Data` 到客户端有哪些方式
  轮询
  WebSocket
- 经常遇到的浏览器的兼容性问题有哪些?原因是什么?如何解决
  由于我的公司是一个致力于培养用户习惯的公司，遇到兼容问题都是**请下载最新版本谷歌浏览器**😝，所以我这个其实没有什么实际的经验，只知道 `babel` 和 `postcss` 。
- 有哪些常用的 `hack` 技巧
- 谈谈你对 `webpack` 的看法
- 主流的前端框架的优缺点是什么
  只用过 `vue` ，优点上面讲过了，缺点嘛，可能就是不支持 `IE8` 。
- 如何消除一个数组里面重复的元素
  - `set`
  - `reduce`
  - `for循环`
  - 能实现方式有很多，原理都是对比两个数组，没有就放进去。
- `css` 如何实现一个幻灯片效果
- 一般请求后端接口，你都怎么弄？
- 你的后端要给你什么样的信息，你才能请求成功呢？
- 请求参数有什么格式？
- 如何给后端传递一个文件？
- 你如何理解前端工程化?
- 要买个电脑，找 `A` 借 `1k`，找 `B` 借 `2K`，找 `C` 借 `3K`，拿着六千块钱买电脑，抽象成前端的逻辑就是请求不同的接口获取数据，拿到所有的数据之后进行展示，这个怎么实现？
- 不使用 `promise.all` , `async/await` 怎么实现?
- `promise.all` 和 `async/await` 有什么区别?
- `promise.all` 是为了解决什么问题?
- 有一批不定数量的人，第一个人去超市买一个东西，第一个人买回来以后第二个人再去买，第二个回来以后第三个再去买，抽象成前端的逻辑如何实现？（其实他想听的答案就是递归，结果我把洋葱圈原理讲了一遍）
- 如何删除事件监听，一个元素绑定了多个事件，你怎么确认删除的是哪个？
- 你都如何调试代码？（这个阶段就是打开谷歌控制台，一个个讲各种功能都能干什么事）
- 谷歌调试工具你都会用什么功能？
- 怎么进行断点调试？
- 控制台都能干什么事？
- 不熟悉的项目，如何找到接口所在的代码？
- 如果接口地址是动态的呢，是其他接口返回的？
- `localStorage，session，cookie`的区别是什么？
- 然后问了我自己的几个开源项目
- 因为我带了电脑，所以还看了看我的代码
- 一般请求后端接口，你都怎么弄？
  这个问题其实没有搞懂面试官想问什么，参照接口文档发起请求就行了呗，顶多就是再二次封装一个 `axios`。
- 你的后端要给你什么样的信息，你才能请求成功呢？
  请求方式
  请求参数
- 请求参数有什么格式？
  `Query String Parameters`
  `Form Data`
  `Request Payload`
- 如何给后端传递一个文件？
- 你如何理解前端工程化?
- `promise.all` 和 `async/await` 有什么区别?
  答：`Async Await` 是基于 `promise` 实现，是改良版的 `promise`，使代码看起来更加简洁，异步代码执行像同步代码一样。
  答：汇总大量的异步操作结果。
- 如何删除事件监听，一个元素绑定了多个事件，你怎么确认删除的是哪个？
  element.removeEventListener(type，handler，false/true)
  - **type**:事件类型
  - **handler**:事件执行触发的函数
  - **false/true**:`false` 为冒泡 ，`true` 为捕获，参数是 `true`，表示在捕获阶段调用事件处理程序；`如果是false`，表示在冒泡阶段调用事件处理程序。
    需要注意的是，通过匿名函数是无法消除监听事件，只有通过实名函数才能。
- 不熟悉的项目，如何找到接口所在的代码？
  答：可以搜接口的地址。
- `localStorage，session，cookie`的区别是什么？
- 我看你掘金了，简单描述一下 `call`，`apply`，`bind` 有什么区别和应用场景。（说的好像是我不写他就不问了）
- 说一说盒子模型？
- 公司项目负责哪部分功能？
- 表单和表格封装过么？
- 表单是怎么封装的？
- 大数据的表单怎么处理，`select` 选项过多的时候？（优化问题）
- 自己做过脚手架么？
- `vue2` 和 `vue3` 有什么区别？
- 从输入 `url` 到页面渲染完成之间发生了什么？
- 浏览器原理了解过么？
- `http` 状态码都有哪些？
- 前端如何处理这些状态码？
- `localStorage`，`session`，`cookie` 的区别是什么？
- 前端安全问题，`CSRF`，`XSS`
- 如何解决跨域问题？
- 跨域问题实际上改的是 `http` 里面哪个参数？
- `call`，`apply`，`bind` 有什么区别和应用场景
- `vue2` 和 `vue3` 有什么区别
  - 响应式原理
  - 生命周期钩子名称
  - 自定义指令钩子名称
  - 新的内置组件
  - `diff` 算法
  - `Composition API`
- 从输入 `url` 到页面渲染完成之间发生了什么
- 浏览器原理了解过么
- `http` 状态码都有哪些
  状态码第一位数字决定了不同的响应状态，如下：
  - 1 表示消息
  - 2 表示成功
  - 3 表示重定向
  - 4 表示请求错误
  - 5 表示服务器错误
    **1xx**
    代表请求已被接受，需要继续处理，这类响应是临时响应，只包含状态行和某些可选的响应信息，并一空行结束
    常见的有：
  - `100` （客户继续发送请求，这是临时响应） 这个临时响应是用来通知客户端它的部分请求已经被服务器接收，且仍未被拒绝。客户端印当据需发送请求的剩余部分，或者如果请求已经完成，忽略这个响应，服务器必须在请求完成后向客户端发送一个最终响应
  - `101` 服务器根据客户端的请求切换协议，主要用于 `websocket` 或 `HTTP2` 升级
    **2xx**
    代表请求已成功被服务器接收，处理，并接受
  - `200` （成功） 请求已成功，请求所希望的响应头或数据体将随此响应返回
  - `201` （已创建）请求成功并且服务器创建了新的资源
  - `202` （已创建）服务器已经接受请求，但尚未处理
  - `203` （非授权信息）服务器已成功处理请求，但返回的信息可能来自另一来源
  - `204` （无内容）服务器成功处理请求，但没有返回任何内容
  - `205` （重置内容）服务器成功处理请求，但没有返回任何内容
  - `206` （部分内容）服务器成功处理了部分请求
    **3xx**
    表示要完成请求，需要进一步操作，通常这些状态代码用来重定向
  - `300` （多种选择）针对请求，服务器可执行多种操作。
  - `301` （永久移动）请求的网页已永久移动到新位置。
  - `302` （临时移动）服务器目前从不同位置的网页响应请求，但请求者应该继续使用原有位置来进行以后的请求
  - `303` （查看其它位置）请求者应当对不同位置使用单独的 `GET` 请求来检索响应时，服务器返回此代码
  - `305` （使用代理）请求者只能使用代理访问请求的网页。
  - `307` （临时重定向）服务器目前从不同位置的网页响应请求，但请求者应继续使用原有位置来进行以后的请求
    **4xx**
    代表了客户端看起来可能发生了错误，妨碍了服务器的处理
  - `400` （错误请求）服务器不理解请求的语法
  - `401` （未授权）请求要求身份验证。
  - `403` （禁止）服务器拒绝请求
  - `404` （未找到）服务器找不到请求的网页
  - `405` （方法禁用）禁用请求中指定的方法
  - `406` （不接受）无法使用请求的内容特性响应请求的网页
  - `407` （需要代理授权）此状态代码与 `401`（未授权）类似，但指定请求者应当授权使用代理
  - `408` （请求超时）服务器等候请求时发生超时
    **5xx**
    表示服务器无法完成明显有效的请求。这类状态代码代表了服务器在处理请求的过程中有错误或异常状态发生
    - `500` （服务器内部错误）服务器遇到错误，无法完成请求
    - `501` （尚未实施）服务器服务器不具备完成请求的功能
    - `502` （错误网关）服务器作为网关或代理，从上游服务器收到无效响应
    - `503` （服务不可用）服务器目前无法使用，（由于超载或停机维护）
    - `504` （网关超时）服务器作为网关或代理，但是没有及时从上游服务器收到请求
    - `505` （ `HTTP` 版本不受支持）服务器不支持请求中所用的 `HTTP` 协议版本
- 前端如何处理这些状态码
  答：在 `axios` 的请求拦截当中根据不同的状态码进行不同的操作。
- 前端安全问题，`CSRF`，`XSS`
- 跨域问题实际上改的是 `http` 里面哪个参数
  答：`Access-Control-Allow-Origin` ？这个不确定，有大佬可以指点一下。
- `localStorage`，`session`，`cookie` 的区别是什么
- `vuex` 的 `mutation` 和 `action`
- `vuex` 模块化
- 数组深拷贝
- `css` 盒子模型
- `css` 实现斑马线的效果
- 跨域问题
- `localStorage`，`session`，`cookie` 的区别是什么
- `vuex` 的 `mutation` 和 `action`
- `vuex` 模块化
- 数组深拷贝
- `css` 盒子模型
- `css` 实现斑马线的效果
  答：可以通过伪元素，父级元素使用绝对定位，伪元素使用相对定位，大小和父元素一样，位置重合。再利用 `nth-child` 选择器选择奇数行，只给奇数行设置伪元素即可实现。
- `ts` 和 `js` 的优缺点
- `es6` 有哪些新特性
- 遍历数组的 `n` 种方法
- `vue` 生命周期
- `watch` 和 `computed` 区别和使用场景
  **对于 Computed：**
  - 它支持缓存，只有依赖的数据发生了变化，才会重新计算
  - 不支持异步，当 `Computed` 中有异步操作时，无法监听数据的变化
  - 如果一个属性是由其他属性计算而来的，这个属性依赖其他的属性，一般会使用 computed
  - 如果 `computed` 属性的属性值是函数，那么默认使用 `get` 方法，函数的返回值就是属性的属性值；在 `computed` 中，属性有一个 `get` 方法和一个 `set` 方法，当数据发生变化时，会调用 `set` 方法。
    **对于 Watch：**
  - 它不支持缓存，当一个属性发生变化时，它就会触发相应的操作
  - 支持异步监听
  - 监听的函数接收两个参数，第一个参数是最新的值，第二个是变化之前的值
  - 监听数据必须是 `data` 中声明的或者父组件传递过来的 `props` 中的数据，当发生变化时，会触发其他操作
  - 函数有两个的参数：
    - **immediate**：组件加载立即触发回调函数
    - **deep**：深度监听，发现数据内部的变化，在复杂数据类型中使用，例如数组中的对象发生变化。
- `vue3` 和 `vue2` 的区别
- 虚拟 `dom` 和真实 `dom` 的区别
  虚拟 `DOM` 不会进行排版与重绘操作
  虚拟 `DOM` 就是把真实 `DOM` 转换为 `Javascript` 代码
  虚拟 `DOM` 进行频繁修改，然后一次性比较并修改真实 `DOM` 中需要改的部分，最后并在真实 `DOM` 中进行排版与重绘，减少过多 `DOM` 节点排版与重绘损耗
- 组件传值的 `n` 种方式
- 元素水平垂直居中的方法
- `flex` 和 `grid` 有什么区别
- `flex：1` 是什么意思
- 一个父容器，三个子容器，两边的子容器宽度固定，中间自适应，如何实现？
- 说一下闭包和函数柯里化
- 解释一下事件循环，微任务和宏任务都有哪些？
- 解释一下原型链
- 所有的对象都有原型吗？
- `vue` 的生命周期
- 跨域，解决跨域问题的方案
- 说一下 `sourcemap` 都有哪些配置，开发环境和生产环境如何选择？
- 浏览器从输入 `url` 到页面渲染之间做了哪些事情？
- 元素水平垂直居中的方法
- `flex` 和 `grid` 有什么区别
- `flex：1` 是什么意思
- 一个父容器，三个子容器，两边的子容器宽度固定，中间自适应，如何实现？
  - `flex` 布局
  - `grid` 布局
  - `定位 + calc`
- JavaScript 闭包
- 函数柯里化
- 解释一下事件循环，微任务和宏任务都有哪些？
- EventLoop
- 原型与原型链
- 所有的对象都有原型吗？
  答：不是的, 用 `Object.create(null)` 创建的对象没有原型。
- `vue` 的生命周期
- 九种跨域方式实现原理
- 说一下 `sourcemap` 都有哪些配置，开发环境和生产环境如何选择？
- 从输入 URL 到看到页面发生了什么？
- 我看你熟悉 `vue`，那你讲讲 `vue` 的模板编译原理吧
- 讲一讲 `vuex` 的挂载过程
- 讲一讲 `vue-router` 的几种模式和守卫吧
- `vue` 为什么要用 `template` 啊
  答：我说的是书写起来更像原生的 `html` 。
- vuex 的 store 是如何挂载到每个组件中
- vue-router 有几种钩子函数？具体是什么及执行流程是怎样的？
- `nuxt` 怎样配置路由，如何自定义路由，自定义的和约定路由哪个优先级高
  答：约定路由，`nuxt` 内部会根据文件路径自动生成路由，自定义路由不会了。
- `express` 和 `koa` 有什么区别
  **1. 语法区别**
  - `experss` 异步使用 回调
  - `koa1` 异步使用 `generator + yeild`
  - `koa2` 异步使用 `await/async`
    **2. 中间件区别**
  - `koa` 采用洋葱模型，进行顺序执行，出去反向执行，支持 `context` 传递数据
  - `express` 本身无洋葱模型，需要引入插件，不支持 `context`
    **3. 集成度区别**
  - `express` 内置了很多中间件，集成度高，使用省心
  - `koa` 轻量简洁，容易定制
- `ts` 跟 `js`有什么区别，优点和缺点
  - `ts` 是 `js` 的超集，即你可以在 `ts` 中使用原生 `js` 语法。
  - `ts` 需要静态编译，它提供了强类型与更多面向对象的内容。
  - `ts` 最终仍要编译为弱类型，基于对象的原生的 `js`，再运行。
- `CSS` 盒模型
- 一些常用的页面布局要了解
- `es6` 新特性，遍历数组的 `n` 种方法
- `JS` 原型和原型链
- `ts` 跟 `js`有什么区别，特点，优点和缺点
- 浏览器从输入 `url` 到页面渲染之间做了哪些事情
- 什么是跨域问题，如何解决
- 前端安全问题
- 如果你写了自己会 `node`，可能会问 `express` 和 `koa` 的相关问题
- `webpack` 优化
- 如何理解执行上下文
  JavaScript 执行上下文(context)主要指代码执行环境的抽象概念。执行上下文分为三种：
  - 全局执行上下文
  - 函数执行上下文
  - eval 执行上下文
    每一段 js 代码执行，都会先创建一个上下文环境。
- 如何理解原型链
  每个函数都拥有一个 prototype 属性，每个函数**实例对象**都拥有一个**proto**属性，而这个属性指向了函数的 prototype，当我们访问**实例对象**的属性或者方法时，会先从自身构造函数中查找，如果没有就通过**proto**去原型中查找，这个查找的过程我们称之为原型链。（跟作用域链有点像）
- 继承有哪些方法
  - 原型继承
  - 构造继承
  - 实例继承
  - call/apply 继承(组合继承)
  - ES6 使用 class extends 继承
- 什么是深/浅拷贝，有哪些实现方式
  JS 数据类型分别基本数据类型和引用数据类型，基本数据类型保存的是值，引用类型保存的是引用地址(this 指针)。浅拷贝共用一个引用地址，深拷贝会创建新的内存地址。
  - 浅拷贝方法
    - 直接对象复制
    - Object.assign
  - 深拷贝
    - JSON.stringify 转为字符串再 JSON.parse
    - 深度递归遍历
    - 如何准确判断一个对象是数组
- 数组有哪些常用方法
  这个非常多，说起来也很快，我主要考察你会多少，另外也为了引出下一个问题,slice 和 splice 区别
  - push 末尾添加
  - pop 末尾删除
  - shift 首部删除
  - unshift 首部添加
  - concat 数组合并
  - join 数组元素 通过连接符 连接
  - reverse 数组反转
  - sort 数组排序
  - map/forEach/filter/indexOf/includes/slice/splice
    slice 表示截取，slice(start,end)不改变原数组，返回新数组。
    splice 表示删除，splice(start,length,item)，会改变原数组，从某个位置开始删除多个元素，并可以插入新的元素。
- DOM 节点创建和修改有哪些常用 API
  创建节点
  - createElement
  - createTextNode
  - createDocumentFragment(临时节点)
    修改节点
  - appendChild`parent.appendChild(child)`
  - insertBefore `parentNode.insertBefore(newNode,refNode);`
  - removeChild `parent.removeChild(node)`
  - replaceChild
- CSS 清除浮动有哪些方法
  父级元素设置高度，手动撑开
  浮动元素结尾增加空标签，设置 clear:both
  父元素设置 overflow:hidden
  父元素添加伪类:after 和 zoom
- 谈一下 flex 布局
  flex 是一种弹性布局，包含 flex-container 和 flex-item.
  常用的属性包括 flex-direction、flex-wrap、justify-content、align-items
  水平居中 justify-content\:center 水平两头居中 justify-content\:space-between 垂直居中 align-items\:center
- 谈一下盒模型
  盒模型包括：content,padding,border,margin
  盒模型分为：IE 盒模型和标准 w3c 盒模型
  IE 盒模型宽度包含了 padding 和 border，w3c 盒模型宽度就是内容宽度。
- transition 动画和 animation 有什么区别
  他们虽然都可以做出动画效果，但是 transition 主要做简单的过渡效果，而 animation 可以做复杂的动画效果，在语法和用法上有非常大的区别。
- H5 自适应方案
  H5 自适应方案大家在网上能找到很多，我个人推荐一种我非常喜欢的方式，就是 rem. rem 是一种相对单位，它基于 html 的 font-size 值来进行调整。
  通常我们以 750 为基准，我们会在 header 中嵌套一段 js 脚本，获取手机网页分辨率尺寸除以 375，为了方便计算，我们假设 750 像素下 1rem = 100px；所以 我们除以 375 后需要乘以 50.
- call/apply/bind 作用和区别
  他们都可以改变函数的作用域。
  call/apply 可以直接执行该函数，而 bind 不会立刻执行
  call/apply 作用类似，都可以改变指针和执行函数，区别在于传参不同，call 需要单个传参，apply 通过数组传参
- 观察者和发布订阅者区别
  他们都属于观察者模式，只不过有不同的实现方法。发布订阅相比于观察者多了一个调度中心，发布者通过调度中心向订阅者发布消息。观察者模式中目标和观察者相互依赖，观察者订阅目标主题，当目标发生变化后，会通知对应观察者。
- 浏览器解析渲染页面过程
  ![图片](https://mmbiz.qpic.cn/mmbiz_png/YItGPcJZoxlJEp6zdYzg4QSBa8EnZuibaKDPIIVW28DgZREYxJpG6TPgMNt1HP8O7TwksdGWLiculnibrZx6onwJw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
  - 解析 HTML，生成 DOM 树
  - 解析 CSS，生成 CSSOM 树
  - 将 DOM 树和 CSSOM 树关联，生成渲染树(Render Tree)
  - 布局 render 树（Layout/reflow），负责各元素尺寸、位置的计算
  - 绘制 render 树（paint），绘制页面像素信息
  - 将像素发送给 GPU，展示在页面上。(Display)
- 谈一下 EventLoop
  ![图片](https://mmbiz.qpic.cn/mmbiz_png/YItGPcJZoxlJEp6zdYzg4QSBa8EnZuiba9oD1lTooG6MUCVmDEKaflwaydO3FROepECzaPdxhdhfVNkzkrYvIPw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
  这其中大家需要了解几个概念：调用栈、同步/异步任务、宏任务/微任务
  JavaScript 本身是单线程，也就是同一时刻只能干一件事，JS 任务包含了同步任务和异步任务，遇到执行函数会将其放入**调用栈**(先进后出)中，遇到 setTimeout/setInterval 等异步任务时，会把它放入到消息队列中，等主线程的任务执行完成以后，再回过头执行消息队列中的异步任务，如果异步任务中仍然有异步任务，会继续放入消息队列，以此类推，便形成了一个事件循环。
  异步任务：
  - setTimeout
  - setInterval
    异步任务又分为宏任务和微任务，promise 就属于微任务.
- GET 和 POST 有什么区别
  - 大小方面
    - GET 传输一般 2K-8K，IE 限制 2K，，POST 没有大小限制
  - 安全方面
    - GET 通过 url 明文传输，POST 通过 body 传输，本身都不安全，因为 HTTP 就是明文传输。
  - 浏览器记录
    - GET 请求浏览器会记录，POST 不会
  - 浏览器后退
    - GET 无害，POST 会再次提交
  - 浏览器收藏
    - GET 可以收藏，POST 不可以
  - 浏览器缓存
    - GET 可以缓存，POST 不会
  - 编码方式
    - GET 通过 url 编码，POST 支持多种编码
  - TCP 数据包
    - GET 产生一个数据包，POST 产生 2 个数据包
  - 使用方式(习惯上讲)
    - GET 主要拉取数据，POST 主要提交保存数据
- 数组如何去重
  - ES6 Set 去重
  - 利用 Object key 去重
  - 两层循环逐一对比，生成新数组
  - indexOf 去重
  - sort 排序，再单层循环前后对比
- 谈一下常用设计模式，并选择一个进行场景分析 单例模式 工厂模式 观察者模式 适配器模式
  在 Vue 中通过观察者模式触发视图更新。Vue2.x 通过 Object.defineProperty 劫持 data 数据，当数据变化后触发 setter，setter 内部通过订阅器来 notify 消息，notify 会调用 watcher 更新视图。
  当一套前端对接不同后端服务时，会出现数据解构不一致情况，这个时候可以使用适配器模式来兼容不同后端，使他以统一的数据解构对接前端。
- XSS 攻击
- CSRF 攻击
- Sql 注入
- html 脚本注入
- JSONP 跨域（本质是 JS 调用）
- CORS（后台设置）
- Nginx 反向代理（运维配置）
  跨域是浏览器做出的安全限制，必须同协议、同域名、同端口否则会被浏览器 block
  优化策略：减少请求次数、减小资源大小、提高响应和加载速度、优化资源加载时机、优化加载方式
- 合并、压缩、混淆 html/css/js 文件（webpack 实现，减小资源大小）
- Nginx 开启 Gzip，进一步压缩资源（减小资源大小）
- 图片资源使用 CDN 加速（提高加载速度）
- 符合条件的图标做 base64 处理（减小资源大小）
- 样式表放首部，JS 放尾部（JS 单线程，会阻塞页面；资源加载方式）
- 设置缓存（强缓存和协商缓存，提高加载速度）
- link 或者 src 添加 rel 属性，设置 prefetch 或 preload 可预加载资源。（加载时机）
- 如果使用了 UI 组件库，采用按需加载（减小资源大小）
- SPA 项目，通过 import 或者 require 做路由按需（减小资源大小）
- 服务端渲染 SSR，加快首屏渲染，利于 SEO
- 页面使用骨架屏，提高首页加载速度（提高加载速度）
- 使用 JPEG 2000, JPEG XR, and WebP 的图片格式来代替现有的 jpeg 和 png，当页面图片较多时，这点作用非常明显
- 使用图片懒加载-lazyload
- 常见状态码知道哪些？304 403 405 分别是什么
- http 状态码 302 504 分别代表什么意思
- 响应状态码，200(from disk cache)，200（from memory cache），304 的区别。
- POST 和 GET 的区别，除了长度，安全其他的
- http 介绍一下，为什么 http2.0 不普及，websocket 的基本指令，性能
- 爬虫，网站如何去做防止，如何判断
- tcp 和 udp 区别
- 那如果让你做一个视频聊天软件，你用 tcp 还是 udp ？为什么？
- tcp 是怎么去保证可靠传输的？
- tcp 三次握手
- tcp 握手结束第一次的包有多大
- TCP 的超时重传
- TCP 为什么是三次握手呢？
- TCP 如何去终止之前发送报文的？
- tcp 拥塞控制（四部分）
- CDN 的原理是什么
- HTTP 协议，1.1 和 2.0 的区别，了解哪些请求方法，请求/响应头部
- 为什么项目不用 https 以及 http 与 https 的区别
- https 的加密过程以及如何防止中间人攻击
- 为什么 tcp 连接是可靠的（校验和重传）
- 通过什么机制处理服务端接收数据乱序丢包等（滑动窗口和拥塞控制）
- 在 TCP 建立连接后，路由器发生了什么变化
- http 的 header 和 body 讲的很详细 请求方式 请求头内容 状态码
- http2 相关问题。在 http1 的时代，会经常把很多资源部署在不同域名下，为什么？（有可能是减少 cookie 的传输量）
- TCP 和 UDP 的区别和场景，又问如果让你设计一个既保证准确性速度又快的协议，怎么做
- OSI7 层模型 每层大致用处及相关协议
- https ,http2.0，websocket(提了一下)，TLS 握手，怎么知道数字证书的真假
- http2.0 有了解吗？有抓包看看到底什么个情况吗？
- cookie session 区别
- session 怎么保存、有多台服务器，sessionid 怎么找
- 为什么 cookie 可以用来保存登录状态
- http 头部 chunk
- get 发一个 tcp 包，post 发两个 tcp 包，这种情况是一定的吗，什么情况下不是这样
- post 如何把数据放到 url 中
- 一个 http 的报文的头和 body 之间有什么分隔
- 出现 304 的场景，通过什么协议头来确认（304 的响应头）
- websocket 原理，如何实现，和 http 报文结构有哪些不同（注意是结构不是特性）
- cookie，localStorage，sessionStorage 使用和区别
- ca 验证
- wireshark 能抓包到 https 请求的内容吗
- https 怎么预防中间人攻击
- http 请求的过程中怎么知道数据已经发送完毕要断开连接，怎么断开
- 网络的七层模型
- get post head 这些请求方式有什么不同
- 了解轮询和 websocket 吗？
- 说一下 websocket 的四个阶段（websocket 不能使用时要怎么处理、使用什么方式来代替 websocket）
- 进程和线程
- 进程之间的通信知道吗？node 中自己实现过哪种通信？（说了管道，消息队列，套接字，信号量啥的，表示自己不会 node，没实现过，说了浏览器的多个 tag 之间也属于进程通信，表示不满意，不要说应用层上的东西）
- 同源是什么意思，除了那三个没有了么
- 事件冒泡和事件捕获，应用？注意？
- 事件轮询 Eventloop
- 重绘和重排
- URl 到页面加载过程
- 跨域问题，解决，jsonp 原理，不受跨域影响的标签
- Etag 是什么？
- 浏览器储存 cookie，localStorage，sessionStorage 详细区别
- http 缓存，如果缓存还在有效期内，但是资源变更了怎么办
- jsonp 跨域的安全问题
- cors 跨域，要支持两个域名怎么做
- js 会阻塞加载，怎么阻塞的？
- http 缓存更新静态文件的方式
- postmessage
- 浏览器卡顿，你怎么去排除？（服务器到后台都讲了一遍，他告诉我如果数据没问题，是浏览器的问题怎么排除，我说了代码中打断点调试，他不满意，说我 Chrome 的调试工具台掌握很不好）
- PC 浏览器的分布？主流浏览器的版本
- 缓存问题，Etag 和 IF-modify-since 是怎么来的？
- 非同源 cookie 怎么访问
- 如果要你缓存图片你怎么做？
- 有多台服务器，sessionid 怎么找
- 知道哪些前端危险？如何防御
- XSS 的原理，如何防御 XSS？为什么换成实体字符就好了？
- 假如说某链接获取到你的敏感信息，发送奇怪请求到服务器，你怎么去防御？
- 讲一讲 cookie 是怎么发送到服务端，具体过程，尽量详细
- csrf token 能存储在 cookie 里吗？其实是可以的，只要服务端不要去从 cookie 里面取 csrf token 就行
- 黑客是怎么去利用 cookie 的？这个请求到底是怎么构造的？
- http 请求中 option 主要是干什么的
- xss 的原理和防御措施（讲了加强 cookie，过滤输入，过滤输出）
- CSRF 了解过吗，它的攻击流程是怎样的，如何防御（refencer 可不可以被修改、token 可不可以被窃取，既然有漏洞那不是白做了）
- div 里面嵌套一个 tip，当 tip 改变的时候，div 会重新渲染吗，怎么样实现 div 不会重新渲染
- html5 新特性
- HTML 跟 HTML5 的区别（解释了本质区别，框架上的区别）
- web 语义化、语义化标签有哪些、section 标签的作用
- js 的原型和原型链，原型链的终点在哪里？
- 事件委托，详细讲
- es6 新特性，常用语法有哪些
- this 的原理，call，apply，bind 的区别
- 全等和弱等的区别
- 构造函数的原型
- 函数柯里化
- 数组浅拷贝
- 立即执行函数
- 浏览器事件模型, IE 的有什么特殊, 如何兼容(attachEvent 与 addEventListener)
- js 宏任务和微任务
- 数组查找的方法
- class 继承和 js 继承的区别
- {}的原型链
- typeof null 是什么，为什么是这个结果。
- typeof 和 instanceof 有什么区别，说说判断的原理
- 数组里面新加的方法你有用过哪些？
- 微任务有哪些？
- 如何判断 Array 和 Object
- js 精度问题（0.1+0.2==0.3 的问题）
- 讲一下 generator 生成器
- 原型对象的 constructor 指向谁
- dom 规范跟 js 规范有什么区别？
- js 定时器，设置一个时间，会在那个时间之后准时执行吗？
- transition 有什么需要注意的地方？
- js 的错误监控机制有了解吗？
- 闭包，应用
- setTimeout 第二个参数为 0 时和匿名自执行函数区别
- new 操作符之后的操作
- this 指向
- ES6 的使用，相比 ES5 的好处
- ES6 的新特性（变量声明，字符串模板，数组的新方法 flat，函数的默认值、class 继承，await/async 讲的很详细）
- 如果要同时启动两个异步任务，怎么做
- 深拷贝/浅拷贝问题
- 说一下链表的实现
- bind(object).bind(windows) 后的 this 指向
- 构造继承里 Function.call(argu)里传进来的参数 argu 是什么
- async 是什么的语法糖，generator 怎么用
- ajax 有哪些状态，每个状态分别对应什么
- 手动实现一个 ajax，这样实现的方法叫什么
- require 和 import 的区别？AMD、CMD、ES6
- callback 的缺点，Promise 的状态有哪些，generator，async 和 await
- js 溢出怎么解决
- 如何实现私有的方法/属性
- ES5 实现继承的方法，构造继承，原型链继承，组合继承，寄生组合继承
- 怎么用正则判断当前域名是否为 qq.com，或者 xxx.qq.com
- try...catch...中如果异步代码出错怎么办？
- js 怎么删除 cookie
- cookie 的几个字段的功能
- 怎么创建一个 Promise，参数是什么，怎么中断一个 promise，除了抛异常和 return new Promise()还有什么
- 怎么判断一个空数组
- 普通函数的作用域
- let const, babel 中的实现
- fetch 的使用，考察通信是否了解
- 事件机制，捕获和冒泡，如何阻止冒泡？
- 阻塞、非阻塞和异步同步是对应的吗？一样的吗？
- window.onload 和 document.ready，onload 是所有资源包括图片都加载完才执行
- 如何给不存在的元素绑定事件监听
- 可以在捕获阶段实现事件代理吗，为什么业界都用冒泡？（原因应该是，捕获和冒泡没有明显的优劣之分，但是冒泡事件流模型被大多数浏览器支持，兼容性更好）
- 内存泄漏
- 怎么判断一个元素有没有被引用
- 全局变量为什么不会被垃圾处理
- BOM 和 DOM 的区别,BOM 的方法讲完整一点
- 点击事件是宏任务还是微任务
- class 定义类和 function 定义类的区别
- TS 声明文件
- TS 可选属性
- 介绍一下 css 盒模型
- bfc 是什么。怎么样形成 bfc，bfc 有哪些用
- 实现一个垂直水平居中
- 左右布局，sider + 右侧自适应如何实现
- animation 的参数，怎样实现一个动画
- 说说盒模型和怪异盒模型
- 预处理器 sass 优点
- 样式框架的原理，布局方法有哪些，flex，grid，还有吗
- margin-top 为负值，除了绝对定位还有哪些地方碰到过？
- 怎么使两个 div 并列
- 父元素和子元素宽高不知道的情况如何居中子元素（这个问题其实和父元素高度知不知道无关，因为文档流中父元素默认包裹子元素，高度是由子元素撑开的。）
- CSS 基础好么，知道 DEN 么？
- css 中隐藏元素的方法，display:none, visibility:hidden,区别？还有什么方式
- css 绝对定位和相对定位都是以谁为基准
- css 弹性盒子
- CSS 和 JS 实现动画的方式
- ease-in 怎么用 js 实现？
- CSS 和 JS 实现动画哪个好？为什么？
- 实现一个块从左到右的移动
- css 设置元素隐藏，两种有什么区别？
- css 选择器有哪些？
- css 怎么实现列表中隔一行变一个颜色
- 实现一个自适应内容的正方形盒子
- css 有哪些单位
- 讲一下 css 的 flex 布局
- px 和 rem 的区别，举个例子说明一下
- 浮动布局和 flex 布局相比有什么优缺点
- 写 CSS 喜欢用什么布局
- node 用什么实现模块化管理
- 说一下 node 的 nextTick
- 说说浏览器和 node.js 里面捕获错误的方式
- 谈谈你对 nodejs 的理解
- node 和浏览器有什么区别吗
- 介绍一下 webpack，webpack 有哪些配置，loader 和 plugin 有什么区别
- webpack 的原理机制、配置了入口之后发生了什么
- Webpack 用过么？里面的 tree-shaking 什么原理？（tree-shaking 是因为 import 静态引入的能力，得以对文件内容进行浅层比较，去掉未被使用的代码。）
- webpack 的打包时间优化
- webpack 的打包流程
- Require/import 如何解决循环引用 Webpack 是怎么做的
- webpack 异步加载路由需要怎么配置，问还有优化首屏渲染的其他方法吗
- webpack loader 在什么时期起作用
- 写一个 webpack 插件应该怎么写
- webpack 中如何实现按需加载的
- webpack 依赖 node 吗？
- 有了解过 webpack 里面的拆包吗，说一下你的拆包策略
- 你觉得拆包的意义在哪，结合 http 的缓存详细说下拆包你觉得拆包的意义在哪，结合 http 的缓存详细说下拆包
- 拆包过程有遇到过什么坑吗，如何解决的（有个 webpack 的 bundle 和 module 的 id 自增导致缓存失效的问题）
- 了解 PWA 吗，webpack 怎么做 PWA
- 设计模型 策略模式，单例模式，工厂模式
- 了解有哪些框架，脏数据检测的原理、数据劫持的原理、订阅者发布者
- 用过哪些前端 router ，实现方式原理[hash、history]
- 框架的好处，坏处，单页面应用，seo 如何解决
- jquery 的 each
- jquery 的 ready
- ready 和 upload 区别
- Vue 的生命周期，create 和 mounted 之间发生了什么
- vue created 和 beforemount 之前会发生什么
- vue 什么生命周期以后就不会被监听了
- 钩子？
- 让你实现一个弹窗组件需要注意什么？
- vue 数据双项绑定 + diff 算法
- 既然有双向绑定，为什么 VUE 还有虚拟 dom 这个机制，以及这个机制的好处
- VUE 路由的实现原理
- 怎么去实现 vue 的计算属性
- vue 构建 v-dom 树过程
- vue-cli 做了哪些代码的优化，在开发环境到生产环境
- Vue 的预渲染这个插件，具体是怎么去做的？
- Vue 的子组件与子组件之间的通信讲讲吧
- 父子组件的通信和子父组件的通信是不是也可以实现呢？
- 说说你对 Vue 的总体看法，特点，以及与其他框架的不同的地方
- Vue 的 spa 首屏优化怎么做的，说具体思路
- vue 中通过一个按钮控制 input 获得焦点，怎么实现，通过 ref 获取对象跟原生的 js 有什么不同
- vue 的高级组件了解吗？
- Vue 的 computed 和 watch 有什么区别
- 如果要计算页面渲染时间，应该在哪个阶段为止
- Vue 生命周期中的 mounted ,在原生 js 中怎么实现？
- Vue 的虚拟 DOM 和 patch 算法
- vue 跟 jquery 的不同，操作 DOM,组件化，MVVM ,虚拟 DOM
- Vuex 5 个概念 为什么 mutations 不能异步？异步会怎样？
- 对 vue 中 data 进行更新会发生什么（生命周期进行更新、渲染）
- 如果要复用项目中的某一块逻辑，你怎么做
- vue 中兄弟组件的通信方式（vuex，vue 组件传递分配 props）
- 说说 v-if 和 v-show 的区别
- 假设界面显示价格为 9.99 元，现在我去拉取了后台的价格，现在数据为 8.88 元。当你把数据设置为 8.88 后再到页面显示成 8.88 元。在这个期间你了不了解 vue 帮你做了什么事情？
- 介绍 vuex 的各个模块和简单讲讲原理
- dispatch 和 commit 的区别
- vue 父组件先 mounted 还是子组件 mounted
- Vue 中的 nextTick 了解吗？
- vue 里面的 key 有什么作用
- js 和 react 垃圾处理机制和回收
- 登录功能，从前端到后台是怎么处理的
- 用户登录怎么实现的，怎么知道是同一个用户（用 userId，那手机号不就没用了吗）
- 手机号验证怎么做的，正则表达式的方法
- 发送验证码功能，向同一个手机发送多次验证码（攻击），怎么处理
- 项目前端怎么优化
- 最近最熟悉的项目，遇到最难解决的问题
- jQuery 用过吗，token 如何实现验证登录
- 如果我从前端要请求一张图片，你觉得从前端到后端的整个流程是怎样的，详细讲讲在后端的处理流程，随便扯了点路由匹配啥的
- 很大的日志读取，ip 出现最多的十次，怎么分片
- 你是怎么压缩图片的？
- 项目上线之后，怎样排除 js 中存在的问题？
- 如何上传文件，pc 端
- 本地存储你有做什么特别处理吗？
- 说一下缓加载怎么实现的
- 有 50g 的 QQ 号数据，一次只能运行 20g，想要找出出现次数最多的前十个 qq 号，怎么做？
- 图片压缩后台怎么实现你知道吗？怎么牺牲图片的画质呢？
- 输入 有做什么安全处理吗？（xss 攻击，常见的字符转义处理有哪些？）
- 知道 Base64 吗
- 如果说要展示一个十万的数据在移动端的网页上怎么做
- 自己做一个登录系统从前端到后端需要注意什么
- 介绍一下雅虎的性能优化原则
- 海量日志中找 ip 最多出现次数
- 超大的日志文件, 提取其中的 IP 地址
- 前后端通信数据格式
- 用什么实现离线应用：manifest，原理呢？
- 如何提高首屏加载速度
- 博客的话，做过哪些方面的优化呢？
- 场景题：现在手机 QQ 要做个成语接龙，你怎么去做，说说思路吧
- 你有什么较好的算法可以尽量减少成语库的数量吗？
- 有没有想过前端如何去检测用户输入的是不是成语？
- SSR
- SEO 怎么做的，说说技术细节
- 用 ajax 上传图片
- 预渲染 prerender 怎么做的，说说技术细节,具体说一下预渲染的原理
- 如何减少白屏时间和首屏时间
- 如果部署上去的项目有人打开后一直是白屏，怎么去收集这种情况
- 用户第二次访问网页，会快很多，是什么原理？
- 让你设计一个登录、注册、忘记密码的页面你会怎么设计？
- 组件化开发是为了什么
- 5000 条数据展示
- 如何知道用户发生的错误（`window.onerror`）
- 富文本编辑器怎么实现？（给标签设置 contenteditable 属性，然后使用浏览器支持的 document.execCommand 命令模式 API）
- 富文本编辑器的安全问题
- 如果要实现在离线情况下编辑且不丢失数据，怎么办？（先回答的是使用 localStorage，回答之后不断追问，还问了能否直接用对象存，后面扯到了引擎方面的问题。）
- 从底层谈谈 map 数据结构的设计。如果容量不够了怎么办，扩容过程中可能会耗费比较多的时间，如果在扩容时要访问怎么办；
- 微信附近的人这个功能，如何设计
- severless 的优点
- git 相关操作
- 如何实现一个可编辑的可以无限延伸的表格？
- 除了 websocket 外还有什么方法能实现后端推送？
- 自动化测试是怎么做的，怎么判断输出是不是符合期望
- 100ms 请求事件，有几种写法
- 如何能只发送信息，不进行数据缓存
- 前端要加载一个图片有哪些方式，然后还问到了 base64 是怎么实现的，有什么缺点，icon 是怎么实现的
- 后端一下子给你几万条数据，你要怎么处理。（一开始我说，这种情况下后端一定会分页的，然后又问没分页怎么办。然后我说前端手动分页，然后讲了一下具体的实现方法。）
- 怎么保证 token 的安全性，拿到你的 token 就可以做全部的事情了吗？
- 弱类型语言的缺点，平时哪些地方让你抓狂
- 封装统一的网络请求的好处
- 说一下 babel 是怎么实现各个浏览器兼容的，讲了一下 babel 的工作流程和 AST 树
- 垃圾回收，如何使用这个方法来优化，主流的浏览器垃圾回收的算法，具体流程
- 标记清除为什么比引用清除好
- 要在页面上实行一个特别慢的 js 代码，会遇到什么问题，假设页面已经加载好，用户点击之后开始计算，造成没有响应的现象的原因（被禁用还是被延迟）
- 阻塞会造成什么后果
- 很大的计算，会让页面卡顿，有什么办法可以使页面不卡顿，也让任务完成（我回答了异步的方法，面试官问还有没有其他的方式，例如 html5 的新特性）
- 实现百度搜索,foucs 有下拉框，根据输入内容能模糊查询
- 无限滚动列表优化问题
- 假如说我们的网页有一个表单，有人模拟 http 的 post 绕过了表单将数据发送到了后台应该怎么办
- 怎么去实现一个多人在线文档（从技术和需求说，来自腾讯文档，怎么做到数据的渲染、怎么获取到数据、网络上需要做什么处理）
- 详细说明一下你是怎么通过设置请求头解决了缓存问题吗？
- 说说不用 nuxt 框架怎么实现 SSR，数据预取怎么实现的
- RESTful 的原理
- 数据库百万条数据，有几种语文，数学，计算平均分，排序出来，如何解决
- 后台有注解，前端有吗？装饰器用过吗？
- 关系型和非关系型数据库
- 数据库的索引的原理和用法
- 数据库的事务知道吗？
- 连接查询有哪些方式？
- 你知道 Java 为啥能够运行在几乎所有系统上吗？
- linux 相关操作（查看进程用 ps）
- mysql 跟 mongondb 的不同
- 数据库优化方法
- pm2 查看日志的命令
- koa 的底层原理
- koa 的洋葱模型，和 express 有什么区别
- 事务的原理了解吗
- 什么是内外连接
- 索引了解吗，为什么索引能加快速度
- 同步和异步的区别
- 如果有六百万名考生的高考成绩要排序应该怎么做
- web 服务用过哪些？
- 你提到了 nginx，有做过一些负载均衡吗？
- 找出数组中 n 项，n 项的和为 m
- 口述快速排序
- 冒泡，及冒泡的优化
- 讲讲迪杰斯特拉算法
- 讲讲最小生成树算法
- 讲讲 hash 算法
- 堆排序
- 数组三分，如果一个数组能够分成非空的三个部分，每个部分和相等，则返回 true
- 查找算法应该用堆还是用栈
- 数据结构有那些
- 快排时间复杂度+快排什么时候最慢
- 洗牌算法
- 二叉树根据一个节点查找下一个节点
- 从一个数组的后十个数中找出 3 个和为 10 的数字
- 找出两个字符串（str1,str2）的最大公共子长度
- 一次可以跳一步，两步，三步，问 n 步的路有多少种到达终点方式？（斐波那契，写了个尾递归）
- 大量数据的数组，怎么找出排名前 n 个数
- 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从 0 开始)。如果不存在，则返回 -1
- 实现 string 的 indexOf() 函数
- ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/beNzaWVQLGmDbrwHDk7Hb63nfDZq85eoej3EwP7IVClaBS74XKJiaK3eDQBxWJzuN5P22dhu2By737dFgQCicBkg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
- 链表反转
- 二叉树排序
- 二叉树的翻转
- 出现最多的字母个数
- 找一篇文章中出现最多的英文单词
- 正则匹配字符串
- 现在给你一个树状对象，{value:1,children:{value:2,children:{...}}}这样的结构，如何把所有 value 删去，返回一个新对象？
- 如何判断一个对象中有没有叫 value 的属性？不要考虑代码的复杂性，能说几种说几种
- 说说你知道的排序和查找算法吧
- 堆排序是如何实现的？时间复杂度是多少？
- 有 1000 步的台阶，每次只能选择走 1 步、2 步或者 3 步，走完台阶一共有多少种走法
- 长度为 1 亿的字符串，寻找字符串包含 'tencent' 子串的数量
- 无序数组中选择第 k 大的数，分析算法时间复杂度
- 两个整数求和会超过 int 范围 怎么运算
- DFS 非递归 先序遍历
- 数组中超过一半的数是同一个数，找出那个数（分析复杂度，如何优化）
- 手撕二叉树的题目，leetcode124
- 生成一个 8\*8 的 01 棋盘，每行每列不能多于 1 个 1，输出生成的棋盘和符不符合规定
- 数组和链表随机访问的时间复杂度
- O(N) 寻找最长的连续字符串
- 小明从老板那里拿到了一个密码表，说是如果解开密码表中的秘密，就可以升职加薪，赢取白富美，走向人生巅峰。这个密码表是一个 CSV 文件，里面的数据由数字（没有小数点）、字母组成。小明需要提取每个数据中的数字（例如 1a2b3c 提取后得到 123，提取后的数字整体看作一个十进制数），把数值为奇数的项相加，就可以解开这个秘密。请你实现一个函数 sum，帮小明完成这项工作。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/beNzaWVQLGmDbrwHDk7Hb63nfDZq85eoQPib5t0xA96BSs49YnjraxvdZYiacY4C1X1YKeM86dGOjWDz2SIFDlQA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

- 在一个字符串中找出连续重复的字符，这个字符可以是数字、字母和中文等
- 有效括号 - 判断一个字符串中括号是否都能匹配
- 一个字符串里面有一些不可见的字符，如"\n"，写一个算法剔除它们
- 数据绑定实现【框架和抛开框架，手撕】
- 排序数组，查询某个值，存在则返回索引，不存在返回插入位置；优化，for\~二分 【手撕】
- js 实现阶乘
- 创建一个 Person 类，其包含公有属性 name 和私有属性 age 以及公有方法 setAge ；创建一个 Teacher 类，使其继承 Person ，并包含私有属性 studentCount 和私有方法 setStudentCount
- 实现一个类似百度输入框的功能，根据用户的输入，找出一个数组中匹配到的数显示出来
- 一个输入框实现百度搜索那样的 autocomplete 效果
- 请写一个函数，计算一篇英文文章中出现次数最多的单词及出现次数
- 怎么用 js 实现队列
- js 观察者模式
- 数组扁平化
- 实现一个实数的堆栈，使得其 push pop max 方法的时间复杂度为 O(1)
- 有一个整数二维数组，每行的元素个数不同，输出它的全排列，同一行的数互斥。要求不使用递归完成
- 实现一个函数，检查二叉树是否平衡。
- 实现一个 Http 请求池，需要能够限制并发数
- 合并二叉树
- 奇偶链表
- 使用闭包实现变量自加一
- 双向链表转二叉树，二叉树转双向链表
- url 正则匹配
- nlogn 排序算法有哪些，快排稳定么
- 搜索二叉树找第 k 大的数
- 手写原生 ajax，new XMLHttpRequest()
- 手写对象深拷贝
- 获取标签名称为 div 的元素的个数，并且判断是不是数组，考察类型判断
- 给两个构造函数 A 和 B ，如何实现 A 继承 B
- 用户权限认证过程
- 写个模块导出的案例
- 拖拽代码 (手写)
- 手撕代码：大数相乘
- 手撕代码：函数无限柯里化（有 n 个参数，函数调用 n+1 次得到结果）
- 手撕代码：实现一个轮询器，主要考察 Promise
- 继承（实现私有属性和私有方法）
- 设计实现一个固定执行顺序的 script 加载
- 手写代码题：找出字符串中出现次数最多的字符及出现次数
- 编程题（对输入的一段字符串（有逗号 有回车，挑出其中的数字，然后求和，求和之后再把数中的奇数加） 1.正则做法 2.字符串遍历做法，挑出数字 ， 换行，再按换行分割，再按，号分割，数组扁平，求和，变字符串，遍历
- 数组去重手写，越多越好
- 将一个平铺的数组用 js 写成树的结构
- 完成函数的实现，使得它可以实现达到 `Array.prototype.forEach` 相同的功能
- 看下面代码执行结果，说明原因
- token 过期怎么做
- 怎么知道用户和 token 的对应关系
- token 和 cookie 区别
- token 为什么比 cookie 更不容易受到攻击，为什么要用 cookie
- 手撕 Event bus
- 手撕函数组合
- 手撕对象扁平化
  ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/beNzaWVQLGmDbrwHDk7Hb63nfDZq85eoA4Dnfnll696rB70s4FpclyhK1ALJUiaCMSIgwuPxnx2EhICt87iavFMQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
- JS 实现一个 JSON.stringify() 功能的函数
- 三次重试：假设有一个函数名为 job,调用 job 后会执行一些异步任务，并返回一个 Promise ,但 job 执行的异步任务任务有可能会失败
- 请实现函数 retry ,把 job 作为 retry 函数的参数传入，当 retry 执行后会尝试调用 job,如果 job 返回成功（即 Promise fulfilled），则 retry 函数返回 job 函数的返回内容；
- 如果 job 返回失败（即 Promise rejected ）,retry 函数会再次尝试调用 job 函数。
- 如果 job 连续三次均返回失败，retry 则不再尝试调用，并返回其最后一次失败的内容。
  ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/beNzaWVQLGmDbrwHDk7Hb63nfDZq85eoW7DX5ibmhvxxgrUSw9HusERJS3ss8ia4Impa0jIh4qh9XPb1ibpQT7TLg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
  ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/beNzaWVQLGmDbrwHDk7Hb63nfDZq85eo7asMp4qqg9vtEZAXuIN6OR71TeGSicSGdOKdbAJAMvmj2gEAJU0Ojaw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
- 写了个类型判断函数
  ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/beNzaWVQLGmDbrwHDk7Hb63nfDZq85eoI93qoeiaqpLvibU64YqP6DT6f3Ux2X93mU40vcPQicZRbaJYsQy3GkdZg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
- 遍历根结点下所有子节点
  ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/beNzaWVQLGmDbrwHDk7Hb63nfDZq85eocjO1wv2S7lSoLgQzRDWZDzmC8AJNKLBicgYZpSzEmtXficGJxvH20Kfw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
- 实现页脚在内容最底部![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/beNzaWVQLGmDbrwHDk7Hb63nfDZq85eoicrZF4WhZTE5sxskZnW7h2Zn3ELKbGNDjrDue7Um31OaHLU3BJe1KlA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
  ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/beNzaWVQLGmDbrwHDk7Hb63nfDZq85eonjQreOMrhnEV47CYhIGuGicZuZl8dlqyFyzm2ydjnSm0Iia1vmYUFZ7w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
- 100 人教室 70 人喜欢足球，80 人喜欢篮球，问同时喜欢足球和篮球的人数
- 试探玻璃杯破碎的楼层
- 时针与分针夹角 5.25 时针和分针夹角 上一题拓展\:X 时 Y 分夹角
- 一个班里 60% 喜欢 A, 70% 喜欢 B, 80% 喜欢 C, 问同时喜欢 ABC 的
- 一瓶汽水一块钱，俩空瓶可以换一瓶汽水，给你 20 块钱，最多喝多少瓶？
- 给你一个 A4 纸张，随便剪掉一个随意位置宽高的矩形，给你一个没有刻度的尺子和笔，怎么一刀把剩下的 A4 纸张分成面积同样大小的两半。
- 如何洗开一副扑克牌
- a 和 b 两个人投掷硬币，朝上 a 得 1 分，反之 b 得分，现在 a8 分、b7 分，请问 a 和 b 先到 10 分的概率各是多少。
- 一根不均匀绳子烧完一个小时，问怎么使用多根这种绳子来计算 15 分钟
- 一个烤盘，每次最多烤两块肉，一面烤 10min，问要烤几分钟
- 20 个瓶子，有 19 个瓶子每颗药 1g，有一个瓶子每颗药 1.1g，问怎么用一把称一次找出 1.1g 的瓶子
- excel 同步/冲突
- OT 算法
- 问了计算机组成，问我 cache 知道吗，我大概说了说，然后问为什么 cache 更快
- 操作系统，银行家算法，死锁怎么解决
- flutter 有了解吗
- h5 有写过吗，移动端有了解吗
- 如何衡量一个软件的质量？如何保证产品的质量？（软件工程的思想，敏捷中的测试驱动开发）
- 找出不多于三个关键词形容自己
- 怎么跟一个不懂前端的人介绍前端
- 原型
  构造函数 ，是一种特殊的方法。主要用来在创建对象时初始化对象。每个构造函数都有 prototype(原型)属性
  每个函数都有 prototype(原型)属性，这个属性是一个指针，指向一个对象，
  这个对象的用途是包含特定类型的所有实例共享的属性和方法，即这个原型对象是用来给实例共享属性和方法的。
  而每个实例内部都有一个指向原型对象的指针。
- 闭包
  简单来说就是函数嵌套函数，内部函数引用来外部函数的变量，从而导致来垃圾回收机制没有生效，变量被保存来下来。
  也就是所谓的内存泄漏，然后由于内存泄漏又会导致你项目逐渐变得卡顿等等问题。因此要避免内存泄漏。
- 原型链
  提到原型链就不得不提原型的继承，继承的完美实现方案是借助寄生组合继承，主要实现原理
  PersonB.prototype = Object.create(PersonA.prototype)实现来继承 PersonA 的原型
  当我们通过 new 关键字实例化的对象身上就有了 PersonB 自身的属性和方法，也有了 PersonA 的原型方法
  当实例化对象调用某个方法时会先在自身和原型上查找，然后是在\_proto\_上一层层查找，这种方式就是原型链。
- vuex
  Vuex 是一个专为 Vue.js 应用程序开发的状态管理模式。它采用集中式存储管理应用的所有组件的状态
  并以相应的规则保证状态以一种可预测的方式发生变化。
  tate：Vuex 使用单一状态树——是的，用一个对象就包含了全部的应用层级状态。
  mutation：更改 Vuex 的 store 中的状态的唯一方法是提交 mutation
  action: action 提交的是 mutation，而不是直接变更状态。action 可以包含任意异步操作。
  getter: 相当于 Vue 中的 computed 计算属性
- vue-router
  Vue Router 是 Vue.js 官方的路由管理器。它和 Vue.js 的核心深度集成，让构建单页面应用变得易如反掌 \<router-link>和\<router-view>和\<keep-alive>
- 深拷贝浅拷贝
  深拷贝：
  通过利用 JSON.parse(JSON.stringify(Object))来达到深拷贝的目的
  但是 JSON 深拷贝的缺点是 undefined 和 function 还有 symbol 类型是无法进行深拷贝的
  如有需要可以自己手动封装函数来达到目的
  浅拷贝：
  通过 ES6 新特性 Object.assign()与扩展运算符来达到浅拷贝的目的
- Vue 通信
  第一种：props 和`$emit
第二种：中央事件总线 EventBus(基本不用)
第三种：vuex（状态管理器）
第四种：$`parent 和 \$children
- 你在工作中遇到那些问题，解决方法是什么
  经常遇到的问题就是 Cannot read property ‘prototype’ of undefined 解决办法通过浏览器报错提示代码定位问题，解决问题
  Vue 项目中遇到视图不更新，方法不执行，埋点不触发等问题
  一般解决方案查看浏览器报错，查看代码运行到那个阶段未之行结束，阅读源码以及相关文档等
  然后举出来最近开发的项目中遇到的算是两个比较大的问题。
- webpack 配置入口出口
  module.exports={
  //入口文件的配置项
  entry:{},
  //出口文件的配置项
  output:{},
  //模块：例如解读 CSS,图片如何转换，压缩
  module:{},
  //插件，用于生产模版和各项功能
  plugins:[],
  //配置 webpack 开发服务功能
  devServer:{}
  }
  简单描述了一下这几个属性是干什么的。
- 说说 Vue 原理
  Vue 是采用数据劫持配合发布者-订阅者模式，通过 Object.defineProperty 来()来劫持各个属性的 getter 和 setter
  在数据发生变化的时候，发布消息给依赖收集器，去通知观察者，做出对应的回调函数去更新视图。
  具体就是：
  MVVM 作为绑定的入口，整合 Observe,Compil 和 Watcher 三者，通过 Observe 来监听 model 的变化
  通过 Compil 来解析编译模版指令，最终利用 Watcher 搭起 Observe 和 Compil 之前的通信桥梁
  从而达到数据变化 => 更新视图，视图交互变化(input) => 数据 model 变更的双向绑定效果。
- Vue 路由守卫有哪些，怎么设置，使用场景等
  常用的两个路由守卫：router.beforeEach 和 router.afterEach
  每个守卫方法接收三个参数：
  to: Route: 即将要进入的目标 路由对象
  from: Route: 当前导航正要离开的路由
  next: Function: 一定要调用该方法来 resolve 这个钩子。
  在项目中，一般在 beforeEach 这个钩子函数中进行路由跳转的一些信息判断。
  判断是否登录，是否拿到对应的路由权限等等。
- 数组去重
- 对数组排序
  第一种方法利用 sort 方法
  第二种利用冒泡排序
- 说一说 js 是什么语言
  js 是一种运行在浏览器的脚本语言，这种语言主要的功能是可以制作出动态的页面的效果
  我们可以通过 js+css+html 布局来形成我们现在可以访问展示的页面
  js 语言是弱语言类型， 因此我们在项目开发中当我们随意更改某个变量的数据类型后
  有可能会导致其他引用这个变量的方法中报错等等。
- 原型
  JavaScript 中的对象都有一个特殊的 prototype 内置属性，其实就是对其他对象的引用
  几乎所有的对象在创建时 prototype 属性都会被赋予一个非空的值，我们可以把这个属性当作一个备用的仓库
  当试图引用对象的属性时会触发 get 操作，第一步时检查对象本身是否有这个属性，如果有就使用它，没有就去原型中查找。一层层向上直到 Object.prototype 顶层
  基于原型扩展描述一下原型链，什么是原型链，原型的继承，ES5 和 ES6 继承与不同点。
- ES6 新特性
  1. ES6 引入来严格模式
     变量必须声明后在使用
     函数的参数不能有同名属性, 否则报错
     不能使用 with 语句 (说实话我基本没用过)
     不能对只读属性赋值, 否则报错
     不能使用前缀 0 表示八进制数,否则报错 (说实话我基本没用过)
     不能删除不可删除的数据, 否则报错
     不能删除变量 delete prop, 会报错, 只能删除属性 delete global\[prop]
     eval 不会在它的外层作用域引入变量
     eval 和 arguments 不能被重新赋值
     arguments 不会自动反映函数参数的变化
     不能使用 arguments.caller (说实话我基本没用过)
     不能使用 arguments.callee (说实话我基本没用过)
     禁止 this 指向全局对象
     不能使用 fn.caller 和 fn.arguments 获取函数调用的堆栈 (说实话我基本没用过)
     增加了保留字（比如 protected、static 和 interface）
  2. 关于 let 和 const 新增的变量声明
  3. 变量的解构赋值
  4. 字符串的扩展
     includes()：返回布尔值，表示是否找到了参数字符串。
     startsWith()：返回布尔值，表示参数字符串是否在原字符串的头部。
     endsWith()：返回布尔值，表示参数字符串是否在原字符串的尾部。6.函数的扩展
     函数参数指定默认值 7.数组的扩展
     扩展运算符 8.对象的扩展
     对象的解构
  5. Proxy
     Proxy 可以理解成，在目标对象之前架设一层“拦截”，外界对该对象的访问
     都必须先通过这层拦截，因此提供了一种机制，可以对外界的访问进行过滤和改写。
     Proxy 这个词的原意是代理，用在这里表示由它来“代理”某些操作，可以译为“代理器”。
     Vue3.0 使用了 proxy
     12.Promise
     Promise 是异步编程的一种解决方案，比传统的解决方案——回调函数和事件——更合理和更强大。
     特点是：
     对象的状态不受外界影响。
     一旦状态改变，就不会再变，任何时候都可以得到这个结果。
     13.async 函数
     async 函数对 Generator 函数的区别：
     （1）内置执行器。
     Generator 函数的执行必须靠执行器，而 async 函数自带执行器。也就是说，async 函数的执行，与普通函数一模一样，只要一行。
     （2）更好的语义。
     async 和 await，比起星号和 yield，语义更清楚了。async 表示函数里有异步操作，await 表示紧跟在后面的表达式需要等待结果。
     （3）正常情况下，await 命令后面是一个 Promise 对象。如果不是，会被转成一个立即 resolve 的 Promise 对象。
     （4）返回值是 Promise。
     async 函数的返回值是 Promise 对象，这比 Generator 函数的返回值是 Iterator 对象方便多了。你可以用 then 方法指定下一步的操作。
     14.Class
     class 跟 let、const 一样：不存在变量提升、不能重复声明...
     ES6 的 class 可以看作只是一个语法糖，它的绝大部分功能
     ES5 都可以做到，新的 class 写法只是让对象原型的写法更加清晰、更像面向对象编程的语法而已。
     15.Module
     ES6 的模块自动采用严格模式，不管你有没有在模块头部加上"use strict";。
     import 和 export 命令以及 export 和 export default 的区别
- Css3 新特性 1.过渡 transition 2.动画 animation 3.形状转换 transform 4.阴影 box-shadow 5.滤镜 Filter 6.颜色 rgba 7.栅格布局 gird 8.弹性布局 flex
- 说一说什么是跨域，怎么解决
  因为浏览器出于安全考虑，有同源策略。也就是说，如果协议、域名或者端口有一个不同就是跨域，Ajax 请求会失败。
  为来防止 CSRF 攻击
  - JSONP
    JSONP 的原理很简单，就是利用 \<script> 标签没有跨域限制的漏洞。
    通过 \<script> 标签指向一个需要访问的地址并提供一个回调函数来接收数据当需要通讯时。 \<script src="<http://domain/api?param1=a&param2=b&callback=jsonp"></script>> \<script>
    function jsonp(data) {
    console.log(data)
    } \</script>
    JSONP 使用简单且兼容性不错，但是只限于 get 请求。
  - CORS
    CORS 需要浏览器和后端同时支持。IE 8 和 9 需要通过 XDomainRequest 来实现。
  - document.domain
    该方式只能用于二级域名相同的情况下，比如 a.test.com 和 b.test.com 适用于该方式。
    只需要给页面添加 document.domain = 'test.com' 表示二级域名都相同就可以实现跨域
  - webpack 配置 proxyTable 设置开发环境跨域
  - nginx 代理跨域
  - iframe 跨域
  - postMessage
    这种方式通常用于获取嵌入页面中的第三方页面数据。一个页面发送消息，另一个页面判断来源并接收消息
- 说一说前端性能优化方案
  一：webapck 优化与开启 gzip 压缩
  1. babel-loader 用 include 或 exclude 来帮我们避免不必要的转译，不转译 node_moudules 中的 js 文件
     其次在缓存当前转译的 js 文件，设置 loader: 'babel-loader?cacheDirectory=true'
  2. 文件采用按需加载等等
  3. 具体的做法非常简单，只需要你在你的 request headers 中加上这么一句：accept-encoding:gzip
  4. 图片优化，采用 svg 图片或者字体图标
- 浏览器缓存机制，它又分为强缓存和协商缓存
- 本地存储——从 Cookie 到 Web Storage、IndexedDB
- 说明一下 SessionStorage 和 localStorage 还有 cookie 的区别和优缺点
- 事件代理
- 页面的回流和重绘
- EventLoop 事件循环机制
- 说一说 SessionStorage 和 localStorage 还有 cookie
  共同点：都是保存在浏览器端、且同源的
  不同点：
  1. cookie 数据始终在同源的 http 请求中携带（即使不需要），即 cookie 在浏览器和服务器间来回传递。
     cookie 数据还有路径（path）的概念，可以限制 cookie 只属于某个路径下
     sessionStorage 和 localStorage 不会自动把数据发送给服务器，仅在本地保存。
  2. 存储大小限制也不同，cookie 数据不能超过 4K，sessionStorage 和 localStorage 可以达到 5M
  3. sessionStorage：仅在当前浏览器窗口关闭之前有效；
     localStorage：始终有效，窗口或浏览器关闭也一直保存，本地存储，因此用作持久数据；
     cookie：只在设置的 cookie 过期时间之前有效，即使窗口关闭或浏览器关闭
  4. 作用域不同
     sessionStorage：不在不同的浏览器窗口中共享，即使是同一个页面；
     localstorage：在所有同源窗口中都是共享的；也就是说只要浏览器不关闭，数据仍然存在
     cookie: 也是在所有同源窗口中都是共享的.也就是说只要浏览器不关闭，数据仍然存在
- 说一说你用过的 css 布局
  gird 布局，layout 布局，flex 布局，双飞翼，圣杯布局等
- Promise 是什么，解决了什么，之前怎么实现的
  Promise 是异步编程的一种解决方案，比传统的解决方案——回调函数和事件——更合理和更强大。
  解决来之前在请求中回调请求产生的回调地狱，使得现在的代码更加合理更加优雅，也更加容易定位查找问题。
- 说说浏览器缓存
  缓存可以减少网络 IO 消耗，提高访问速度。浏览器缓存是一种操作简单、效果显著的前端性能优化手段
  很多时候，大家倾向于将浏览器缓存简单地理解为“HTTP 缓存”。
  但事实上，浏览器缓存机制有四个方面，它们按照获取资源时请求的优先级依次排列如下：
  Memory Cache
  Service Worker Cache
  HTTP Cache
  Push Cache
  缓存它又分为强缓存和协商缓存。优先级较高的是强缓存，在命中强缓存失败的情况下，才会走协商缓存
  实现强缓存，过去我们一直用 expires。
  当服务器返回响应时，在 Response Headers 中将过期时间写入 expires 字段，现在一般使用 Cache-Control 两者同时出现使用 Cache-Control
  协商缓存，Last-Modified 是一个时间戳，如果我们启用了协商缓存，它会在首次请求时随着 Response Headers 返回：每次请求去判断这个时间戳是否发生变化。
  从而去决定你是 304 读取缓存还是给你返回最新的数据
- UDP 和 TCP 有什么区别？
  UDP 协议是面向无连接的，不需要在正式传递数据之前先连接起双方，具有不可靠性：不保证有序且不丢失的将数据传递到对端，并且没有任何控制流量的算法。优点是：相比 TCP 更轻便高效。
  TCP 建立连接和断开连接都需要进行握手，并在数据传输过程中，通过算法来保证数据的可靠性。
- 谈谈你对 TCP 的三次握手和四次挥手过程的理解
  关于 TCP 的握手机制，一定不要死记硬背，要理解为什么这么设计，也就很容易记住了。
  **三次握手：**
  在客户端和服务器之间建立正常的 TCP 网络连接时，客户端首先会发出一个 SYN 消息，服务器使用 SYN+ACK 应答表示已经接收到这个消息，最后客户端再以 ACK 消息响应。这样在客户端和服务器之间才能建立起可靠的 TCP 连接，数据才可以在客户端和服务器之间传递。
  1.  建立连接时，客户端发送 SYN 包到服务器，等待服务器响应。（SYN 同步序列编号，是建立连接时使用的握手信号）。
  2.  服务器收到 SYN 包，使用 ACK 包进行确认应答，同时自己也会发送一个 SYN 包，即发送 SYN+ACK 包。
  3.  客户端收到服务器的 SYN 包，向服务器发送确认包 ACK。此包发送完毕，代表 TCP 连接完成，完成了三次握手。
      **四次挥手：**
      四次挥手是释放 TCP 连接的握手过程。
  4.  客户端向服务端发送释放连接报文 FIN，等待服务端确认，并停止发送数据。
  5.  服务器收到连接释放请求后，发送 ACK 包表示确认。（此状态下，表示客户端到服务器的连接已经释放，不再接受客户端发的数据了，但是服务器要是还发送数据，客户端依然接收）
  6.  服务器将最后的数据发送完毕后，就向客户端发送连接释放报文 FIN，等待客户端确认。
  7.  客户端收到服务器连接释放报文后，发出 ACK 包表示确认。此时客户端会进入 TIME_WAIT 状态，该状态将持续 2MSL（最大报文段生存时间，指报文段在网络中生存的时间，超时将被抛弃）时间，若该时间段内没有服务器重发请求的话，就进入关闭状态，当服务端接收到 ACK 应答后，立即进入关闭状态。
      ![](https://mmbiz.qpic.cn/mmbiz_png/2FMs2KmmepgVbJ6Eb4icspSsOS7hUd9hF6vSPzyVvbZYQVvImadsFyib8eBuDFWua4xT0S1OFzmF1Kw2RuaCKaRg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
- 为什么连接的时候需要三次握手，关闭时需要四次握手
  在建立 TCP 连接时，Server 端在接收到客户端的 SYN 连接请求后，可以直接发送 SYN+ACK 包，其中 ACK 作为应答，SYN 用来发起连接请求。但是关闭连接时，服务端收到 FIN 包时，可能还没有发送完数据，不能立即关闭，所以只能先回复 ACK 包进行确认，告知客户端已经收到 FIN 报文。然后等到服务端数据都发送完毕，才能向客户端发送 FIN 包，所以需要四次握手。
- 为什么建立连接要三次握手，为什么不是 2 次，4 次
  三次是最小的安全次数，可以保证通信的双方都具有发送消息和接收响应的能力，发送方和接收方始终同步序号，可以实现可靠传输。
- http 发展的过程及各版本的特点
  了解 http 的发展过程，可以帮助我们清楚 http 协议一直以来所存在的问题，以及所做的更新有什么实际意义。同时 http/1、http/2 的 Keep-Alice、pipline、多路复用、ServerPush 等特点也是我们需要掌握的知识，面试中也会经常提及。
- http 发展历程
  - **http/0.9**
    没有 HEADER 等描述数据的信息，只规定了客户端和服务端的通信形式，只支持 GET 请求。
    增加 status code 和 header。
  - **http/1.0** 正式作为标准，传输内容格式不限制，增加了 PUT、PATCH、HEAD、OPTIONS、DELETE 命令。
  - **http/1.1** 增加了持久连接（Keep-Alive）和管道机制。
  - **http/2** 增加了多路复用，服务端推送，头部️压缩，二进制帧数据传输等。
- 什么是 Keep-Alive
  从上面 http 发展历程中，已经知道 Keep-Alive 是 http/1.1 增加的。 在没有 Keep-Alive 之前，http 请求都是短连接，就是说每一次请求都要建立连接，请求完成后马上关闭连接，也就是我们上面说的三次握手和四次挥手过程，每次请求都要建立连接带来了资源的浪费，为了提高请求效率，于是有了 Keep-Alice。
  Keep—Alive 允许在一定时间内，同一个域名多次请求数据，只建立一次 http 连接，其他请求可以复用这个连接通道，以达到提高请求效率的目的。
- 管道机制的作用是什么？
  如果浏览器要向一个域名发送多个请求，需要在本地维护一个 FIFO 队列，完成了一个再发送下一个，这样就存在一个问题，服务端从完成一个请求开始回传，到收到下一个请求的这段时间内是处于空闲状态的。
  于是提出了管道机制，试图将浏览器的请求一股脑的打包发给服务器，服务器就可以在出开完一个请求后，马上处理下一个，不会在之前说的空闲时间。
- 管道机制存在哪些问题？
  1.  服务端收到多个管道请求后，需要按照接收顺序逐个响应。如果第一个请求处理特别慢，后续的响应的都会被阻塞着，这种情况称为「队首阻塞」。
  2.  服务端为了保证按顺序回传，通常需要缓存多个响应，从而占用更多的服务端资源，也更容易被攻击。
  3.  浏览器连续发送多个请求后，等待响应的这段时间，如果遇到网络异常导致连接断开，无法得知服务器处理情况，如果全部重试，可能会在服务端重复处理。
  4.  服务端和浏览器中间的代理设备不一定支持 http 管道，这给管道技术的普及带来了更多复杂性。
- 谈谈你对多路复用的理解
  多路复用是 http/2 的特性，http/2 最大的特点是使用二进制帧数据进行传输。
  首先介绍 http/2 中几个重要的概念：
  **帧：** http/2 数据通信的最小单位。每个帧都包含帧首部，其中会标识当前帧所属的流。
  **消息：** 指 http/2 中逻辑上的 http 消息。例如请求和响应等，消息由一个或多个帧组成。 、
  **流：** 存在于连接中的虚拟通道。流可以承接双向消息，每个流都有一个唯一的整数 id。
  **连接：** 与 http/1 相同，都是指对应的 TCP 连接。
  http/1 的请求和响应报文，都是由起始行、首部和实体正文（可选）组成，各部分之间以文本换行符分隔。而 http/2 将请求和响应数据分隔成为更小的帧，并对他们采用二进制编码。
  http/2 中，同域名下的所有请求都在一个连接上完成，这个连接可以承载任意数量的双向数据流。每个数据流都以消息的形式发送，消息由一个或多个帧组成。多个帧之间可以乱序发送，然后根据帧首部的流标识可以重新组装。
- http/2 为什么要做头部压缩，实现原理是什么？
  http 请求都是由状态行、请求/响应头部、消息主体三部分组成，一般而言，消息主体都会经过 gzip 压缩，或者本身传输的就是压缩后的二进制文件（例如图片、音频），但是状态行和头部却没有经过任何压缩，直接以文本传输。对于一个请求而言，其 headers 所占的字节数也不少，尤其 cookie，有些时候 headers 甚至超过了主体的大小。
  头部压缩使用了 **HPACK 算法**。会在支持 http/2 的浏览器和服务端之间：
  1. 维护一份相同的静态字典，包含常见的头部名称以及特别常见的头部名称和值的组合。
     这样对完全匹配的头部键值对，例如：method：GET，就可以使用一个字符表示。对于头部名称可以匹配的，例如 cookie： xxx，可以将名称使用一个字符表示。
  2. 维护一份相同的动态字典，可以动态的添加内容。
  3. 支持基于静态哈夫曼码表的哈夫曼编码（Huffman Coding）
- http/2 的 Server Push 有什么优点
  支持服务端推送，意味着服务端可以在发送页面 HTML 时主动推送其它资源，而不用等到浏览器解析到相应位置再发起请求。
  另外，服务端可以主动推送，客户端也有权选择是否接收。如果服务端推送的资源已经被浏览器缓存过，浏览器可以通过发送 RST_STREAM 帧来拒收。
- [HTTP/2 与 WEB 性能优化（一）](https://mp.weixin.qq.com/s?__biz=Mzg2NTA4NTIwNA==&mid=2247485084&idx=1&sn=8a55b0b78aeab1aca5a9f83748ac5b01&chksm=ce5e34e7f929bdf16466c1aaeb257650c920c09d360137bc05fd52202e84cfae8c505d6912be&token=976958660&lang=zh_CN&scene=21#wechat_redirect)
- [HTTP/2 与 WEB 性能优化（二）](https://mp.weixin.qq.com/s?__biz=Mzg2NTA4NTIwNA==&mid=2247485089&idx=1&sn=74bcaac3c37d60baf9fb1884252c546d&chksm=ce5e34daf929bdccb86f57e22e0b3e735ad841c06120dff5cacee002bd06fad8be407abd18f2&token=976958660&lang=zh_CN&scene=21#wechat_redirect)
- [HTTP/2 与 WEB 性能优化（三）](https://mp.weixin.qq.com/s?__biz=Mzg2NTA4NTIwNA==&mid=2247485093&idx=1&sn=b3c7ad554d7613bd8133b95f05cf1994&chksm=ce5e34def929bdc8e0829a0b6f4aa2de357541b8fe3f4be8a79826f614ac86347302057f934a&token=718544654&lang=zh_CN&scene=21#wechat_redirect)
- https 相关
  想要真正的了解 https，需要了解很多相关知识，比如 SSL，对称加密，非对称加密，CA 证书等知识。
  https 协议本身并不是一种新的协议，在 HTTP 跟 TCP 中间加多了一层加密层 TLS/SSL。通常 HTTP 直接和 TCP 通信，而 HTTPS 要先将数据给到 TLS/SSL，数据经加密后，再给到 TCP 进行传输。
  ![](https://mmbiz.qpic.cn/mmbiz_png/2FMs2KmmepgVbJ6Eb4icspSsOS7hUd9hF892vnxqiaeD7sSyuNCEicma6PiaPGDd3khv8HiaZSp83r9GCvDj3AX4bYA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
- https 和 http 有什么区别？
  在回答这个问题之前，我们先看下 http 请求存在哪些不足：
  1.  通信使用明文（不加密），内容可能会被窃听
  2.  不会验证通信方的身份，因此可能会遭遇伪装
  3.  无法保证报文的完整性，请求或响应的内容被篡改也无法知道
      https 就是对上面三点不足的解决，可以认为：
  - https == http + 加密 + 身份验证 + 数据完整性保护
    那么，他们的 **区别** 就明显了：
  1.  http 使用明文传输，https 则是具有安全性的 ssl 加密传输协议
  2.  http 不会验证通信放的身份，https 会通过数字证书来验证身份
  3.  https 可以保证数据的完整性，防止传输内容被中间人冒充或篡改
  4.  除以上外，http 和 https 使用的端口也不同，前者使用 80 端口，后者使用 443 端口
- 介绍一下 https 的握手过程
  1.  客户端发送 Client Hello 报文开始 SSL 通信。请求中包含：客户端支持的 SSL 版本、加密组件列表（所使用的加密算法和秘钥长度等）。
  2.  服务端接收到请求后，以 Server Hello 应答。应答报文中包含：从客户端提供的支持的 SSL 版本和加密组件中筛选出的 SSL 版本和加密组件。
  3.  之后服务端发送 Certificate 报文，报文中包含公开秘钥证书。
  4.  最后服务发送 Server Hello Done 报文，通知客户端最初阶段的 SSL 握手协商部分结束。
  5.  客户端会校验证书通过，创建随机数，并使用证书中提供的公钥对随机数（Pre-master secret）进行加密，并将加密后的随机数通过报文 Client Key Exchange 报文发送给服务端。
  6.  接着客户端继续发送 Change Cipher Spec 报文，告知服务器之后的通信会采用 Pre-master secret 秘钥进行加密。
  7.  客户端发送通过秘钥加密的 Finish 报文。表示握手阶段的客户端部分已经完成。
  8.  服务端通过客户端传入的随机数构造对称加密算法，同样发送 Change Cipher Spec 报文，告知客户端之后的通信会使用随机数秘钥进行加密。
  9.  服务端同样发送 Finish 报文。
  10. 客户端和服务器的 Finish 报文交换完毕后，SSL 连接到此建立完成，之后就发起 http 协议了。
      为了方便理解，简述一下上面过程：
      客户端发起请求，服务端响应给用户端证书，证书中包含公钥；
      客户端接收到证书后，生成随机数，通过公钥加密，将随机数发送给服务端，并凭随机数构造对称加密和服务端通信，并告知服务端此次通信后的通信都将使用随机数秘钥（Pre-master secret）进行加密；
      服务端使用私钥解析随机数，并通过随机数构造对称加密算法，同样告知客户端之后的请求将使用随机数进行加密。
- 为什么 https 数据传输使用对称加密？
  **对称加密**： 对称加密指的就是加密和解密使用同一个秘钥，所以叫做对称加密。对称加密只有一个秘钥。
  **非对称加密**: 加密和解密使用不同的秘钥，一把作为公开的公钥，另一把作为私钥。公钥加密的信息，只有私钥才能解密。
  通过上面的握手过程可知，https 在证书验证阶段，使用非对称加密来传输共享秘钥，之后的传输中都使用对称加密方式。原因是，非对称加密的加解密效率是非常低的，而 http 场景中通常端与端之间的交互量很大，对非对称加密的效率是无法忍受的。另外， HTTPS 场景中只有服务端保存了私钥，一对公私钥只能实现单向加解密过程。因此 HTTPS 中的内容传输采用对称加密。
- 介绍下 https 中间人攻击的过程
  这个问题也可以问成 为什么需要 CA 认证机构颁发证书？
  我们假设如果不存在认证机构，则人人都可以制造证书，这就带来了"中间人攻击"问题。
  中间人攻击的过程如下：
  1.  客户端请求被劫持，将所有的请求发送到中间人的服务器
  2.  中间人服务器返回自己的证书
  3.  客户端创建随机数，使用中间人证书中的公钥进行加密发送给中间人服务器，中间人使用私钥对随机数解密并构造对称加密，对之后传输的内容进行加密传输
  4.  中间人通过客户端的随机数对客户端的数据进行解密
  5.  中间人与服务端建立合法的 https 连接（https 握手过程），与服务端之间使用对称加密进行数据传输，拿到服务端的响应数据，并通过与服务端建立的对称加密的秘钥进行解密。
  6.  中间人再通过与客户端建立的对称加密对响应数据进行加密后传输给客户端
  7.  客户端通过与中间人建立的对称加密的秘钥对数据进行解密
      简单来说，中间人攻击中，中间人首先伪装成服务端和客户端通信，然后又伪装成客户端和服务端进行通信（如图）。 整个过程中，由于缺少了证书的验证过程，虽然使用了 https，但是传输的数据已经被监听，客户端却无法得知。
      ![](https://mmbiz.qpic.cn/mmbiz_png/2FMs2KmmepgVbJ6Eb4icspSsOS7hUd9hFVgYcTUz2rp2Xw233jrFiaFphw6P0IlufAhDpiczbJvzwKo0J7Gicsv8Tg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)
- HTTPS 握手过程中，客户端如何验证证书的合法性
  CA 证书中会包含颁发机构信息、公钥、公司信息、域名、有效期等信息，浏览器验证证书：
  1.  首先就是要验证域名、有效期等信息是否正确
  2.  然后判断证书来源的合法性。每份签发证书都可以根据验证链查找到对应的根证书，操作系统、浏览器会在本地存储权威机构的根证书，利用本地根证书可以对对应机构签发证书完成来源验证
  3.  判断证书是否被篡改。需要与 CA 服务器进行校验
  4.  判断证书是否已吊销
      以上任意一步都满足的情况下浏览器才认为证书是合法的。
- 有关 gzip 压缩、cdn、，将在系列文章的「性能优化篇」介绍，欢迎持续关注。
- window.performance.now()
- -webkit-tap-highlight-color
- emmet 语法
- CSS.supports
- :invalid 与 :valid
- :placeholder-shown
- caller callee
- Intl.NumberFormat
- text-orientation
- KeyboardEvent.getModifierState()
- 操作系统中进程和线程怎么通信
- 实现原生 ajax
- vue-router 源码
- vue 原理（手写代码，实现数据劫持）
- 你知道哪些 http 头部
- 怎么与服务端保持连接
- webpack 怎么优化
- 你了解哪些请求方法，分别有哪些作用和不同
- 你觉得 typescript 和 javascript 有什么区别
- typescript 你都用过哪些类型
- typescript 中 type 和 interface 的区别
- 你了解 node 多进程吗，node 进程中怎么通信，node 可以开启多线程吗
- node 中 cluster 是怎样开启多进程的，并且一个端口可以被多个进程监听吗
- 算法：树的遍历有几种方式，实现下层次遍历
- 算法题：老师分饼干，每个孩子只能得到一块饼干，但每个孩子想要的饼干大小不尽相同。目标是尽量让更多的孩子满意。如孩子的要求是 1, 3, 5, 4, 2，饼干是 1, 1，最多能让 1 个孩子满足。如孩子的要求是 10, 9, 8, 7, 6，饼干是 7, 6, 5，最多能让 2 个孩子满足。
- 算法题：给定一个正整数数列 a, 对于其每个区间, 我们都可以计算一个 X 值;X 值的定义如下: 对于任意区间, 其 X 值等于区间内最小的那个数乘上区间内所有数和;现在需要你找出数列 a 的所有区间中, X 值最大的那个区间;如数列 a 为: 3 1 6 4 5 2; 则 X 值最大的区间为 6, 4, 5, X = 4 \* (6+4+5) = 60;
- 算法题：合并乱序区间
- 你知道哪些状态码
- options 请求方法有什么用
- HTML5 新增了哪些内容或 API，使用过哪些
- 用一个 div 模拟 textarea 的实现 `<div contenteditable="true"></div>`
- 实现页面加载进度条
- 实现 extend 函数
- 为什么会有跨域的问题以及解决方式
- http 请求跨域问题，你都知道哪些解决跨域的方法
- cors 预请求
- jsonp 原理、postMessage 原理
- 实现拖拽功能，比如把 5 个兄弟节点中的最后一个节点拖拽到节点 1 和节点 2 之间
- 动画：setTimeout 何时执行，requestAnimationFrame 的优点
- 编写分页器组件的时候，为了减少服务端查询次数，点击“下一页”怎样能确保还有数据可以加载（请求数据不会为空）？
- JS 模块化的实践
- require.js 的实现原理（如果使用过 webpack，进一步会问，两者打包的异同及优缺点）
- 实现 gulp 的功能
- 使用前端框架（angular/vue/react）带来哪些好处，相对于使用 jQuery
- vue 双向数据绑定的实现
- 单页应用，如何实现其路由功能
- CSS 实现三角形
- 数组乱序
- for in 和 for of 区别
- 监听一段时间内用户对我方网页的操作
- css 两列布局，右列定宽，左列自适应。
- flex，轴
- addEventListener 细节，如何删除 addEventListener 绑定的事件
- 手撕代码：reduce 实现 map
- for in 和 for of
- 手撕代码: call 实现 bind
- 手撕代码：实现一个函数，每隔 wait 秒执行 func，一共执行 times 次
- 手撕代码：实现一个函数,该函数接收一个 obj, 一个 path, 一个 value，实现 obj[path] = value，obj 类似 json 格式
- 手撕代码：数组扁平化
- this 指向的问题
- 上下文
- dva 解决了什么？如何解决？为什么使用？
- 受控组件 vs 非受控组件
- new ？
- 206 ？
- cookie，session，token，withcredintrals ? cookie，session，token 各种细节，cookie 有哪些属性
- 怎么禁止 js 访问 cookie
- cookie ? session ? httponly?
- cookie,session,localstorage,sessionstorage 有什么区别
- token 为什么能抵抗 csrf？ XSS, CSRF？区别？举个例子？
- 如何定位（检查）内存泄漏？
- GC
- 轮询 websocket
- 事件委托? 阻止冒泡？
- 把 arguments 变成数组？兼容？
- 为什么 reducer 是纯函数？
- 尾递归？
- 组件之间通信
- antd 表单组件 api？底层如何实现的？有没有看过源码
- antd Form.create？
- 事件模型
- 手撕代码 二叉树节点之和 leetcode 原题
- cdn
- 浏览器内核
- 协议
- 布局 水平垂直居中？
- 左右布局：左边定宽、右边自适应，不少于 3 种方法
- 对栅格的理解
- （水平）居中有哪些实现方式
- BFC、IFC
- 回流，重绘
- MVC vs MVVM
- mobx
- 快排的稳定性，手撕代码：快排
- 观察者模式
- 事件循环 event loop 使用场景
- 如果给我一个规定期限内无法完成的任务，我怎么办
- 块级元素和内联元素
- CSS 初始化
- 配过 webpack 吗？
- Promise 链式调用的时候怎么终止它?
- 304
- 盒模型
- http(s) 简述 https 原理，以及与 http 的区别
- https 缺点？如何防范?如何解决？
- http 2.0 新特性？ 头部压缩详细讲讲？
- HTTP 缓存
- HTTP vs HTTPS
- http1.0/1.1/2.0 http 1.1 vs 2.
  基本概念：

  HTTP，全称为 HyperText Transfer Protocol，即为超文本传输协议。是互联网应用最为广泛的一种网络协议
  所有的 www 文件都必须遵守这个标准。

  http 特性：

  HTTP 是无连接无状态的
  HTTP 一般构建于 TCP/IP 协议之上，默认端口号是 80
  HTTP 可以分为两个部分，即请求和响应。

  http 请求：

  HTTP 定义了在与服务器交互的不同方式，最常用的方法有 4 种
  分别是 GET，POST，PUT， DELETE。URL 全称为资源描述符，可以这么认为：一个 URL 地址
  对应着一个网络上的资源，而 HTTP 中的 GET，POST，PUT，DELETE
  就对应着对这个资源的查询，修改，增添，删除 4 个操作。

  HTTP 请求由 3 个部分构成，分别是：状态行，请求头(Request Header)，请求正文。

  HTTP 响应由 3 个部分构成，分别是：状态行，响应头(Response Header)，响应正文。

  HTTP 响应中包含一个状态码，用来表示服务器对客户端响应的结果。
  状态码一般由 3 位构成：

  1xx : 表示请求已经接受了，继续处理。
  2xx : 表示请求已经处理掉了。
  3xx : 重定向。
  4xx : 一般表示客户端有错误，请求无法实现。
  5xx : 一般为服务器端的错误。

  比如常见的状态码：

  200 OK 客户端请求成功。
  301 Moved Permanently 请求永久重定向。
  302 Moved Temporarily 请求临时重定向。
  304 Not Modified 文件未修改，可以直接使用缓存的文件。
  400 Bad Request 由于客户端请求有语法错误，不能被服务器所理解。
  401 Unauthorized 请求未经授权，无法访问。
  403 Forbidden 服务器收到请求，但是拒绝提供服务。服务器通常会在响应正文中给出不提供服务的原因。
  404 Not Found 请求的资源不存在，比如输入了错误的 URL。
  500 Internal Server Error 服务器发生不可预期的错误，导致无法完成客户端的请求。
  503 Service Unavailable 服务器当前不能够处理客户端的请求，在一段时间之后，服务器可能会恢复正常。

  大概还有一些关于 hhtp 请求和响应头信息的介绍。

- SSL/TLS 握手, 保密性？ 完整性？证书？浏览器如何验证 CA 是否正确？CA 证书，验证？
- 中间人攻击？
- 浏览器向服务器发送请求，相应数据包被拦截怎么办?
- tcp/ip 三次握手，四次挥手

- 优化中会提到缓存的问题，问：静态资源或者接口等如何做缓存优化
- 页面 DOM 节点太多，会出现什么问题？如何优化？
- 项目中使用过哪些优化方法，前端性能优化
- 前端安全
- 闭包？使用场景？缺点？
- 继承，几种继承方法
- 原型，原型链最顶层是什么?

```markdown
# window 对象上频繁绑定内容，有什么风险？

微前端，快照沙箱

## 风险分析

1. 命名冲突
2. 全局污染
3. 安全风险
4. 性能问题，增加内存开销

## 解决方案

1. 模块化
2. 命名空间
3. IIFE（形成闭包，形成独立作用域）
4. 开启严格模式

了解 qiankun 的快照沙箱实现原理
```

```markdown
什么是多态？

在父类中定义的属性和方法被子类继承后，可以有不同的实现
```

```javascript
// 手写 call
function method(a, b) {
  console.log('args:', a, b)
  console.log('this:', a, b)
}

method.call(1, 2, 3)

Function.prototype.myCall = function (ctx, ...args) {
  ctx = ctx === null || ctx === undefined ? globalThis : Object(ctx)
  const fn = this
  Object.defineProperty(ctx, key, {
    value: fn,
    enumerable: false
  })
  const r = ctx[key](...args)
  delete ctx[key]
  return r
}
```

```markdown
- url 到显示页面全过程，输入 url 到渲染的全过程，页面的渲染过程 1.读取缓存：搜索自身的 DNS 缓存。(如果 DNS 缓存中找到 IP 地址就跳过了接下来查找 IP 地址步骤，直接访问该 IP 地址。)
  2.DNS 解析:将域名解析成 IP 地址
  3.TCP 连接：TCP 三次握手，简易描述三次握手
  客户端：服务端你在么？
  服务端：客户端我在，你要连接我么？
  客户端：是的服务端，我要链接。
  连接打通，可以开始请求来 4.发送 HTTP 请求 5.服务器处理请求并返回 HTTP 报文 6.浏览器解析渲染页面 7.断开连接：TCP 四次挥手

  关于第六步浏览器解析渲染页面又可以聊聊如果返回的是 html 页面
  根据 HTML 解析出 DOM 树
  根据 CSS 解析生成 CSS 规则树
  结合 DOM 树和 CSS 规则树，生成渲染树
  根据渲染树计算每一个节点的信息
  根据计算好的信息绘制页面

- 从输入 URL 到页面展示发生了什么？(我说了大概 2 分钟 DNS 解析过程，被喊停，然后继续讲 HTML 解析，CSS 解析，合成图层、合成线程调用光栅化线程池，生成位图后浏览器进程间通信过程，显卡缓存与显示器的关系，大概说 10-15 分钟吧)
- 详细讲讲 DNS 如何进行解析
- 能不能说说从输入 URL 到页面渲染经历了什么？(被问过很多次了，DNS 解析过程，HTML 词法分析和语法分析，CSS 解析， 合成图层、合成线程调用光栅化线程池，生成位图后浏览器进程间通信过程，显卡缓存与显示器的关系，面试官说可以)

- 从 url 到页面渲染过程。你刚说到 DNS 解析 能详细说说嘛？DNS 递归和迭代的区别呢？
- 介绍一下 DNS，什么是迭代查询和递归查询，什么是一级域名、二级域名
- dns 相关，dns 服务器是什么，如何查询 dns 的？🌟
- dns 解析（如何优化）
- 说出一个网站从输入到回车到页面渲染出来的样子. 这期间可以怎么做优化？
- - 只答了熟悉的几个阶段
  - dns 解析阶段 预解析
  - 建立 tcp 三次握手 链路复用 keep-alive
  - url 解析：是否命中强缓存，协商缓存等等
  - 页面呈现: 解析 HTML，解析 css,合并 dom 树和 css 规则，生成 render 树,布局 render 树，负责各元素尺寸，位置的计算.绘制 render 树

# 请说说你对 DNS 协议的理解

将域名映射到 IP 上

## 域名解析整个过程

浏览器渲染原理，从地址栏输入到页面渲染完成，经理的所有阶段，详细说明？

1. 用户输入域名
2. 检查自身 DNS 缓存
3. 操作系统 DNS 缓存
4. 本地域名服务器
5. 根据本地 DNS 服务器去查找根 DNS 服务器、顶级域名服务器（TLD）、权威 DNS 服务器
6. 返回结果，浏览器缓存并向 IP 发送请求

## DNS 记录类型

1. A 记录：将域名解析为 IPv4 地址
2. AAAA 记录：将域名解析为 IPv6 地址
3. CNAME 记录：将域名解析为 CNAME 记录指向的域名
4. MX 记录：将域名解析为邮件服务器地址
5. TXT：文本信息存储，域名验证， SPF 记录

## DNS 常见问题

### DNS 解析慢

1. DNS 预解析
2. 使用 CDN，CDN 节点用户就近
3. 减少外部资源请求

### DNS 劫持

1. HTTPS，证书保证传输安全性
2. DNSSEC，DNS 安全扩展

## 优化

1. DNS 缓存
2. nslookup
3. dig
4. 在线 dns.google.com, dnschecker.org

<!-- DNS预解析 -->
<link rel="dns-prefetch" href="xxxx" />

- 从输入 URL 到页面展现这一过程中，浏览器都做了哪些工作

1. 解析 URL
2. 查找缓存
3. DNS 查询
4. 建立 TCP 链接
5. 发送 HTTP 请求
6. 服务器处理请求
7. 服务器发送 HTTP 响应
8. 浏览器接收并解析响应
9. 资源加载与渲染
10. 布局和绘制
11. JS 执行
12. 交互与更新

## url 到加载渲染全过程

1.  DNS 域名解析。
2.  TCP 三次握手，建立接连。
3.  发送 HTTP 请求报文。
4.  服务器处理请求返回响应报文。
5.  浏览器解析渲染页面。
6.  四次挥手，断开连接。

**DNS 协议**提供通过`域名查找 IP地址`，或逆向从 `IP地址反查域名`的服务。DNS 是一个网络服务器，我们的域名解析简单来说就是在 DNS 上记录一条信息记录。

**TCP 三次握手，四次挥手**：握手挥手都是客户端发起，客户端结束。三次握手与四次挥手详解

**负载均衡**：请求在进入到真正的应用服务器前，可能还会先经过负责负载均衡的机器，它的作用是将请求`合理地分配到多个服务器上`，转发 HTTP 请求；同时具备具备防攻击等功能。可分为 DNS 负载均衡，HTTP 负载均衡，IP 负载均衡，链路层负载均衡等。

**Web Server**：请求经过前面的负载均衡后，将进入到对应服务器上的 Web Server，比如 `Apache`、`Tomcat`

**反向代理**是工作在 HTTP 上的，一般都是 `Nginx`。全国各地访问 baidu.com 就肯定要通过代理访问，不可能都访问百度的那台服务器。 （VPN 正向代理，代理客户端）

**浏览器解析渲染过程**：返回的 html 传递到浏览器后，如果有 gzip 会先解压，找出文件编码格式，外链资源的加载 html 从上往下解析，遇到 js，css 停止解析渲染，直到 js 执行完成。解析 HTML，构建 DOM 树 解析 CSS，生成 CSS 规则树 合并 DOM 树和 CSS 规则，生成 render 树去渲染

不会引起 DOM 树变化，页面布局变化，改变元素样式的行为叫**重绘**

引起 DOM 树结构变化，页面布局变化的行为叫**回流**

`GUI渲染线程`负责渲染浏览器界面 HTML 元素,当界面需要 `重绘(Repaint)` 或由于某种操作引发 `回流(reflow)` 时,该线程就会执行。**在 Javascript 引擎运行脚本期间,GUI 渲染线程都是处于挂起状态的,也就是说被”冻结”了. 直到 JS 程序执行完成**，才会接着执行。因此如果 JS 执行的时间过长，这样就会造成页面的渲染不连贯，导致页面渲染加载阻塞的感觉。JavaScript 是可操纵 DOM 的，如果在修改这些元素属性同时渲染界面，渲染前后元素数据可能不一致

GPU 绘制**多进程的浏览器**：主控进程，插件进程，GPU，tab 页（浏览器内核）**多线程的浏览器内核**：每一个 tab 页面可以看作是浏览器内核进程，然后这个进程是多线程的。

它有几大类子线程：

- GUI 线程
- JS 引擎线程
- 事件触发线程
- 定时器线程
- HTTP 请求线程

从 URL 到页面显示的过程(我扩展了 DNS 解析过程和 304 缓存问题)

### 1. 从“在浏览器输入域名”到“页面静态资源完全加载”的整个流程

> **见于：某游戏公司、小鹅通、阿里一面、另外三家小公司**

这问题的答案，我结合了`yck`《前端面试之道》和 浏览器原理专栏：

整个过程可以分为几步：

1.  用户输入

    当用户输入关键字并键入回车之后，这意味着当前页面即将要被替换成新的页面，不过在这个流程继续之前，浏览器还给了当前页面一次执行 `beforeunload` 事件的机会，`beforeunload` 事件允许页面在退出之前执行一些数据清理操作，还可以询问用户是否要离开当前页面。

2.  `URL` 请求过程

    首先，网络进程会查找本地缓存是否缓存了该资源。

    如果有缓存资源，那么直接返回资源给浏览器进程；如果在缓存中没有查找到资源，那么直接进入网络请求流程。这请求前的第一步是要进行 `DNS` 解析，以获取请求域名的服务器 `IP` 地址。如果请求协议是 `HTTPS`，那么还需要建立 `TLS` 连接。

    接下来就是利用 `IP` 地址和服务器建立 `TCP` 连接。连接建立之后，浏览器端会构建请求行、请求头等信息，并把和该域名相关的 `Cookie` 等数据附加到请求头中，然后向服务器发送构建的请求信息。

    数据在进入服务端之前，可能还会先经过负责负载均衡的服务器，它的作用就是将请求合理的分发到多台服务器上，这时假设服务端会响应一个 `HTML` 文件。

    首先浏览器会判断状态码是什么，如果是 `200` 那就继续解析，如果 `400` 或 `500` 的话就会报错，如果 `300` 的话会进行重定向，这里会有个重定向计数器，避免过多次的重定向，超过次数也会报错。

    浏览器开始解析文件，如果是 `gzip` 格式的话会先解压一下，然后通过文件的编码格式知道该如何去解码文件。

3.  - 其中，`DNS`也有几步缓存：浏览器缓存，`hosts`文件，
    - 如果本地域名解析服务器也没有该域名的记录，则开始递归+迭代解析
    - `TCP`三次握手，`HTTP`。`TLS`握手，`HTTPS`。

4.  准备渲染进程

    默认情况下，`Chrome` 会为每个页面分配一个渲染进程，也就是说，每打开一个新页面就会配套创建一个新的渲染进程。

5.  渲染阶段

    文件解码成功后会正式开始渲染流程，先会根据 `HTML` 构建 `DOM` 树，有`CSS`的话会去构建 `CSSOM` 树。如果遇到 `script` 标签的话，会判断是否存在 `async` 或者 `defer` ，前者会并行进行下载并执行 JS，后者会先下载文件，然后等待 `HTML` 解析完成后顺序执行。

    如果以上都没有，就会阻塞住渲染流程直到 `JS` 执行完毕。

`CSSOM` 树和 `DOM` 树构建完成后会开始生成 `Render` 树，这一步就是确定页面元素的布局、样式等等诸多方面的东西

在生成 `Render` 树的过程中，浏览器就开始调用`GPU` 绘制，合成图层，将内容显示在屏幕上了。

- DNS 解析会出错吗，为什么
```

```javascript
/**
 * 有很多 IP 地址，如何最快找出 RTT 最短的 IP 地址
 * 假设最大并发数为 10
 *
 * [RTT：Round-Trip Time，往返时延]
 */

function chunk(arr, size) {
  return Array.from({ length: Math.ceil(arr.length / size) }, (v, i) => arr.slice(i * size, i * size + size))
}

async function race(ips, rtt) {
  return new Promise((resolve) => {
    const controller = new AbortController()
    const signal = controller.signal
    setTimeout(() => {
      resolve(null)
      // 取消所有请求
      controller.abort()
    }, rtt)
    let start = Date.now()
    for (const ip of ips) {
      fetch(`http://${ip}/ping`, { signal }).then(() => {
        const rtt = Date.now() - start
        resolve({ rtt, ip })
      })
      // 取消所有请求
      controller.abort()
    }
  })
}

async function findShortestRTT(ips, parallelCount = 10) {
  // 对 ip 地址分组
  const ipChunks = chunk(ips, parallelCount)
  let result = {
    rtt: Infinity,
    ip: ''
  }
  for (const chunk of ipChunks) {
    const temp = await race(chunk, result.rtt)
    if (temp) {
      result = temp
    }
  }
  return result.ip
}
```

```javascript
/**
 * ajax
 *  XHR
 *  Fetch
 *  axios -- > XHR
 *  umi - request -- > Fetch
 */

// xhr 请求进度监控
xhr.upload.addEventListener('progress', (e) => {
  console.log(e.loaded, e.total)
})

// xhr 响应进度监控
xhr.addEventListener('progress', (e) => {
  console.log(e.loaded, e.total)
  onProgress &&
    onProgress({
      loaded: e.loaded,
      total: e.total
    })
})
xhr.open(method, url)
xhr.send(data)

// fetch 响应进度监控
const resp = await fetch(url, {
  method,
  body: data
})
const total = +resp.headers.get('content-length')
const decoder = new TextDecoder()
let body = ''
const reader = resp.body.getReader()
let loaded = 0
while (1) {
  const { done, value } = await reader.read()
  if (done) {
    break
  }
  loaded += value.length
  body += decoder.decode(value)
  onProgress &&
    onProgress({
      loaded,
      total
    })
}
```

```javascript
// 给 fetch 添加超时功能
function createRequestWithTimeout(timeout = 5000) {
  return function (url, options) {
    return new Promise((resolve, reject) => {
      const abort = new AbortController()
      options = options || {}
      if (options.signal) {
        options.signal.addEventListener('abort', () => {
          abort.abort()
        })
      }
      options.signal = abort.signal
      setTimeout(() => {
        reject(new Error('timeout'))
        abort.abort()
      }, timeout)

      fetch(url, options).then(resolve, reject)
    })
  }
}
```

```javascript
// js 实现函数重载
function createOverload() {
  const fnMap = new Map()
  function overload(...args) {
    const key = args.map((item) => typedof(item)).join(',')
    const fn = fnMap.get(key)
    if (!fn) {
      throw new TypeError('没有找到对应的实现')
    }
    return fn.apply(this, args)
  }
  overload.addImpl = function (...args) {
    const fn = args.pop()
    if (typeof fn !== 'function') {
      throw new TypeError('fn must be a function')
    }
    const key = args.join(',')
    fnMap.set(key, fn)
  }
  return overload
}
```

```javascript
const obj = {
  flag: 'Jhon',
  func: function () {
    console.log(this)
    console.log(this.flag)
  }
}

const p = new Proxy(obj, {})
p.func()
obj.func()
```

```javascript
// 使用代理实现单例
class MyVideo {
  constructor() {
    console.log('new MyVideo')
  }
}

function sington(className) {
  let ins = null
  const proxy = new Proxy(className, {
    construct(target, args) {
      if (!ins) {
        ins = Reflect.construct(target, args)
      }
      return ins
    }
  })
  proxy.prototype.construct = proxy
  return proxy
}
```

- 【可视化】主导完成平台可视化渲染引擎（可视化图表的组件、数据协议）设计与开发，基于 echarts（svgRenderer、canvasRenderer 一千万行数据的表格渲染【不能使用虚拟滚动】canvas table，chunk）封装业务图表库，服务于平台可视化场景

  - 用库
  - 初级：table dom
  - 中级：虚拟表格
  - 高级： canvas table
  - 专家：canvas+tile 技术
  - 高级专家：skia+webassembly (白板 webassembly+Skia Engine)

- 说说项目中遇到的坑，怎么解决的
- 项目中有考虑到哪些优化的地方？

```markdown
正则表达式

- 匹配量的：\* + ? {n} {n,} {n,m} .
- 匹配位置的：^ $
- 匹配并且需要支持分组的时候需要括号来包裹：(匹配的模式)
- 匹配条件的：|
- 匹配集合的：[]
- 匹配非集合的：[^]
```

```shell
git config pull.rebase true
git pull --rebase
优化仓库commit
```

- `npm cache clean --force` 命令强制清理缓存

- 请求头字段

|   请求头名称    |                                    含义                                    |
| :-------------: | :------------------------------------------------------------------------: |
|     Accept      |                 客户端可以处理的内容类型，如 `Accept: */*`                 |
| Accept-Charset  |           客户端可以处理的字符集类型，如 `Accept-Charset: utf-8`           |
| Accept-Encoding |       客户端可以处理的压缩编码，如 `Accept-Encoding: gzip, deflate`        |
| Accept-Language |         客户端当前设置的语言，如 `Accept-Language: zh-CN,zh;q=0.9`         |
|   Connection    |         客户端与服务器之间连接的类型，如 `Connection: keep-alive`          |
|     Cookie      |                         当前页面设置的任何 Cookie                          |
|      Host       |                            发送请求页面所在的域                            |
|     Referer     |   当前请求页面的来源页面的地址，即当前页面是通过此来源页面里的链接进入的   |
|   User-Agent    | 客户端的用户代理字符串，一般包含浏览器、浏览器内核和操作系统的版本型号信息 |
|  Content-Type   |  客户端告诉服务器实际发送的数据类型，如 `Content-Type: application/json`   |

```javascript
const first = () =>
  new Promise((resolve, reject) => {
    console.log(3)
    let p = new Promise((resolve, reject) => {
      console.log(7)
      setTimeout(() => {
        console.log(5)
        resolve(6)
      }, 0)
      resolve(1)
    })
    resolve(2)
    p.then((arg) => {
      console.log(arg)
    })
  })

first().then((arg) => {
  console.log(arg)
})
console.log(4)
```

- 与获取普通对象的属性值不同，使用 for...in、for...of、Object.keys()、Object.values()、Object.entries()、Object.getOwnPropertyNames()这些方法并不能获取 Symbol 类型的属性名。ES6 专门提供了 Object.getOwnPropertySymbols()方法，用来获取一个给定对象自身的所有 Symbol 属性，返回的结果为一个数组。
- font-size-adjust
- offset-position 和 offset-path

```javascript
typedof NaN
9999999999999999
0.5+0.1==0.6
0.1+0.2==0.3
Math.max()
Math.min()
[]+[]
[]+{}
{}+[]
true+true+true===3
true-true
true==1
true===1
(!+[]+[]+![]).length
9+'1'
91-'1'
[]==0
```

- 数字计算类库 Math.js, decimal.js, big.js
- 组合函数、管道函数、函数柯里化

```markdown
- 为什么需要 DOM 树？
  结构化数据：将 HTML 标签（如<div>、<p>）和文本内容转化为节点对象，以树形结构表示标签的父子嵌套关系。
  JavaScript 动态操作的基础：这一过程解决了原生 HTML 文本的局限性，允许 JavaScript 通过属性与方法直接操作节点。
  渲染过程的核心输入：DOM 树提供内容结构，CSSOM 树提供样式规则，两者结合生成渲染树（Render Tree），决定页面元素的可见性与布局。
  安全性：DOM 解析阶段会过滤恶意内容。

在构建 DOM 的过程中，如果遇到 link 标签，当把它插入到 DOM 树上后，此时如果外部的 CSS 文件还没有下载完，主线程也不会停下来等待，因为下载和解析 CSS 的工作是在预解析线程中进行的，所以 CSS 并不会阻塞 html 的解析。

解析 html 的目的是为了生成 DOM 树，而解析 CSS 的目的同样是为了生成 CSSOM 树，两者都是为了转换成浏览器能够理解的结构，也可以方便 javascript 的访问。

- CSS 是否会阻塞渲染？
  虽然 CSS 并不会阻塞 html 的解析，但由于渲染树的生成需要 CSSOM 的参与，所以 CSS 是会阻塞页面渲染的
  真的原因是，如果浏览器在 CSS 检查之前展示了页面，那么每个页面都是没有样式的，等一会之后又突然有了样式，整个页面的体验就会很差。由于 CSSOM 被用作创建渲染树，那么如果不能高效的利用 CSS 会导致白屏时间的增加

在构建 DOM 的过程中，如果遇到 script，在默认情况下主线程会停止对 html 的解析，转而等待 JS 文件下载好，并将全局代码解析执行完成后，才会继续解析 html。这是因为 JS 代码的执行过程可能会修改当前的 DOM 树，所以 DOM 树的生成必须暂停。这就是 JS 会阻塞 HTML 解析的根本原因。

- defer
  延迟脚本执行：带有 defer 属性的脚本，加载不会阻塞页面的解析和渲染过程，浏览器可以继续解析页面的其余部分，当整个文档完成解析后，在触发 DOMContentLoaded 事件之前执行这些脚本。
  顺序执行：带有 defer 属性的脚本，尽管是异步加载的，但是它们之间会保持顺序执行。
- async
  非阻塞加载：带有 async 属性的脚本加载是异步的，不会阻塞 HTML 文档的解析，浏览器可以继续向下解析和渲染。不过，当脚本加载完成后，会立即执行脚本内的代码，此时如果 HTML 还没有解析完成，则会暂停对 html 的解析，从而阻塞页面渲染。但如果当脚本加载完准备执行之前，html 已经解析完成，此时也不会阻塞页面渲染。
  执行不可控：带有 async 属性的脚本，执行是不可控的，因为无法确定脚本的下载速度与脚本内容的执行速度，如果存在多个 script async 时，他们之间的执行的顺序也是不可控的，完全取决于各自的下载速度，谁先下载完成就先执行谁。
- module
  非阻塞加载：带有 type="module"的脚本加载是异步的，这类标签视为 ES6 模块来处理，而 ES6 模块是设计为异步加载的，当浏览器遇到此类标签时，会开始异步下载改模块及其依赖项，不会暂停页面的解析和渲染工作，当 HTML 文档被解析完成后，会在触发 DOMContentLoaded 事件之前执行这些脚本。所以它的表现有点类似 defer。
  模块化支持：带有 type="module"的脚本会自动分割成不同的模块，并且相互之间作用域是隔离的，浏览器会自动加载这些模块，无需手动管理依赖关系。
  支持静态导入和动态导入：可以使用 import 语句静态地导入其它模块，这些导入的模块加载时自动解析和执行。还可以使用 import()函数动态地导入模块，根据需要在运行时加载模块，进一步控制模块的加载和执行时机。
```

- 磨砂玻璃效果 backdrop-filter

```javascript
// 打印三角形
function print(n) {
  const result = new Array(n)
    .fill('')
    .map((_, i) => {
      const line = new Array(2 * n - 1).fill(' ')
      line[n - 1] = 1
      for (let j = 2; j <= i + 1; j++) {
        line[n - j] = j
        line[n + j - 2] = j
      }
      return line.join('')
    })
    .join('\n')
  console.log(result)
}
```

```javascript
// 函数的链式调用
class MyCalculator {
  constructor(value) {
    this.value = value
  }

  add(num) {
    this.value += num
    return this
  }
  minus(num) {
    this.value -= num
    return this
  }
  multiply(num) {
    this.value *= num
    return this
  }
  divide(num) {
    this.value /= num
    return this
  }
  toString() {
    return this.value
  }
}

const calculartor = new MyCalculator(121)
console.log(calculartor.add(1).minus(2).multiply(3).divide(4) == 90)
```
