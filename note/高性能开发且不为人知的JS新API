# 经典设计模式：发布订阅

```javascript
let sub = (function () {
  // 自定义事件池
  let pond = {}
  
  // 向事件池中存放方法
  const on = function on(type, func) {
    !pond.hasOwnProperty(type) ? pond[type] = [] : null
    let arr = pond[type]
    let i = 0
    // 存储之前实现去重处理
    for(; i < arr.lenth; i++){
      if(arr[i] === func){
        return
      }
    }
    arr.push(func)
  }
  
  // 向事件池中存放方法
  const off = function on(type, func) {
    let arr = pond[type] || []
    let i = 0
    for(; i < arr.lenth; i++){
      if(arr[i] === func){
        // 移除这一项：为了不产生数组塌陷问题，我们不直接从原始数组中删除，只是把当前项赋值为null
        arr[i] = null
        return
      }
    }
  }
  
  // 通知事件池中的方法执行
  const fire = function on(type, ...params) {
    let arr = pond[type] || []
    let i = 0
    for(; i < arr.lenth; i++){
      if(arr[i] === null){
        arr.splice(i, 1)
       	i--
        continue
      }
      arr[i](...params)
    }
  }
  
  return {
    on,
    off,
    fire
  }
})()

const fn1 = x => console.log('fn1', x)
const fn2 = x => console.log('fn2', x)

sub.on('LBJhui', fn1)
sub.on('LBJhui', fn1)
sub.on('LBJhui', fn2)

setTimeoouut(() => {
  sub.fire('LBJhui', 100)
})
```

# 自定义DOM事件

JavaScript中的模拟事件触发：无需手动操作，也可以基于一些代码触发事件「不兼容IE6-8」

- createEvent 创建事件对象「DOM2中事件参数是“复数”，DOM3中是“单数”」
  - MouseEvent
  - KeyboardEvent 「DOM新增」
  - Event
  - ...
- initMouseEvent / initKeyboardEvent / initEvent 模式事件对象数据
  - type事件类型
  - bubbles 是否冒泡传播
  - cancelable 事件是否可以取消
- dispatchEvent 手动触发事件

```javascript
let box = document.querySelector('.box')

//DOM0 事件绑定
box.onclick = function (ev) {
  console.log('DOM0 CLICK', ev)
}

//DOM2 事件绑定：事件池
box.addEventListener('click', function (ev) {
  console.log('DOM2 CLICK', ev)
})	

setTimeout(() => {
  // box.onclick() // 缺少事件对象
  
  // 1.创建事件对象
  let evv = document.createEvent('MouseEvent')
  ev.initMouseEvent('click', true, true)
  
  // 2.自动触发事件
  box.dispatchEvent(ev)
})
```

自定义DOM事件

- document.createEvent('CustomEvent') 或者 new CustomEvent('event_name', {'detail': xxx })

```javascript
let box = document.querySelector('.box')

// 创建自定义事件
let ev = document.createEvent('CustomEvent')
ev.initCustomEvent('LBJhui', true, true, {
  clientX: 10,
  clientY: 20
})

box.addEventListener('LBJhui', ev => {
  console.log(ev)
})
```

# 定时器动画

- setInterval / clearInterval 
- setTimeout / clearTimeout

「弊端」

- 容易出现卡顿、抖动的现象「丢帧」
  - 定时器设定的等待执行时间是不可靠的
  - 不同设备的刷新频率不一样，我们设定的等待时间和刷新频率不一致

扩展：屏幕刷新频率(图像在屏幕上更新的速度，也即屏幕上的图像每秒钟出现的次数)

- 60赫兹(Hz):显示器以每秒60次的频率不断的更新屏幕上的图像
- 视觉停留效应：16.7ms

requestAnimationFrame / cancelAnimationFrame 「不兼容IE6-9」

- 由系统来决定回调函数的执行时机
- CPU节能：当页面被隐藏或最小化时，setTimeout仍然在处理中；requestAnimationFrame只有在页面处于激活状态下才会执行
- 函数节流：回调函数在屏幕每一次的刷新间隔中只被执行一次
- requestAnimationFrame会把每一帧中的所有DOM操作集中起来，在一次重绘或回流中就完成，在隐藏或不可见的元素中，将不会进行重绘或回流

requestIdleCallback:在浏览器的空闲时间段调用的函数，这样一些不重要的任务可以延后执行，防止页面卡顿

- requestIdleCallback([callback], [option -> timeout])
- 只有新版浏览器才支持