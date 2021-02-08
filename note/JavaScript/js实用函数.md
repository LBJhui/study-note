[toc]

## 1. 类型强制转换

### 1.1 string 强制转换为数字

可以用 `*1`来转化为数字(实际上是调用 `.valueOf`方法)

---

`valueOf() `方法返回 Math 对象的原始值。`valueOf() `是数组对象的默认方法。

```javascript
var fruits = ['Banana', 'Orange', 'Apple', 'Mango']
var v = fruits.valueOf()
console.log(v) //(4) ["Banana", "Orange", "Apple", "Mango"]s
```

---

然后使用 `Number.isNaN`来判断是否为 `NaN`，或者使用 `a!==a` 来判断是否为 `NaN`，因为 `NaN!==NaN`

```javascript
32 * 1 // 32
ds * 1 // NaN
null * 1 // 0
undefined * 1 // NaN
1 * { valueOf: () => 3 } // 3
```

**常用：** 也可以使用 `+`来转化字符串为数字

```javascript
;+123 + // 123
  ds + // NaN // 0
  +null + // 0
  undefined + // NaN
  { valueOf: () => 3 } // 3
```

### 1.2 object 强制转化为 string

可以使用 `字符串+Object` 的方式来转化对象为字符串(实际上是调用 `.toString()` 方法)

---

```javascript
var num = 15
var n = num.toString()
console.log(n) //"15"
```

---

```javascript
'the Math object:' + Math // "the Math object:[object Math]"
'lbj' + [1, 2, 3] //"lbj1,2,3"
'the JSON object:' + JSON // "the JSON object:[object JSON]"
'lbj' + { name: 'hui' } //"lbj[object Object]"
```

当然也可以覆盖对象的 `toString`和 `valueOf`方法来自定义对象的类型转换：

```javascript
2 * { valueOf: () => 3 } // 6
'J' + { toString: () => 'S' } // "JS"
```

> 《Effective JavaScript》P11：<mark>当 `+`用在连接字符串时，当一个对象既有 `toString`方法又有 `valueOf`方法时候，JS 通过盲目使用 `valueOf`方法来解决这种含糊。</mark>

对象通过 `valueOf`方法强制转换为数字，通过 `toString`方法强制转换为字符串

```javascript
;+{ toString: () => 'S', valueOf: () => 'J' } // NaN
```

### 1.3 使用 Boolean 过滤数组中的所有假值

我们知道 JS 中有一些假值：`false`， `null`， `0`， `""`， `undefined`， `NaN`，怎样把数组中的假值快速过滤呢，可以使用 Boolean 构造函数来进行一次转换

```javascript
const compact = (arr) => arr.filter(Boolean)
compact([0, 1, false, 2, , 3, 'a', 'e' * 23, NaN, 's', 34])
//(6) [1, 2, 3, "a", "s", 34]
```

### 1.4 双位运算符 ~~

可以使用双位操作符来替代正数的 `Math.floor()`，替代负数的 `Math.ceil()`。双否定位操作符的优势在于它执行相同的操作运行速度更快。

```javascript
Math.floor(4.9) === 4 //true
// 简写为：
~~4.9 === 4 //true
```

不过要注意，对正数来说 `~~` 运算结果与 `Math.floor()` 运算结果相同，而对于负数来说与 `Math.ceil()`的运算结果相同：

```javascript
~~4.5 // 4
Math.floor(4.5) // 4
Math.ceil(4.5) // 5

~~-4.5 // -4
Math.floor(-4.5) // -5
Math.ceil(-4.5) // -4
```

### 1.5 短路运算符

我们知道逻辑与 `&&`与逻辑或 `||`是短路运算符，短路运算符就是从左到右的运算中前者满足要求，就不再执行后者了；

可以理解为：

- `&&`为取假运算，从左到右依次判断，如果遇到一个假值，就返回假值，以后不再执行，否则返回最后一个真值

- `||`为取真运算，从左到右依次判断，如果遇到一个真值，就返回真值，以后不再执行，否则返回最后一个假值

```javascript
let param1 = expr1 && expr2
let param2 = expr1 || expr2
```

| 运算符 |      示例      |                                                                  说明                                                                   |
| :----: | :------------: | :-------------------------------------------------------------------------------------------------------------------------------------: | ------ | --- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  `&&`  | `expr1&&expr2` | 如果 expr1 能转换成 false 则返回 expr1,否则返回 expr2. 因此, 在 Boolean 环境中使用时, 两个操作结果都为 true 时返回 true,否则返回 false. |
|   `    |                |                                                                    `                                                                    | `expr1 |     | expr2` | 如果 expr1 能转换成 true 则返回 expr1,否则返回 expr2. 因此,在 boolean 环境(在 if 的条件判断中)中使用时, 二者操作结果中只要有一个为 true,返回 true;二者操作结果都为 false 时返回 false. |
|  `!`   |    `!expr`     |                                        如果单个表达式能转换为 true 的话返回 false,否则返回 true.                                        |

因此可以用来做很多有意思的事，比如给变量赋初值：

```javascript
let variable1
let variable2 = variable1 || foo
```

如果 variable1 是真值就直接返回了，后面短路就不会被返回了，如果为假值，则会返回后面的 `foo`。

也可以用来进行简单的判断，取代冗长的 `if`语句：

```javascript
let variable = param && param.prop
```

如果 `param`如果为真值则返回 `param.prop`属性，否则返回 `param`这个假值，这样在某些地方防止 `param`为 `undefined`的时候还取其属性造成报错。

### 1.6 取整 `|0`

对一个数字 `|0`可以取整，负数也同样适用， `num|0`

```javascript
;1.3 |
  (0 - // 1
    1.9) |
  0 // -1
```

### 1.7 判断奇偶数 `&1`

对一个数字 `&1`可以判断奇偶数，负数也同样适用， `num&1`

```javascript
const num = 3
!!(num & 1) // true
!!(num % 2) // true
```

## 2. 函数

### 2.1 函数默认值

```javascript
func = (l, m = 3, n = 4) => l * m * n
func(2) //output: 24
```

注意，<mark>传入参数为 `undefined`或者不传入的时候会使用默认参数，但是传入 `null`还是会覆盖默认参数。</mark>

### 2.2 强制参数

默认情况下，如果不向函数参数传值，那么 JS 会将函数参数设置为 `undefined`。其它一些语言则会发出警告或错误。要执行参数分配，可以使用 `if`语句抛出未定义的错误，或者可以利用 `强制参数`。

```javascript
mandatory = ( ) => {
  throw new Error( Missing parameter! );
}
foo = (bar = mandatory( )) => {     // 这里如果不传入参数，就会执行manadatory函数报出错误
  return bar;
}
```

### 2.3 隐式返回值

返回值是我们通常用来返回函数最终结果的关键字。只有一个语句的箭头函数，可以隐式返回结果（函数必须省略大括号 `{}`，以便省略返回关键字）。

要返回多行语句（例如对象文本），需要使用 `()`而不是 `{}`来包裹函数体。这样可以确保代码以单个语句的形式进行求值。

```javascript
function calcCircumference(diameter) {
  return Math.PI * diameter
}
// 简写为：
calcCircumference = diameter => (
  Math.PI * diameter;
)
```

### 2.4 惰性载入函数

在某个场景下我们的函数中有判断语句，这个判断依据在整个项目运行期间一般不会变化，所以判断分支在整个项目运行期间只会运行某个特定分支，那么就可以考虑惰性载入函数

```javascript
function foo() {
  if (a !== b) {
    console.log(aaa)
  } else {
    console.log(bbb)
  }
}

// 优化后
function foo() {
  if (a != b) {
    foo = function () {
      console.log(aaa)
    }
  } else {
    foo = function () {
      console.log(bbb)
    }
  }
  return foo()
}
```

那么第一次运行之后就会覆写这个方法，下一次再运行的时候就不会执行判断了。当然现在只有一个判断，如果判断很多，分支比较复杂，那么节约的资源还是可观的。

### 2.5 一次性函数

跟上面的惰性载入函数同理，可以在函数体里覆写当前函数，那么可以创建一个一次性的函数，重新赋值之前的代码相当于只运行了一次，适用于运行一些只需要执行一次的初始化代码

```javascript
var sca = function () {
  console.log(msg)
  sca = function () {
    console.log(foo)
  }
}
sca() // msg
sca() // foo
sca() // foo
```

## 3. 字符串

### 3.1 字符串比较时间先后

比较时间先后顺序可以使用字符串：

```javascript
var a = '2014-08-08'
var b = '2014-09-09'

console.log(a > b, a < b) // false true
console.log('21:00' < '09:10') // false
console.log('21:00' < '9:10') // true   时间形式注意补0
```

因为字符串比较大小是按照字符串从左到右每个字符的 `charCode`来的，但所以特别要注意时间形式注意补 0

## 4. 数字

### 4.1 不同进制表示法

ES6 中新增了不同进制的书写格式，在后台传参的时候要注意这一点。

```javascript
29 // 10进制
035 // 8进制29      原来的方式
0o35 // 8进制29      ES6的方式
0x1d // 16进制29
0b11101 // 2进制29
```

