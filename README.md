```text
https://www.zhangxinxu.com/wordpress/2024/11/js-selectionchange-event/
tsup
白板 webassembly+Skia Engine
免费课合集：https://qmdqi.xetlk.com/s/376rbn
https://www.zhangxinxu.com/wordpress/2024/09/js-scrollend-event/
https://www.zhangxinxu.com/wordpress/2024/09/js-object-groupby/
https://www.zhangxinxu.com/wordpress/2024/09/css-math-round-function/
HTMLCollection(动态) & NodeList(静态) 伪数组
CSS文本自定义高亮AP简介 https://www.zhangxinxu.com/wordpress/2024/07/css-custom-highlight-api/
initial-letter https://www.zhangxinxu.com/wordpress/2024/03/css-initial-letter/
margin-trim 属性设置在容器元素上，可以让子元素(需边缘接触) margin 设置计算值变成 0 https://www.zhangxinxu.com/wordpress/2023/05/css-margin-trim/
align-content也适用于普通元素
Math.hypot
grid-template-rows: masonry;
vue方法中属性丢失的问题 methods配置的方法与组件实例的方法
console.log(([][[]] + [])[+!![]] + ([] + {})[+!![] + +!![]])
展示组件和容器组件
使用computed拦截v-model https://juejin.cn/post/7338634091397431330
v-model 父传子值，元素更改后获取值滞后，nextTick
右键菜单组件的封装 https://blog.csdn.net/DuyiZiChen/article/details/131405493
SocketIO
视频文本化 text-image
使用冻结对象提升效率 Object.freeze() 冻结对象在vue中不会变为响应式
symbol.toStringTag
backface-visibility
行盒的截断样式：box-decoration-break
CSS实现奥林匹克五环
全局导入和局部导入的区别
ESModule 的工作原理
transform 从右到左 translate3d
localeCompare 字典顺序
依赖检查工具 depcheck
mask-image
vue3 expose defineExpose
正则匹配的贪婪模式和惰性模式有什么区别
node 版本管理工具:`volta` `nvm`
new.target 可以判断函数是否被 new 调用
浏览器的自动播放策略
BFF 层 backends for frontends
函数签名 = 函数名 + 参数 + 返回值
改变 webkit 表单输入框 placeholder 的颜色值：input::-webkit-input-placehold
去掉 ios 系统中元素被触摸时产生的半透明灰色遮罩：tip-highlight-color:rgba(0,0,0,0)
http accept-lang/navigator.lang
git 忽略文件名大小写 git config core.ignorecase false
content-type
showDirectoryPicker FileSystem API
insertBefore
removeProperty
Web Locks API
preventDefault、stopPropagation
俄罗斯方块实现思路
conic-gradient
web-vitals
?? 运算符 返回第一个已定义的值
色彩空间 hex rgb hsl hsv
Object.defineProperty 只能监听到对象属性的读取或者是写入，而 Proxy 除读写外还可以监听对象中属性的删除，对对象当中方法的调用
object-fit
不规则的文字环绕:shape-outside
getPrototypeOf、setPrototypeOf
Array.from()
[动画库：GSAP scrolltrigger]https://gsap.com/
addEventListener compositionstart 'contextmenu'
markRaw、withModifiers
数组新增的纯函数 API：toSorted、toReversed、toSpliced、with(修改数组)
font-variant、text-transform
js 文档注释：jsDoc
vscode 正则插件：Regex Previewer
ElementUI 日期选择器时间选择范围限制
自定义指令控制权限的弊端 https://blog.csdn.net/layonly/article/details/139402930 DOM 元素删除后，生命周期会正常进行，还会请求数据
组件循环依赖：动态导入
实现 sleep 函数
实现 throttle 节流函数
图片调色盘：colorThief
符号绑定
css 新单位 vmin vmax
前端ocr图片文字提取功能: tesseract.js
拖拽组件: vue-draggable-plus
重绘和回流
防截屏防录制：Encrypted Media Extensions API
console.log() 打印对象时，点击小三角实时加载
元素倒影:-webkit-box-reflect
页面可见度 API page visibility
禁止触发系统菜单和长按选中：`touch-callout:none` contextmenu
禁止用户选中文字：`user-select:none`
使用data url预览图片 https://blog.csdn.net/u012804440/article/details/136018598
在 TypeScript 中正确的遍历一个对象
```

```javascript
Array.prototype.myForEach = async function (callback, thisArg) {
  const _arr = this,
    _isArray = Array.isArray(_arr),
    _thisArg = thisArg ? Object(thisArg) : globalThis
  if (!_isArray) {
    throw new TypeError('The caller of myForEach must be the type an array')
  }
  for (let i = 0; i < _arr.length; i++) {
    await callback.call(_thisArg, _arr[i], i, _arr)
  }
}

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

```javascript
// Web网页 阻止息屏 Screen Wake Lock API https://www.zhangxinxu.com/wordpress/2024/03/js-screen-wake-lock-api/
navigator.wakeLock.request('screen')
// 当前页面最小化，或者非当前显示标签页，屏幕的 Wake 锁定行为会被释放
document.addEventListener('visibility', () => {
  if (document.visibilityState === 'visible') {
    navigator.wakeLock.request('screen')
  }
})

// wakeLock 是个 WakeLockSentinel 对象
let wakeLock = null
navigator.wakeLock.request('screen').then((result) => {
  wakeLock = result
})

// 释放锁
wakeLock.release().then(() => {
  wakeLock = null
})

// 知道何时释放
wakeLock.addEventListener('release', () => {
  console.log('唤醒锁定已释放')
})
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

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      /* @scope规则 */
      @scope (#app) {
        .box {
          width: 100px;
          height: 100px;
          background-color: red;
        }
      }
    </style>
  </head>
  <body>
    <div id="app">
      <div class="box"></div>
    </div>
  </body>
</html>
```

```text
跨标签页通信常见方案
  BroadcastChannel API
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

```
打包结果分析工具
  Webpack:webpack-bundle-analyzer
  vite:vite-bundle-visualizer
       rollup-bundle-visualizer
```

```
元素的绘制顺序
  可替换元素
    元素本身
    元素内容
  堆叠上下文、层叠上下文
    z-index,position:relative
    transform
```

```javascript
// 文件上传
//   单文件上传 multiport/form-data
//   二进制格式上传文件 binary/application/octet-stream

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

```ts
// never类型的妙用
type Method = 'GET' | 'POST'

function request(url: string, method: Method) {
  if (method === 'GET') {
    // do something
  } else if (method === 'POST') {
    // do something
  } else {
    // 之后 Method 方法修改，这里会报错
    const n: never = method
  }
}

// never类型的妙用2
function m<T>(x: T extends number ? never : T) {}
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
    vdo.mute = true
    vdo.autoplay = true
    vdo.src = URL.createObjectURL(file)
    vdo = oncanplay = () => {
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

```ts
class A {
  a: number = 1
  b: string = 'a'
}

type AFields = keypf
InstanceType<typeof A>
```

```text
值传递
引用传递
js 引用传递 具名导入 import { n as main } from 'a.js'
https://blog.csdn.net/brilliantSt/article/details/136300491
```

```js
/**
 * 对象的属性迭代顺序大致遵循以下规则：
 *  1、数值属性：首先会迭代对象的所有数值键，按照数值的升序进行。
 *  2、字符串属性：然后按字符串的插入顺序依次迭代字符串属性
 *  3、symbol属性：再然后按symbol的插入顺序依次迭代symbol属性
 *  4、继承属性：当一个对象上有自己的属性，并且还继承一些属性的时候。整体也是按照上述三条规则排序的，但是插入顺序可能需要注意。这里暂不考虑这种特殊复杂情况。
 */
const obj = {
  a: 0,
}
obj['1'] = 0
obj[++obj.a] = obj.a++
const values = Object.values(obj)
obj[values[1]] = obj.a
console.log(obj)
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

```js
// JSLabel语法
outer: for (let i = 0; i < 10; i++) {
  console.log('顶层循环')
  for (let j = 0; j < 10; j++) {
    console.log('内层循环', i, j)
    if (i * j > 30) {
      console.log('退出顶层循环')
      break outer
    }
  }
}
```

```js
/**
 * nums 数组中包含 1 个或多个正整数
 * 其他的数字都出现 2 次
 * 只有一个数字出现了 1 次
 * 找出只出现了 1 次的数字
 */
function uniqueNumber(nums) {
  // 0 异或 别的数等于数本身
  // 相同的数异或结果为 0
  var result = 0
  for (const n of nums) {
    result ^= n
  }
  return result
  // return nums.reduce((a, b) => a ^ b, 0)
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
// 对防抖函数进行类型标注
declare function debounce<T extends any[]>(fn: (...args: T) => any, delay: number): (...args: T) => void
```

```javascript
/**
 * 两个超过整数存储范围的大正整数求和
 * @param {String} a
 * @param {String} b
 */

function sum(a, b) {
  let result = ''
  const len = Math.max(a.length, b.length)
  a = a.padStart(len, '0')
  b = b.padStart(len, '0')
  let addOne = 0
  for (let i = len - 1; i >= 0; i--) {
    const n = +a[i] + +b[i] + addOne
    addOne = Math.floor(n / 10)
    result = (n % 10) + result
  }
  if (addOne) result = addOne + result
  return result
}
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
```

```javascript
// 2048游戏核心逻辑
const matrix = [
  [0, 2, 2, 0],
  [0, 0, 2, 2],
  [2, 4, 4, 2],
  [2, 4, 4, 4],
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
    right: (i, j) => [i, j - 1],
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
    value: null,
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
// call 方法第一个参数为 null 或 undefined，this 会被设置为全局对象
// call和apply的链式调用
const r = console.log.call.call.call.call.call.call.call.apply((a) => a, [1, 2])

console.log(r)

console.log(console.log.__proto__ === Function.prototype)
console.log(console.log.call === Function.prototype.call)

// const r = Function.prototype.call.apply((a) => a, [1, 2])
```

```javascript
Promise.myAll = function (promises) {
  let res, rej
  const p = new Promise((resolve, reject) => {
    res = resolve
    rej = reject
  })
  let i = 0
  let result = []
  for (const prom of promises) {
    const index = i
    i++
    Promise.resolve(prom).then((data) => {
      // 1.将完成的数据加入到最终结果
      result[index] = data
      // 2.判断是否全部完成
      i--
      if (i === 0) {
        res(result)
      }
    }, rej)
  }
  if (i === 0) {
    res([])
  }
  return p
}

Promise.myAll([1, 2, 3, Promise.reject(4)])
  .then((data) => {
    console.log('%c 🍑 data', 'font-size:16px;color:#ea7e5c', data)
  })
  .catch((e) => {
    console.log('%c 🎂 e', 'font-size:16px;color:#f5ce50', e)
  })
```

```js
// ①
Pormise.resolve()
  .then(() => {
    console.log(0)
    return Promise.resolve(4)
  })
  .then((res) => {
    console.log(res)
  })
Promise.resolve()
  .then(() => {
    console.log(1)
  })
  .then(() => {
    console.log(2)
  })
  .then(() => {
    console.log(3)
  })
  .then(() => {
    console.log(5)
  })
  .then(() => {
    console.log(6)
  })

/**
 * thenable
 *  1. 完成，所有注册的 thenable 进队列
 *  2. 调用 then，如果已完成，直接进队列
 */

// ②
new Promise((resolve, reject) => {
  resolve(2)
  new Promise((resolve, reject) => {
    resolve(5)
  }).then((v) => console.log(v))
}).then((v) => console.log(v))

// ③
new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve(2)
    new Promise((resolve, reject) => {
      resolve(5)
    }).then((v) => console.log(v))
  })
}).then((v) => console.log(v))

