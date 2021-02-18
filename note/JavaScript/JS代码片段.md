## 15条你可能不知道的JS高效技巧

### **1、延迟函数delay**

```
const delay = ms => new Promise((resolve, reject) => setTimeout(resolve, ms))

const getData = status => new Promise((resolve, reject) => {
  status ? resolve('done') : reject('fail')
})
const getRes = async (data) => {
  try {
    const res = await getData(data)
    const timestamp = new Date().getTime()
    await delay(1000)
    console.log(res, new Date().getTime() - timestamp)
  } catch (error) {
    console.log(error)
  }
}
getRes(true) // 隔了1秒
```

### **2、分割指定长度的元素数组** 

```
const listChunk = (list, size = 1, cacheList = []) => {
  const tmp = [...list]
  if (size <= 0) {
    return cacheList
  }
  while (tmp.length) {
    cacheList.push(tmp.splice(0, size))
  }
  return cacheList
}

console.log(listChunk([1, 2, 3, 4, 5, 6, 7, 8, 9])) // [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
console.log(listChunk([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)) // [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
console.log(listChunk([1, 2, 3, 4, 5, 6, 7, 8, 9], 0)) // []
console.log(listChunk([1, 2, 3, 4, 5, 6, 7, 8, 9], -1)) // []
```

### **3、获取数组交集**

```
const intersection = (list, ...args) => list.filter(item => args.every(list => list.includes(item)))

console.log(intersection([2, 1], [2, 3])) // [2]
console.log(intersection([1, 2], [3, 4])) // []
```

### **4、函数柯里化**

```
const curring = fn => {
  const { length } = fn
  const curried = (...args) => {
    return (args.length >= length
      ? fn(...args)
      : (...args2) => curried(...args.concat(args2)))
  }
  return curried
}

const listMerge = (a, b, c) => [a, b, c]
const curried = curring(listMerge)
console.log(curried(1)(2)(3)) // [1, 2, 3]

console.log(curried(1, 2)(3)) // [1, 2, 3]

console.log(curried(1, 2, 3)) // [1, 2, 3]
```

### **5、字符串前面空格去除与替换** 

```
const trimStart = str => str.replace(new RegExp('^([\\s]*)(.*)$'), '$2')
console.log(trimStart(' abc ')) // abc
console.log(trimStart('123 ')) // 123
```

### **6、字符串后面空格去除与替换**

```
const trimEnd = str => str.replace(new RegExp('^(.*?)([\\s]*)$'), '$1')
console.log(trimEnd(' abc ')) //   abc
console.log(trimEnd('123 ')) // 123
```

### **7、获取当前子元素是其父元素下子元素的排位**

```
const getIndex = el => {
  if (!el) {
    return -1
  }
  let index = 0
  do {
    index++
  } while (el = el.previousElementSibling)
  return index
}
```

### **8、获取当前元素相对于document的偏移量**

```
const getOffset = el => {
  const {
    top,
    left
  } = el.getBoundingClientRect()
  const {
    scrollTop,
    scrollLeft
  } = document.body
  return {
    top: top + scrollTop,
    left: left + scrollLeft
  }
}
```

### **9、获取元素类型**

```
const dataType = obj => Object.prototype.toString.call(obj).replace(/^\[object (.+)\]$/, '$1').toLowerCase();
```

### **10、判断是否是移动端**

```
 const isMobile = () => 'ontouchstart' in window
```

### **11、fade动画**

```
const fade = (el, type = 'in') {
  el.style.opacity = (type === 'in' ? 0 : 1)
  let last = +new Date()
  const tick = () => {
      const opacityValue = (type === 'in' 
                          ? (new Date() - last) / 400
                          : -(new Date() - last) / 400)
      el.style.opacity = +el.style.opacity + opacityValue
      last = +new Date()
      if (type === 'in'
        ? (+el.style.opacity < 1)
        : (+el.style.opacity > 0)) {
          requestAnimationFrame(tick)
      }
  }
  tick()
} 
```

### **12、将指定格式的字符串解析为日期字符串**

```
const dataPattern = (str, format = '-') => {
  if (!str) {
    return new Date()
  }
  const dateReg = new RegExp(`^(\\d{2})${format}(\\d{2})${format}(\\d{4})$`)
  const [, month, day, year] = dateReg.exec(str)
  return new Date(`${month}, ${day} ${year}`)
}

console.log(dataPattern('12-25-1995')) // Mon Dec 25 1995 00:00:00 GMT+0800 (中国标准时间)
```

### **13、禁止网页复制粘贴**

```
const html = document.querySelector('html')
html.oncopy = () => false
html.onpaste = () => false
```

### **14、input框限制只能输入中文**

```
const input = document.querySelector('input[type="text"]')
const clearText = target => {
  const {
    value
  } = target
  target.value = value.replace(/[^\u4e00-\u9fa5]/g, '')
}
input.onfocus = ({ target }) => {
  clearText(target)
}
input.onkeyup = ({ target }) => {
  clearText(target)
}
input.onblur = ({ target }) => {
  clearText(target)
}
input.oninput = ({ target }) => {
  clearText(target)
}
```

### **15、去除字符串中的html代码**

```
const removehtml = (str = '') => str.replace(/<[\/\!]*[^<>]*>/ig, '')
console.log(removehtml('<h1>哈哈哈哈<呵呵呵</h1>')) // 哈哈哈哈<呵呵呵
```