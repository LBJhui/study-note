### **1px 方案**

做过移动端需求的前端肯定是避免不了处理 `1px` 细线问题，这个问题的原因就是 UI 对页面美观度的要求越来越高（不要和我说这是 retina 屏的问题）。

据小生所知好像没有什么兼容性特别好的方案，这里我只是提供两种种相对较好的方案。

#### **使用伪类 + transform**

```css
.border_bottom {
  overflow: hidden;
  position: relative;
  border: none !important;
}
.border_bottom:after {
  content: '.';
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 1px;
  background-color: #d4d6d7;
  -webkit-transform-origin: 0 0;
  transform-origin: 0 0;
  -webkit-transform: scaleY(0.5);
  transform: scaleY(0.5);
}
```

当然这个方案在一些版本较低的机型也是会出现粗细不均、细线消失断裂的兼容性问题。不过现在在已经 2019 年了，版本较低的机型也淘汰的差不多了。

#### **使用 box-shadow 模拟**

```css
.border_bottom {
  box-shadow: inset 0px -1px 1px -1px #d4d6d7;
}
```

这个方案基本可以满足所有场景，不过有个缺点也就是颜色会变浅。