// ④
const promise1 = Promise.resolve('first')

const promise2 = new Promise((resolve) => {
  setTimeout(() => {
    resolve('second')
  }, 1000)
})

const promise3 = Promise.reject('third')

function handlePromise(promise) {
  return promise
    .then((value) => {
      console.log(value)
      return value
    })
    .catch((error) => {
      console.log('Error', error)
      return 'Error handler'
    })
}

async function runPromises() {
  try {
    const result1 = await handlePromise(promise1)
    console.log('result1', result1)
    // const result2 = await handlePromise(promise2)
    const result2 = handlePromise(promise2)
    console.log('result2', result2)
    const result3 = await handlePromise(promise3)
    console.log('result3', result3)
  } catch (error) {
    console.error('Caught error', error)
  }
}

runPromises()
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

```css
/* 黏性定位 */
position: sticky

;
样式计算 视觉格式化模型
包含块
最近可滚动祖先
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
    bgColor: #fff,
  ),
  dark: (
    textColor: #fff,
    bgColor: #333,
  ),
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
  c: 3,
}
module.exports = {
  d: 4,
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
// 标签化模板 styled components
function tag(strings, ...values) {
  console.log(strings)
  console.log(values)
}

const user = {
  name: 'LBJhui',
  age: 18,
}

const hi = tag`My name is ${user.name}, I'm ${user.age} years old.`
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
;[NaN]
  .includes(NaN) // true
  [NaN].indexOf(NaN) // -1
isNaN(NaN) // true
isNaN(1) // false
isNaN('1') // false
isNaN('x') // true

Number(undefined) // NaN
Number('   123    ') // 123
Number('12 3') // NaN (only whitespace from the start and end are removed)
NaN ** 0 // 1
isNaN('this is a string not a NaN value') // true
Number.isNaN('this is a string not a NaN value') // false

// NaN 和 Number.isNaN 有什么区别 Not a Number
console.log(NaN === NaN) // false
console.log(Number.isNaN(NaN)) // true
console.log(Number.isNaN('42')) // false
console.log(Number.isNaN('NaN')) // false
console.log(isNaN(NaN)) // true
console.log(isNaN(42)) // false
console.log(isNaN('NaN')) // true

/**
 * NaN 与任何值相加结果都为 NaN
 * NaN 与任何值相等结果都为 false
 *
 * isNaN() 先尝试转换为数字，若无法转换为数字，则返回 true，否则返回 false
 * Number.isNaN 直接检查一个值是否是 NaN
 */

console.log(isNaN('0yd'))
console.log(isNaN('0xd'))
console.log(NaN === NaN)
console.log(Number.isNaN('0yd'))
console.log(Number.isNaN('0xd'))
```

```js
Object.freeze(obj)
let person = {
  a: '1',
  b: '2',
}
Object.freeze(person)
person.a = '3'
console.log(person) // {a: '1', b: '2'}
person = {
  c: '3',
}
console.log(person) // {c: '3'}

/**
 * Object.freeze() 返回的是一个不可变的对象。这就意味着我们不能添加，删除或更改对象的任何属性
 * const 和 Object.freeze 并不同，const 是防止变量重新分配，而 Object.freeze 是使对象具有不可变性
 *
 * Object.freeze 只能冻结当前对象
 *  Object.freeze 仅能冻结对象的当前层级属性，换而言之，如果对象的某个属性本身也是一个对象，那么这个内部对象并不会被 Object.freeze 冻结
 */

// 深冻结
function deepFreeze(obj) {
  var propNames = Object.getOwnPropertyNames(obj)
  propNames.forEach((name) => {
    var prop = obj[name]
    if (typeof prop == 'object' && prop !== null) deepFreeze(prop)
  })
  return Object.freeze(obj)
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
    },
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
// 监听元素的重叠度
const ob = new IntersectionObserver(entries => {
  const entry = entries[0]
  if (entry.isIntersecting) {
    console.log('加载更多')
  }
}, {
  root: null
  threshold: 0
})
const dom = document.querySelector('.loading')
ob.observe(dom)
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

```text
非严格相等
  两端类型一致
    等同于严格相等
  两端类型不一致
    特殊
      null == undefined
      null === undefined
      null == 0
      null == ''
      undefined == ''
    规则 1 均为原始，转数字
    规则 2 有对象，转原始

1. 相等比较（==）
  1. 如果两个操作数类型相同，执行严格比较
  2. 如果两个操作数类型不同，则进行**类型转换后**再进行比较，规则如下：
    1. 如果一个操作数是数值，另一个操作数是字符串，则将字符串转换为数值，然后进行比较
    2. 如果一个操作数十布尔值，则将布尔值转换为数值，然后进行比较
    3. 如果一个操作数十对象，另一个操作数十数值或字符串，则将对象转换为原始值，然后进行比较

如果一个操作数是对象，另一个操作数是字符串或者数字，会首先调用对象的 valueOf 方法，将对象转化为基本类型，再进行比较
当valueOf 返回的不是基本类型的时候，才会调用 toString 方法

Object.is 和 === 规则如下
Object.is 和 === 在比较两个值时都不会进行类型转换

Object.is：
  当比较 NaN 是，Object.is(NaN,NaN) 返回 true
  当比较 +0 和 -0 时，Object.is(+0,-0) 返回 false，因为它能区分正零和负零

===：
  NaN === NaN 返回 false， 因为 NaN 不等于任何值，包括它自身
  对于 +0 和 -0，+0 === -0 返回 true，因为严格相等不区分正负
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

```js
const o = (function () {
  const obj = {
    a: 1,
    b: 2,
  }
  return {
    get: function (k) {
      return obj[k]
    },
  }
})()
// 闭包代码的提权漏洞
// 如何在不改变上面代码的情况下，修改 obj 对象
Object.defineProperty(Object.prototype, 'abc', {
  get() {
    return this
  },
})
console.log(o.get('abc'))

// 解决
const o = (function () {
  // var obj = Object.create(null)
  const obj = {
    a: 1,
    b: 2,
  }
  // Object.setPropertytypeOf(obj, null)
  return {
    get: function (k) {
      if (obj.hasOwnProperty(k)) {
        return obj[k]
      }
    },
  }
})()
```

```js
let a = 5
let b = 6

// ①
const temp = b
b = a
a = temp

// ②
;[a, b] = [b, a]

// ③ 数字
a = a + b
b = a - b
a = a - b
// a = b + (b = a) - b

// ④ 整数
a = a ^ b
b = a ^ b
a = a ^ b
```

```js
// 手写 call
Function.prototype.myCall = function (ctx, ...args) {
  ctx = ctx === null || ctx === undefined ? globalThis : Object(ctx)
  const fn = this
  const key = Symbol()
  Object.defineProperty(ctx, key, {
    value: fn,
    enumerable: false,
  })
  const r = ctx[key](...args)
  delete ctx[key]
  return r
}

