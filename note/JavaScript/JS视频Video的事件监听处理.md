在日常应用场景中，可能会遇到这么一个情况，需要判断用户是否完整的观看完了一部视频，在这个场景中，和视频相关的事件大体涉及到几个部分，获取视频长度，视频开始播放，暂停播放和播放结束，下面来看下如何通过JavaScript来监听获取视频的这几种状态。

1）html页面视频标签大体如下

```html
<video id="video" controls="controls">
  <source type="video/mp4" src="mi.mp4" />
</video>
```

（2）视频加载后获取视频的长度

```javascript
var elevideo = document.getElementById('video')
elevideo.addEventListener('loadedmetadata', function () { // 加载数据
  // 视频的总长度
  console.log(elevideo.duration)
})
```

（3）视频开始播放

```javascript
var elevideo = document.getElementById('video')
elevideo.addEventListener('play', function () { // 播放开始执行的函数
  console.log('开始播放')
})
```

（4） 视频正在播放中

```javascript
var elevideo = document.getElementById('video')
elevideo.addEventListener('playing', function () { // 播放中
  console.log('播放中')
})

```

（5）视频加载中

```javascript
var elevideo = document.getElementById('video')
elevideo.addEventListener('waiting', function () { // 加载
  console.log('加载中')
})
```

（6）视频暂停播放

```javascript
var elevideo = document.getElementById('video')
elevideo.addEventListener('pause', function () { // 暂停开始执行的函数
  console.log('暂停播放')
})
```

（7）视频结束播放

```javascript
var elevideo = document.getElementById('video')
elevideo.addEventListener('ended', function () { // 结束
  console.log('播放结束')
}, false)
```