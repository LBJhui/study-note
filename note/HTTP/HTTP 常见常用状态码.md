**101 Switch Protocol**

升级协议，如从 http 到 ws，此时需要反向代理支持，如 Nginx，在 Nginx 配置 websockt 如下:

```shell
location / {
  proxy_http_version 1.1;
  proxy_set_header Upgrade $http_upgrade;
  proxy_set_header Connection  $connection_upgrade;
}
```

**200 Ok**

表示资源请求成功，也是最常见到的状态码

**201 Created**

资源创建成功，多用于 POST 请求

**204 No Content**

响应不会返回 Body，一般由以下两种情况

1. 与 Options/Delete 请求搭配
2. 打点类

示例一: 掘金为 Options 请求的状态码设置为 204

示例二: 知乎为 Delete 请求的状态码设置为 204，以下请求为取消关注

示例三: 当你在知乎看段子时，不妨打开控制台，会发现一个是 204 的状态码

**206 Partial Content**

当请求多媒体数据数据较大时，会进行分片传输。当你在 B 站观看视频，打开开发者工具，会发现许多 206 状态码以及响应头 Content-Range

**301 Moved Permanently**

永久重定向。http 转向 https 时，有时会使用 301，**此时浏览器会自动缓存，下次直接自动跳转，不再请求服务器**。当更新域名需要 SEO 优化时，同样使用 301 或者 308。如 B 站：

```nginx
$ curl www.bilibili.com -vvv
< HTTP/1.1 301 Moved Permanently
< Server: Tengine
< Date: Thu, 22 Oct 2020 08:04:59 GMT
< Content-Type: text/html
< Content-Length: 239
< Connection: keep-alive
< Location: https://www.bilibili.com/
```

**302 Found**

暂时重定向。http 转向 https 时，有时也会使用 302，如知乎的跳转

```nginx
$ curl www.zhihu.com -vvv
< HTTP/1.1 302 Found
< Location: https://www.zhihu.com/
< Content-Length: 0
< X-NWS-LOG-UUID: 16068764905156850032
< Connection: keep-alive
< Server: Lego Server
< Date: Thu, 22 Oct 2020 08:20:29 GMT
< X-Cache-Lookup: Return Directly
```

**304 Not Modified**

资源已被缓存，与之相关的响应头部有：

- `ETag`
- `last-modified`/`if-modified-since`

一般用作 `index.html` 等不带 hash 的资源

**307 Temporary Redirect**

暂时重定向。也可作为 http 到 https 的重定向。还有一种用途用作 HSTS，当谷歌浏览器发现某 http 资源已被加入到 HSTS 列表，浏览器内部会通过 307 作重定向

> http 状态码中 301，302 和 307 有什么区别

- 301，Moved Permanently。永久重定向，该操作比较危险，需要谨慎操作：如果设置了 301，但是一段时间后又想取消，但是浏览器中已经有了缓存，还是会重定向。
- 302，Found。临时重定向，但是会在重定向的时候改变 method: 把 POST 改成 GET，于是有了 307
- 307，Temporary Redirect。临时重定向，在重定向时不会改变 method

**308 Permanent Redirect**

永久重定向。与 301 不同的是，当它重定向到新的地址时，并不会改变 method。

**400 Bad Request**

对于服务器无法理解的参数，将会使用 400 作为返回码

示例一: 当 Content-Type: JSON 时，服务器解析 JSON 却失败

```nginx
HTTP/1.1 400 Bad Request
Content-Length: 35

{"message":"Problems parsing JSON"}
```

**401 Unauthorized**

当没有权限的用户请求需要带有权限的资源时，会返回 401，此时携带正确的权限凭证再试一次可以解决问题

有时认证失败也会返回 401

示例一: 知乎登录时密码不正确

示例二: Github 中错误的凭证信息请求带权限资源

**403 Forbidden**

我就是不想让你访问，不管你的权限凭证是否正确！

> In summary, a 401 Unauthorized response should be used for missing or bad authentication, and a 403 Forbidden response should be used afterwards, when the user is authenticated but isn’t authorized to perform the requested operation on the given resource.

**404 Not Found**

未找到资源

**405 Method Not Allowed**

我需要 POST 这条资源，你去 GET 个锤子

**413 Payload Too Large**

不要给我扔这么大的 Body，我处理不过来

**418 I'm A Teapot**

我是一个茶壶

我要抛咖啡，你却扔给我一个茶壶？

也可以用来处理不合法的参数校验，我想要个字符串，你给了我一个整数？

**422 Unprocessable Entity**

常用来处理不合法的参数校验。

Github 上给某个项目点赞时，故意设置一个不正确的参数命名，会返回状态码 422

**429 Too Many Request**

请求过多被限流。

超过某一个 API 的 Rate Limit 规则，会被限流，返回 429 状态码

示例: 在 Sentry 中异常上报过于频繁被限流

**500 Internal Server Error**

服务器内部错误，很有可能是应用层未捕获错误而导致整个服务挂掉

**502 Bad Gateway**

Nginx 上常见，从上游应用层未返回响应，上游应用层挂了

由于大量流量造成服务忙，稍等一下说不定就能用了

网关超时，上游应用层迟迟未响应
