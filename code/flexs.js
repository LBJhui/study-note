//flexs.js
;(function (win) {
  var bodyStyle = document.createElement('style')
  // 这里根据具体的设计稿尺寸来定
  bodyStyle.innerHTML = `body{width:1920px; height:1080px!important;}`
  document.documentElement.firstElementChild.appendChild(bodyStyle)

  function refreshScale() {
    let docWidth = document.documentElement.clientWidth
    let docHeight = document.documentElement.clientHeight
    var designWidth = 1920, // 这里根据具体的设计稿尺寸来定
      designHeight = 1080, // 这里根据具体的设计稿尺寸来定
      widthRatio = docWidth / designWidth,
      heightRatio = docHeight / designHeight
    document.body.style = `transform:scale(${widthRatio},${heightRatio});transform-origin:left top;overflow: hidden;`
    // 应对浏览器全屏切换前后窗口因短暂滚动条问题出现未占满情况
    setTimeout(function () {
      var lateWidth = document.documentElement.clientWidth,
        lateHeight = document.documentElement.clientHeight
      if (lateWidth === docWidth) return

      widthRatio = lateWidth / designWidth
      heightRatio = lateHeight / designHeight
      document.body.style =
        'transform:scale(' +
        widthRatio +
        ',' +
        heightRatio +
        ');transform-origin:left top;overflow: hidden;'
    }, 0)
  }
  refreshScale()

  win.addEventListener(
    'pageshow',
    function (e) {
      if (e.persisted) {
        // 浏览器后退的时候重新计算
        refreshScale()
      }
    },
    false,
  )
  win.addEventListener('resize', refreshScale, false)
})(window)
