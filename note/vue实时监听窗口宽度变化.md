【自适应】向来是前端工程师需要解决的一大问题——即便作为当今非常火热的 vue 框架，也无法摆脱——虽然 elementui、iview 等开源 UI 组件库层出不穷，但官方库毕竟不可能满足全部需求，因此我们可以通过【监听窗口变化】达到想要的绝大部分自适应效果。

```bash
获取窗口宽度：document.body.clientWidth
监听窗口变化：window.onresize
```

同时回顾一下 JS 里这些方法：

```bash
网页可见区域宽：document.body.clientWidth
网页可见区域高：document.body.clientHeight
网页可见区域宽：document.body.offsetWidth (包括边线的宽)
网页可见区域高：document.body.offsetHeight (包括边线的宽)
```

我们将 document.body.clientWidth 赋值给 data 中自定义的变量：

```bash
data:{
    screenWidth: document.body.clientWidth
}
```

在页面 mounted 时，挂载 window.onresize 方法：

```bash
mounted () {
    const that = this
    window.onresize = () => {
        return (() => {
            window.screenWidth = document.body.clientWidth
            that.screenWidth = window.screenWidth
        })()
    }
}
```

监听 screenWidth 属性值的变化，打印并观察 screenWidth 发生变化的值：

```bash
watch:{
    screenWidth(val){
        // 为了避免频繁触发resize函数导致页面卡顿，使用定时器
        if(!this.timer){
            // 一旦监听到的screenWidth值改变，就将其重新赋给data里的screenWidth
            this.screenWidth = val
            this.timer = true
            let that = this
            setTimeout(function(){
                // 打印screenWidth变化的值
                console.log(that.screenWidth)
                that.timer = false
            },400)
        }
    }
}
```

上面的方案每隔 0.4 秒会获取一次屏幕的宽度，并将宽度值赋值给`data`中的`screenWide`，就可以直接通过`this.screenWide`获取了

好！既然可以监听到窗口 screenWidth 值的变化，就可以根据这个值设定不同的自适应方案了！