// 手写 bind
Function.prototype.myBind = function (ctx, ...args) {
  const fn = this
  return function (...restArgs) {
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

```text
# 查询当前使用的镜像源
npm get registry

# 设置为淘宝镜像源
npm config set registry https://registry.npmmirror.com/

# 还原为官方镜像源
npm config set registry https://registry.npmjs.org/


github 慢
C:\Windows\System32\drivers\etc\hosts
140.82.114.4 github.com
199.232.69.194 github.global.ssl.fastly.net
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

```js
// 函数的length
function fun1(a) {}

function fun2(b = 'a', a) {}

function fun3(a, b = 'a') {}

function fun4(a, ...arr) {}

console.log(fun1.length)
console.log(fun2.length)
console.log(fun3.length)
console.log(fun4.length)
```

```text
parseInt和Math.floor有什么区别
Math.floor()
无论正负，Math.floor都只是简单地将一个数向下取整到最接近的整数
它只接收一个参数：你想要向下取整的数

Math.floor(-4.05)
parseInt(-4.05)

parseInt：向零取整
对于负数，会 ** 向上取整 ** 到最接近的整数
对于正数，会 ** 向下取整到 ** 最接近的整数

parseInt
会忽略任何数字后面的非数字字符
parseInt('4.05abc') // 4
Math.floor('4.05abc') // NaN

parseInt
处理不同的进制数据,将其他进制转换为十进制
parseInt('11', 2)  // 结果是3，因为在2进制中，11表示的是十进制中的3

;['1', '2', '3'].map(parseInt) // parseInt(item,index,arr)

parseInt
第二个参数：
  1.  不传递、undefined、0  自动
    1）0x 十六进制
    2）0 十进制 / 八进制
    3）十进制
  2. 无效进制（2 - 36 有效） NaN
  3. 有效进制
      正常转换

BigInt('0b' + a)
num.toString(2) // 十进制转换为二进制
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
  enumerable: false,
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

```ts
type Props = {
  onClick: (e: MouseEvent) => void
  onDrag: (e: DragEvent) => void
  news1Types: string
  class2Name: string
}

type t1 = keyof Props
type t2 = keyof Props & {}
type t3 = keyof Props & `on${string}`
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
  },
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
  },
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
  },
}
obj.innerFunction1()
obj.innerFunction2()
```

```text
object 和 map 有什么相同点和不同点
创建方式的区别
  通过字面量创建 Object、通过构造函数创建 Object
  通过构造函数创建 Map
key 的类型不同
  Object：对象的键是字符串或者Symbol
  Map：Map可以使用任何类型的值作为键，包括对象、函数、原始值等。
key 的顺序
  Object：key的顺序与插入顺序无关
  Map：key的顺序就是插入的顺序
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

```js
中文输入法导致的高频事件
// 多个按键对应一个字符
dom.addEventListener('compositionstart', function (e) {})
dom.addEventListener('compositionend', function (e) {})
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
统计字符频率的风骚写法
const str = 'dlskdlkdsowjfood'
const result = [...str].reduce((a, b) => (a[b]++ || (a[b] = 1), a), {})
```

```ts
// TS中字符串索引带来的类型问题
const obj = {
  name: 'LBJhui',
  age: 18,
}

function method(key: string) {
  const v = obj[key as keyof typeof obj]
}
```

```text
为什么需要箭头函数
  消除函数二义性
  指令序列
  创建实例
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
const match

=
matchMedia

(
'(prefers-color-scheme: dark)'
)
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

```js
// 隐式转换和布尔判定
;[] + []
;[] + ![]
```

```js
// 数字格式化
const str = '10000000000'
const s = str.replace(/\B(?=(\d{3})+$)/g, ',')
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
inital: 默认值
unset 清除浏览器样式
revert 使用浏览器的样式
```

```text
Cookie 中的 SameSite：用于限制跨站请求
None:不作任何限制，使用该值必须保证 Cookie 为 Secure，否则无效
lax:阻止发送 Cookie，但对超链接放行，默认值
strict:阻止发送 Cookie
```

```html
<!-- 图片的马赛克效果 -->
①
<!-- step 1 -->
<svg>
  <filter id="mosaic">
    <feFlood x="4" y="4" height="2" width="2" />
    <feComposite width="8" heigth="8" />
    <feTile result="a" />
    <feComposite in="SourceGraphic" in2="a" operator="in" />
    <feMorphology operator="dilate" raduis="4" />
  </filter>
</svg>
<!-- step 2 马赛克图片应用滤镜 -->
<style>
  img {
    filter: url(#mosaic);
  }
</style>

② image-rendering:pixelated 图片要小 vite-imagetools
<style>
  img {
    image-rendering: pixelated;
  }
</style>

<style>
  /* 磨砂玻璃效果 */
  backdrop-filter: blur (10 px);

  /* 阴影效果 */
  filter: drop-shadow (0 0 5 px #000);
  filter: blur (5 px);
  filter: grayscale (50 %);
  filter: hue-rotate (90 deg);
</style>
```

---

# 为什么要使用 Typescript？

增加了静态类型 代码质量更好 更健壮

优势

- 杜绝手误导致变量名写错
- 类型一定程度充当文档
- IDE 自动填充 自动联想

---

const readonly
const 防止变量值被修改
readonly 防止变量属性值被修改

枚举
常量枚举 编译阶段会被删除 被内敛

接口
类型别名 可以用于其他类型，基本类型，联合类型，元组
都可以用来描述对象或函数类型

---

- any 动态类型变量 失去了类型检查的作用
- never 永远不存在的值的类型
  - 抛出异常 根本没有返回值的函数表达式 或者箭头函数表达式返回值类型
- unknown 任何类型的值都可以赋值给 unknown，unknown 只能赋值给 unknown、any
- null & undefined 默认是所有类型的子类型 --strictNullChecks 标记 null 或者 undefined 只能赋值给 void 或者它们自己
- void 没有任何类型 函数没有返回值 可以定义为 void

---

# interface 可以给 Function / Array / Class 做声明吗？

```ts
// 函数声明
interface Say {
  (name: string): void
}

let say: Say = (name: string): void => {}

// Array
interface NumberArray {
  [index: number]: number
}

let list: NumberArray = [1, 2, 4, 5]

// Class 声明
interface Person {
  name: string

  sayHi(name: string): string
}
```

---

# Typescript 中的 this 和 JavaScript 中的 this 有什么差异？

TS：noImplicitThis:true 必须去声明 this 类型，才能在函数或者对象中使用 this

# Typescript 中使用 Union Types 时有哪些注意事项？

属性或者方法访问：只能访问共有属性或者方法

# Typescript 如何设计 Class 的声明？

```ts
class Greet {
  greeting: string

  constructor(message: string) {
    this.greeting = message
  }

  greet(): string {
    return `hello,${this.message}`
  }
}

let greeter = new Greet('world')
```

# Typescript 中如何联合枚举类型的 key

```ts
enum str {
  A,
  B,
  C,
  D,
}

type strUnion = keyof typeof str // 'A'|'B'|'C'|'D'
```

# type 和 interface 的区别

相同点：

- 都可以描述对象或者函数
- 都允许拓展

不同点：

- type 可以声明基本类型 联合类型 元组
- type 可以使用 typeof 获取实例类型进行赋值
- 多个相同的 interface 可以自动合并

类型兼容性

# 对象展开会有什么副作用

1. 展开对象后面的属性会覆盖前面的属性
2. 仅包含可枚举的属性，不可枚举属性丢失

# 全局声明和局部声明

不包含 import export 变成全局声明
包含 局部声明 不会影响到全局声明

# Typescript 项目引入并识别编译为 JavaScript 的 npm 库包？

1. 选择安装 ts 版本 npm install @types/xxx --save
2. 没有类型的 js 库 需要编写同名的 .d.ts

# Typescript 中如何设置模块导入的路径别名

tsconfig.json paths

```json
{
  "compilerOptions": {
    "paths": {
      "@/helper/*": ["src/helper/*"]
    }
  }
}
```

# declare，declare global 是什么

declare 定义全局变量 全局函数 全局命名空间 js modules class 等
delcare global 为全局对象 window 增加新的属性

```ts
declare global {
  interface Window {
    csrf: string
  }
}
```

# keypf 和 typedof 关键字的作用

keyof 索引类型查询操作符 获取某种类型的所有键，其返回类型是联合类型
typeof 获取一个变量或者对象的类型

---

#

```
对等依赖 peerDependencies(package.json)
npm i --legacy-peer-deps
```

```
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

```js
垃圾回收监听：FinalizationRegistry
引用计数
标记清除
memory
management
```

```js
ajax
XMLHttpRequest
XHR
Fetch
axios-- > XHR
umi - request-- > Fetch

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
      total: e.total,
    })
})
xhr.open(method, url)
xhr.send(data)

// fetch 响应进度监控
const resp = await fetch(url, {
  method,
  body: data,
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
      loaded: e.loaded,
      total: e.total,
    })
}
```

| 功能点                     |   XHR    |  Fetch   |
| -------------------------- | :------: | :------: |
| 基本的请求功能             |    √     |    √     |
| 基本的获取相应能力         |    √     |    √     |
| 监控请求进度               |    √     |    ×     |
| 监控相应进度               |    √     |    √     |
| Service Workder 中是否可用 |    ×     |    √     |
| 精细控制 cookie 的携带     |    ×     |    √     |
| 控制重定向                 |    ×     |    √     |
| 请求取消                   |    √     |    √     |
| 自定义 referrer            |    ×     |    √     |
| 流                         |    ×     |    √     |
| API 风格                   |  Event   | Promise  |
| 活跃度                     | 停止更新 | 不断更新 |

```
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

```
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
// 自动注入Less全局变量
module.exports = defineConfig({
  css: {
    loaderOptions: {
      less: {
        additionalData: '@import "~@/var.less"',
      },
    },
  },
})
// vite esbulid rollup
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '~@': './src',
    },
  },
  css: {
    preprocessOptions: {
      less: {
        additionalData: '@import "~@/var.less"',
      },
    },
  },
})

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
        code: `export default ${dataurl}`,
      }
    },
  }
}

export default definConfig({
  build: {
    // 统一vite中的图片转换逻辑
    assetsInlineLimit: 0,
    rollupOptions: {
      // 在vite中手动分包
      manualChunks (id) {
        if (id.includes('node_modules')) {
          return 'vendor'
        }
      },
      // vite打包结构控制
      output: {
        entryFileNames: 'js/[name]-[hash].js',
        chunkFileNames: 'js/[name]-[hash].js',
        assetFileNames (assetInfo) {
          if (assetInfo.name.endsWith('.css')) {
            return 'css/[name]-[hash].css'
          }
          const imgExts = ['.png', '.jpg', '.jpeg', '.webp', '.svg', '.gif', '.ico']
          if (imgExt.some((e) => assetInfo.name.endsWith(e))) {
            return 'imgs/[name]-[hash].[ext]'
          }
          return 'asset/[name]-[hash].[ext]'
        },
      },
    },
  },
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

```css
: 伪类
:: 伪元素
```

```txt
GET 和 POST 的区别？
协议层面：**语义区别**
应用层面：**GET 请求体为空**
浏览器层面：
```

```html
<!-- DNS预解析 -->
<link rel="dns-prefetch" href="xxxx" />
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
      vue: 'Vue',
    },
  }
}
```

```
let 和 var 的区别
1.全局污染，可以跨标签
2.块级作用域  var 全局作用域，函数作用域，let 块级作用域
3.TDZ 暂时性死区
4.重复声明  var 可以重新声明，let 不可以重新声明
```

```
拼音标注
<ruby></ruby>
import pinyin from 'pinyin';
判断是不是中文
```

```javascript
typeof null // object

