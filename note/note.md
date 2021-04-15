### **文字超出省略、文字两端对齐**

需求中我们也经常遇到这样的需求，这里直接提供方案。

#### **超出省略**

```
.line-camp( @clamp:2 ) {    text-overflow: -o-ellipsis-lastline;    overflow: hidden;    text-overflow: ellipsis;    display: -webkit-box;    -webkit-line-clamp: @clamp;    -webkit-box-orient: vertical;}
```

**所遇到的问题：**

> `-webkit-box-orient:vertical` 在使用 webpack 打包的时候这段代码会被删除掉，原因是`optimize-css-assets-webpack-plugin` 这个插件的问题。

**解决方案：**

可以使用如下的写法：

```
.line-camp( @clamp:2 ) {    text-overflow: -o-ellipsis-lastline;    overflow: hidden;    text-overflow: ellipsis;    display: -webkit-box;    -webkit-line-clamp: @clamp;    /*! autoprefixer: off */    -webkit-box-orient: vertical;    /* autoprefixer: on */}
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/iccXN8sGPLT4hFEAdGrN8C406yW3fS6KxK2X5sySTIf0kepicBgPT5nDGLB0ufTibhSqmbuDibOMu9tmWqOYq57KRw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

#### **两端对齐**

```
// html<div>姓名</div><div>手机号码</div><div>账号</div><div>密码</div>
// cssdiv {    margin: 10px 0;    width: 100px;    border: 1px solid red;    text-align-last: justify;}
```

效果如下：![图片](https://mmbiz.qpic.cn/mmbiz_png/iccXN8sGPLT4hFEAdGrN8C406yW3fS6Kx11VibqObrV7cKiaXJzVwx08gemBYK0QX1sdCicQUpNbQ5G6THUcWWPOfQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

元素的 margin 的 top、bottom 及 padding 的 top、bottom 使用百分比作为单位时，其是相对父元素的宽度 width 的而不是我们想象的高度 height；

当父容器里有绝对定位的子元素时，子元素设置 width:100%实际上指的是相对于父容器的 padding+content 的宽度。当子元素是非绝对定位的元素时 width:100%才是指子元素的 content ，其等于父元素的 content 宽度。

#### `exportdefault` 和 `export` 的区别

1. 在一个文件或模块中 `export` 可以有多个，但 `exportdefault` 仅有一个
2. 通过 `export` 方式导出，在导入时要加 { }，而 `exportdefault` 则不需要

**ES5 和 ES6 实现继承的区别**

ES5 的继承，实质是先创造子类的实例对象 `this`，然后再将父类的方法添加到 `this` 上面（ `Parent.apply(this)`）。
ES6 的继承机制完全不同，实质是先创造父类的实例对象 `this` （所以必须先调用 `super()` 方法），然后再用子类的构造函数修改 `this`。

闭包就是指有权访问另一个函数作用域中的变量的函数。

padding 的百分比是相对于宽度的
