## 实用的 JavaScript 小技巧

### 1. 将 arguments 对象转换为数组

**arguments** 对象是函数内部可访问的类似数组的对象，其中包含传递给该函数的参数的值。

但它与其他数组不同，我们可以访问其元素值并获得长度，但是不能在其上使用其他的数组方法。

幸运的是，我们可以将其转换为常规数组：

```javascript
var argArray = Array.prototype.slice.call(arguments);
```

### 2. 对数组中所有的值求和

我最初的想法是使用循环，但是那样做太费事了。

```javascript
var numbers = [3, 5, 7, 2];
var sum = numbers.reduce((x, y) => x + y);
console.log(sum); // returns 17
```

### 3. 条件短路

我们有以下代码：

```javascript
if (hungry) {
    goToFridge();
}
```

通过将变量与函数一起使用，我们可以使其更短：

```javascript
hungry && goToFridge()
```

### 4. 对条件使用逻辑或

我曾经在函数的开头声明自己的变量，只是为了避免在出现任何意外错误的情况下得到 `undefined`。

```javascript
function doSomething(arg1){ 
    arg1 = arg1 || 32; // 如果变量尚未设置，则 arg1 将以 32 作为默认值
}
```

### 5. 逗号运算符

逗号运算符（ `,`）用来评估其每个操作数（从左到右）并返回最后一个操作数的值。

```javascript
let x = 1;

x = (x++, x);

console.log(x);
// expected output: 2

x = (2, 3);

console.log(x);
// expected output: 3
```

### 6. 用 length  调整数组大小

你可以调整数组大小或清空数组。

```javascript
var array = [11, 12, 13, 14, 15];  
console.log(array.length); // 5  

array.length = 3;  
console.log(array.length); // 3  
console.log(array); // [11,12,13]

array.length = 0;  
console.log(array.length); // 0  
console.log(array); // []
```

### 7. 通过数组解构对值进行交换

解构赋值语法是一种 JavaScript 表达式，可以将数组中的值或对象中的属性解压缩为不同的变量。

```javascript
let a = 1, b = 2
[a, b] = [b, a]
console.log(a) // -> 2
console.log(b) // -> 1
```

### 8. 随机排列数组中的元素

*我每天我都在洗牌'*

```javascript
var list = [1, 2, 3, 4, 5, 6, 7, 8, 9];
console.log(list.sort(function() {
    return Math.random() - 0.5
})); 
// [4, 8, 2, 9, 1, 3, 6, 5, 7]
```

### 9. 属性名可以是动态的

你可以在声明对象之前分配动态属性。

```javascript
const dynamic = 'color';
var item = {
    brand: 'Ford',
    [dynamic]: 'Blue'
}
console.log(item); 
// { brand: "Ford", color: "Blue" }
```

### 10. 过滤唯一值

对于所有 ES6 爱好者，我们可以通过使用带有展开运算符的 Set 对象来创建一个仅包含唯一值的新数组。

```javascript
const my_array = [1, 2, 2, 3, 3, 4, 5, 5]
const unique_array = [...new Set(my_array)];
console.log(unique_array); // [1, 2, 3, 4, 5]
```