let numbers = {
  0: 0
}

console.log(numbers.
"0"
)
; // error
console.log(numbers[0]); // 0


```

```shell
git clone <repository> --recursive 递归的方式克隆整个项目
git submodule add <repository> <path> 添加子模块
git submodule init 初始化子模块
git submodule update 更新子模块
git submodule foreach git pull 拉取所有子模块
```

```js
监控页面是否出现卡顿
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
  postman/apifox
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
  域名与 DNS
  SSL/TLS/HTTPS
  HTTP2
  WebSocket
```

```text
网络状态监控
  navigator.connection
  navigator.onLine
  window.addEventListener('online', () => {})
  window.addEventListener('offline', () => {})
  navigatot.connection.addEventListener('change', () => {})
```

```
微队列
  MutationObserver
  ob.observe(target, { childList: true })
```

```
资源提示符
  async: 作用于 script 元素
  defer: 作用于 script 元素
  prefetch
  preload
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


滚动元素到可视区域：scrollIntoView
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
Houdini

@property

CSS

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
  "
/>

原始尺寸=样式尺寸*缩放倍率 元素尺寸： - clientWidth：content + padding - offsetWidth：content + padding + scroll(滚动条) + border - scrollWidth：visible + invisible - 可见尺寸 getBoundingClientRect()
dom.style.width DOM树 getComputedStyle(dom).width CSSOM树 layout tree 布局树 几何信息
```

```js
监听复制事件
addEventListener
{
  passive: false
}
copy
paste
e.clipboardData.setData('text/palin', 'hello world')
Clipboard
API
navigator.clipboard.readText().then((text) => {})
```

```css
/* 调整文字方向： */
writing-mode、
margin-block-start、
margin-block-end、
text-combine-upright
margin-inline-start
```

```js
属性到底存在不存在
Object.keys()
对象自有可枚举的属性
hasOwnProperty()
对象自有属性
getOwnPropertyDescriptor()
defineProperty()
value
writable
enumerable
configurable
使用 in 遍历属性，原型上也会查找

对象属性
symbol
属性不能被json序列化
symbol
属性可以删除，configurable:true
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
          loader: 'raw-loader',
        },
      ],
    },
  },
})

// vite: ?raw
import data from './data.dataurl?raw'

// vite 寻找 views 文件夹中所有的 page.js
import.meta.glob('../views/**/page.js', {
  eager: true,
  import: 'default',
})
```

```
保持元素宽高比
css 属性: aspect-ratio
padding 相对于父元素宽度
```

```js
手动解析
DOM
树: removeTag
new DOMParser().parseFromString(str, 'text/html')
```

```html
show,showModel
<dialog open></dialog>
::backdrop
```

## 你能详细描述一下 qiankun 微前端框架的工作原理吗？

> qiankun 是一个基于 single-spa 的微前端实现框架。它的工作原理主要涉及到以下几个方面：

1. **应用加载**：qiankun 通过动态创建 script 标签的方式加载子应用的入口文件。加载完成后，会执行子应用暴露出的生命周期函数。
2. **生命周期管理**：qiankun 要求每个子应用都需要暴露出 bootstrap、mount 和 unmount 三个生命周期函数。bootstrap 函数在应用加载时被调用，mount 函数在应用启动时被调用，unmount
   函数在应用卸载时被调用。
3. **沙箱隔离**：qiankun 通过 Proxy 对象创建了一个 JavaScript 沙箱，用于隔离子应用的全局变量，防止子应用之间的全局变量污染。
4. **样式隔离**：qiankun 通过动态添加和移除样式标签的方式实现了样式隔离。当子应用启动时，会动态添加子应用的样式标签，当子应用卸载时，会移除子应用的样式标签。
5. **通信机制**：qiankun 提供了一个全局的通信机制，允许子应用之间进行通信。

## 在使用 qiankun 时，如果子应用是基于 jQuery 的多页应用，你会如何处理静态资源的加载问题？

> 在使用 qiankun 时，如果子应用是基于 jQuery 的多页应用，静态资源的加载问题可能会成为一个挑战。这是因为在微前端环境中，子应用的静态资源路径可能需要进行特殊处理才能正确加载。这里有几种可能的解决方案：

#### 方案一：使用公共路径

在子应用的静态资源路径前添加公共路径前缀。例如，如果子应用的静态资源存放在 `http://localhost:8080/static/`，那么可以在所有的静态资源路径前添加这个前缀。

#### 方案二：劫持标签插入函数

这个方案分为两步：

-

- 1.  对于 HTML 中已有的 img/audio/video 等标签，qiankun 支持重写 getTemplate 函数，可以将入口文件 index.html 中的静态资源路径替换掉。

-

- 1.  对于动态插入的 img/audio/video 等标签，劫持 appendChild、innerHTML、insertBefore 等事件，将资源的相对路径替换成绝对路径。

例如，我们可以传递一个 getTemplate 函数，将图片的相对路径转为绝对路径，它会在处理模板时使用：

```

start({
getTemplate(tpl,...rest) {
// 为了直接看到效果，所以写死了，实际中需要用正则匹配
return tpl.replace('<img src="./img/jQuery1.png">', '<img src="http://localhost:3333/img/jQuery1.png">');
}
});

```

对于动态插入的标签，劫持其插入 DOM 的函数，注入前缀。

```

beforeMount: app => {
if(app.name === 'purehtml'){
// jQuery 的 html 方法是一个挺复杂的函数，这里只是为了看效果，简写了
$.prototype.html = function(value){
const str = value.replace('<img src="/img/jQuery2.png">', '<img src="http://localhost:3333/img/jQuery2.png">')
this[0].innerHTML = str;
}
}
}

```

#### 方案三：给 jQuery 项目加上 webpack 打包

这个方案的可行性不高，都是陈年老项目了，没必要这样折腾。

## 在使用 `qiankun` 时，如果子应用动态插入了一些标签，你会如何处理？

> 在使用 `qiankun` 时，如果子应用动态插入了一些标签，我们可以通过劫持 DOM 的一些方法来处理。例如，我们可以劫持 `appendChild`、`innerHTML` 和 `insertBefore` 等方法，将资源的相对路径替换为绝对路径。

以下是一个例子，假设我们有一个子应用，它使用 jQuery 动态插入了一张图片：

```js
const render = ($) => {
  $('#app-container').html('<p>Hello, render with jQuery</p><img src="./img/my-image.png">')
  return Promise.resolve()
}
```

我们可以在主应用中劫持 jQuery 的 `html` 方法，将图片的相对路径替换为绝对路径：

```js
beforeMount: (app) => {
  if (app.name === 'my-app') {
    // jQuery 的 html 方法是一个复杂的函数，这里为了简化，我们只处理 img 标签
    $.prototype.html = function (value) {
      const str = value.replace('<img src="./img/my-image.png">', '<img src="http://localhost:8080/img/my-image.png">')
      this[0].innerHTML = str
    }
  }
}
```

在这个例子中，我们劫持了 jQuery 的 `html` 方法，将图片的相对路径 `./img/my-image.png` 替换为了绝对路径 `http://localhost:8080/img/my-image.png`。这样，无论子应用在哪里运行，图片都可以正确地加载。

## 在使用 `qiankun` 时，你如何处理老项目的资源加载问题？你能给出一些具体的解决方案吗？

> 在使用 `qiankun` 时，处理老项目的资源加载问题可以有多种方案，具体的选择取决于项目的具体情况。以下是一些可能的解决方案：

1. **使用 `qiankun` 的 `getTemplate` 函数重写静态资源路径**：对于 HTML 中已有的 `img/audio/video` 等标签，`qiankun` 支持重写 `getTemplate` 函数，可以将入口文件 `index.html`
   中的静态资源路径替换掉。例如：

```js
start({
  getTemplate(tpl, ...rest) {
    // 为了直接看到效果，所以写死了，实际中需要用正则匹配
    return tpl.replace('<img src="./img/my-image.png">', '<img src="http://localhost:8080/img/my-image.png">')
  },
})
```

1. **劫持标签插入函数**：对于动态插入的 `img/audio/video` 等标签，我们可以劫持 `appendChild` 、 `innerHTML` 、`insertBefore` 等事件，将资源的相对路径替换成绝对路径。例如，我们可以劫持
   jQuery 的 `html` 方法，将图片的相对路径替换为绝对路径：

```js
beforeMount: (app) => {
  if (app.name === 'my-app') {
    $.prototype.html = function (value) {
      const str = value.replace('<img src="./img/my-image.png">', '<img src="http://localhost:8080/img/my-image.png">')
      this[0].innerHTML = str
    }
  }
}
```

1. **给老项目加上 webpack 打包**：这个方案的可行性不高，都是陈年老项目了，没必要这样折腾。
2. **使用 iframe 嵌入老项目**：虽然 `qiankun` 支持 jQuery 老项目，但是似乎对多页应用没有很好的解决办法。每个页面都去修改，成本很大也很麻烦，但是使用 iframe 嵌入这些老项目就比较方便。

