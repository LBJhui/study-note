# CSS 选择器

## 选择器的语法

**1. 基本选择器语法**

|        选择器         |    类型    |                        功能描述                        |
| :-------------------: | :--------: | :----------------------------------------------------: |
|          `*`          | 通配选择器 |                选择文档中所有 HTML 元素                |
|          `E`          | 元素选择器 |                选择指定类型的 HTML 元素                |
|         `#id`         | ID 选择器  |         选择指定 ID 属性值为“id”的任意类型元素         |
|       `.class`        |  类选择器  | 选择指定 class 属性值为“class”的任意类型的任意多个元素 |
| `selector1,selectorN` | 群组选择器 |             将每一个选择器匹配的元素集合并             |

**2. 层次选择器语法**

| 选择器 |           类型           |                          功能描述                           |
| :----: | :----------------------: | :---------------------------------------------------------: |
| `E F`  | 后代选择器（包含选择器） |  选择匹配的 F 元素，且匹配的 F 元素被包含在匹配的 E 元素内  |
| `E>F`  |         子选择器         |  选择匹配的 F 元素，且匹配的 F 元素所匹配的 E 元素的子元素  |
| `E+F`  |      相邻兄弟选择器      | 选择匹配的 F 元素，且匹配的 F 元素紧位于匹配的 E 元素的后面 |
| `E~F`  |        通用选择器        | 选择匹配的 F 元素，且位于匹配的 E 元素后的所有匹配的 F 元素 |

**3. 动态伪类选择器语法**

|   选择器    |      类型      |                                   功能描述                                   |
| :---------: | :------------: | :--------------------------------------------------------------------------: |
|  `E:link`   | 链接伪类选择器 | 选择匹配的 E 元素，而且匹配元素被定义了超链接并未被访问过。常用于链接描点上  |
| `E:visited` | 链接伪类选择器 | 选择匹配的 E 元素，而且匹配元素被定义了超链接并已被访问过。常用于链接描点上  |
| `E:active`  | 用户行为选择器 |         选择匹配的 E 元素，且匹配元素被激活。常用于链接描点和按钮上          |
|  `E:hover`  | 用户行为选择器 | 选择匹配的 E 元素，且用户鼠标停留在元素 E 上。IE6 及以下浏览器仅支持 a:hover |
|  `E:focus`  | 用户行为选择器 |                   选择匹配的 E 元素，而且匹配元素获取焦点                    |

**4. 目标伪类选择器**

|   选择器   |                     功能描述                     |
| :--------: | :----------------------------------------------: |
| `E:target` | 选择匹配 E 的所有元素，且匹配元素被相关 URL 指向 |

**5. UI 元素状态伪类选择器语法**

|    选择器    |         类型         |                功能描述                |
| :----------: | :------------------: | :------------------------------------: |
| `E:checked`  |  选中状态伪类选择器  | 匹配选中的复选按钮或者单选按钮表单元素 |
| `E:enabled`  |  启用状态伪类选择器  |         匹配所有启用的表单元素         |
| `E:disabled` | 不可用状态伪类选择器 |         匹配所有禁用的表单元素         |

**6. 结构伪类选择器使用语法**

|         选择器          |                                                                                  功能描述                                                                                  |
| :---------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|     `E:first-child`     |                                                          作为父元素的第一个子元素的元素 E。与 E:nth-child(1)等同                                                           |
|     `E:last-child`      |                                                       作为父元素的最后一个子元素的元素 E。与 E:nth-last-child(1)等同                                                       |
|        `E:root`         |                              选择匹配元素 E 所在文档的根元素。在 HTML 文档中，根元素始终是 html，此时该选择器与 html 类型选择器匹配的内容相同                              |
|   `E F:nth-child(n)`    |                    选择父元素 E 的第 n 个子元素 F。其中 n 可以是整数（1，2，3）、关键字（even，odd）、可以是公式（2n+1）,而且 n 值起始值为 1，而不是 0.                    |
| `E F:nth-last-child(n)` | 选择父元素 E 的倒数第 n 个子元素 F。此选择器与 E:nth-child(n)选择器计算顺序刚好相反，但使用方法都是一样的，其中：nth-last-child(1)始终匹配最后一个元素，与 last-child 等同 |
|   `E:nth-of-type(n)`    |                                                                  选择父元素内具有指定类型的第 n 个 E 元素                                                                  |
| `E:nth-last-of-type(n)` |                                                                选择父元素内具有指定类型的倒数第 n 个 E 元素                                                                |
|    `E:first-of-type`    |                                                      选择父元素内具有指定类型的第一个 E 元素，与 E:nth-of-type(1)等同                                                      |
|    `E:last-of-type`     |                                                  选择父元素内具有指定类型的最后一个 E 元素，与 E:nth-last-of-type(1)等同                                                   |
|     `E:only-child`      |                                                             选择父元素只包含一个子元素，且该子元素匹配 E 元素                                                              |
|    `E:only-of-type`     |                                                          选择父元素只包含一个同类型子元素，且该子元素匹配 E 元素                                                           |
|        `E:empty`        |                                                            选择没有子元素的元素，而且该元素也不包含任何文本节点                                                            |

