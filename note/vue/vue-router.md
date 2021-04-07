## vue-router 是什么

这里的路由并不是指我们平时所说的硬件路由器，**这里的路由就是 SPA（单页应用）的路径管理器**。再通俗的说，vue-router 就是 WebApp 的链接路径管理系统。 vue-router 是 Vue.js 官方的路由插件，它和 vue.js 是深度集成的，适合用于构建单页面应用。vue 的单页面应用是基于路由和组件的，路由用于设定访问路径，并将路径和组件映射起来。传统的页面应用，是用一些超链接来实现页面切换和跳转的。在 vue-router 单页面应用中，则是路径之间的切换，也就是组件的切换。**路由模块的本质 就是建立起 url 和页面之间的映射关系**。

至于我们为啥不能用 a 标签，这是因为用 Vue 做的都是单页应用（**当你的项目准备打包时，运行 `npm run build`时，就会生成 dist 文件夹，这里面只有静态资源和一个 index.html 页面**），所以你写的标签是不起作用的，你必须使用 vue-router 来进行管理。

## vue-router 实现原理

SPA(single page application):单一页面应用程序，只有一个完整的页面；它在加载页面时，不会加载整个页面，而是只更新某个指定的容器中内容。**单页面应用(SPA)的核心之一是: 更新视图而不重新请求页面**;vue-router 在实现单页面前端路由时，提供了两种方式：Hash 模式和 History 模式；根据 mode 参数来决定采用哪一种方式。

### 1、Hash 模式：

vue-router 默认 hash 模式 —— 使用 URL 的 hash 来模拟一个完整的 URL，于是当 URL 改变时，页面不会重新加载。hash（#）是 URL 的锚点，代表的是网页中的一个位置，单单改变#后的部分，浏览器只会滚动到相应位置，不会重新加载网页，也就是说 hash 出现在 URL 中，但不会被包含在 http 请求中，对后端完全没有影响，因此改变 hash 不会重新加载页面；同时每一次改变#后的部分，都会在浏览器的访问历史中增加一个记录，使用”后退”按钮，就可以回到上一个位置；所以说**Hash 模式通过锚点值的改变，根据不同的值，渲染指定 DOM 位置的不同数据**。hash 模式的原理是 onhashchange 事件(监测 hash 值变化)，可以在 window 对象上监听这个事件。

### 2、History 模式：

由于 hash 模式会在 url 中自带#，如果不想要很丑的 hash，我们可以用路由的 history 模式，只需要在配置路由规则时，加入"mode: 'history'",这种模式充分利用了 html5 history interface 中新增的 pushState() 和 replaceState() 方法。这两个方法应用于浏览器记录栈，在当前已有的 back、forward、go 基础之上，它们提供了对历史记录修改的功能。只是当它们执行修改时，虽然改变了当前的 URL ，但浏览器不会立即向后端发送请求。

```javascript
//main.js文件中
const router = new VueRouter({
	mode: 'history',
	routes: [...]
})
```

当你使用 history 模式时，URL 就像正常的 url，例如 http://yoursite.com/user/id，比较好看！ 不过这种模式要玩好，还需要后台配置支持。因为我们的应用是个单页客户端应用，如果后台没有正确的配置，当用户在浏览器直接访问 http://oursite.com/user/id 就会返回 404，这就不好看了。 所以呢，**你要在服务端增加一个覆盖所有情况的候选资源：如果 URL 匹配不到任何静态资源，则应该返回同一个 index.html 页面，这个页面就是你 app 依赖的页面。**

```javascript
export const routes = [
  { path: '/', name: 'homeLink', component: Home },
  { path: '/register', name: 'registerLink', component: Register },
  { path: '/login', name: 'loginLink', component: Login },
  { path: '*', redirect: '/' },
]
```

此处就设置如果 URL 输入错误或者是 URL 匹配不到任何静态资源，就自动跳到到 Home 页面

### 3、使用路由模块来实现页面跳转的方式

方式 1：直接修改地址栏

方式 2：this.$router.push(‘路由地址’)

方式 3： `<router-linkto="路由地址"></router-link>`
