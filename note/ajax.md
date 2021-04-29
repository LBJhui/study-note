# 谈一谈你对 ajax 的理解

## 实现方式？

- 在后端当中可以**直接**用 ajax 吗？不可以

是 XHR 来实现的   XMLHttpRequest

XML: Extensible Markup Language

HTML: Hyper Text Markup Language

Ajax: Asynchronous JavaScript and XML



无加载刷新技术； 实现局部渲染技术；

1999 IE5 利用 JavaScript 单独的向服务器发送 http 请求



所有基于 ajax 的通讯基本都是 json 的数据格式



```javascript
var xhr
if (window.XMLHttpRequest) {
  xhr = new XMLHttpRequest() // ie7+
} else {
  xhr = new ActiveObject('Microsoft.XMLHttp')
}
```



ajax 的步骤：

1. 创建 XHR
2. 发送 HTTP 请求 Hyper Text Transfer protocol
3. 接受服务器给前端的结果
4. 处理服务器给到的结果

`xhr.open()`  // 请求的方式

status:

- responseText:文本
- responseXML: XML.      'application/xml'   区别（'text/xml'）
- status
- statusText

`If(xhr.status >= 200 && xhr.status < 300 || xor.status ===304) { }`

`readyState`		`onreadystatechange`

- 0 初始化
- 1 启动
- 2 发送
- 3 接收
- 4 完成

`xhr.send()`

简单请求、复杂请求

**get、post 的区别**

1. post 更安全
   - 不会作为 url 的一部分、不会被缓存、保存在服务器日志和浏览器记录中
2. post 发送的数据量更大( get 有 url 长度限制)
   - 长度限制： IE( 2083 字节)	firefox( 65536 字符)	chrome( 8182 字符)	safari( 80000 字符)	opera( 190000 字符)
3. post 能发送更多的数据类型(各种类型的文件)
   - get 只能发送 ASCII 字符

## 缺陷？



## 影响？

