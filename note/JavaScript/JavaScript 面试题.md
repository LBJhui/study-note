# JavaScript 面试题

## 交换两个变量的值

1.

```javascript
let a = 2
let b = 3
let temp = a
a = b
b = temp
```

2.

```javascript
let a = 2
let b = 3
a = a + b
b = a - b
a = a - b
```

3.

```javascript
let a = 2
let b = 3
a = a * b
b = a / b
a = a / b
```

4.

```javascript
let a = 2
let b = 3
a = [a, b]
b = a[0]
a = a[1]
```

5.

```javascript
let a = 2
let b = ((3)[(a, b)] = [b, a])
```

## 冒泡排序

1. 相邻元素进行比较，大的到后面去
2. 比较趟数等于元素数量-1

```javascript
let arr = [3, 4, 1, 6, 8, 2]
for (let i = 0; i < arr.length - 1; i++) {
  let isSwapped = false // 假设没有元素进行交换，如果在某一趟的时候发现没有元素进行交换，说明顺序是对的
  for (let j = 0; j < arr.length - 1; j++) {
    if (arr[j] > arr[j + 1]) {
      let temp = arr[j]
      arr[j] = arr[j + 1]
      arr[j + 1] = arr[j]
      isSwapped = true
    }
  }
  if (!isSwapped) {
    break
  }
}
```

## 九九乘法表

```javascript
for(let i = 1; i < 9; i++){
  for(let j = 1;j < i; j++){
    document.write(j + 'x' + i + '=' j * i)
  }
  document.write('<br>')
}
```