### 4.2 精确到指定位数的小数

将数字四舍五入到指定的小数位数。使用 `Math.round()` 和模板字面量将数字四舍五入为指定的小数位数。省略第二个参数 `decimals` ，数字将被四舍五入到一个整数。

```javascript
const round = (n, decimals = 0) =>
  Number(`${Math.round(`${n}e${decimals}`)}e-${decimals}`)
round(1.345, 2) // 1.35
round(1.345, 1) // 1.3
```

### 4.3 数字补 0 操作

感谢网友 @JserWang @vczhan 提供 这个小技巧

有时候比如显示时间的时候有时候会需要把一位数字显示成两位，这时候就需要补 0 操作，可以使用 `slice`和 string 的 `padStart`方法

```javascript
const addZero1 = (num, len = 2) => `0${num}`.slice(-len)
const addZero2 = (num, len = 2) => `${num}`.padStart(len, 0)
addZero1(3) // 03

addZero2(32, 4) // 0032
```

## 5. 数组

### 5.1 reduce 方法同时实现 map 和 filter

假设现在有一个数列，你希望更新它的每一项（map 的功能）然后筛选出一部分（filter 的功能）。如果是先使用 map 然后 filter 的话，你需要遍历这个数组两次。

在下面的代码中，我们将数列中的值翻倍，然后挑选出那些大于 50 的数。

```javascript
const numbers = [10, 20, 30, 40]
const doubledOver50 = numbers.reduce((finalList, num) => {
  num = num * 2
  if (num > 50) {
    finalList.push(num)
  }
  return finalList
}, [])
doubledOver50 // [60, 80]
```

### 5.2 统计数组中相同项的个数

很多时候，你希望统计数组中重复出现项的个数然后用一个对象表示。那么你可以使用 reduce 方法处理这个数组。

下面的代码将统计每一种车的数目然后把总数用一个对象表示。

```javascript
var cars = [BMW, Benz, Benz, Tesla, BMW, Toyota]
var carsObj = cars.reduce(function (obj, name) {
  obj[name] = obj[name] ? ++obj[name] : 1
  return obj
}, {})
carsObj // => { BMW: 2, Benz: 2, Tesla: 1, Toyota: 1 }
```

### 5.3 使用解构来交换参数数值

有时候你会将函数返回的多个值放在一个数组里。我们可以使用数组解构来获取其中每一个值。

```javascript
let param1 = 1
let param2 = 2
;[param1, param2] = [param2, param1]
console.log(param1) // 2
console.log(param2) // 1
```

当然我们关于交换数值有不少其他办法：

```javascript
var temp = a
a = b
b = temp
b = [a, (a = b)][0]
a = a + b
b = a - b
a = a - b
```

### 5.4 接收函数返回的多个结果

在下面的代码中，我们从/post 中获取一个帖子，然后在/comments 中获取相关评论。由于我们使用的是 async/await，函数把返回值放在一个数组中。而我们使用数组解构后就可以把返回值直接赋给相应的变量。

```javascript
async function getFullPost(){
  return await Promise.all([
     fetch( /post ),
     fetch( /comments )
  ]);
}
const [post, comments] = getFullPost();
```

### 5.5 将数组平铺到指定深度

使用递归，为每个深度级别 `depth` 递减 1 。使用 `Array.reduce()` 和 `Array.concat()` 来合并元素或数组。基本情况下， `depth` 等于 1 停止递归。省略第二个参数， `depth` 只能平铺到 1 (单层平铺) 的深度。

```javascript
const flatten = (arr, depth = 1) =>
  depth != 1
    ? arr.reduce(
        (a, v) => a.concat(Array.isArray(v) ? flatten(v, depth - 1) : v),
        []
      )
    : arr.reduce((a, v) => a.concat(v), [])
flatten([1, [2], 3, 4]) // [1, 2, 3, 4]
flatten([1, [2, [3, [4, 5], 6], 7], 8], 2) // [1, 2, 3, [4, 5], 6, 7, 8]
```

### 5.6 数组的对象解构

数组也可以对象解构，可以方便的获取数组的第 n 个值

```javascript
const csvFileLine =  1997,John Doe,US,john@doe.com,New York ;
const { 2: country, 4: state } = csvFileLine.split( , );


country            // US
state            // New Yourk
```

## 6. 对象

### 6.1 使用解构删除不必要属性

有时候你不希望保留某些对象属性，也许是因为它们包含敏感信息或仅仅是太大了（just too big）。你可能会枚举整个对象然后删除它们，但实际上只需要简单的将这些无用属性赋值给变量，然后把想要保留的有用部分作为剩余参数就可以了。

下面的代码里，我们希望删除\_internal 和 tooBig 参数。我们可以把它们赋值给 internal 和 tooBig 变量，然后在 cleanObject 中存储剩下的属性以备后用。

```javascript
let { _internal, tooBig, ...cleanObject } = {
  el1: 1,
  _internal: 'secret',
  tooBig: {},
  el2: 2,
  el3: 3,
}

console.log(cleanObject) // {el1:  1 , el2:  2 , el3:  3 }
```

### 6.2 在函数参数中解构嵌套对象

在下面的代码中，engine 是对象 car 中嵌套的一个对象。如果我们对 engine 的 vin 属性感兴趣，使用解构赋值可以很轻松地得到它。

```javascript
var car = {
  model:  bmw 2018 ,
  engine: {
    v6: true,
    turbo: true,
    vin: 12345
  }
}
const modelAndVIN = ({model, engine: {vin}}) => {
  console.log(`model: ${model} vin: ${vin}`);
}
modelAndVIN(car); // => model: bmw 2018  vin: 12345
```

## 7. 代码复用

### 7.1 Object [key]

虽然将 `foo.bar` 写成 `foo[bar]` 是一种常见的做法，但是这种做法构成了编写可重用代码的基础。许多框架使用了这种方法，比如 element 的表单验证。

请考虑下面这个验证函数的简化示例：

```javascript
function validate(values) {
  if (!values.first) return false
  if (!values.last) return false
  return true
}
console.log(validate({ first: Bruce, last: Wayne })) // true
```

上面的函数完美的完成验证工作。但是当有很多表单，则需要应用验证，此时会有不同的字段和规则。如果可以构建一个在运行时配置的通用验证函数，会是一个好选择。

```javascript
// object validation rules
const schema = {
  first: {
    required: true,
  },
  last: {
    required: true,
  },
}

// universal validation function
const validate = (schema, values) => {
  for (field in schema) {
    if (schema[field].required) {
      if (!values[field]) {
        return false
      }
    }
  }
  return true
}
console.log(validate(schema, { first: Bruce })) // false
console.log(validate(schema, { first: Bruce, last: Wayne })) // true
```

现在有了这个验证函数，我们就可以在所有窗体中重用，而无需为每个窗体编写自定义验证函数。

## 清空和截短数组

最简单的清空和截短数组的方法就是改变 `length` 属性：

```
const arr = [11, 22, 33, 44, 55, 66];

// 截取
arr.length = 3;
console.log(arr); //=> [11, 22, 33];

// 清空
arr.length = 0;
console.log(arr); //=> []
console.log(arr[2]); //=> undefined
复制代码
```

## 使用对象结构模拟命名参数

以前，当我们希望向一个函数传递多个参数时，可能会采用`配置对象`的模式：

```
doSomething({ foo: 'Hello', bar: 'Hey!', baz: 42 });
function doSomething(config) {
  const foo = config.foo !== undefined ? config.foo : 'Hi';
  const bar = config.bar !== undefined ? config.bar : 'Yo!';
  const baz = config.baz !== undefined ? config.baz : 13;
  // ...
}
复制代码
```

这是一个古老但是有效的模式，有了 `ES2015` 的对象结构，你可以这样使用：

```
function doSomething({ foo = 'Hi', bar = 'Yo!', baz = 13 }) {
  // ...
}
复制代码
```

如果你需要这个`配置对象`参数变成可选的，也很简单：

```
function doSomething({ foo = 'Hi', bar = 'Yo!', baz = 13 } = {}) {
  // ...
}
复制代码
```

## 数组的对象解构

使用对象解构将数组项赋值给变量：

```
const csvFileLine = '1997,John Doe,US,john@doe.com,New York';
const { 2: country, 4: state } = csvFileLine.split(',');
复制代码
```

> 注：本例中，`2` 为 `split` 之后的数组下标，`country` 为指定的变量，值为 `US`

## `switch` 语句中使用范围

这是一个在 `switch` 语句中使用范围的例子：

```
function getWaterState(tempInCelsius) {
  let state;

  switch (true) {
    case (tempInCelsius <= 0):
      state = 'Solid';
      break;
    case (tempInCelsius > 0 && tempInCelsius < 100):
      state = 'Liquid';
      break;
    default:
      state = 'Gas';
  }
  return state;
}
复制代码
```

## `await` 多个 `async` 函数

`await` 多个 `async` 函数并等待他们执行完成，我们可以使用 `Promise.all`：

```
await Promise.all([anAsyncCall(), thisIsAlsoAsync(), oneMore()])
复制代码
```

## 创建纯对象

