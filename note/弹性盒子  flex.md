# 一、Flex 布局是什么？

Flex 是 Flexible Box 的缩写，翻译成中文就是“弹性盒子”，用来为盒装模型提供最大的灵活性。任何一个容器都可以指定为 Flex 布局。

```css
.box {
  display: -webkit-flex; /*在webkit内核的浏览器上使用要加前缀*/
  display: flex; //将对象作为弹性伸缩盒显示
}
```

当然，行内元素也可以使用 Flex 布局。

```css
.box {
  display: inline-flex; //将对象作为内联块级弹性伸缩盒显示
}
兼容性写法 .box {
  display: flex || inline-flex;
}
```

# 二、基本概念

采用 Flex 布局的元素，被称为 Flex 容器(flex container)，简称“容器”。其所有子元素自动成为容器成员，成为 Flex 项目(Flex item)，简称“项目”。

结构示意图

![结构示意图](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex1.jpg)

容器默认存在两根主轴：水平方向主轴(main axis)和垂直方向交叉轴(cross axis)，默认项目按主轴排列。

- main start/main end：主轴开始位置/结束位置；
- cross start/cross end：交叉轴开始位置/结束位置；
- main size/cross size：单个项目占据主轴/交叉轴的空间；

# 三、容器属性

> 设置在容器上的属性有 6 种。

- flex-direction
- flex-wrap
- flex-flow
- justify-content
- align-item
- align-content

## flex-direction 属性：决定主轴的方向（即项目的排列方向）

```css
.box {
  flex-direction: row | row-reverse | column | column-reverse;
}
```

- row（默认）：主轴水平方向，起点在左端；
- row-reverse：主轴水平方向，起点在右端；
- column：主轴垂直方向，起点在上边沿；
- column-reserve：主轴垂直方向，起点在下边沿。

主轴的 4 个方向

![主轴的4个方向](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex2.jpg)

## flex-wrap 属性：定义换行情况

> 默认情况下，项目都排列在一条轴线上，但有可能一条轴线排不下。

![一条轴线排不下](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex3.jpg)
一条轴线排不下

```css
.box {
  flex-wrap: nowrap | wrap | wrap-reverse;
}
```

- nowrap（默认）：不换行

![不换行nowrap](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex4.jpg)

- wrap：换行，第一行在上方；

![换行，第一行在上](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex5.jpg)

- wrap-reverse：换行，第一行在下方。

![换行，第一行在下](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex6.jpg)

## flex-flow 属性：flex-direction 和 flex-wrap 的简写，默认 row nowrap

```css
.box {
  flex-flow: <flex-direction> || <flex-wrap>;
}
```

## justify-content 属性：定义项目在主轴上的对齐方式。

> 对齐方式与轴的方向有关，本文中假设主轴从左到右。

```css
.box {
  justify-content: start | end | flex-start | flex-end | center | left | right |
    space-between | space-around | space-evenly | stretch | safe | unsafe |
    baseline | first baseline | last baseline;
}
```

- flex-start（默认值）：左对齐；

![左对齐](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex7.jpg)

- flex-end：右对齐；

![右对齐](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex8.jpg)

- center：居中；

![居中对齐](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex9.jpg)

- space-between：两端对齐，项目之间间隔相等；

![两端对齐](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex10.jpg)

- space-around：每个项目两侧的间隔相等，即项目之间的间隔比项目与边框的间隔大一倍。

![两侧间隔相等](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex11.jpg)

## align-items 属性：定义在交叉轴上的对齐方式

> 对齐方式与交叉轴的方向有关，假设交叉轴从下到上。

```css
.box {
  align-items: flex-start | flex-end | center | baseline | stretch;
}
```

- flex-start：起点对齐；

![起点对齐](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex12.jpg)

- flex-end：终点对齐；

![终点对齐](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex13.jpg)

- center：中点对齐；

![中点对齐](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex14.jpg)

- baseline：项目的第一行文字的基线对齐；

![基线对齐](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex15.jpg)

- stretch（默认值）：如果项目未设置高度或设为 auto，将占满整个容器的高度。

![stretch（默认值）](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex16.jpg)

## align-content 属性：定义多根轴线的对齐方式