## 你能解释一下 `qiankun` 的 `start` 函数的作用和参数吗？如果只有一个子项目，你会如何启用预加载？

> `qiankun` 的 `start` 函数是用来启动微前端应用的。在注册完所有的子应用之后，我们需要调用 `start` 函数来启动微前端应用。

`start` 函数接收一个可选的配置对象作为参数，这个对象可以包含以下属性：

- `prefetch`：预加载模式，可选值有 `true`、`false`、`'all'`、`'popstate'`。默认值为 `true`，即在主应用 `start` 之后即刻开始预加载所有子应用的静态资源。如果设置为 `'all'`，则主应用 `start`
  之后会预加载所有子应用静态资源，无论子应用是否激活。如果设置为 `'popstate'`，则只有在路由切换的时候才会去预加载对应子应用的静态资源。
- `sandbox`：沙箱模式，可选值有 `true`、`false`、`{ strictStyleIsolation: true }`。默认值为 `true`，即为每个子应用创建一个新的沙箱环境。如果设置为 `false`，则子应用运行在当前环境下，没有任何的隔离。如果设置为
  `{ strictStyleIsolation: true }`，则会启用严格的样式隔离模式，即子应用的样式会被完全隔离，不会影响到其他子应用和主应用。
- `singular`：是否为单例模式，可选值有 `true`、`false`。默认值为 `true`，即一次只能有一个子应用处于激活状态。如果设置为 `false`，则可以同时激活多个子应用。
- `fetch`：自定义的 `fetch` 方法，用于加载子应用的静态资源。

如果只有一个子项目，要想启用预加载，可以这样使用 `start` 函数：

```js
start({ prefetch: 'all' })
```

这样，主应用 `start` 之后会预加载子应用的所有静态资源，无论子应用是否激活。

## 在使用 `qiankun` 时，你如何处理 `js` 沙箱不能解决的 `js` 污染问题？

> `qiankun` 的 `js` 沙箱机制主要是通过代理 `window` 对象来实现的，它可以有效地隔离子应用的全局变量，防止子应用之间的全局变量污染。然而，这种机制并不能解决所有的 `js` 污染问题。例如，如果我们使用
> `onclick` 或 `addEventListener` 给 `<body>` 添加了一个点击事件，`js` 沙箱并不能消除它的影响。

对于这种情况，我们需要依赖于良好的代码规范和开发者的自觉。在开发子应用时，我们需要避免直接操作全局对象，如 `window` 和 `document`。如果必须要操作，我们应该在子应用卸载时，清理掉这些全局事件和全局变量，以防止对其他子应用或主应用造成影响。

例如，如果我们在子应用中添加了一个全局的点击事件，我们可以在子应用的 `unmount` 生命周期函数中移除这个事件：

```js
export async function mount(props) {
  // 添加全局点击事件
  window.addEventListener('click', handleClick)
}

export async function unmount() {
  // 移除全局点击事件
  window.removeEventListener('click', handleClick)
}

function handleClick() {
  // 处理点击事件
}
```

这样，当子应用卸载时，全局的点击事件也会被移除，不会影响到其他的子应用。

## 你能解释一下 `qiankun` 如何实现 `keep-alive` 的需求吗？

> 在 `qiankun` 中，实现 `keep-alive` 的需求有一定的挑战性。这是因为 `qiankun` 的设计理念是在子应用卸载时，将环境还原到子应用加载前的状态，以防止子应用对全局环境造成污染。这种设计理念与
> `keep-alive` 的需求是相悖的，因为 `keep-alive` 需要保留子应用的状态，而不是在子应用卸载时将其状态清除。

然而，我们可以通过一些技巧来实现 `keep-alive` 的效果。一种可能的方法是在子应用的生命周期函数中保存和恢复子应用的状态。例如，我们可以在子应用的 `unmount` 函数中保存子应用的状态，然后在
`mount` 函数中恢复这个状态：

```

// 伪代码
let savedState;

export async function mount(props) {
// 恢复子应用的状态
if (savedState) {
restoreState(savedState);
}
}

export async function unmount() {
// 保存子应用的状态
savedState = saveState();
}

function saveState() {
// 保存子应用的状态
// 这个函数的实现取决于你的应用
}

function restoreState(state) {
// 恢复子应用的状态
// 这个函数的实现取决于你的应用
}

```

这种方法的缺点是需要手动保存和恢复子应用的状态，这可能会增加开发的复杂性。此外，这种方法也不能保留子应用的 DOM 状态，只能保留 JavaScript 的状态。

还有一种就是手动`*loadMicroApp*`+`display:none`，直接隐藏 Dom

另一种可能的方法是使用 `single-spa` 的 `Parcel` 功能。`Parcel` 是 `single-spa` 的一个功能，它允许你在一个应用中挂载另一个应用，并且可以控制这个应用的生命周期。通过 `Parcel`
，我们可以将子应用挂载到一个隐藏的 DOM 元素上，从而实现 `keep-alive` 的效果。然而，这种方法需要对 `qiankun` 的源码进行修改，因为 `qiankun` 目前并不支持 `Parcel`。

## 你能解释一下 `qiankun` 和 `iframe` 在微前端实现方式上的区别和优劣吗？在什么情况下，你会选择使用 `iframe` 而不是 `qiankun`？

`qiankun` 和 `iframe` 都是微前端的实现方式，但它们在实现原理和使用场景上有一些区别。

`qiankun` 是基于 `single-spa` 的微前端解决方案，它通过 JavaScript 的 `import` 功能动态加载子应用，然后在主应用的 DOM 中挂载子应用的 DOM。`qiankun` 提供了一种 JavaScript
沙箱机制，可以隔离子应用的全局变量，防止子应用之间的全局变量污染。此外，`qiankun` 还提供了一种样式隔离机制，可以防止子应用的 CSS 影响其他应用。这些特性使得 `qiankun`在处理复杂的微前端场景时具有很高的灵活性。

`iframe` 是一种较为传统的前端技术，它可以在一个独立的窗口中加载一个 HTML 页面。`iframe` 本身就是一种天然的沙箱，它可以完全隔离子应用的 JavaScript 和 CSS，防止子应用之间的相互影响。然而，
`iframe` 的这种隔离性也是它的缺点，因为它使得主应用和子应用之间的通信变得困难。此外，`iframe` 还有一些其他的问题，比如性能问题、SEO 问题等。

在选择 `qiankun` 和 `iframe` 时，需要根据具体的使用场景来决定。如果你的子应用是基于现代前端框架（如 React、Vue、Angular 等）开发的单页应用，那么 `qiankun`
可能是一个更好的选择，因为它可以提供更好的用户体验和更高的开发效率。如果你的子应用是基于 jQuery 或者其他传统技术开发的多页应用，或者你需要在子应用中加载一些第三方的页面，那么 `iframe`
可能是一个更好的选择，因为它可以提供更强的隔离性。

## 在使用 `qiankun` 时，你如何处理多个子项目的调试问题？

在使用`qiankun`处理多个子项目的调试问题时，通常的方式是将每个子项目作为一个独立的应用进行开发和调试。每个子项目都可以在本地启动，并通过修改主应用的配置，让主应用去加载本地正在运行的子应用，这样就可以对子应用进行调试了。这种方式的好处是，子应用与主应用解耦，可以独立进行开发和调试，不会相互影响。

对于如何同时启动多个子应用，你可以使用`npm-run-all`这个工具。`npm-run-all`是一个 CLI 工具，可以并行或者串行执行多个 npm 脚本。这个工具对于同时启动多个子应用非常有用。使用方式如下：

1. 首先，你需要在你的项目中安装`npm-run-all`，可以通过下面的命令进行安装：

```

npm install --save-dev npm-run-all

```

1. 然后，在你的`package.json`文件中定义你需要并行运行的脚本。比如，你有两个子应用，分别为`app1`和`app2`，你可以定义如下的脚本：

```

"scripts": {
"start:app1": "npm start --prefix ./app1",
"start:app2": "npm start --prefix ./app2",
"start:all": "npm-run-all start:app1 start:app2"
}

```

在这个例子中，`start:app1`和`start:app2`脚本分别用于启动`app1`和`app2`应用，`start:all`脚本则用于同时启动这两个应用。

1. 最后，通过执行`npm run start:all`命令，就可以同时启动`app1`和`app2`这两个应用了。

`npm-run-all`不仅可以并行运行多个脚本，还可以串行运行多个脚本。在某些情况下，你可能需要按照一定的顺序启动你的应用，这时你可以使用`npm-run-all`的`-s`选项来串行执行脚本，例如：
`npm-run-all -s script1 script2`，这将会先执行`script1`，然后再执行`script2`。

## qiankun 是如何实现 CSS 隔离的，该方案有什么缺点，还有其它方案么

`qiankun`主要通过使用`Shadow DOM`来实现 CSS 隔离。

1. `Shadow DOM`：`Shadow DOM`是一种浏览器内置的 Web 标准技术，它可以创建一个封闭的 DOM 结构，这个 DOM 结构对外部是隔离的，包括其 CSS 样式。`qiankun`在挂载子应用时，会将子应用的 HTML
   元素挂载到`Shadow DOM`上，从而实现 CSS 的隔离。

```

// qiankun 使用 Shadow DOM 挂载子应用
const container = document.getElementById('container');
const shadowRoot = container.attachShadow({mode: 'open'});
shadowRoot.innerHTML = '<div id="subapp-container"></div>';

```

对于`qiankun`的隔离方案，一个潜在的缺点是它需要浏览器支持`Shadow DOM`，这在一些旧的浏览器或者不兼容`Shadow DOM`的浏览器中可能会出现问题。

