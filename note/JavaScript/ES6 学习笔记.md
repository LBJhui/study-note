# let 和 const

`let`

1. 变量不能重复声明
2. 块级作用域
3. 不存在变量提升
4. 不影响作用域链

`const`

1. 一定要赋初始值
2. 一般常量使用大写（潜规则）
3. 常量的值不能修改
4. 块级作用域
5. 对于数据和对象的元素修改，不算做对常量的修改，不会报错

详细请参考：[let 和 const](https://www.jianshu.com/p/3931348bcf37)

# 变量的结构赋值

ES6 允许按照一定模式从数组和对象中提取值，对变量进行赋值，这被称为解构赋值

1. 数组的解构
2. 对象的解构

# 模版字符串

ES6 引入新的声明字符串的方式` [``]`

1. 声明
2. 内容中可以直接出现换行符
3. 变量拼接

# 对象的简化写法

ES6 允许在大括号里面，直接写入变量和函数，作为对象的属性和方法

```javascript
let name = 'LBJhui'
let change = () => {
  console.log('湖人总冠军')
}

const NBA = {
  name,
  change,
  improve() {
    console.log('湖人总冠军')
  },
}
```

# 箭头函数

1. this 是静态的。 this 始终指向函数声明时所在作用域下的 this 的值
2. 不能作为构造实例化对象

```javascript
let Person = (name, age) => {
  this.name = name
  this.age = age
}

let me = new Person('xiao', 30)
console.log(me) // Person is not a constructor
```

3. 不能使用 arguments 变量
4. 箭头函数的简写
   1. 省略小括号，当形参有且只有一个的时候
   2. 省略花括号，当代码体只有一条语句的时候，此时 return 必须省略，而且语句的执行结果就是函数的返回值

箭头函数适合与 this 无关的回调。定时器，数组的方法回顾

箭头函数不适合与 this 有关的回调。时间回调，对象的方法

# 函数形参默认值设置

ES6 允许给函数参数赋值初始值

1. 形参初始值，具有默认值的参数，一般位置要靠后（潜规则）
2. 与解构赋值结合

# rest 参数

ES6 引入 rest 参数，用于获取函数的实参，用来代替 arguments

# 扩展运算符

[ ... ] 扩展运算符能将 [数组] 转换为逗号分隔的 [参数序列]

1. 数组的合并

```javascript
const arr1 = [1, 2]
const arr2 = [3, 4]

const arr = [...arr1, ...arr2]
```

2. 数组的克隆

```javascript
const name = ['L', 'B', 'J', 'h', 'u', 'i']
const newName = [...name]
```

3. 将伪数组转为真正的数组

# Symbol

ES6 引入一种新的原始数据类型 Symbol，表示独一无二的值。它是 JavaScript 语言的第七种数据类型，是一种类似于字符串的数据类型

Symbol 特点

1. Symbol 的值是唯一的，用来解决命名冲突的问题
2. Symbol 值不能与其他数据进行运算
3. Symbol 定义的对象属性不能使用`for...in`循环遍历，但是可以使用`Reflect.ownKeys` 来获取对象的所有键名

```javascript
// 创建Symbol
let s = Symbol()
console.log(s, typeof s)
let s2 = Symbol('LBJhui')
let s3 = Symbol('LBJhui')
console.log(s2 === s3) // false
let s4 = Symbol.for('LBJhui')
let s5 = Symbol.for('LBJhui')
console.log(s4 === s5) // true
```

不能与其他数据进行运算

## Symbol 的内置值

|    Symbol.hasInstance     | 当其他对象使用 instance 运算符，判断是否为该对象的实例时，会调用这个方法                                     |
| :-----------------------: | ------------------------------------------------------------------------------------------------------------ |
| Symbol.isConcatSpreadable | 对象的 Symbol.isConcatSpreadable 属性等于是一个布尔值，表示该对象用于 Array.prototype.concat()，是否可以展开 |
|    Symbol.unscopables     | 该对象指定了使用 with 关键字时，哪些属性会被 with 环境排除                                                   |
|       Symbol.match        | 当执行 str.match(myObject) 时，如果该属性存在，会调用它，返回该方法的返回值                                  |
|      Symbol.replace       | 当该对象被 str.replace(myObject) 方法调用时，会返回该方法的返回值                                            |
|       Symbol.search       | 当该对象被 str.search(myObject) 方法调用时，会返回该方法的返回值                                             |
|       Symbol.split        | 当该对象被 str.split(myObject) 方法调用时，会返回该对象的返回值                                              |
|      Symbol.iterator      | 对象进行 for...of 循环时，会调用 Symbol.iterator 方法，返回该对象的默认遍历器                                |
|    Symbol.toPrimitive     | 该对象被转为原始类型的值时，会调用这个方法，返回该对象对应的原始类型值                                       |
|    Symbol.toStringTag     | 在该对象上面调用 toString 方法时，返回该方法的返回值                                                         |
|      Symbol.species       | 创建衍生对象时，会使用该属性                                                                                 |

# 迭代器（iterator）

遍历器（iterator）就是一种机制。它是一种接口，为各种不同的数据结构提供统一的访问机制。任何数据结构只要部署 iterator 接口，就可以完成遍历操作。

1. ES6 创造了一种新的遍历命令 for...of 循环，Iterator 接口主要供 for...of 循环

2. 原生具备 iterator 接口的数据（可用 for of 遍历）

   a. Array

   b. Arguments

   c. Set

   d. Map

   e. String

   f. TypedArray

   g. NodeList

3. 工作原理

   1. 创建一个指针对象，指向当前数据结构的起始位置
   2. 第一次调用对象的 next 方法，指针自动指向数据结构的第一个成员
   3. 接下来不断调用 next 方法，指针一直往后移动，直到指向最后一个成员
   4. 每调用 next 方法返回一个包含 value 和 done 属性的对象

**注：需要自定义遍历数据的时候，要想到迭代器**

# 生成器

# Promise

# Set

# Map

# class