你可以创建一个 100% 的纯对象，这个对象不会继承 `Object` 的任何属性和方法（比如 `constructor`，`toString()` 等）：

```
const pureObject = Object.create(null);
console.log(pureObject); //=> {}
console.log(pureObject.constructor); //=> undefined
console.log(pureObject.toString); //=> undefined
console.log(pureObject.hasOwnProperty); //=> undefined
复制代码
```

## 格式化 `JSON` 代码

`JSON.stringify` 不仅可以`字符串`化对象，它也可以格式化你的 `JSON` 输出：

```
const obj = {
  foo: { bar: [11, 22, 33, 44], baz: { bing: true, boom: 'Hello' } }
};

// 第三个参数为格式化需要的空格数目
JSON.stringify(obj, null, 4);
// =>"{
// =>    "foo": {
// =>        "bar": [
// =>            11,
// =>            22,
// =>            33,
// =>            44
// =>        ],
// =>        "baz": {
// =>            "bing": true,
// =>            "boom": "Hello"
// =>        }
// =>    }
// =>}"
复制代码
```

## 移除数组重复项

使用 `ES2015` 和扩展运算符，你可以轻松移除数组中的重复项：

```
const removeDuplicateItems = arr => [...new Set(arr)];
removeDuplicateItems([42, 'foo', 42, 'foo', true, true]);
//=> [42, "foo", true]
复制代码
```

> 注：只适用于数组内容为`基本数据类型`

## 扁平化多维数组

使用扩展运算符可以快速扁平化数组：

```
const arr = [11, [22, 33], [44, 55], 66];
const flatArr = [].concat(...arr); //=> [11, 22, 33, 44, 55, 66]
复制代码
```

不幸的是，上面的技巧只能适用`二维数组`，但是使用递归，我们可以扁平化任意纬度数组：

```
function flattenArray(arr) {
  const flattened = [].concat(...arr);
  return flattened.some(item => Array.isArray(item)) ?
    flattenArray(flattened) : flattened;
}

const arr = [11, [22, 33], [44, [55, 66, [77, [88]], 99]]];
const flatArr = flattenArray(arr);
//=> [11, 22, 33, 44, 55, 66, 77, 88, 99]
复制代码
```

作者：超 zhCN
链接：https://juejin.im/post/6844903635223068680
来源：掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。清空和截短数组

最简单的清空和截短数组的方法就是改变 `length` 属性：

```
const arr = [11, 22, 33, 44, 55, 66];

// 截取
arr.length = 3;
console.log(arr); //=> [11, 22, 33];

// 清空
arr.length = 0;
console.log(arr); //=> []
console.log(arr[2]); //=> undefined
复制代码
```

## 使用对象结构模拟命名参数

以前，当我们希望向一个函数传递多个参数时，可能会采用`配置对象`的模式：

```
doSomething({ foo: 'Hello', bar: 'Hey!', baz: 42 });
function doSomething(config) {
  const foo = config.foo !== undefined ? config.foo : 'Hi';
  const bar = config.bar !== undefined ? config.bar : 'Yo!';
  const baz = config.baz !== undefined ? config.baz : 13;
  // ...
}
复制代码
```

这是一个古老但是有效的模式，有了 `ES2015` 的对象结构，你可以这样使用：

```
function doSomething({ foo = 'Hi', bar = 'Yo!', baz = 13 }) {
  // ...
}
复制代码
```

如果你需要这个`配置对象`参数变成可选的，也很简单：

```
function doSomething({ foo = 'Hi', bar = 'Yo!', baz = 13 } = {}) {
  // ...
}
复制代码
```

## 数组的对象解构

使用对象解构将数组项赋值给变量：

```
const csvFileLine = '1997,John Doe,US,john@doe.com,New York';
const { 2: country, 4: state } = csvFileLine.split(',');
复制代码
```

> 注：本例中，`2` 为 `split` 之后的数组下标，`country` 为指定的变量，值为 `US`

## `switch` 语句中使用范围

这是一个在 `switch` 语句中使用范围的例子：

```
function getWaterState(tempInCelsius) {
  let state;

  switch (true) {
    case (tempInCelsius <= 0):
      state = 'Solid';
      break;
    case (tempInCelsius > 0 && tempInCelsius < 100):
      state = 'Liquid';
      break;
    default:
      state = 'Gas';
  }
  return state;
}
复制代码
```

## `await` 多个 `async` 函数

`await` 多个 `async` 函数并等待他们执行完成，我们可以使用 `Promise.all`：

```
await Promise.all([anAsyncCall(), thisIsAlsoAsync(), oneMore()])
复制代码
```

## 创建纯对象

你可以创建一个 100% 的纯对象，这个对象不会继承 `Object` 的任何属性和方法（比如 `constructor`，`toString()` 等）：

```
const pureObject = Object.create(null);
console.log(pureObject); //=> {}
console.log(pureObject.constructor); //=> undefined
console.log(pureObject.toString); //=> undefined
console.log(pureObject.hasOwnProperty); //=> undefined
复制代码
```

## 格式化 `JSON` 代码

`JSON.stringify` 不仅可以`字符串`化对象，它也可以格式化你的 `JSON` 输出：

```
const obj = {
  foo: { bar: [11, 22, 33, 44], baz: { bing: true, boom: 'Hello' } }
};

// 第三个参数为格式化需要的空格数目
JSON.stringify(obj, null, 4);
// =>"{
// =>    "foo": {
// =>        "bar": [
// =>            11,
// =>            22,
// =>            33,
// =>            44
// =>        ],
// =>        "baz": {
// =>            "bing": true,
// =>            "boom": "Hello"
// =>        }
// =>    }
// =>}"
复制代码
```

## 移除数组重复项

使用 `ES2015` 和扩展运算符，你可以轻松移除数组中的重复项：

```
const removeDuplicateItems = arr => [...new Set(arr)];
removeDuplicateItems([42, 'foo', 42, 'foo', true, true]);
//=> [42, "foo", true]
复制代码
```

> 注：只适用于数组内容为`基本数据类型`

## 扁平化多维数组

使用扩展运算符可以快速扁平化数组：

```
const arr = [11, [22, 33], [44, 55], 66];
const flatArr = [].concat(...arr); //=> [11, 22, 33, 44, 55, 66]
复制代码
```

不幸的是，上面的技巧只能适用`二维数组`，但是使用递归，我们可以扁平化任意纬度数组：

```
function flattenArray(arr) {
  const flattened = [].concat(...arr);
  return flattened.some(item => Array.isArray(item)) ?
    flattenArray(flattened) : flattened;
}

const arr = [11, [22, 33], [44, [55, 66, [77, [88]], 99]]];
const flatArr = flattenArray(arr);
//=> [11, 22, 33, 44, 55, 66, 77, 88, 99]
复制代码
```

# 为元素添加 on 方法

```
Element.prototype.on = Element.prototype.addEventListener;

NodeList.prototype.on = function (event, fn) {、
    []['forEach'].call(this, function (el) {
        el.on(event, fn);
    });
    return this;
};
```

# 为元素添加 trigger 方法

```
Element.prototype.trigger = function(type, data) {
  var event = document.createEvent("HTMLEvents");
  event.initEvent(type, true, true);
  event.data = data || {};
  event.eventName = type;
  event.target = this;
  this.dispatchEvent(event);
  return this;
};

NodeList.prototype.trigger = function(event) {
  []["forEach"].call(this, function(el) {
    el["trigger"](event);
  });
  return this;
};
```

# 转义 html 标签

```
function HtmlEncode(text) {
  return text
    .replace(/&/g, "&")
    .replace(/\"/g, '"')
    .replace(/</g, "<")
    .replace(/>/g, ">");
}
```

# HTML 标签转义

```
// HTML 标签转义
// @param {Array.<DOMString>} templateData 字符串类型的tokens
// @param {...} ..vals 表达式占位符的运算结果tokens
//
function SaferHTML(templateData) {
  var s = templateData[0];
  for (var i = 1; i < arguments.length; i++) {
    var arg = String(arguments[i]);
    // Escape special characters in the substitution.
    s += arg
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
    // Don't escape special characters in the template.
    s += templateData[i];
  }
  return s;
}
// 调用
var html = SaferHTML`<p>这是关于字符串模板的介绍</p>`;
```

# 跨浏览器绑定事件

```
function addEventSamp(obj, evt, fn) {
  if (!oTarget) {
    return;
  }
  if (obj.addEventListener) {
    obj.addEventListener(evt, fn, false);
  } else if (obj.attachEvent) {
    obj.attachEvent("on" + evt, fn);
  } else {
    oTarget["on" + sEvtType] = fn;
  }
}
```

# 加入收藏夹

```
function addFavorite(sURL, sTitle) {
  try {
    window.external.addFavorite(sURL, sTitle);
  } catch (e) {
    try {
      window.sidebar.addPanel(sTitle, sURL, "");
    } catch (e) {
      alert("加入收藏失败，请使用Ctrl+D进行添加");
    }
  }
}
```

# 提取页面代码中所有网址