另一种可能的方案是使用 CSS 模块（CSS Modules）。CSS 模块是一种将 CSS 类名局部化的方式，可以避免全局样式冲突。在使用 CSS 模块时，每个模块的类名都会被转换成一个唯一的名字，从而实现样式的隔离。

例如，假设你有一个名为`Button`的 CSS 模块：

```

/_ Button.module.css _/
.button {
background-color: blue;
}

```

在你的 JavaScript 文件中，你可以这样引入并使用这个模块：

```

import styles from './Button.module.css';

function Button() {
return <button className={styles.button}>Click me</button>;
}

```

在这个例子中，`button`类名会被转换成一个唯一的名字，如`Button_button__xxx`，这样就可以避免全局样式冲突了。

3.BEM 命名规范隔离

## qiankun 中如何实现父子项目间的通信？如果让你实现一套通信机制，你该如何实现？

- `Actions` 通信：`qiankun` 官方提供的通信方式，适合业务划分清晰，较简单的微前端应用。这种通信方式主要通过 `setGlobalState` 设置 `globalState`，并通过 `onGlobalStateChange` 和
  `offGlobalStateChange` 来注册和取消 `观察者` 函数，从而实现通信。
- 自己实现一套通信机制（可以思考一下如何追踪 State 状态，类似 Redux 模式）

1. **全局变量**：在全局（window）对象上定义共享的属性或方法。这种方式简单明了，但有可能导致全局污染，需要注意变量命名以避免冲突。

2. **自定义事件**：使用原生的 CustomEvent 或类似的第三方库来派发和监听自定义事件。这种方式避免了全局污染，更加符合模块化的原则，但可能需要更复杂的事件管理。

3. - 2.1. **定义一个全局的通信对象**，例如 window.globalEvent，这个对象提供两个方法，emit 和 on。
   - 2.2. **emit 方法**用于派发事件，接收事件名称和可选的事件数据作为参数。
   - 2.3. **on 方法**用于监听事件，接收事件名称和回调函数作为参数。当相应的事件被派发时，回调函数将被执行。

```

window.globalEvent = {
events: {},
emit(event, data) {
if (!this.events[event]) {
return;
}
this.events[event].forEach(callback => callback(data));
},
on(event, callback) {
if (!this.events[event]) {
this.events[event] = [];
}
this.events[event].push(callback);
},
};

```

### 1.在主项目中使用 qiankun 注册子项目时，如何解决子项目路由的 hash 与 history 模式之争？

### 如果主项目使用 `history` 模式，并且子项目可以使用 `history` 或 `hash` 模式，这是 `qiankun` 推荐的一种形式。在这种情况下，子项目可以选择适合自己的路由模式，而且对于已有的子项目不需要做太多修改。但是子项目之间的跳转需要通过父项目的

`router` 对象或原生的 `history` 对象进行。

### 2. 如果主项目和所有子项目都采用 `hash` 模式，可以有两种做法：

- 使用 `path` 来区分子项目：这种方式不需要对子项目进行修改，但所有项目之间的跳转需要借助原生的 `history` 对象。
- 使用 `hash` 来区分子项目：这种方式可以通过自定义 `activeRule` 来实现，但需要对子项目进行一定的修改，将子项目的路由加上前缀。这样的话，项目之间的跳转可以直接使用各自的 `router` 对象或
  `<router-link>`。

### 3. 如果主项目采用 `hash` 模式，而子项目中有些采用 `history` 模式，这种情况下，子项目间的跳转只能借助原生的 `history` 对象，而不使用子项目自己的 `router` 对象。对于子项目，可以选择使用

`path` 或 `hash` 来区分不同的子项目。

## 在 qiankun 中，如果实现组件在不同项目间的共享，有哪些解决方案？

> 在项目间共享组件时，可以考虑以下几种方式：

1. **父子项目间的组件共享**：主项目加载时，将组件挂载到全局对象（如`window`）上，在子项目中直接注册使用该组件。
2. **子项目间的组件共享（弱依赖）**：通过主项目提供的全局变量，子项目挂载到全局对象上。子项目中的共享组件可以使用异步组件来实现，在加载组件前先检查全局对象中是否存在，存在则复用，否则加载组件。
3. **子项目间的组件共享（强依赖）**：在主项目中通过`loadMicroApp`手动加载提供组件的子项目，确保先加载该子项目。在加载时，将组件挂载到全局对象上，并将`loadMicroApp`
   函数传递给子项目。子项目在需要使用共享组件的地方，手动加载提供组件的子项目，等待加载完成后即可获取组件。

需要注意的是，在使用异步组件或手动加载子项目时，可能会遇到样式加载的问题，可以尝试解决该问题。另外，如果共享的组件依赖全局插件（如`store`和`i18n`），需要进行特殊处理以确保插件的正确初始化。

## 在 qiankun 中，应用之间如何复用依赖，除了 npm 包方案外？

1. 在使用`webpack`构建的子项目中，要实现复用公共依赖，需要配置`webpack`的`externals`，将公共依赖指定为外部依赖，不打包进子项目的代码中。

2. 子项目之间的依赖复用可以通过保证依赖的 URL 一致来实现。如果多个子项目都使用同一份 CDN 文件，加载时会先从缓存读取，避免重复加载。

3. 子项目复用主项目的依赖可以通过给子项目的`index.html`中的公共依赖的`script`和`link`标签添加自定义属性`ignore`来实现。在`qiankun`运行子项目时，`qiankun`会忽略这些带有`ignore`
   属性的依赖，子项目独立运行时仍然可以加载这些依赖。

4. 在使用`qiankun`微前端框架时，可能会出现子项目之间和主项目之间的全局变量冲突的问题。这是因为子项目不配置`externals`时，子项目的全局`Vue`变量不属于`window`对象，而`qiankun`
   在运行子项目时会先找子项目的`window`，再找父项目的`window`，导致全局变量冲突。

5. 解决全局变量冲突的方案有三种：

6. - 方案一是在注册子项目时，在`beforeLoad`钩子函数中处理全局变量，将子项目的全局`Vue`变量进行替换，以解决子项目独立运行时的全局变量冲突问题。
   - 方案二是通过主项目将依赖通过`props`传递给子项目，子项目在独立运行时使用传递过来的依赖，避免与主项目的全局变量冲突。
   - 方案三是修改主项目和子项目的依赖名称，使它们不会相互冲突，从而避免全局变量冲突的问题。

## 说说 webpack5 联邦模块在微前端的应用

> Webpack 5 的联邦模块（Federation Module）是一个功能强大的特性，可以在微前端应用中实现模块共享和动态加载，从而提供更好的代码复用和可扩展性

### 1. 模块共享

Webpack 5 的联邦模块允许不同的微前端应用之间共享模块，避免重复加载和代码冗余。通过联邦模块，我们可以将一些公共的模块抽离成一个独立的模块，并在各个微前端应用中进行引用。这样可以节省资源，并提高应用的加载速度。

```

// main-app webpack.config.js
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { ModuleFederationPlugin } = require('webpack').container;

module.exports = {
// ...其他配置

plugins: [
new HtmlWebpackPlugin(),
new ModuleFederationPlugin({
name: 'main_app',
remotes: {
shared_module: 'shared_module@http://localhost:8081/remoteEntry.js',
},
}),
],
};

// shared-module webpack.config.js
const { ModuleFederationPlugin } = require('webpack').container;

module.exports = {
// ...其他配置

plugins: [
new ModuleFederationPlugin({
name: 'shared_module',
filename: 'remoteEntry.js',
exposes: {
'./Button': './src/components/Button',
},
}),
],
};

```

在上述示例中，`main-app` 和 `shared-module` 分别是两个微前端应用的 webpack 配置文件。通过 `ModuleFederationPlugin` 插件，`shared-module` 将 `Button` 组件暴露给其他应用使用，而
`main-app` 则通过 `remotes` 配置引入了 `shared-module`。

### 2. 动态加载

Webpack 5 联邦模块还支持动态加载模块，这对于微前端应用的按需加载和性能优化非常有用。通过动态加载，可以在需要时动态地加载远程模块，而不是在应用初始化时一次性加载所有模块。

```

// main-app
const remoteModule = () => import('shared_module/Button');

// ...其他代码

// 在需要的时候动态加载模块
remoteModule().then((module) => {
// 使用加载的模块
const Button = module.default;
// ...
});

```

在上述示例中，`main-app` 使用 `import()` 函数动态加载 `shared_module` 中的 `Button` 组件。通过动态加载，可以在需要时异步地加载远程模块，并在加载完成后使用模块。

在微前端应用中可以实现模块共享和动态加载，提供了更好的代码复用和可扩展性。通过模块共享，可以避免重复加载和代码冗余，而动态加载则可以按需加载模块，提高应用的性能和用户体验。

## 说说 qiankun 的资源加载机制（import-html-entry）

> `qiankun import-html-entry` 是 qiankun 框架中用于加载子应用的 HTML 入口文件的工具函数。它提供了一种方便的方式来动态加载和解析子应用的 HTML 入口文件，并返回一个可以加载子应用的
> JavaScript 模块。

具体而言，`import-html-entry` 实现了以下功能：

-

- 1.  加载 HTML 入口文件：`import-html-entry` 会通过创建一个 `<link>` 标签来加载子应用的 HTML 入口文件。这样可以确保子应用的资源得到正确加载，并在加载完成后进行处理。

-

- 1.  解析 HTML 入口文件：一旦 HTML 入口文件加载完成，`import-html-entry` 将解析该文件的内容，提取出子应用的 JavaScript 和 CSS 资源的 URL。

-

- 1.  动态加载 JavaScript 和 CSS 资源：`import-html-entry` 使用动态创建 `<script>` 和 `<link>` 标签的方式，按照正确的顺序加载子应用的 JavaScript 和 CSS 资源。

-

- 1.  创建沙箱环境：在加载子应用的 JavaScript 资源时，`import-html-entry` 会创建一个沙箱环境（sandbox），用于隔离子应用的全局变量和运行环境，防止子应用之间的冲突和污染。