> 如果项目只有一根轴线，该属性不起作用。
> 所以，容器必须设置 flex-wrap：···；

```css
.box {
  align-content: flex-start | flex-end | center | space-between | space-around |
    stretch;
}
```

- flex-start：与交叉轴的起点对齐；

![起点对齐](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex17.jpg)

- flex-end：与交叉轴的终点对齐；

![终点对齐](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex18.jpg)

- center：与交叉轴的中点对齐；

![中点对齐](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex19.jpg)

- space-between：与交叉轴的两端对齐，轴线之间的间隔平均分布；

![轴线之间等间距](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex20.jpg)

- space-around：每根轴线两侧的间隔相等，即轴线之间的间隔比轴线与边框的间隔大一倍；

![轴线两侧等间距](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex21.jpg)

- stretch（默认值）：轴线占满整个交叉轴。

![项目未设置高度时](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex22.jpg)

有意思的是，当你不给项目设置高度但是给容器设置 align-content 不为 stretch 时，同一轴线上的项目的高度将等于项目中高度最高的项目。

![项目未设置高度时](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex23.jpg)

# 四、项目的属性

> 设置在项目上的属性也有 6 个。

- order
- flex-grow
- flex-shrink
- flex-basis
- flex
- align-self

## order 属性：定义项目的排列顺序。

> 数值越小，排列越靠前，默认为 0，可以是负值。

```css
.item {
  order: <整数>;
}
```

![order](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex24.jpg)

## flex-grow 属性：定义项目的放大比例

> 默认值为 0，即如果空间有剩余，也不放大。
> 可以是小数，按比例占据剩余空间。

![默认情况](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex25.jpg)

```css
.item {
  flex-grow: <数字>;
}
```

若所有项目的 flex-grow 的数值都相同，则等分剩余空间

![等分剩余空间](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex26.jpg)

若果有一个项目 flex-grow 为 2，其余都为 1，则该项目占据剩余空间是其余的 2 倍

![不等分占据](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex27.jpg)

## flex-shrink 属性：定义项目的缩小比例

> 默认值都为 1，即如果空间不足将等比例缩小。
> 如果有一个项目的值为 0，其他项目为 1，当空间不足时，该项目不缩小。
> 负值对该属性无效，容器不应该设置 flex-wrap。

```css
.item {
  flex-shrink: <非负整数>;
}
```

如果一个项目设置 flex-shrink 为 0；而其他项目都为 1，则空间不足时，该项目不缩小。

![设置flex-shrink为0的项目不缩小](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex28.jpg)

如果所有项目都为 0，则当空间不足时，项目撑破容器而溢出。

![不缩小](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex29.jpg)

如果设置项目的 flex-shrink 不为 0 的非负数效果同设置为 1。

![不为0的非负数](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex30.jpg)

## flex-basis 属性：定义在分配多余空间之前，项目占据的主轴空间。

> 默认值为 auto，浏览器根据此属性检查主轴是否有多余空间。

```css
.item {
  flex-basis: <auto或者px>;
}
```

注意设置的 flex-basis 是分配多余空间之前项目占据的主轴空间，如果空间不足则默认情况下该项目也会缩小。

![设置flex-basis为350px，但空间充足](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex31.jpg)
设置 flex-basis 为 350px，但空间充足

![空间不足，项目缩小，小于设定值](https://cdn.jsdelivr.net/gh/LBJhui/image-host/images/flex/flex32.jpg)
空间不足，项目缩小，小于设定值

## flex 属性是 flex-grow，flex-shrink 和 flex-basis 的简写

> 默认值为 0 1 auto，第一个属性必须，后两个属性可选。

```css
.item {
  flex: none | [<flex-grow><flex-shrink><flex-basis>];
}
```

- 可以用 flex:auto; 代替 flex: 1 1 auto;；
- 可以用 flex: none;代替 flex: 0 0 auto；

## align-self 属性：允许单个项目与其他项目有不一样的对齐方式

> 默认值为 auto，表示继承父元素的 align-items 属性，并可以覆盖 align-items 属性。

```css
.item {
  align-self: auto | flex-start | flex-end | center | baseline | stretch;
}
```