```
var aa = document.documentElement.outerHTML
  .match(
    /(url\(|src=|href=)[\"\']*([^\"\'\(\)\<\>\[\] ]+)[\"\'\)]*|(http:\/\/[\w\-\.]+[^\"\'\(\)\<\>\[\] ]+)/gi
  )
  .join("\r\n")
  .replace(/^(src=|href=|url\()[\"\']*|[\"\'\>\) ]*$/gim, "");
alert(aa);
```

# 动态加载脚本文件

```
function appendscript(src, text, reload, charset) {
  var id = hash(src + text);
  if (!reload && in_array(id, evalscripts)) return;
  if (reload && $(id)) {
    $(id).parentNode.removeChild($(id));
  }

  evalscripts.push(id);
  var scriptNode = document.createElement("script");
  scriptNode.type = "text/javascript";
  scriptNode.id = id;
  scriptNode.charset = charset
    ? charset
    : BROWSER.firefox
    ? document.characterSet
    : document.charset;
  try {
    if (src) {
      scriptNode.src = src;
      scriptNode.onloadDone = false;
      scriptNode.onload = function() {
        scriptNode.onloadDone = true;
        JSLOADED[src] = 1;
      };
      scriptNode.onreadystatechange = function() {
        if (
          (scriptNode.readyState == "loaded" ||
            scriptNode.readyState == "complete") &&
          !scriptNode.onloadDone
        ) {
          scriptNode.onloadDone = true;
          JSLOADED[src] = 1;
        }
      };
    } else if (text) {
      scriptNode.text = text;
    }
    document.getElementsByTagName("head")[0].appendChild(scriptNode);
  } catch (e) {}
}
```

# 返回顶部的通用方法

```
function backTop(btnId) {
  var btn = document.getElementById(btnId);
  var d = document.documentElement;
  var b = document.body;
  window.onscroll = set;
  btn.style.display = "none";
  btn.onclick = function() {
    btn.style.display = "none";
    window.onscroll = null;
    this.timer = setInterval(function() {
      d.scrollTop -= Math.ceil((d.scrollTop + b.scrollTop) * 0.1);
      b.scrollTop -= Math.ceil((d.scrollTop + b.scrollTop) * 0.1);
      if (d.scrollTop + b.scrollTop == 0)
        clearInterval(btn.timer, (window.onscroll = set));
    }, 10);
  };
  function set() {
    btn.style.display = d.scrollTop + b.scrollTop > 100 ? "block" : "none";
  }
}
backTop("goTop");
```

# 实现 base64 解码

```
function base64_decode(data) {
  var b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
  var o1,
    o2,
    o3,
    h1,
    h2,
    h3,
    h4,
    bits,
    i = 0,
    ac = 0,
    dec = "",
    tmp_arr = [];
  if (!data) {
    return data;
  }
  data += "";
  do {
    h1 = b64.indexOf(data.charAt(i++));
    h2 = b64.indexOf(data.charAt(i++));
    h3 = b64.indexOf(data.charAt(i++));
    h4 = b64.indexOf(data.charAt(i++));
    bits = (h1 << 18) | (h2 << 12) | (h3 << 6) | h4;
    o1 = (bits >> 16) & 0xff;
    o2 = (bits >> 8) & 0xff;
    o3 = bits & 0xff;
    if (h3 == 64) {
      tmp_arr[ac++] = String.fromCharCode(o1);
    } else if (h4 == 64) {
      tmp_arr[ac++] = String.fromCharCode(o1, o2);
    } else {
      tmp_arr[ac++] = String.fromCharCode(o1, o2, o3);
    }
  } while (i < data.length);
  dec = tmp_arr.join("");
  dec = utf8_decode(dec);
  return dec;
}
```

# 确认是否是键盘有效输入值

```
function checkKey(iKey) {
  if (iKey == 32 || iKey == 229) {
    return true;
  } /*空格和异常*/
  if (iKey > 47 && iKey < 58) {
    return true;
  } /*数字*/
  if (iKey > 64 && iKey < 91) {
    return true;
  } /*字母*/
  if (iKey > 95 && iKey < 108) {
    return true;
  } /*数字键盘1*/
  if (iKey > 108 && iKey < 112) {
    return true;
  } /*数字键盘2*/
  if (iKey > 185 && iKey < 193) {
    return true;
  } /*符号1*/
  if (iKey > 218 && iKey < 223) {
    return true;
  } /*符号2*/
  return false;
}
```

# 全角半角转换

```
//iCase: 0全到半，1半到全，其他不转化
function chgCase(sStr, iCase) {
  if (
    typeof sStr != "string" ||
    sStr.length <= 0 ||
    !(iCase === 0 || iCase == 1)
  ) {
    return sStr;
  }
  var i,
    oRs = [],
    iCode;
  if (iCase) {
    /*半->全*/
    for (i = 0; i < sStr.length; i += 1) {
      iCode = sStr.charCodeAt(i);
      if (iCode == 32) {
        iCode = 12288;
      } else if (iCode < 127) {
        iCode += 65248;
      }
      oRs.push(String.fromCharCode(iCode));
    }
  } else {
    /*全->半*/
    for (i = 0; i < sStr.length; i += 1) {
      iCode = sStr.charCodeAt(i);
      if (iCode == 12288) {
        iCode = 32;
      } else if (iCode > 65280 && iCode < 65375) {
        iCode -= 65248;
      }
      oRs.push(String.fromCharCode(iCode));
    }
  }
  return oRs.join("");
}
```

# 版本对比

```
function compareVersion(v1, v2) {
  v1 = v1.split(".");
  v2 = v2.split(".");

  var len = Math.max(v1.length, v2.length);

  while (v1.length < len) {
    v1.push("0");
  }

  while (v2.length < len) {
    v2.push("0");
  }

  for (var i = 0; i < len; i++) {
    var num1 = parseInt(v1[i]);
    var num2 = parseInt(v2[i]);

    if (num1 > num2) {
      return 1;
    } else if (num1 < num2) {
      return -1;
    }
  }
  return 0;
}
```

# 压缩 CSS 样式代码

```
function compressCss(s) {
  //压缩代码
  s = s.replace(/\/\*(.|\n)*?\*\//g, ""); //删除注释
  s = s.replace(/\s*([\{\}\:\;\,])\s*/g, "$1");
  s = s.replace(/\,[\s\.\#\d]*\{/g, "{"); //容错处理
  s = s.replace(/;\s*;/g, ";"); //清除连续分号
  s = s.match(/^\s*(\S+(\s+\S+)*)\s*$/); //去掉首尾空白
  return s == null ? "" : s[1];
}
```

# 获取当前路径

```
var currentPageUrl = "";
if (typeof this.href === "undefined") {
  currentPageUrl = document.location.toString().toLowerCase();
} else {
  currentPageUrl = this.href.toString().toLowerCase();
}
```

# 字符串长度截取

```
function cutstr(str, len) {
    var temp,
        icount = 0,
        patrn = /[^\x00-\xff]/，
        strre = "";
    for (var i = 0; i < str.length; i++) {
        if (icount < len - 1) {
            temp = str.substr(i, 1);
                if (patrn.exec(temp) == null) {
                   icount = icount + 1
            } else {
                icount = icount + 2
            }
            strre += temp
            } else {
            break;
        }
    }
    return strre + "..."
}
```

# 时间日期格式转换

```
Date.prototype.format = function(formatStr) {
  var str = formatStr;
  var Week = ["日", "一", "二", "三", "四", "五", "六"];
  str = str.replace(/yyyy|YYYY/, this.getFullYear());
  str = str.replace(
    /yy|YY/,
    this.getYear() % 100 > 9
      ? (this.getYear() % 100).toString()
      : "0" + (this.getYear() % 100)
  );
  str = str.replace(
    /MM/,
    this.getMonth() + 1 > 9
      ? (this.getMonth() + 1).toString()
      : "0" + (this.getMonth() + 1)
  );
  str = str.replace(/M/g, this.getMonth() + 1);
  str = str.replace(/w|W/g, Week[this.getDay()]);
  str = str.replace(
    /dd|DD/,
    this.getDate() > 9 ? this.getDate().toString() : "0" + this.getDate()
  );
  str = str.replace(/d|D/g, this.getDate());
  str = str.replace(
    /hh|HH/,
    this.getHours() > 9 ? this.getHours().toString() : "0" + this.getHours()
  );
  str = str.replace(/h|H/g, this.getHours());
  str = str.replace(
    /mm/,
    this.getMinutes() > 9
      ? this.getMinutes().toString()
      : "0" + this.getMinutes()
  );
  str = str.replace(/m/g, this.getMinutes());
  str = str.replace(
    /ss|SS/,
    this.getSeconds() > 9
      ? this.getSeconds().toString()
      : "0" + this.getSeconds()
  );
  str = str.replace(/s|S/g, this.getSeconds());
  return str;
};

// 或
Date.prototype.format = function(format) {
  var o = {
    "M+": this.getMonth() + 1, //month
    "d+": this.getDate(), //day
    "h+": this.getHours(), //hour
    "m+": this.getMinutes(), //minute
    "s+": this.getSeconds(), //second
    "q+": Math.floor((this.getMonth() + 3) / 3), //quarter
    S: this.getMilliseconds() //millisecond
  };
  if (/(y+)/.test(format))
    format = format.replace(
      RegExp.$1,
      (this.getFullYear() + "").substr(4 - RegExp.$1.length)
    );
  for (var k in o) {
    if (new RegExp("(" + k + ")").test(format))
      format = format.replace(
        RegExp.$1,
        RegExp.$1.length == 1 ? o[k] : ("00" + o[k]).substr(("" + o[k]).length)
      );
  }
  return format;
};
alert(new Date().format("yyyy-MM-dd hh:mm:ss"));
```

