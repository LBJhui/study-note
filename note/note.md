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