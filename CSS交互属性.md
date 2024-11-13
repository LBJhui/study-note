# CSS交互属性

## Scroll Snap

## Overscroll Behavior

**作用**

`overscroll-behavior: contain;` contain表示保留默认的边界行为，阻止父容器滚动

`overscroll-behavior: none;` none表示边界行为和父容器滚动，两者都阻止

**可解决问题**

**1. macOS 的滚动容器中默认会有一个“触底反弹”效果，也就是常说的“橡皮筋”效果**

```css
body{
    overscroll-behavior: none;
}
```

**2. 在macOS中，还有一个系统级别的导航手势**

在页面之间横扫，就是那个，烦人的在双指左滑右滑时候出现的箭头图标，容易误切换页面

```css
body{
    overscroll-behavior: none;
}
```

**3. 保留弹性滚动，只阻止手势导航，可以设置：**

```css
body{
　　overscroll-behavior: contain;
}
```

**4. 防止滚动穿透**

```css
.modal{
　　overscroll-behavior: contain;
}
```

## Scrollbar Gutter

这个属性允许开发者为滚动条预留空间，避免内容溢出时导致的布局变化。

通过 `scrollbar-gutter` 属性，可以设置 `auto`、`stable`、`always` 等值，确保滚动条出现时不会影响页面的视觉布局。

## Overflow Anchor

这个属性控制滚动锚定行为，防止动态内容加载时导致的滚动跳跃。

通过 `overflow-anchor` 属性，开发者可以设置 `auto` 或 `none`，以控制浏览器是否调整滚动位置。例如，`overflow-anchor: none;` 可以防止聊天应用中新消息加载时改变用户的滚动位置。

## Touch Action

这个属性控制触摸设备上的手势行为，决定浏览器是否处理默认手势（如缩放和滚动），或者将事件传递给 JavaScript 进行自定义处理。通过 `touch-action` 属性，开发者可以设置 `auto`、`none`、`pan-x`、`pan-y` 等值，以控制元素的触摸行为。例如，`touch-action: pan-y;` 可以确保垂直滚动元素时不会触发水平滚动。

## Scroll Timeline 和 View Timeline

这两个新属性允许开发者根据用户的滚动行为创建动态动画。`scroll-timeline` 将动画与页面或元素的滚动关联，而 `view-timeline` 则根据元素在视口中的位置创建动画。这些属性可以替代 JavaScript 库，提供更好的性能。

## View Transition API

这个 API 提供了一种创建平滑视图过渡动画的方法，适用于单页应用（SPA）和多页应用（MPA）。通过 `document.startViewTransition(callback)`，开发者可以在 DOM 状态变化时捕捉当前屏幕截图，并在更新后平滑过渡到新状态。