# 跨浏览器删除事件

```
function delEvt(obj, evt, fn) {
  if (!obj) {
    return;
  }
  if (obj.addEventListener) {
    obj.addEventListener(evt, fn, false);
  } else if (oTarget.attachEvent) {
    obj.attachEvent("on" + evt, fn);
  } else {
    obj["on" + evt] = fn;
  }
}
```

# 判断是否以某个字符串结束

```
String.prototype.endWith = function(s) {
  var d = this.length - s.length;
  return d >= 0 && this.lastIndexOf(s) == d;
};
```

# 返回脚本内容

```
function evalscript(s) {
  if (s.indexOf("<script") == -1) return s;
  var p = /<script[^\>]*?>([^\x00]*?)<\/script>/gi;
  var arr = [];
  while ((arr = p.exec(s))) {
    var p1 = /<script[^\>]*?src=\"([^\>]*?)\"[^\>]*?(reload=\"1\")?(?:charset=\"([\w\-]+?)\")?><\/script>/i;
    var arr1 = [];
    arr1 = p1.exec(arr[0]);
    if (arr1) {
      appendscript(arr1[1], "", arr1[2], arr1[3]);
    } else {
      p1 = /<script(.*?)>([^\x00]+?)<\/script>/i;
      arr1 = p1.exec(arr[0]);
      appendscript("", arr1[2], arr1[1].indexOf("reload=") != -1);
    }
  }
  return s;
}
```

# 格式化 CSS 样式代码

```
function formatCss(s) {
  //格式化代码
  s = s.replace(/\s*([\{\}\:\;\,])\s*/g, "$1");
  s = s.replace(/;\s*;/g, ";"); //清除连续分号
  s = s.replace(/\,[\s\.\#\d]*{/g, "{");
  s = s.replace(/([^\s])\{([^\s])/g, "$1 {\n\t$2");
  s = s.replace(/([^\s])\}([^\n]*)/g, "$1\n}\n$2");
  s = s.replace(/([^\s]);([^\s\}])/g, "$1;\n\t$2");
  return s;
}
```

# 获取 cookie 值

```
function getCookie(name) {
  var arr = document.cookie.match(new RegExp("(^| )" + name + "=([^;]*)(;|$)"));
  if (arr != null) return unescape(arr[2]);
  return null;
}
```

# 获得 URL 中 GET 参数值

```
// 用法：如果地址是 test.htm?t1=1&t2=2&t3=3, 那么能取得：GET["t1"], GET["t2"], GET["t3"]
function getGet() {
  querystr = window.location.href.split("?");
  if (querystr[1]) {
    GETs = querystr[1].split("&");
    GET = [];
    for (i = 0; i < GETs.length; i++) {
      tmp_arr = GETs.split("=");
      key = tmp_arr[0];
      GET[key] = tmp_arr[1];
    }
  }
  return querystr[1];
}
```

# 获取移动设备初始化大小

```
function getInitZoom() {
  if (!this._initZoom) {
    var screenWidth = Math.min(screen.height, screen.width);
    if (this.isAndroidMobileDevice() && !this.isNewChromeOnAndroid()) {
      screenWidth = screenWidth / window.devicePixelRatio;
    }
    this._initZoom = screenWidth / document.body.offsetWidth;
  }
  return this._initZoom;
}
```

# 获取页面高度

```
function getPageHeight() {
  var g = document,
    a = g.body,
    f = g.documentElement,
    d = g.compatMode == "BackCompat" ? a : g.documentElement;
  return Math.max(f.scrollHeight, a.scrollHeight, d.clientHeight);
}
```

# 获取页面 scrollLeft

```
function getPageScrollLeft() {
  var a = document;
  return a.documentElement.scrollLeft || a.body.scrollLeft;
}
```

# 获取页面 scrollTop

```
function getPageScrollTop() {
  var a = document;
  return a.documentElement.scrollTop || a.body.scrollTop;
}
```

# 获取页面可视高度

```
function getPageViewHeight() {
  var d = document,
    a = d.compatMode == "BackCompat" ? d.body : d.documentElement;
  return a.clientHeight;
}
```

# 获取页面可视宽度

```
function getPageViewWidth() {
  var d = document,
    a = d.compatMode == "BackCompat" ? d.body : d.documentElement;
  return a.clientWidth;
}
```

# 获取页面宽度

```
function getPageWidth() {
  var g = document,
    a = g.body,
    f = g.documentElement,
    d = g.compatMode == "BackCompat" ? a : g.documentElement;
  return Math.max(f.scrollWidth, a.scrollWidth, d.clientWidth);
}
```

# 获取移动设备屏幕宽度

```
function getScreenWidth() {
  var smallerSide = Math.min(screen.width, screen.height);
  var fixViewPortsExperiment =
    rendererModel.runningExperiments.FixViewport ||
    rendererModel.runningExperiments.fixviewport;
  var fixViewPortsExperimentRunning =
    fixViewPortsExperiment && fixViewPortsExperiment.toLowerCase() === "new";
  if (fixViewPortsExperiment) {
    if (this.isAndroidMobileDevice() && !this.isNewChromeOnAndroid()) {
      smallerSide = smallerSide / window.devicePixelRatio;
    }
  }
  return smallerSide;
}
```

# 获取网页被卷去的位置

```
function getScrollXY() {
  return document.body.scrollTop
    ? {
        x: document.body.scrollLeft,
        y: document.body.scrollTop
      }
    : {
        x: document.documentElement.scrollLeft,
        y: document.documentElement.scrollTop
      };
}
```

# 获取 URL 上的参数

```
// 获取URL中的某参数值,不区分大小写
// 获取URL中的某参数值,不区分大小写,
// 默认是取'hash'里的参数，
// 如果传其他参数支持取‘search’中的参数
// @param {String} name 参数名称
export function getUrlParam(name, type = "hash") {
  let newName = name,
    reg = new RegExp("(^|&)" + newName + "=([^&]*)(&|$)", "i"),
    paramHash = window.location.hash.split("?")[1] || "",
    paramSearch = window.location.search.split("?")[1] || "",
    param;

  type === "hash" ? (param = paramHash) : (param = paramSearch);

  let result = param.match(reg);

  if (result != null) {
    return result[2].split("/")[0];
  }
  return null;
}
```

# 检验 URL 链接是否有效

```
function getUrlState(URL) {
  var xmlhttp = new ActiveXObject("microsoft.xmlhttp");
  xmlhttp.Open("GET", URL, false);
  try {
    xmlhttp.Send();
  } catch (e) {
  } finally {
    var result = xmlhttp.responseText;
    if (result) {
      if (xmlhttp.Status == 200) {
        return true;
      } else {
        return false;
      }
    } else {
      return false;
    }
  }
}
```

# 获取窗体可见范围的宽与高

```
function getViewSize() {
  var de = document.documentElement;
  var db = document.body;
  var viewW = de.clientWidth == 0 ? db.clientWidth : de.clientWidth;
  var viewH = de.clientHeight == 0 ? db.clientHeight : de.clientHeight;
  return Array(viewW, viewH);
}
```

# 获取移动设备最大化大小

```
function getZoom() {
  var screenWidth =
    Math.abs(window.orientation) === 90
      ? Math.max(screen.height, screen.width)
      : Math.min(screen.height, screen.width);
  if (this.isAndroidMobileDevice() && !this.isNewChromeOnAndroid()) {
    screenWidth = screenWidth / window.devicePixelRatio;
  }
  var FixViewPortsExperiment =
    rendererModel.runningExperiments.FixViewport ||
    rendererModel.runningExperiments.fixviewport;
  var FixViewPortsExperimentRunning =
    FixViewPortsExperiment &&
    (FixViewPortsExperiment === "New" || FixViewPortsExperiment === "new");
  if (FixViewPortsExperimentRunning) {
    return screenWidth / window.innerWidth;
  } else {
    return screenWidth / document.body.offsetWidth;
  }
}
```

# 判断是否安卓移动设备访问

```
function isAndroidMobileDevice() {
  return /android/i.test(navigator.userAgent.toLowerCase());
}
```

# 判断是否苹果移动设备访问

```
function isAppleMobileDevice() {
  return /iphone|ipod|ipad|Macintosh/i.test(navigator.userAgent.toLowerCase());
}
```

# 判断是否为数字类型

```
function isDigit(value) {
  var patrn = /^[0-9]*$/;
  if (patrn.exec(value) == null || value == "") {
    return false;
  } else {
    return true;
  }
}
```

# 是否是某类手机型号