注：（1）. “ul>li:nth-child(3)”表达的并不是一定选择列表 ul 元素中的第 3 个子元素 li，仅有列表 ul 中第 3 个 li 元素前不存在其他的元素，命题才有意义，否则不会改变列表第 3 个 li 元素的样式。

（2）. :nth-child(n) 中参数只能是 n，不可以用其他字母代替。

（3）. :nth-child(odd) 选择的是奇数项，而使用:nth-last-child(odd) 选择的却是偶数项。

**7. 否定伪类选择器**

|   选择器   |           功能描述           |
| :--------: | :--------------------------: |
| `E:not(F)` | 匹配所有除元素 F 外的 E 元素 |

**8. 属性选择器语法**

|         选择器          |                           功能描述                           |
| :---------------------: | :----------------------------------------------------------: |
|      `[attribute]`      |                 用于选取带有指定属性的元素。                 |
|  `[attribute="value"]`  |               用于选取带有指定属性和值的元素。               |
| `[attribute~="value"]`  |             用于选取属性值中包含指定词汇的元素。             |
| `[attribute\|="value"]` | 用于选取带有以指定值开头的属性值的元素，该值必须是整个单词。 |
| `[attribute^="value"]`  |              匹配属性值以指定值开头的每个元素。              |
| `[attribute$="value"]`  |              匹配属性值以指定值结尾的每个元素。              |
| `[attribute*="value"]`  |              匹配属性值中包含指定值的每个元素。              |

注：例`<div class="links item"></div>`其中 a[class="links"]{……} 是找不到匹配元素，只有 a[class="links item"]{……}才匹配。

## 组合选择器

让我们从熟悉的选择器开始。组合选择器用于选择子元素和兄弟元素，并且相信大家已经使用了很长一段时间了吧。

- 一般子元素选择器（空格）。例如 `A B`。
- 直接子元素选择器。例如 `A>B` 。
- 相邻兄弟元素选择器。例如 `A+B`。
- 一般兄弟元素选择器。例如 `A~B`。

`A+B` ，他会选择紧跟 A 的 B 元素。但是一般兄弟元素选择器 `A~B` 呢？ 他将选择跟随 A 的所有兄弟 B 元素

以下是实例：

