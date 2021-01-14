# CSS 盒模型详解

CSS 的盒模型是 CSS 的基础，同时也是难点，属于经典问题。

可以认为每个 html 标签都是一个方块，然后这个方块又包着几个小方块，如同盒子一层层的包裹着，这就是所谓的盒模型。

盒模型分为 IE 盒模型和 W3C 标准盒模型。

IE 盒模型和 W3C 标准盒模型的区别是什么？

**1. W3C 标准盒模型：**

属性 width,height 只包含内容 content，不包含 border 和 padding。

**2. IE 盒模型：**

属性 width,height 包含 border 和 padding，指的是 content+padding+border。

在 ie8+浏览器中使用哪个盒模型可以由`box-sizing`(CSS 新增的属性)控制，默认值为`content-box`，即标准盒模型；如果将`box-sizing`设为`border-box`则用的是 IE 盒模型。

如果在 ie6,7,8 中 DOCTYPE 缺失会触发 IE 模式。在当前 W3C 标准中盒模型是可以通过`box-sizing`自由的进行切换的。

content-box（标准盒模型）

width = 内容的宽度

height = 内容的高度

border-box（IE 盒模型）

width = border + padding + 内容的宽度

height = border + padding + 内容的高度

我们在编写页面代码时应尽量使用标准的 W3C 模型(需在页面中声明 DOCTYPE 类型)，这样可以避免多个浏览器对同一页面的不兼容。

因为若不声明 DOCTYPE 类型，IE 浏览器会将盒子模型解释为 IE 盒子模型，FireFox 等会将其解释为 W3C 盒子模型；若在页面中声明了 DOCTYPE 类型，所有的浏览器都会把盒模型解释为 W3C 盒模型。