```
// 用devicePixelRatio和分辨率判断
const isIphonex = () => {
  // X XS, XS Max, XR
  const xSeriesConfig = [
    {
      devicePixelRatio: 3,
      width: 375,
      height: 812
    },
    {
      devicePixelRatio: 3,
      width: 414,
      height: 896
    },
    {
      devicePixelRatio: 2,
      width: 414,
      height: 896
    }
  ];
  // h5
  if (typeof window !== "undefined" && window) {
    const isIOS = /iphone/gi.test(window.navigator.userAgent);
    if (!isIOS) return false;
    const { devicePixelRatio, screen } = window;
    const { width, height } = screen;
    return xSeriesConfig.some(
      item =>
        item.devicePixelRatio === devicePixelRatio &&
        item.width === width &&
        item.height === height
    );
  }
  return false;
};
```

# 判断是否移动设备

```
function isMobile() {
  if (typeof this._isMobile === "boolean") {
    return this._isMobile;
  }
  var screenWidth = this.getScreenWidth();
  var fixViewPortsExperiment =
    rendererModel.runningExperiments.FixViewport ||
    rendererModel.runningExperiments.fixviewport;
  var fixViewPortsExperimentRunning =
    fixViewPortsExperiment && fixViewPortsExperiment.toLowerCase() === "new";
  if (!fixViewPortsExperiment) {
    if (!this.isAppleMobileDevice()) {
      screenWidth = screenWidth / window.devicePixelRatio;
    }
  }
  var isMobileScreenSize = screenWidth < 600;
  var isMobileUserAgent = false;
  this._isMobile = isMobileScreenSize && this.isTouchScreen();
  return this._isMobile;
}
```

# 判断吗是否手机号码

```
function isMobileNumber(e) {
  var i =
      "134,135,136,137,138,139,150,151,152,157,158,159,187,188,147,182,183,184,178",
    n = "130,131,132,155,156,185,186,145,176",
    a = "133,153,180,181,189,177,173,170",
    o = e || "",
    r = o.substring(0, 3),
    d = o.substring(0, 4),
    s =
      !!/^1\d{10}$/.test(o) &&
      (n.indexOf(r) >= 0
        ? "联通"
        : a.indexOf(r) >= 0
        ? "电信"
        : "1349" == d
        ? "电信"
        : i.indexOf(r) >= 0
        ? "移动"
        : "未知");
  return s;
}
```

# 判断是否是移动设备访问

```
function isMobileUserAgent() {
  return /iphone|ipod|android.*mobile|windows.*phone|blackberry.*mobile/i.test(
    window.navigator.userAgent.toLowerCase()
  );
}
```

# 判断鼠标是否移出事件

```
function isMouseOut(e, handler) {
  if (e.type !== "mouseout") {
    return false;
  }
  var reltg = e.relatedTarget
    ? e.relatedTarget
    : e.type === "mouseout"
    ? e.toElement
    : e.fromElement;
  while (reltg && reltg !== handler) {
    reltg = reltg.parentNode;
  }
  return reltg !== handler;
}
```

# 判断是否 Touch 屏幕

```
function isTouchScreen() {
  return (
    "ontouchstart" in window ||
    (window.DocumentTouch && document instanceof DocumentTouch)
  );
}
```

# 判断是否为网址

```
function isURL(strUrl) {
  var regular = /^\b(((https?|ftp):\/\/)?[-a-z0-9]+(\.[-a-z0-9]+)*\.(?:com|edu|gov|int|mil|net|org|biz|info|name|museum|asia|coop|aero|[a-z][a-z]|((25[0-5])|(2[0-4]\d)|(1\d\d)|([1-9]\d)|\d))\b(\/[-a-z0-9_:\@&?=+,.!\/~%\$]*)?)$/i;
  if (regular.test(strUrl)) {
    return true;
  } else {
    return false;
  }
}
```

# 判断是否打开视窗

```
function isViewportOpen() {
  return !!document.getElementById("wixMobileViewport");
}
```

# 加载样式文件

```
function loadStyle(url) {
  try {
    document.createStyleSheet(url);
  } catch (e) {
    var cssLink = document.createElement("link");
    cssLink.rel = "stylesheet";
    cssLink.type = "text/css";
    cssLink.href = url;
    var head = document.getElementsByTagName("head")[0];
    head.appendChild(cssLink);
  }
}
```

# 替换地址栏

```
function locationReplace(url) {
  if (history.replaceState) {
    history.replaceState(null, document.title, url);
    history.go(0);
  } else {
    location.replace(url);
  }
}
```

# 解决 offsetX 兼容性问题

```
// 针对火狐不支持offsetX/Y
function getOffset(e) {
  var target = e.target, // 当前触发的目标对象
    eventCoord,
    pageCoord,
    offsetCoord;

  // 计算当前触发元素到文档的距离
  pageCoord = getPageCoord(target);

  // 计算光标到文档的距离
  eventCoord = {
    X: window.pageXOffset + e.clientX,
    Y: window.pageYOffset + e.clientY
  };

  // 相减获取光标到第一个定位的父元素的坐标
  offsetCoord = {
    X: eventCoord.X - pageCoord.X,
    Y: eventCoord.Y - pageCoord.Y
  };
  return offsetCoord;
}

function getPageCoord(element) {
  var coord = { X: 0, Y: 0 };
  // 计算从当前触发元素到根节点为止，
  // 各级 offsetParent 元素的 offsetLeft 或 offsetTop 值之和
  while (element) {
    coord.X += element.offsetLeft;
    coord.Y += element.offsetTop;
    element = element.offsetParent;
  }
  return coord;
}
```

# 打开一个窗体通用方法

```
function openWindow(url, windowName, width, height) {
  var x = parseInt(screen.width / 2.0) - width / 2.0;
  var y = parseInt(screen.height / 2.0) - height / 2.0;
  var isMSIE = navigator.appName == "Microsoft Internet Explorer";
  if (isMSIE) {
    var p = "resizable=1,location=no,scrollbars=no,width=";
    p = p + width;
    p = p + ",height=";
    p = p + height;
    p = p + ",left=";
    p = p + x;
    p = p + ",top=";
    p = p + y;
    retval = window.open(url, windowName, p);
  } else {
    var win = window.open(
      url,
      "ZyiisPopup",
      "top=" +
        y +
        ",left=" +
        x +
        ",scrollbars=" +
        scrollbars +
        ",dialog=yes,modal=yes,width=" +
        width +
        ",height=" +
        height +
        ",resizable=no"
    );
    eval("try { win.resizeTo(width, height); } catch(e) { }");
    win.focus();
  }
}
```

# 将键值对拼接成 URL 带参数

```
export default const fnParams2Url = obj=> {
      let aUrl = []
      let fnAdd = function(key, value) {
        return key + '=' + value
      }
      for (var k in obj) {
        aUrl.push(fnAdd(k, obj[k]))
      }
      return encodeURIComponent(aUrl.join('&'))
 }
```

# 去掉 url 前缀

```
function removeUrlPrefix(a) {
  a = a
    .replace(/：/g, ":")
    .replace(/．/g, ".")
    .replace(/／/g, "/");
  while (
    trim(a)
      .toLowerCase()
      .indexOf("http://") == 0
  ) {
    a = trim(a.replace(/http:\/\//i, ""));
  }
  return a;
}
```

# 替换全部

```
String.prototype.replaceAll = function(s1, s2) {
  return this.replace(new RegExp(s1, "gm"), s2);
};
```

# resize 的操作

```
(function() {
  var fn = function() {
    var w = document.documentElement
        ? document.documentElement.clientWidth
        : document.body.clientWidth,
      r = 1255,
      b = Element.extend(document.body),
      classname = b.className;
    if (w < r) {
      //当窗体的宽度小于1255的时候执行相应的操作
    } else {
      //当窗体的宽度大于1255的时候执行相应的操作
    }
  };
  if (window.addEventListener) {
    window.addEventListener("resize", function() {
      fn();
    });
  } else if (window.attachEvent) {
    window.attachEvent("onresize", function() {
      fn();
    });
  }
  fn();
})();
```

# 滚动到顶部

```
// 使用document.documentElement.scrollTop 或 document.body.scrollTop 获取到顶部的距离，从顶部
// 滚动一小部分距离。使用window.requestAnimationFrame()来滚动。
// @example
// scrollToTop();
function scrollToTop() {
  var c = document.documentElement.scrollTop || document.body.scrollTop;

  if (c > 0) {
    window.requestAnimationFrame(scrollToTop);
    window.scrollTo(0, c - c / 8);
  }
}
```

# 设置 cookie 值

```
function setCookie(name, value, Hours) {
  var d = new Date();
  var offset = 8;
  var utc = d.getTime() + d.getTimezoneOffset() * 60000;
  var nd = utc + 3600000 * offset;
  var exp = new Date(nd);
  exp.setTime(exp.getTime() + Hours * 60 * 60 * 1000);
  document.cookie =
    name +
    "=" +
    escape(value) +
    ";path=/;expires=" +
    exp.toGMTString() +
    ";domain=360doc.com;";
}
```

# 设为首页