<p class="codepen" data-height="339" data-theme-id="default" data-default-tab="html,result" data-user="lbjhui" data-slug-hash="WNrpwdP" style="height: 339px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="组合选择器">
  <span>See the Pen <a href="https://codepen.io/lbjhui/pen/WNrpwdP">
  组合选择器</a> by LBJhui (<a href="https://codepen.io/lbjhui">@lbjhui</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

第二行 New York 行被选中是因为它紧跟在第一行之后 `table tbody tr:first-child + tr`，并且最后两个城市被高亮显示，因为他们被一般兄弟选择器 `table tbody tr:nth-child(4) ~ tr` 匹配，也就是第四行之后的所有行。

## 属性选择器

<p class="codepen" data-height="348" data-theme-id="default" data-default-tab="html,result" data-user="lbjhui" data-slug-hash="ExPWKEK" style="height: 348px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="属性选择器1">
  <span>See the Pen <a href="https://codepen.io/lbjhui/pen/ExPWKEK">
  属性选择器1</a> by LBJhui (<a href="https://codepen.io/lbjhui">@lbjhui</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

此示例演示如何选择所有复选框元素并将样式应用于其匹配标签，以使其变为粗体和蓝色。

然后，我们覆盖具有特定名称的 `chk2` 复选框的样式，并将其匹配的标签着色为红色。 请注意其他表单元素标签如何不受影响且未应用标签样式。

属性选择器不仅适用于表单元素，它们还可以定位任何元素的属性。 您可以匹配任何属性，而不仅仅是官方支持的属性。 此外，您可以检查属性是否存在，如下所示：

CSS 代码:

```
button[icon]
```

这匹配包含 `icon` 属性的 `<button>` 元素。它将匹配 `icon` 属性，无论 `icon` 属性是空值还是设置为特定值。

<p class="codepen" data-height="411" data-theme-id="default" data-default-tab="css,result" data-user="lbjhui" data-slug-hash="KKVWzBj" style="height: 411px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="属性选择器2">
  <span>See the Pen <a href="https://codepen.io/lbjhui/pen/KKVWzBj">
  属性选择器2</a> by LBJhui (<a href="https://codepen.io/lbjhui">@lbjhui</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

第一个链接没有 `target` 属性，因此不匹配。 接下来的两个链接是匹配的，因为它们的 `target` 属性具有空值或特定值的属性。 最后，最后一个链接设置为粉红色，因为它 `fluffy` 属性匹配。 它的值无关紧要，只需要与 `a[fluffy]` 选择器相匹配即可。

一个实际的例子可能是突出显示没有 alt 属性的图像。 此属性对于网页的可访问性来说是所必需的，因此对于 SEO 而言，确保所有图像元素都包含此属性非常重要。

我们可以使用以下规则来实现此目的：

CSS 代码:

```css
img:not([alt]) {
  border: 2px red dashed;
}
```

<p class="codepen" data-height="318" data-theme-id="default" data-default-tab="html,result" data-user="lbjhui" data-slug-hash="XWXMdPd" style="height: 318px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="属性选择器3">
  <span>See the Pen <a href="https://codepen.io/lbjhui/pen/XWXMdPd">
  属性选择器3</a> by LBJhui (<a href="https://codepen.io/lbjhui">@lbjhui</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

如果要匹配属性值的特定部分，则可以使用一些非常有用的选择器。

- `A[attr^=val]` – 属性值以 `val` 开头。
- `A[attr|=val]` – 属性值以 `val` 开头，或者以 `val-` 开头。
- `A[attr$=val]` – 属性值以 `val` 结尾。
- `A[attr*=val]` – 属性值中包含 `val` 。
- `A[attr~=val]` – 匹配用空格分隔的属性值列表，并且列表中包含 `val` 。

以下是每个例子：

<p class="codepen" data-height="435" data-theme-id="default" data-default-tab="html,result" data-user="lbjhui" data-slug-hash="mdVWPQL" style="height: 435px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="属性选择器4">
  <span>See the Pen <a href="https://codepen.io/lbjhui/pen/mdVWPQL">
  属性选择器4</a> by LBJhui (<a href="https://codepen.io/lbjhui">@lbjhui</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

前两个示例非常相似，不同之处是 `A[attr|=val]` 匹配后跟一个 `-` 字符串的值。 这对于匹配语言属性 `lang` 很有用。 例如 `<p lang ="en-us">`。

使用 `A[attr$="val"]` 可以轻松匹配文件扩展名，并且与 `::after` 相结合你可以轻松显示匹配文件。 注意使用 `attr()` 方法和 `content` 属性将它与静态字符串连接起来。

`A[attr*=val]` 显示了无论使用何种协议或子域，您都可以匹配特定域 `mysite.com`。

最后，`A[attr~=val]`，它非常适合匹配由空格分隔的值列表组成的属性中的值。 这只匹配整个单词而不是单词片段，而 `*=` 匹配单词片段，因此单词复数形式将不匹配。这个有点不好理解：例如某 div 元素的 `categories` 属性为 `<div categories="table wooden maple">`，其 `categories` 属性用空格分隔。那么 `div[categories~="table"]` 将匹配各元素，还有一个特别要注意的是， `<div categories="wooden maple table">` 也将被匹配。而 `<div categories="wooden maple tables">` 或者 `<div categories="wooden tableee maple">` 都不会被 `div[categories~="table"]` 匹配。

以上所有属性选择器示例都区分大小写。 但是我们有一个技巧。 如果我们在结束方括号之前插入一个 `i` ，我们可以启用区分大小写的匹配，这有点类似于 JavaScript 中的正则表达式匹配。

<p class="codepen" data-height="265" data-theme-id="default" data-default-tab="html,result" data-user="lbjhui" data-slug-hash="dyGvMwZ" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="属性选择器5">
  <span>See the Pen <a href="https://codepen.io/lbjhui/pen/dyGvMwZ">
  属性选择器5</a> by LBJhui (<a href="https://codepen.io/lbjhui">@lbjhui</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

除 Internet Explorer 和 Microsoft Edge 外，大多数主流浏览器都支持不区分大小写的匹配。

## 用户交互选择器

如果您处理过表单样式，那么您之前无疑会遇到这些类型的伪类选择器：

- :enabled
- :disabled
- :checked

例如，我们可以使用 `:checked` 来设置一个简单的待办事项列表。

<p class="codepen" data-height="330" data-theme-id="default" data-default-tab="html,result" data-user="lbjhui" data-slug-hash="ZEQeWwb" style="height: 330px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="用户交互选择器1">
  <span>See the Pen <a href="https://codepen.io/lbjhui/pen/ZEQeWwb">
  用户交互选择器1</a> by LBJhui (<a href="https://codepen.io/lbjhui">@lbjhui</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

这是非常标准的，但我们可以使用其他一些有趣的伪类。 `:default` 匹配一个或多个元素，这些元素是一组相关元素中的默认元素。这也可以与复位按钮类型组合使用。

<p class="codepen" data-height="363" data-theme-id="default" data-default-tab="html,result" data-user="lbjhui" data-slug-hash="zYrZqeK" style="height: 363px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="用户交互选择器2">
  <span>See the Pen <a href="https://codepen.io/lbjhui/pen/zYrZqeK">
  用户交互选择器2</a> by LBJhui (<a href="https://codepen.io/lbjhui">@lbjhui</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

我们可以使用伪类选择器来匹配输入值是否与 CSS 直接有效，以及在提交表单之前检查是否需要任何元素。

- :valid
- :invalid
- :required
- :optional (即不必须)

<p class="codepen" data-height="265" data-theme-id="default" data-default-tab="css,result" data-user="lbjhui" data-slug-hash="oNbZxmG" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="用户交互选择器3">
  <span>See the Pen <a href="https://codepen.io/lbjhui/pen/oNbZxmG">
  用户交互选择器3</a> by LBJhui (<a href="https://codepen.io/lbjhui">@lbjhui</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

如果您开始输入个人 email 输入字段，则必须检查有效性。 但是，工作 email 地址始终是必需的，并且需要有效检查有效性，因此不能留空。 还要注意我们可以链接伪类选择器（例如 `:required:invalid` ）来实现我们所需要的。

接下来，如果表单元素（支持 `min` 和 `max` 属性）在范围内，我们有两个可以匹配的伪类。

- :in-range
- :out-of-range

<p class="codepen" data-height="265" data-theme-id="default" data-default-tab="css,result" data-user="lbjhui" data-slug-hash="QWypNYX" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="用户交互选择器4">
  <span>See the Pen <a href="https://codepen.io/lbjhui/pen/QWypNYX">
  用户交互选择器4</a> by LBJhui (<a href="https://codepen.io/lbjhui">@lbjhui</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

同样，我们可以使用重置按钮类型来重置数字输入元素的默认值。

为了完善本节，我们来看看 `:read-only` ，`:read-write` 和 `:placeholder-shown` 的伪类。

<p class="codepen" data-height="265" data-theme-id="default" data-default-tab="css,result" data-user="lbjhui" data-slug-hash="MWKpyxw" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="用户交互选择器5">
  <span>See the Pen <a href="https://codepen.io/lbjhui/pen/MWKpyxw">
  用户交互选择器5</a> by LBJhui (<a href="https://codepen.io/lbjhui">@lbjhui</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

使用这些可以轻松匹配只读或可写（可编辑）的元素。 匹配元素不必是表单输入字段，如示例中所示。

最后，`:placeholder-shown` 将匹配尚未与之交互的元素，并仍显示默认占位符文本。 应谨慎使用此特定选择器，因为它尚未得到广泛支持。

## 结构选择器

结构选择器非常强大，基于它们在 DOM 中的位置匹配元素。 它们使您可以灵活地将元素与 CSS 完全匹配，否则需要 JavaScript 执行相同的操作。

这种类型的选择器与显示的选择器不同，因为其中一些选择器允许您传入参数来修改选择器的工作方式。

例如：`nth-child()` 接收一个值，该值将匹配特定子元素相对于其父容器的值。

因此，如果我们有一个项目列表，则以下选择器将匹配第三个项目：

CSS 代码:

```css
ul: nth-child(3);
```

但是，参数不是必须是简单的数字，它可以是一个简单的表达式，而使伪类更强大。

有效表达式有：

- `ul:nth-child(2)` – 匹配第 2 个子元素
- `ul:nth-child(4n)` – 匹配每 4th 个子元素（4,8,12，…）
- `ul:nth-child(2n + 1)` – 匹配每 2n + 1 个子元素偏移一个（1,3,5，…）
- `ul:nth-child(3n - 1)` – 匹配每 3n – 1 个子元素偏移负数 1（2,5,8，…）
- `ul:nth-child(odd)` – 匹配奇数元素（1,3,5，…）
- `ul:nth-child(even)` – 匹配偶数元素（2,4,6，…）

表达式变量 `n` 总是从零开始，因此确切地计算出哪些元素将匹配，`n` 从 `0` 开始，然后 `n` 为 `1` ，依此类推以编译元素列表。

这里还有 1 个简单而实用的小技巧，我们把`n` 当做负数来用，会发生什么呢？

- `ul li:nth-child(-n+3)` – 匹配第 1 到 第 3 个 li 子元素 （1,2,3）
- `ul li:nth-child(-2n+6)` – 匹配每 2th 个子元素，最多不超过第 8 个 li 子元素 （2,4,6,8）
- `ul li:nth-child(n + 10):nth-child(-n + 12)` – 匹配第 10 到 第 12 个 li 子元素 （10,11,12）

例如：

<p class="codepen" data-height="265" data-theme-id="default" data-default-tab="html,result" data-user="lbjhui" data-slug-hash="ExPWKMN" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="结构选择器1">
  <span>See the Pen <a href="https://codepen.io/lbjhui/pen/ExPWKMN">
  结构选择器1</a> by LBJhui (<a href="https://codepen.io/lbjhui">@lbjhui</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

您可以将简单表达式与以下结构选择器一起使用：

- `:nth-child()`
- `:nth-last-child()`
- `:nth-of-type()`
- `:nth-last-of-type()`

<p class="codepen" data-height="350" data-theme-id="default" data-default-tab="css,result" data-user="lbjhui" data-slug-hash="qBbrZvj" style="height: 350px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="结构选择器2">
  <span>See the Pen <a href="https://codepen.io/lbjhui/pen/qBbrZvj">
  结构选择器2</a> by LBJhui (<a href="https://codepen.io/lbjhui">@lbjhui</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

`:nth-last-child()` 和 `:nth-last-of-type()` 非常类似于 `:nth-child()` 和 `nth-of-type()` ，唯一区别是 `:nth-last-child()` 和 `:nth-last-of-type()` 是从最后一个元素开始匹配，而不是第一个元素开始匹配。

通过玩各种组合，您可以通过选择器获得相当多的创意。 例如，之前的示例包含选择器：

CSS 代码:

```css
ul:last-of-type li:nth-last-of-type(2)::after {
  content: '(2nd from end)';
  /* Other styles… */
}
```

这匹配第 2 个无序列表中最后一个列表项之后的伪元素。 如果你一直在努力解码一个复杂的选择器，那么最好从右到左阅读它，这样它就可以在逻辑上解构。

下一组选择器是专用的结构选择器，因为它们只匹配特定的子元素。 您无法将表达式传递给它们以修改其行为。

- `:first-child`
- `:last-child`
- `:only-child`
- `:only-of-type`
- `:first-of-type`
- `:last-of-type`

<p class="codepen" data-height="330" data-theme-id="default" data-default-tab="html,result" data-user="lbjhui" data-slug-hash="dyGvMrZ" style="height: 330px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="结构选择器3">
  <span>See the Pen <a href="https://codepen.io/lbjhui/pen/dyGvMrZ">
  结构选择器3</a> by LBJhui (<a href="https://codepen.io/lbjhui">@lbjhui</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

乍一看，这里有很多事情，你在使用这些类型的选择器时需要小心，因为你可能得到你没想到的结果。

例如，您可能想知道为什么在 `<section>` 标记内的等等……文本是蓝色的。 实际上所有部分内容都是蓝色的，因为它是主 div 容器的最后一个子节点。 其他部分元素通过其他选择器覆盖自己的颜色，使单个段落变为蓝色。

如果你觉得这些结构选择器还不够，或者你觉得记不住，使用起来很 麻烦， 那么你可以使用 [Family.scss](https://www.html.cn/archives/8400) – 轻松搞定这些 `:nth-child` 伪类 :nth-child

- `:empty`伪类表示**一个元素里面没有任何内容**。

这个选择器可以用很多种用途。比如，你在你的“sidebar”中有若干个盒子，但是不想让空盒子显示出来：

```css
#sidebar .box:empty {
  display: none;
}
```

注意，就算”box”div 里面只有一个空格，它也不会被 css 当作空标签的，这样就不能匹配该选择器了。

Internet Explorer (直到 8.0 版本)都不支持结构伪类。Firefox、Safari 和 Opera 在其最新版本的浏览器中指出这些选择器。这意味着，使用这些选择器对**网站的可用性和可访问性**是很有用的，或者如果网站的用户中的大部分是使用 IE 而且你不想在某些细节上无视他们，最好还是保持使用通用的 class 和简单的选择器来迎合这些选择器。否则你会被搞疯的！

## 否定、排除选择器

CSS 否定伪类选择器 `:not(X)`，是以一个简单的以选择器 `X` 为参数的功能性标记函数，将从匹配的元素集合中排除选择器 `X` 所匹配的元素。选择器 `X` 中不能包含另外一个 `:not` 选择器。

`:not()` 伪类的优先级即为它参数选择器的优先级。 可以利用这个伪类提高规则的优先级。例如， `#foo:not(#bar)` 和 `#foo` 会匹配相同的元素。 但是前者的优先级更高。但是 `:not()` 伪类不像其它伪类，它不会增加选择器的优先级。

`:not()` 伪类可以将一个或多个以逗号分隔的选择器作为其参数。但是以多个以逗号分隔的选择器作为参数是实验性的，尚未广泛支持。

`:not()` 伪类时我们得选择器组合更加灵活，我们来看一些简单应用：

<p class="codepen" data-height="362" data-theme-id="default" data-default-tab="html,result" data-user="lbjhui" data-slug-hash="vYLxGPR" style="height: 362px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="否定、排除选择器1">
  <span>See the Pen <a href="https://codepen.io/lbjhui/pen/vYLxGPR">
  否定、排除选择器1</a> by LBJhui (<a href="https://codepen.io/lbjhui">@lbjhui</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

上例中，`.content :not(.notice) em` 匹配了 `.content` 中所有的 `em` 元素，但是排除了 `.content .notice` 中 `em` 元素。

我们再来看看 `:not()` 和其他伪类选择器结合的例子：

<p class="codepen" data-height="351" data-theme-id="default" data-default-tab="css,result" data-user="lbjhui" data-slug-hash="OJMpNqa" style="height: 351px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="否定、排除选择器2">
  <span>See the Pen <a href="https://codepen.io/lbjhui/pen/OJMpNqa">
  否定、排除选择器2</a> by LBJhui (<a href="https://codepen.io/lbjhui">@lbjhui</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

在做一个有间隔线的列表时，我们通常会去除最后一个 `li` 下的横线。`li:not(:last-child)` 表示除了最后一个 `li` 元素之外的所有其他 `li` 元素。

## 内容选择器

这些属于用于匹配内容的一组专用选择器。我们可以立即使用的是：

- `::first-line`
- `::first-letter`
- `::selection` – 兼容方案：[CSS ::Selection 伪类选择器](https://www.html.cn/archives/5169)

---

### CSS ::Selection 伪类选择器

**::selection** 伪类选择器用于突出显示的页面用户选择的任何部分，包括可编辑文本字段中的文本。

此伪元素可应用于 color ， background-color ，background（background-color 部分） 和 text-shadow（注：到目前位置 IE 下该属性无效）属性。设置其他属性是没有任何效果的。

火狐下需要加-moz-属性前缀；

支持浏览器：Chrome，Firefox (Gecko)，Internet Explorer 9+，Opera，Safari

例如：

css 代码:

```css
/* draw any selected text yellow on red background */
::-moz-selection {
  color: gold;
  background: red;
}
::selection {
  color: gold;
  background: red;
}

/* draw selected text in a paragraph white on black */
p::-moz-selection {
  color: white;
  background: black;
}
p::selection {
  color: white;
  background: black;
}
```

一个完整的例子：

html 代码:

```html
<!DOCTYPE html>
<html lang="zh-cn">
  <head>
    <meta charset="utf-8" />
    <title>CSS ::Selection 伪类选择器-WEB前端开发</title>
    <meta name="author" content=",www.css88.com" />
    <style>
      p {
        text-shadow: 2px 2px 5px #333333;
      }
      p::-moz-selection {
        background: #000;
        color: #f00;
        text-shadow: 2px 2px 5px #ffff2e;
      }
      p::selection {
        background: #000;
        color: #f00;
        text-shadow: 2px 2px 5px #ffff2e;
      }
    </style>
  </head>
  <body>
    <h1>选中下面的文字，看看它的颜色</h1>
    <p>
      你选中这段文字后，看看它们的文本颜色和背景色，就能明白::selection的作用。
    </p>
  </body>
</html>
```

---

<p class="codepen" data-height="358" data-theme-id="default" data-default-tab="html,result" data-user="lbjhui" data-slug-hash="WNrpwmB" style="height: 358px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="内容选择器">
  <span>See the Pen <a href="https://codepen.io/lbjhui/pen/WNrpwmB">
  内容选择器</a> by LBJhui (<a href="https://codepen.io/lbjhui">@lbjhui</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

`::first-line` 和 `::first-letter` 仅在应用于块级元素时才起作用。另外要小心只在特定元素上使用 `::first-letter` ，否则每个段落都可能会应用。

目前还没有一些令人兴奋的内容选择器，但是当它们得到支持时，它们将开启各种可能性。

以下是需要注意的内容选择器列表：

- `::inactive-selection`?—?非活动窗口内的选定内容
- `::spelling-error`?—?检查可编辑元素的拼写和语法
- `::grammar-error`?—?匹配语法错误
- `::marker`?—?匹配列表项标记
- `::placeholder`?—?匹配表单元素的 placeholder 文本样式；兼容方案：[HTML5 input Placeholder（占位符）样式](https://www.html.cn/archives/5689)

---

### HTML5 input Placeholder（占位符）样式

placeholder 属性
placeholder（占位符）在实际的应用中非常常见，主要用作提示输入内容，现代浏览器都支持：

html 代码:

```html
<input placeholder="搜索" type="text" />
```

placeholder 样式

这里网上搜索了一下 placeholder 样式相关知识，分享一下：

css 代码:

```css
/* all */
::-webkit-input-placeholder {
  color: #f00;
}
::-moz-placeholder {
  color: #f00;
} /* firefox 19+ */
:-ms-input-placeholder {
  color: #f00;
} /* Internet Explorer 10+ */
:-moz-placeholder {
  color: #f00;
} /* firefox 14-18 */

/*  webkit 私有 */
#field2::-webkit-input-placeholder {
  color: #00f;
}
#field3::-webkit-input-placeholder {
  color: #090;
  background: lightgreen;
  text-transform: uppercase;
}
#field4::-webkit-input-placeholder {
  font-style: italic;
  text-decoration: overline;
  letter-spacing: 3px;
  color: #999;
}

/* mozilla 私有 */
#field2::-moz-placeholder {
  color: #00f;
}
#field3::-moz-placeholder {
  color: #090;
  background: lightgreen;
  text-transform: uppercase;
}
#field4::-moz-placeholder {
  font-style: italic;
  text-decoration: overline;
  letter-spacing: 3px;
  color: #999;
}
```

可以看出 placeholder 伪类样式还是相对丰富的。

---

## 其他选择器

我们接下来提到其他几个选择器不适合不适合归类到上面任何类别。 别担心我们差不多完成了！ 不幸的是，其中大部分是实验性的，所以你必须等待一段时间才能在生产中使用它们。

`:target` 选择器的目标是一个 `id` 与当前 `URL` 的一部分匹配的元素。 比如下面 `URL` 匹配该 URL 页面中 `id` 为 `part1` 的元素：

CSS 代码:

```CSS
https://css88.com#part1
```

我们可以将该元素应用以下样式：

CSS 代码:

```CSS
:target { border: 1px red solid; }
```

其实 `:target` 选择器目前可以用于一些特殊的用例，欢迎查看： [:target 伪类使用技巧](https://www.html.cn/archives/6256)

如果你有一个很大的选择器，那么 `:matches()` 可以帮助简化它。例如，如果您有以下选择器：

CSS 代码:

```CSS
nav p.content,
header p.content,
main p.content,
sidebar p.content,
footer p.content {
  margin: 15px;
  padding: 10px;
}
```

然后可以通过 `:matches()` 简化，相当于：

太好了！这将有助于使样式表更具可读性。

接下来我们还有一个 `:any-link` 选择器，这个选择器是`:link` 和 `:visited` 组合的简写。 所以下面这两个选择器实际上是相同的：

CSS 代码:

```CSS
:any-link {
  color: red;
}

:link, :visited {
  color: red;
}
```

- `:dir()`
- `:lang()`

这些都与您网站的语言有关。

`:dir()` 接受参数 `ltr` 或 `rtl` ，具体取决于您要匹配的文本的方向，目前仅 Firefox 支持。

所以：`:dir(rtl)` 会匹配所有具有 RTL 方向内容的元素。

HTML 文档中的每个元素都可以使用 `lang` 属性设置自己的单独语言。

html 代码:

```html
<div lang="en">The language of this element is set to English.</div>
<div lang="el">Η γλ?σσα αυτο? του στοιχε?ου ?χει οριστε? στα ελληνικ?.</div>
<div lang="is">Tungumál ?essa ?áttar er sett á íslensku.</div>
```

将相同的基本文本输入到三个 `<div>` 标记中，但将特定国家/地区添加到内容的末尾。此外，`lang` 属性中使用的国家代码代表相应的国家/地区。

CSS 代码:

```CSS
:lang(en) { color: red; }
:lang(el) { color: green; }
:lang(is) { color: blue; }
```

演示：

<p class="codepen" data-height="265" data-theme-id="default" data-default-tab="html,result" data-user="lbjhui" data-slug-hash="yLeMOry" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="其他选择器">
  <span>See the Pen <a href="https://codepen.io/lbjhui/pen/yLeMOry">
  其他选择器</a> by LBJhui (<a href="https://codepen.io/lbjhui">@lbjhui</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

好消息是所有主流浏览器都支持 `:lang()` 选择器。

## 伪元素

伪元素允许你操作**HTML 中不是真实存在的元素**，比如一个文本块的第一行或者第一个字母。

伪元素在 CSS 2.1 中就已经存在，但是 CSS 3 说明书表示他们应该使用双冒号“::”，以与伪类区分开来。在 CSS 2.1 中，他们也是使用单个冒号“:”的。浏览器会将能够接受两种格式，除非这些伪元素只存在于 CSS3 中。

**::first-line**

::first-line 伪元素将匹配 block、inline-block、table-caption、table-cell 等等级别元素的**第一行**

这对在你的文字块上添加**一些微妙的排版细节**相当有用，比如，将一片文章的第一行文字改成小写字母：

```css
h1 + p::first-line {
  font-variant: small-caps;
}
```

如果你专心的阅读了我们前面的内容，你将会了解到上面的语法意味着，紧紧的跟在 h1 标签之后(+)的段落会将其第一行文字显示为小写字母。

你也可以针对相关的 div 的第一行，而不用针对实际的段落标签(p):

```css
div.post p::first-line {
  font-variant: small-caps;
}
```

或者更进一步，定位某个特低的 div 的第一个段落的第一行：

```css
div.post > p:first-child::first-line {
  font-variant: small-caps;
}
```

这里，“>”符号表示你指定的是 post div 的直接子级元素，这样如果段落被包括在第二级 div 中，它就不会匹配这个选择器。

**::first-letter**

::first-letter 伪元素将会匹配一个文本块的**第一个字母**，除非在同一行里面包含一些其它元素，比如图片。

和::first-line 伪类一样，::first-letter 通常用于给文本元素**添加排版细节**，比如下沉字母或首字母。

这里是如何使用::first-letter 伪元素创建**首字下沉**的例子:

```css
p {
  font-size: 12px;
}

p::first-letter {
  font-size: 24px;
  float: left;
}
```

注意如果你在某些元素中同时使用::first-line 和::first-letter ，::first-letter 属性将覆盖从::first-line 中继承下来的某些属性。

如果你不知道 W3C 规则的话，这个元素有时会产生意想不到的结果：它事实上是使用最长的规则的选择器！所以如果你计划使用它的话最好仔细的阅读一下 (其它选择器也一样)。

**::before 和 ::after**

::before 和::after 伪元素用于在一个元素的前面或后面**插入内容**，纯 CSS 方法。

这些元素将继承它们将附加的元素的大部分属性。

假设你想在你的页面中的图标的描述前面添加文字“Graphic number x:”。你将无需写文字“Graphic number”，或者自己手动添加数字：

```css
.post {
  counter-reset: image;
}

p.description::before {
  content: 'Figure number ' counter(image) ': ';
  counter-increment: image;
}
```

那么这会产生什么？

首先，我们告诉 HTML 来**创建“image”计数器**。比如我们可以添加该属性到页面的 body。同样我们也可以给该计数器起任何一个名字，只要你想，只要我们常常使用同样的名字引用它：自己试试吧！

那么我们想在 class 为”description”的每一个段落之前添加这一块内容: “Figure number ” — 注意只有我们在引号里面写的内容才会被创建到页面中，所以我们也要添加一个空格！

然后，我们就有了 counter(image):这将用到我们之前在.post 选择器中定义的属性。它默认会从数字 1 开始。

下一个属性在那里表示计数器知道对于每一个 p.description，它需要将 image 计数器增加 1 (counter-increment: image)。

它并不像看起来的那么复杂，而且还会灰常的有用。

::before 和::after 伪元素常常只**使用 content 属性**，来添加一些短语或排版元素，但是这里我们展示了我们如果以一种更加强大的结合 counter-reset 和 counter-increment 属性的方式来使用它们。

**有趣的是**: ::first-line 和::first-letter 伪元素可以匹配使用::before 伪元素生成的内容，如果存在的话。

浏览器支持
如果使用单个冒号的话(比如, :first-letter, 而不是::first-letter)，这些伪元素被 IE8 支持(但是不被 IE7 或 6 支持)。但是左右其他的主流浏览器都支持这些选择器。

## CSS 选择器优先级

当两个规则都作用到了同一个 html 元素上时，如果定义的属性有冲突，那么应该用谁的值的，CSS 有一套优先级的定义

**不同级别**

1. 在属性后面使用`!important`会覆盖页面内任何位置定义的元素样式。
2. 作为 style 属性写在元素内的样式
3. id 选择器
4. 类选择器
5. 标签选择器
6. 通配符选择器
7. 浏览器自定义或继承

**总结排序：`！important` > 行内样式 > ID 选择器 > 类选择器 > 标签 > 通配符 > 继承 > 浏览器默认属性**

**同一级别**

同一级别中后写的会覆盖先写的样式

上上面的级别还是很容易看懂的，但是有时候有些规则是多个级别的组合

CSS 优先级：是由四个级别和各个级别的出现次数决定的。

四个级别分别为：行内选择符、ID 选择符、类别选择符、元素选择符。

**优先级的算法**

```
每个规则对应一个初始“四位数”：
0、0、0、0
若是 行内选择符，则加1、0、0、0
若是 ID选择符，则加0、1、0、0
若是 类选择符/伪类选择符，则分别加0、0、1、0
若是 元素选择符，则分别加0、0、0、1
```

算法：将每条规则中，选择符对应的数相加后得到的”四位数“，从左到右进行比较，大的优先级越高。

**需要注意的：**

1. `！important`的优先级是最高的，但出现冲突时则需比较“四位数”；
2. 优先级相同时，则采用就近原则，选择最后出现的样式；
3. 继承得来的属性，其优先级最低