-

- 1.  返回子应用的入口模块：最后，`import-html-entry` 返回一个可以加载子应用的 JavaScript 模块。这个模块通常是一个包含子应用初始化代码的函数，可以在主应用中调用以加载和启动子应用。

通过使用 `qiankun import-html-entry`，开发者可以方便地将子应用的 HTML 入口文件作为模块加载，并获得一个可以加载和启动子应用的函数，简化了子应用的加载和集成过程。

## 说说现有的几种微前端框架，它们的优缺点？

以下是对各个微前端框架优缺点的总结：

1. **qiankun 方案**

   **优点**

   **缺点**

2. - 适配成本较高，包括工程化、生命周期、静态资源路径、路由等方面的适配；
   - css 沙箱的严格隔离可能引发问题，js 沙箱在某些场景下执行性能下降；
   - 无法同时激活多个子应用，不支持子应用保活；
   - 不支持 vite 等 esmodule 脚本运行。
   - 降低了应用改造的成本，通过 html entry 的方式引入子应用；
   - 提供了完备的沙箱方案，包括 js 沙箱和 css 沙箱；
   - 支持静态资源预加载能力。

3. **micro-app 方案**

   **优点**

   **缺点**

4. - 接入成本虽然降低，但路由依然存在依赖；
   - 多应用激活后无法保持各子应用的路由状态，刷新后全部丢失；
   - css 沙箱无法完全隔离，js 沙箱做全局变量查找缓存，性能有所优化；
   - 支持 vite 运行，但必须使用 plugin 改造子应用，且 js 代码没办法做沙箱隔离；
   - 对于不支持 webcomponent 的浏览器没有做降级处理。
   - 使用 webcomponent 加载子应用，更优雅；
   - 复用经过大量项目验证过的 qiankun 沙箱机制，提高了框架的可靠性；
   - 支持子应用保活；
   - 降低了子应用改造的成本，提供了静态资源预加载能力。

5. **EMP 方案**

   **优点**

   **缺点**

6. - 对 webpack 强依赖，对于老旧项目不友好；
   - 没有有效的 css 沙箱和 js 沙箱，需要靠用户自觉；
   - 子应用保活、多应用激活无法实现；
   - 主、子应用的路由可能发生冲突。
   - webpack 联邦编译可以保证所有子应用依赖解耦；
   - 支持应用间去中心化的调用、共享模块；
   - 支持模块远程 ts 支持。

7. **无界方案**

   **优点**

   **缺点**

8. - 在继承了 iframe 优点的同时，缺点依旧还是存在
   - 基于 webcomponent 容器和 iframe 沙箱，充分解决了适配成本、样式隔离、运行性能、页面白屏、子应用通信、子应用保活、多应用激活、vite 框架支持、应用共享等问题。

---

**小程序 已被代码依赖分析忽略，无法被其他模块引用。你可根据控制台中的【代码依赖分析】告警信息修改代码，或关闭【过滤无依赖文件】功能**

只需在“project.config.json”=>“setting”里面将"ignoreDevUnusedFiles"和"ignoreUploadUnusedFiles"都设置为 false，然后保存，重新编译即可。

```json
"ignoreDevUnusedFiles": false,
"ignoreUploadUnusedFiles": false,
```

---

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

```
文字描边
-webkit-text-stroke 居中描边
paint-order 配合 -webkit-text-stroke 使用，值为 stroke 时，外描边
paint-order:markers|stroke|fill
text-shadow：只适合小的外描边
```

前端打印 printjs

# 【阿里】如何实现页面文本不可复制

有 CSS 和 JS 两种方法，以下任选其一或结合使用

使用 CSS 如下：

```css
user-select: none;
```

或使用 JS 如下，监听 `selectstart` 事件，禁止选中。

当用户选中一片区域时，将触发 `selectstart` 事件，Selection API 将会选中一片区域。禁止选中区域即可实现页面文本不可复制。

```javascript
document.body.onselectstart = (e) => {
  e.preventDefault()
}

document.body.oncopy = (e) => {
  e.preventDefault()
}
```

# 【字节】简单介绍 requestIdleCallback 及使用场景

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
        },
      })
    }, 1)
  }
```

可以在 `ric` 中执行任务时需要注意以下几点：

1. 执行重计算而非紧急任务
2. 空闲回调执行时间应该小于 50ms，最好更少
3. 空闲回调中不要操作 DOM，因为它本来就是利用的重拍重绘后的间隙空闲时间，重新操作 DOM 又会造成重拍重绘

# 【头条】前端上传文件时如何读取文件内容

```
<input type="file" id="input" onchange="handleFiles(this.files)">
```

在浏览器中，通过 `input[type=file]` 来点击上传文件，此时监听 `onChange` 事件，可以获取到 `File` 对象，其中从中可以读取文件内容

而读取文件内容，需要转化 `File/Blob` 到 `Text`，一般使用以下两种方案

## **FileReader API**

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

## **Response API**

而是用 `Response API` 只需要一行内容

```javascript
const readBlob = (blob) => new Response(blob).text()
```

# 箭头函数

1. 不能使用 new 调用（不能当作构造函数）

2. 没有原型， 即没有 `prototype` 属性

3. 没有 arguments

4. 没有 this

   箭头函数中的 this 是在箭头函数定义时就决定的，而且不可修改的（call、apply、bind）

   箭头函数的 this 指向定义时，外层中第一个普通函数的 this

# computed、methods、watch 有什么区别？

1. computed 和 methods 的区别

   computed 是有缓存的，methods 没有缓存

2. computed 和 watch 的区别

   watch 是监听，数据或者路由发生了改变才可以响应（执行）

   computed 计算某一个属性的改变，如果某一个值改变了，计算属性会监测到进行返回

   watch 是当前监听到数据改变了，才会执行内部代码

# var let const

都是用来声明变量

区别一：

var 具有变量提升机制，let 和 const 没有变量提升的机制

区别二：

var 可以多次声明同一个变量，let 和 const 不可以多次声明同一个变量

区别三：

var、let 声明变量的，const 声明常量

var 和 let 声明的变量可以再次赋值，但是 const 不可以再次赋值

区别四：块级作用域

var 声明的变量没有自身作用域，let 和 const 声明的变量有自身的作用域

var 声明的变量被挂到 window

# computed 的值可以用 v-model 绑定吗？

不可以。准确地说，用 v-model 绑定了 computed 的值后，可以在绑定的元素中得到 computed 的结果，但不能实现双向绑定。

v-model 通常用来绑定 input、select 等标签，目的是为了实现双向绑定，当原始属性发生变化时，绑定标签的值也会发生变化；当标签的值发生变化时，原始属性同样变化。而 computed
是通过原始属性计算出的结果，是单向只读的，不能直接修改。

# mutations 和 actions 区别

action 提交的是 mutation，而不是直接变更状态

action 可以包含任意异步操作

# JS 中的计时器是否能精确计时？为什么？

1. 硬件

   原子钟

2. 系统

   操作系统的计时

3. 标准 w3c

   setTimeout `>=5` 的嵌套层级，最小 4ms

4. 事件循环

# ref 与 toRef 的区别是什么？

1. ref 本质是将原数据进行拷贝，然后通过 proxy 转为响应式数据；所以不管是修改原数据还是修改响应式数据，它们是不会受到影响的
2. toRef 本质是将一个对象的一个属性，通过 ref 转为响应式数据，是引用关系；且不管是修改源数据还是修改 toRef 后的数据，两者都会改变
3. ref 数据发生变化后，界面会马上更新；toRef 数据发生变化后，界面不会自动更新
4. ref 方法只接收一个参数，toRef 接收两个参数

# vue3 如何实现一个组件的异步加载？

1. Suspense
2. defineAsyncComponent

# 如何创建一个没有 prototype 的对象？

Object.create(null)

# 前端性能优化的手段？

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

# 如何将一个字符串转为二进制？

1. 将字符串转为字符数组
2. 遍历字符数组，使用 charCodeAt() 将每个字符元素转为 ASCII 码
3. 使用 toString(2) 将 ASCII 码元素转为二进制
4. 使用 join() 拼接数组元素，转为二进制字符串

# 严格模式下有哪些限制？

- 变量必须声明后再使用
- 不能使用 with 语句
- 禁止 this 指向 window
- 不能删除变量
- 禁止在函数内部遍历调用栈
- 禁止使用 arguments.callee

# 如何判断一个数据是否可以转成日期？

方法一：用 new Date() 方法，将数据转换成日期对象，转换失败的值是字符串 "Invalid Date"

方法二：用 new Date() 方法，将数据转换成日期对象，再用 getTime() 方法，获取该日期的时间戳，最后用 isNaN() 判断该时间戳是否为一个数组

# 如何关闭 ios 键盘首字母自动大写

`<input type="text" autocapoitalize="off" />`

# 如何检测一个数组中是否包含某一个元素？

1. indexOf 返回元素下标，没有返回 -1
2. find 查找并返回目标元素，没有 undefined
3. findIndex 查找并返回目标元素下标，没有返回 -1
4. some 查找数组中是否有符合条件的元素，返回 true/false
5. includes 返回数组是否包含指定的元素，返回 true/false

# 微信小程序面试题：组件与普通页面有什么不同？

1. 组件的 .js 文件执行的 Component() 函数，页面 .js 文件执行的是 Page() 函数
2. 组件在 .json 文件中必须声明 "component": true 属性
3. 组件的事件处理函数需要定义到 methods 节点中
4. 生命周期不同

# rgba 和 opacity 都可以设置透明度，它们有什么不同？

1. rgba 指的是颜色，rgb 分别是红、绿、蓝，a 指 Alpha 透明度。所以 rgba 只能作用于颜色；而 opacity 作用于整个元素
2. opacity 会被子元素继承；rgba 不会

# 匹配字符

```javascript
let reg = new RegExp(key, 'gi')
str.replace(reg, '替换值或回调函数')
```

# 键盘事件

键盘事件由用户击打键盘触发，主要有 keydown、keypress、keyup 三个事件：

keydown：按下键盘时触发

keyup：松开键盘时触发该事件

keypress：按下有值的键时触发。即按下 ctrl alt shift meta 这样的无值的键，这个事件不会触发

对于有值的键，按下时先触发 keydown 事件，再触发这个事件。

# 如何实现自适应布局

无限适配方案 + rem 单位

无限适配的核心原理：把屏幕划分为一定的份数（10 份），通过 JS 动态监测屏幕尺寸宽度，实时计算并设置 html 元素的基础字体大小

# CDN

CDN：内容分发网络，是一组分布在世界各地的服务器网络，可以为全球用户提供快速、安全的内容传送服务

原理：

1. CDN 服务器在全球各地分布
2. 用户访问网站的时候，用户浏览器会向最近的 CDN 发送请求
3. CDN 服务会把内容缓存在离用户最近的服务器上面，把内容返回给用户

作用：

1. 提高页面的加载速度
2. 减轻源服务器的负担
3. 提高网站的可用性

# 文字转语音

如何把文字转语音

web api：语音不统一/兼容性

第三方平台

优化：

断句

并发控制

缓存

客户端 localStorage（md5 base64）

服务器

# 重绘和回流有什么区别？

1. 重绘
   - 元素样式的可见属性发生改变（颜色、背景色），但布局不改变的时候
   - 重绘不影响页面布局，只会重绘受影响的元素
2. 回流
   - 布局的变化导致元素的尺寸、位置或隐藏状态的变化，需要重新计算整个布局
   - 回流会造成重绘，但重绘不一定会回流

css3 硬件加速

批量操作元素，然后再使用文档碎片进行操作

缓存样式属性

# SPA 的优缺点，以及在何种场景下更适合使用 SPA

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

# 从输入 URL 到页面展现这一过程中，浏览器都做了哪些工作

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

# 如何避免 JavaScript 中的全局变量污染？

1. 立即执行函数
2. 严格模式

# window.onload 和 DOMContentLoaded 的区别

都是用来标识 DOM 文档加载完成的事件

1. 加载时机：
   1. window.onload 页面所有 DOM 加载完成后触发
   2. DOMContentLoaded 在 DOM 树构建完成后触发
2. 事件是否能多次触发：
   1. window.onload 不行
   2. DOMContentLoaded 可以
3. 兼容性
   1. window.onload IE8 以下不支持
   2. DOMContentLoaded IE9 以上才支持

# 谈谈移动端布局的几种方式

1. 流式布局

   相对单位定义元素的宽高

2. 固定宽度布局

3. 响应式布局

   弹性布局+媒体查询

4. 栅格布局

5. flex 布局（弹性布局）

6. 瀑布流

# 响应式设计

网站在不同的设备和屏幕尺寸上都可以提供一致的用户体验

原理：

1. 弹性和网格布局
2. 弹性图片：图片会根据屏幕大小进行调整
3. 媒体查询
4. 流式布局
5. 适应图片

# 点击穿透

在进行快速滑动的时候，某个可点击元素的点击事件透过了当前元素传递到了下方元素

1. 阻止默认事件

   e.preventDefault()

2. 使用 touch 事件

3. 使用第三方库

   fastclick zepto

4. css

# rem 和 em 的区别是什么？

```
px em rem 区别
1.px：固定值绝对单位
2.em：相对单位：相对于它的父元素的字体大小
3.rem：相对单位：相对于根元素（html）字体大小
```

1. rem

   相对于根元素的字体大小来计算的

   根元素的 font-size：16px，另外一个元素 width:1rem

2. em

   em 相对于当前元素的父元素字体大小来计算

   如果父元素设置了字体大小，子元素使用 em 单位，它的大小会受到父元素字体大小的影响

# 清除浮动的方法有哪些？伪元素清除的原理是什么？

1. 额外标签法

   浮动元素之后添加一个空 div 或其他块级元素，并设置 clear:both

2. 使用 overflow 属性触发 BFC

   浮动元素的父容器上设置 overflow:hidden

3. 伪元素清除法

   利用 after 伪元素为浮动元素的父容器添加看不见的内容，然后设置 clear:both;display:block;content:''

4. 直接设置高度

# forEach

```javascript
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
```

```javascript
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