```
function setHomepage() {
  if (document.all) {
    document.body.style.behavior = "url(#default#homepage)";
    document.body.setHomePage("http://w3cboy.com");
  } else if (window.sidebar) {
    if (window.netscape) {
      try {
        netscape.security.PrivilegeManager.enablePrivilege(
          "UniversalXPConnect"
        );
      } catch (e) {
        alert(
          "该操作被浏览器拒绝，如果想启用该功能，请在地址栏内输入 about:config,然后将项 signed.applets.codebase_principal_support 值该为true"
        );
      }
    }
    var prefs = Components.classes[
      "@mozilla.org/preferences-service;1"
    ].getService(Components.interfaces.nsIPrefBranch);
    prefs.setCharPref("browser.startup.homepage", "http://w3cboy.com");
  }
}
```

# 按字母排序，对每行进行数组排序

```
function setSort() {
  var text = K1.value
    .split(/[\r\n]/)
    .sort()
    .join("\r\n"); //顺序
  var test = K1.value
    .split(/[\r\n]/)
    .sort()
    .reverse()
    .join("\r\n"); //反序
  K1.value = K1.value != text ? text : test;
}
```

# 延时执行

```
// 比如 sleep(1000) 意味着等待1000毫秒，还可从 Promise、Generator、Async/Await 等角度实现。
// Promise
const sleep = time => {
  return new Promise(resolve => setTimeout(resolve, time));
};

sleep(1000).then(() => {
  console.log(1);
});

// Generator
function* sleepGenerator(time) {
  yield new Promise(function(resolve, reject) {
    setTimeout(resolve, time);
  });
}

sleepGenerator(1000)
  .next()
  .value.then(() => {
    console.log(1);
  });

//async
function sleep(time) {
  return new Promise(resolve => setTimeout(resolve, time));
}

async function output() {
  let out = await sleep(1000);
  console.log(1);
  return out;
}

output();

function sleep(callback, time) {
  if (typeof callback === "function") {
    setTimeout(callback, time);
  }
}

function output() {
  console.log(1);
}

sleep(output, 1000);
```

# 判断是否以某个字符串开头

```
String.prototype.startWith = function(s) {
  return this.indexOf(s) == 0;
};
```

# 清除脚本内容

```
function stripscript(s) {
  return s.replace(/<script.*?>.*?<\/script>/gi, "");
}
```

# 时间个性化输出功能

```
/*
1、< 60s, 显示为“刚刚”
2、>= 1min && < 60 min, 显示与当前时间差“XX分钟前”
3、>= 60min && < 1day, 显示与当前时间差“今天 XX:XX”
4、>= 1day && < 1year, 显示日期“XX月XX日 XX:XX”
5、>= 1year, 显示具体日期“XXXX年XX月XX日 XX:XX”
*/
function timeFormat(time) {
  var date = new Date(time),
    curDate = new Date(),
    year = date.getFullYear(),
    month = date.getMonth() + 10,
    day = date.getDate(),
    hour = date.getHours(),
    minute = date.getMinutes(),
    curYear = curDate.getFullYear(),
    curHour = curDate.getHours(),
    timeStr;

  if (year < curYear) {
    timeStr = year + "年" + month + "月" + day + "日 " + hour + ":" + minute;
  } else {
    var pastTime = curDate - date,
      pastH = pastTime / 3600000;

    if (pastH > curHour) {
      timeStr = month + "月" + day + "日 " + hour + ":" + minute;
    } else if (pastH >= 1) {
      timeStr = "今天 " + hour + ":" + minute + "分";
    } else {
      var pastM = curDate.getMinutes() - minute;
      if (pastM > 1) {
        timeStr = pastM + "分钟前";
      } else {
        timeStr = "刚刚";
      }
    }
  }
  return timeStr;
}
```

# 全角转换为半角函数

```
function toCDB(str) {
  var result = "";
  for (var i = 0; i < str.length; i++) {
    code = str.charCodeAt(i);
    if (code >= 65281 && code <= 65374) {
      result += String.fromCharCode(str.charCodeAt(i) - 65248);
    } else if (code == 12288) {
      result += String.fromCharCode(str.charCodeAt(i) - 12288 + 32);
    } else {
      result += str.charAt(i);
    }
  }
  return result;
}
```

# 半角转换为全角函数

```
function toDBC(str) {
  var result = "";
  for (var i = 0; i < str.length; i++) {
    code = str.charCodeAt(i);
    if (code >= 33 && code <= 126) {
      result += String.fromCharCode(str.charCodeAt(i) + 65248);
    } else if (code == 32) {
      result += String.fromCharCode(str.charCodeAt(i) + 12288 - 32);
    } else {
      result += str.charAt(i);
    }
  }
  return result;
}
```

# 金额大写转换函数

```
function transform(tranvalue) {
  try {
    var i = 1;
    var dw2 = new Array("", "万", "亿"); //大单位
    var dw1 = new Array("拾", "佰", "仟"); //小单位
    var dw = new Array(
      "零",
      "壹",
      "贰",
      "叁",
      "肆",
      "伍",
      "陆",
      "柒",
      "捌",
      "玖"
    );
    //整数部分用
    //以下是小写转换成大写显示在合计大写的文本框中
    //分离整数与小数
    var source = splits(tranvalue);
    var num = source[0];
    var dig = source[1];
    //转换整数部分
    var k1 = 0; //计小单位
    var k2 = 0; //计大单位
    var sum = 0;
    var str = "";
    var len = source[0].length; //整数的长度
    for (i = 1; i <= len; i++) {
      var n = source[0].charAt(len - i); //取得某个位数上的数字
      var bn = 0;
      if (len - i - 1 >= 0) {
        bn = source[0].charAt(len - i - 1); //取得某个位数前一位上的数字
      }
      sum = sum + Number(n);
      if (sum != 0) {
        str = dw[Number(n)].concat(str); //取得该数字对应的大写数字，并插入到str字符串的前面
        if (n == "0") sum = 0;
      }
      if (len - i - 1 >= 0) {
        //在数字范围内
        if (k1 != 3) {
          //加小单位
          if (bn != 0) {
            str = dw1[k1].concat(str);
          }
          k1++;
        } else {
          //不加小单位，加大单位
          k1 = 0;
          var temp = str.charAt(0);
          if (temp == "万" || temp == "亿")
            //若大单位前没有数字则舍去大单位
            str = str.substr(1, str.length - 1);
          str = dw2[k2].concat(str);
          sum = 0;
        }
      }
      if (k1 == 3) {
        //小单位到千则大单位进一
        k2++;
      }
    }
    //转换小数部分
    var strdig = "";
    if (dig != "") {
      var n = dig.charAt(0);
      if (n != 0) {
        strdig += dw[Number(n)] + "角"; //加数字
      }
      var n = dig.charAt(1);
      if (n != 0) {
        strdig += dw[Number(n)] + "分"; //加数字
      }
    }
    str += "元" + strdig;
  } catch (e) {
    return "0元";
  }
  return str;
}
//拆分整数与小数
function splits(tranvalue) {
  var value = new Array("", "");
  temp = tranvalue.split(".");
  for (var i = 0; i < temp.length; i++) {
    value = temp;
  }
  return value;
}
```

# 清除空格

```
String.prototype.trim = function() {
  var reExtraSpace = /^\s*(.*?)\s+$/;
  return this.replace(reExtraSpace, "$1");
};

// 清除左空格
function ltrim(s) {
  return s.replace(/^(\s*|　*)/, "");
}

// 清除右空格
function rtrim(s) {
  return s.replace(/(\s*|　*)$/, "");
}
```

# 随机数时间戳

```
function uniqueId() {
  var a = Math.random,
    b = parseInt;
  return (
    Number(new Date()).toString() + b(10 * a()) + b(10 * a()) + b(10 * a())
  );
}
```

# 实现 utf8 解码

```
function utf8_decode(str_data) {
  var tmp_arr = [],
    i = 0,
    ac = 0,
    c1 = 0,
    c2 = 0,
    c3 = 0;
  str_data += "";
  while (i < str_data.length) {
    c1 = str_data.charCodeAt(i);
    if (c1 < 128) {
      tmp_arr[ac++] = String.fromCharCode(c1);
      i++;
    } else if (c1 > 191 && c1 < 224) {
      c2 = str_data.charCodeAt(i + 1);
      tmp_arr[ac++] = String.fromCharCode(((c1 & 31) << 6) | (c2 & 63));
      i += 2;
    } else {
      c2 = str_data.charCodeAt(i + 1);
      c3 = str_data.charCodeAt(i + 2);
      tmp_arr[ac++] = String.fromCharCode(
        ((c1 & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63)
      );
      i += 3;
    }
  }
  return tmp_arr.join("");
}
```

以下是 Puxiao 投稿推荐的几个函数，用作常见的输入值校验和替换操作，主要针对中国大陆地区的校验规则：

# 校验是否为一个数字，以及该数字小数点位数是否与参数 floats 一致

校验规则：

- 若参数 floats 有值，则校验该数字小数点后的位数。
- 若参数 floats 没有值，则仅仅校验是否为数字。

