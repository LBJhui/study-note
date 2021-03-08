### padding

```html
<div>
  <span>LBJhui</span>
</div>
```

```css
div {
  width: 200px;
  padding-top: 50px;
  padding-bottom: 50px;
}
span {
  font-size: 50px;
}
```

优点：简单，只需设置上下内边距

缺点：父元素不能设置固定高度

### line-height

优点：可设置父元素固定高度

缺点：不太适合多行文字

### display：flex；

### display：table-cell；

### display：grid；

### transform

```html
<div>
  <p>LBJhui</span>
</div>
```

```css
div {
  position: relative;
}
span {
  height: 50px;
  width: 50px;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}
```

优点：容易上手

缺点：脱离文档流

### vertical-align： middle；

```html
<div class="main">
  <div class="search">
    <form>
      <input type="text" />
      <div class="button">
        <i></i>
      </div>
    </form>
  </div>
</div>
```

```css
div.search{
  display: inline-block;
  vertical-align: middle;
}

div.main::after {
  content: "",
  display: inline-block;
 	backkground-color: gold;
  height: 100%;
  width: 0;
  vertical-align: middle;
}
```

### calc 动态计算

```css
.div0 {
  width: 200px;
  height: 150px;
  border: 1px solid #000;
}
.redbox {
  position: relative;
  width: 30px;
  height: 30px;
  background: #c00;
  float: left;
  top: calc(50% - 15px);
  margin-left: calc(50% - 45px);
}
.greenbox {
  position: relative;
  width: 30px;
  height: 80px;
  background: #0c0;
  float: left;
  top: calc(50% - 40px);
}
.bluebox {
  position: relative;
  width: 30px;
  height: 40px;
  background: #00f;
  float: left;
  top: calc(50% - 20px);
}
```
