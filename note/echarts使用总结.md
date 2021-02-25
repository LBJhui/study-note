# Echarts 配置项之 title(标题)

## 1.标题居中

```javascript
// left的值为'left', 'center', 'right'
title: {
  left: 'center'
}
```

## 2.主副标题之间的间距

```javascript
title: {
  // 默认为10
  itemGap: 20
}
```

## 3.标题文本样式

```javascript
title: {
  text: '标题文本',
  textStyle: {
    // 文字颜色
    color: '#ccc',
    // 字体风格,'normal','italic','oblique'
    fontStyle: 'normal',
    // 字体粗细 'normal','bold','bolder','lighter',100 | 200 | 300 | 400...
    fontWeight: 'bold',
    // 字体系列
    fontFamily: 'sans-serif',
    // 字体大小
    fontSize: 18
  }
}
```

## 4.副标题

```javascript
title: {
  subtext: '副标题',
  // 副标题文本样式
  subtextStyle: {}
}
```

## 5.grid 组件离容器左侧的距离。

```javascript
title: {
  // left 的值可以是像 20 这样的具体像素值，可以是像 '20%' 这样相对于容器高宽的百分比，也可以是 'left', 'center', 'right'。
  // 如果 left 的值为'left', 'center', 'right'，组件会根据相应的位置自动对齐。
  left: 'center'
}
```

同理，top,right,bottom 用法同 left.

# Echarts 宽度自适应的 3 种方法

```javascript
window.onresize = function () {
  mychart.resize()
}
```

这段代码能解决 echarts 未自适应的问题，但是当页面中有多个图表时只有最后一个有效，要想同页面多个图表都有效可以使用 jquery 来实现:

```javascript
$(window).onresize = function () {
  mychart.resize()
}
```

最近，又遇到这个问题，但是我们项目中没有使用 jquery，研究半天发现 js 原生代码使用事件也可以实现多个图表自适应:

```javascript
window.addEventListener('resize', function () {
  mychart.resize()
})
```

# Echarts 饼图中间添加文字、title、graphic

![饼图中间添加](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/echarts/1.webp)

```javascript
// 指定图表的配置项和数据
var option = {
  tooltip: {
    trigger: 'item',
    formatter: '{a} <br/>{b}: {c} ({d}%)',
  },
  color: ['#27D9C8', '#D8D8D8'],
  title: {
    text: '80%',
    left: 'center',
    top: '50%',
    textStyle: {
      color: '#27D9C8',
      fontSize: 36,
      align: 'center',
    },
  },
  graphic: {
    type: 'text',
    left: 'center',
    top: '40%',
    style: {
      text: '运动达标率',
      textAlign: 'center',
      fill: '#333',
      fontSize: 20,
      fontWeight: 700,
    },
  },
  series: [
    {
      name: '运动情况',
      type: 'pie',
      radius: ['65%', '70%'],
      avoidLabelOverlap: false,
      label: {
        normal: {
          show: false,
          position: 'center',
        },
      },

      data: [
        { value: 80, name: '已完成' },
        { value: 20, name: '未完成' },
      ],
    },
  ],
}
```