```
function isNum(value,floats=null){
    let regexp = new RegExp(`^[1-9][0-9]*.[0-9]{${floats}}$|^0.[0-9]{${floats}}$`);
    return typeof value === 'number' && floats?regexp.test(String(value)):true;
}
function anysicIntLength(minLength,maxLength){
    let result_str = '';
    if(minLength){
        switch(maxLength){
            case undefined:
                result_str = result_str.concat(`{${minLength-1}}`);
                break;
            case null:
                result_str = result_str.concat(`{${minLength-1},}`);
                break;
            default:
                result_str = result_str.concat(`{${minLength-1},${maxLength-1}}`);
        }
    }else{
        result_str = result_str.concat('*');
    }

    return result_str;
}
```

# 校验是否为非零的正整数

```
function isInt(value,minLength=null,maxLength=undefined){
    if(!isNum(value)) return false;

    let regexp = new RegExp(`^-?[1-9][0-9]${anysicIntLength(minLength,maxLength)}$`);
    return regexp.test(value.toString());
}
```

# 校验是否为非零的正整数

```
function isPInt(value,minLength=null,maxLength=undefined) {
    if(!isNum(value)) return false;

    let regexp = new RegExp(`^[1-9][0-9]${anysicIntLength(minLength,maxLength)}$`);
    return regexp.test(value.toString());
}
```

# 校验是否为非零的负整数

```
function isNInt(value,minLength=null,maxLength=undefined){
    if(!isNum(value)) return false;
    let regexp = new RegExp(`^-[1-9][0-9]${anysicIntLength(minLength,maxLength)}$`);
    return regexp.test(value.toString());
}
```

# 校验整数是否在取值范围内

校验规则：

- minInt 为在取值范围中最小的整数
- maxInt 为在取值范围中最大的整数

```
function checkIntRange(value,minInt,maxInt=9007199254740991){
    return Boolean(isInt(value) && (Boolean(minInt!=undefined && minInt!=null)?value>=minInt:true) && (value<=maxInt));
}
```

# 校验是否为中国大陆手机号

```
function isTel(value) {
    return /^1[3,4,5,6,7,8,9][0-9]{9}$/.test(value.toString());
}
```

# 校验是否为中国大陆传真或固定电话号码

```
function isFax(str) {
    return /^([0-9]{3,4})?[0-9]{7,8}$|^([0-9]{3,4}-)?[0-9]{7,8}$/.test(str);
}
```

# 校验是否为邮箱地址

```
function isEmail(str) {
    return /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/.test(str);
}
```

# 校验是否为 QQ 号码

校验规则：

- 非 0 开头的 5 位-13 位整数

```
function isQQ(value) {
    return /^[1-9][0-9]{4,12}$/.test(value.toString());
}
```

# 校验是否为网址

校验规则：

- 以 https://、http://、ftp://、rtsp://、mms://开头、或者没有这些开头
- 可以没有 www 开头(或其他二级域名)，仅域名
- 网页地址中允许出现/%\*?@&等其他允许的符号

```
function isURL(str) {
    return /^(https:\/\/|http:\/\/|ftp:\/\/|rtsp:\/\/|mms:\/\/)?[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+[\/=\?%\-&_~`@[\]\':+!]*([^<>\"\"])*$/.test(str);
}
```

# 校验是否为不含端口号的 IP 地址

校验规则：

- IP 格式为 xxx.xxx.xxx.xxx，每一项数字取值范围为 0-255
- 除 0 以外其他数字不能以 0 开头，比如 02

```
function isIP(str) {
    return /^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$/.test(str);
}
```

# 校验是否为 IPv6 地址

校验规则：

- 支持 IPv6 正常格式
- 支持 IPv6 压缩格式

```
function isIPv6(str){
    return Boolean(str.match(/:/g)?str.match(/:/g).length<=7:false && /::/.test(str)?/^([\da-f]{1,4}(:|::)){1,6}[\da-f]{1,4}$/i.test(str):/^([\da-f]{1,4}:){7}[\da-f]{1,4}$/i.test(str));
}
```

# 校验是否为中国大陆第二代居民身份证

校验规则：

- 共 18 位，最后一位可为 X(大小写均可)
- 不能以 0 开头
- 出生年月日会进行校验：年份只能为 18/19/2\*开头，月份只能为 01-12，日只能为 01-31

```
function isIDCard(str){
    return /^[1-9][0-9]{5}(18|19|(2[0-9]))[0-9]{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)[0-9]{3}[0-9Xx]$/.test(str);
}
```

# 校验是否为中国大陆邮政编码

参数 value 为数字或字符串

校验规则：

- 共 6 位，且不能以 0 开头

```
function isPostCode(value){
    return /^[1-9][0-9]{5}$/.test(value.toString());
}
```

# 校验两个参数是否完全相同，包括类型

校验规则：

- 值相同，数据类型也相同

```
function same(firstValue,secondValue){
    return firstValue===secondValue;
}
```

# 校验字符的长度是否在规定的范围内

校验规则：

- minInt 为在取值范围中最小的长度
- maxInt 为在取值范围中最大的长度

```
function lengthRange(str,minLength,maxLength=9007199254740991) {
    return Boolean(str.length >= minLength && str.length <= maxLength);
}
```

# 校验字符是否以字母开头

校验规则：

- 必须以字母开头
- 开头的字母不区分大小写

```
function letterBegin(str){
    return /^[A-z]/.test(str);
}
```

# 校验字符是否为纯数字(整数)

校验规则：

- 字符全部为正整数(包含 0)
- 可以以 0 开头

```
function pureNum(str) {
    return /^[0-9]*$/.test(str);
}
function anysicPunctuation(str){
    if(!str) return null;
    let arr = str.split('').map(item => {
        return item = '\\' + item;
    });
    return arr.join('|');
}
function getPunctuation(str){
    return anysicPunctuation(str) || '\\~|\\`|\\!|\\@|\\#|\\$|\\%|\\^|\\&|\\*|\\(|\\)|\\-|\\_|\\+|\\=|\\||\\\|\\[|\\]|\\{|\\}|\\;|\\:|\\"|\\\'|\\,|\\<|\\.|\\>|\\/|\\?';
}
function getExcludePunctuation(str){
    let regexp = new RegExp(`[${anysicPunctuation(str)}]`,'g');
    return getPunctuation(' ~`!@#$%^&*()-_+=\[]{};:"\',<.>/?'.replace(regexp,''));
}
```

# 返回字符串构成种类(字母，数字，标点符号)的数量

LIP 缩写的由来：L(letter 字母) + I(uint 数字) + P(punctuation 标点符号)

参数 punctuation 的说明：

- punctuation 指可接受的标点符号集
- 若需自定义符号集，例如“仅包含中划线和下划线”，将参数设置为"-\_"即可
- 若不传值或默认为 null，则内部默认标点符号集为除空格外的其他英文标点符号：~`!@#$%^&\*()-\_+=[]{};:"',<.>/?

```
function getLIPTypes(str,punctuation=null){
    let p_regexp = new RegExp('['+getPunctuation(punctuation)+']');
    return /[A-z]/.test(str) + /[0-9]/.test(str) + p_regexp.test(str);
}
```

# 校验字符串构成的种类数量是否大于或等于参数 num 的值。通常用来校验用户设置的密码复杂程度。

校验规则：

- 参数 num 为需要构成的种类(字母、数字、标点符号)，该值只能是 1-3。
- 默认参数 num 的值为 1，即表示：至少包含字母，数字，标点符号中的 1 种
- 若参数 num 的值为 2，即表示：至少包含字母，数字，标点符号中的 2 种
- 若参数 num 的值为 3，即表示：必须同时包含字母，数字，标点符号
- 参数 punctuation 指可接受的标点符号集，具体设定可参考 getLIPTypes()方法中关于标点符号集的解释。

```
function pureLIP(str,num=1,punctuation=null){
    let regexp = new RegExp(`[^A-z0-9|${getPunctuation(punctuation)}]`);
    return Boolean(!regexp.test(str) && getLIPTypes(str,punctuation)>= num);
}
```

# 清除所有空格

```
function clearSpaces(str){
    return str.replace(/[ ]/g,'');
}
```

# 清除所有中文字符(包括中文标点符号)

```
function clearCNChars(str){
    return str.replace(/[\u4e00-\u9fa5]/g,'');
}
```

# 清除所有中文字符及空格

```
function clearCNCharsAndSpaces(str){
    return str.replace(/[\u4e00-\u9fa5 ]/g,'');
}
```

# 除保留标点符号集以外，清除其他所有英文的标点符号(含空格)

全部英文标点符号为：~`!@#$%^&\*()-\_+=[]{};:"',<.>/?

参数 excludePunctuation 指需要保留的标点符号集，例如若传递的值为'*'，即表示清除*以外的其他所有英文标点符号。

```
function clearPunctuation(str,excludePunctuation=null){
    let regexp = new RegExp(`[${getExcludePunctuation(excludePunctuation)}]`,'g');
    return str.replace(regexp,'');
}
```

# 校验是否包含空格

```
function haveSpace(str) {
    return /[ ]/.test(str);
}
```

# 校验是否包含中文字符(包括中文标点符号)

```
function haveCNChars(str){
    return /[\u4e00-\u9fa5]/.test(str);
}
```
