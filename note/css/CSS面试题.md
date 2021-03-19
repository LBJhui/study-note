# CSS 面试题

## link 标签和@import 的区别？

相同点：他们两者都可以引入外部样式

不同点：

1. 从属关系区别

   @import 是 CSS 提供语法规则，他的作用只有一个引入外部样式

   link 标签是 HTML 中标签不仅仅可以加载样式，还可以定义一些属性

2. 加载顺序区别

   加载页面的是时候，link 标签引入到的样式也同时加载了

   @import 引入的 CSS 样式，是在页面加载完毕以后样式才被加载

3. 兼容性区别

   @import 是 CSS2.1 才有的语法，兼容 IE5+才可以识别

   link 属于 HTML 中标签，没有兼容的问题

4. DOM 操作区别

   link 它是一个标签，完全可以通过 DOM 操作这个标签，引入样式

   @import 是 CSS 样式层的东西，没有办法进行 DOM 操作

## png、jpg、gif 这些图片格式解释一下，分别什么时候用？有没有了解过 webp？

- png：是便携式网络图片（Portable Network Graphics）是一种无损数据压缩位图文件格式，优点是：压缩比高，色彩好。大多数地方都可以用。
- jpg：是一种针对相片使用的一种失真压缩的方法，是一种破坏性的压缩，在色调及颜色平滑变化做的不错。在 www 上，被用来储存和传输照片的格式
- gif：是一种位图文件格式，以 8 位色重现真色彩的图像。可以实现动画效果。
- webp 格式是谷歌在 2010 年推出的图片格式，压缩率只有 jpg 的 2/3，大小比 png 小了 45%。缺点是压缩的时间更久了，兼容性不好，目前谷歌和 opera 支持。

## BFC

block formatting context 块级格式化上下文

形成独立的渲染区域

内部元素的渲染不会影响外界

形成 BFC 常见的条件

- 浮动元素 float 不是 none
- 绝对定位元素 position 是 absolute 或 fixed
- 块级元素 overflow 不是 visible
- flex 元素
- inline-block 元素

应用场景：清除浮动

## margin 负值

- margin-top：负值，元素向上拖拽
- margin-left：负值，元素向左拖拽
- margin-bottom：负值，元素本身不变，下边元素上移
- margin-right：负值，元素本身不变，右边元素左移

## 圣杯布局、双飞翼布局

圣杯布局（一般用于 PC 端网页布局）

目的：

1. 两侧内容宽度固定，中间内容宽度自适应
2. 三栏布局，中间一栏最先加载，、渲染出来

实现方法：

float + margin

## 水平居中

- 行内 inline 元素 `text-align: center; `
- 块级 block 元素 `margin: 0 auto;`
- absolute 定位元素 `left: 50%; margin-left: 负值`

## 多行文字垂直居中

父元素 `dispaly: table;`

子元素 `display: table-cell; vertical-align: center;`

## relative 和 absolute 定位

relative 定位 相对于 自身 定位

absolute 定位 相对于 最近的一层父级元素 定位

定位元素 relative absolute fixed 或 body

## flex 布局

**父级容器相关**

`flex-direction` 主轴方向 水平方向和垂直方向

`justify-content` 主轴上的对齐方式 开始对齐、结束对齐、居中对齐、两端对齐

`align-item` 交叉轴上的对齐方式 开始对齐、结束对齐、居中对齐

`flex-wrap` 是否换行

**子元素相关**

`align-self` 子元素在交叉轴上的对齐方式 开始对齐、结束对齐、居中对齐，可以覆盖 `align-item`属性

## line-height 继承时的坑

- 像素 ，继承
- 比例， 继承
- 百分比，先根据父元素的高度计算出结果再继承