# 立即执行函数

```javascript
;(function test() {
  test = 'LBJhui'
  console.log(test)
})()
// 函数的名称是只读的，所以不能在函数内部修改函数的名称。因此函数内部 test = 'LBJhui' 这行代码其实是无效的
```

# 在前端开发中如何优化 DOM 操作以提高页面性能

1. 减少 DOM 查询
2. 批量处理 DOM 操作
3. 避免不必要的重排重绘
4. 使用现代 api
5. 异步编程和延迟加载
6. 使用原生方法替代字符串操作
7. 事件委托

# CORS 的工作原理是什么？

预检请求

服务器响应

实际请求和响应

浏览器检验

# JSONP 是什么？它是如何绕过同源策略的

利用浏览器对 script 标签的特殊处理来规避同源策略的限制

原理核心：

机制

- 客户端请求
- 服务端响应
- 客户端处理

绕过同源策略

场景限制：GET

# scoped 原理

1. 作用：让样式在本组件中生效，不影响其他组件
2. 原理：给结点新增自定义属性，然后 css 根据属性选择器添加样式

# 什么是 XSS 攻击？如何防止 XSS 攻击？

XSS：指攻击者通过在目标网站输入字段中注入恶意脚本代码，当其他用户浏览这个网站的时候，脚本会在他的浏览器中执行，获取用户的敏感信息。

防止措施：

1. 输入验证和过滤
2. 输出编码
3. 使用 HTTP 头部设置
4. 妥善管理 cookies
5. 建立安全的开发实践
6. 更新和软件升级

# Vue 路由模式

路由模式有两种：history、hash

区别：

1. 表现形态不同
2. 跳转请求，路径不存在时，history 会发送请求，hash 不会发送请求
3. 打包后前端自测要使用 hash，如果使用 history 会出现空白页

# 在处理跨域时，如果考虑安全性因素

1. 精确控制允许的源
2. 限制请求方法和头信息
3. 预检请求验证
4. 使用 https
5. 设置适当的 CSP 策略
6. 验证和过滤请求数据
7. 限制第三方 API 使用
8. 实施速率限制
9. 日志和监控

# post 请求和 get 请求在跨域时有何不同？

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
     POST 请求都可能会产生不同的结果（例如，创建新的资源或更新现有资源）。

6. **浏览器限制**：

   - 某些浏览器可能会对 GET 请求的 URL 长度施加限制（尽管这个限制可能因浏览器和版本而异）。如果 URL 超过了这个限制，那么 GET 请求可能会失败。相比之下，POST 请求没有这样的限制，因为数据可以包含在请求体中而不是
     URL 中。因此，在需要发送大量数据或复杂查询参数的跨域场景中，POST 请求可能更合适。

# 解释一下 CSP 与跨域的关系

CSP（Content Security Policy）与跨域（Cross-Origin）在 Web 安全领域中是两个重要的概念，但它们各自关注的安全问题和实现机制有所不同。以下是关于 CSP 与跨域关系的详细解释：

### CSP（内容安全策略）

1. **定义**：CSP 是为了缓解跨站脚本（XSS）等安全威胁而引入的一种安全机制。它允许网站开发者创建并强制应用一些规则，以管理网站允许加载的内容。
2. **工作原理**：CSP 以白名单的机制对网站加载或执行的资源起作用。在网页中，这样的策略通过 HTTP 头信息或者 meta 元素定义。例如，通过设置`Content-Security-Policy` HTTP
   头，可以限制哪些外部资源（如脚本、样式表、图片等）可以被加载和执行。
3. **限制与影响**：CSP 虽然提供了强大的安全保护，但也可能造成一些限制，如 Eval 及相关函数被禁用、内嵌的 JavaScript 代码将不会执行、只能通过白名单来加载远程脚本等。这些限制可能会增加开发者的工作量，需要花费更多时间来分离内嵌的
   JavaScript 代码和调整应用逻辑。

### 跨域（Cross-Origin）

1. **定义**：跨域是指一个域下的文档或脚本试图去请求另一个域下的资源。由于浏览器的同源策略（Same-Origin Policy），跨域请求通常会被限制或阻止，以防止恶意脚本攻击和数据泄露。
2. **同源策略**：同源策略要求协议、域名和端口三者都相同才被认为是同源的。如果其中任何一个不同，则被视为跨域。
3. **解决方案**：为了实现跨域请求，开发者可以采用一些技术手段，如 CORS（跨来源资源共享）、Proxy（代理）和 JSONP 等。这些技术允许服务器设置特定的响应头（如`Access-Control-Allow-Origin`
   ），以允许来自不同源的请求。

### CSP 与跨域的关系

- **独立性**：CSP 和跨域是两个独立的概念，各自关注不同的安全问题。CSP 关注的是如何限制和管理网站加载的内容，而跨域关注的是如何允许或限制来自不同源的请求。
- **相互影响**：在某些情况下，CSP 的设置可能会影响跨域请求的实现。例如，在使用 CSP 限制脚本加载时，如果跨域请求需要加载并执行远程脚本，可能会受到 CSP 策略的限制。同样，跨域请求的实现也可能需要考虑
  CSP 策略的影响，以确保请求的资源符合 CSP 规则。

综上所述，CSP 和跨域在 Web 安全领域中各自扮演着重要的角色。开发者需要根据实际需求合理配置 CSP 策略和跨域请求的实现方式，以确保 Web 应用的安全性和可用性。
