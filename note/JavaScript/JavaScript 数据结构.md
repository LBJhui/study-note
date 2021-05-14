# 什么是数据结构

数据结构是计算机存储、组织数据的方式，允许我们管理数据

例如：数组(Arrays)、对象(objects)、映射(Maps)、集合(Sets)

不同的场景需要不同的数据结构

- 有序列表数据允许重复——数组——Array
- 无序列表不允许重复——集合——Set
- 无序数据键值对形式——对象——Object
- 有序键值对可遍历数据——映射——Map

## JavaScript 数组

- 保留插入顺序
- 通过索引访问元素
- 可遍历(for 循环)
- 大小（长度）动态调整
- 允许重复
- 删除和查找元素比较耗费性能

```javascript
const names = ['LBJ', 'hui', 'LBJhui']

// 索引值从 0 开始
console.log(names[1])
console.log(names.length)

// for 循环遍历
for (const name of names) {
  console.log(name)
}

// 添加元素
name.push('James')
console.log(names.length)

// 查询元素
const huiIndex = names.findIndex((name) => name === 'hui')
console.log('huiIndex: ', huiIndex)

// 删除元素
names.splice(2, 1)
console.log(names)
```

## JavaScript 集合

- 无序（存储和读取的顺序可能不一样）
- 通过方法访问和获取元素
- 可遍历（for 循环）
- 大小（长度）动态调整
- 不允许重复（要求元素唯一）
- 删除和查找元素简单快捷

```javascript
const ids = new Set()

// 添加元素
ids.add('a')
ids.add(1)
ids.add('b')
ids.add(1)

// for 循环遍历
for (const id of ids) {
  console.log(id)
}

// 访问元素
ids.has('a')

// 删除元素
ids.delete('b')
```

## 数组 vs 集合

- 数组
  - 总是使用数组
  - 如果强调排序和元素重复，则必须使用
- 集合
  - 仅在顺序无关紧要且仅要求唯一值时可用
  - 与数组相比，可以简化数据访问（例如查找，删除）

## JavaScript 对象

- 无序的键值对数据
- 通过键（属性）访问元素
- 不可遍历（除了 for-in 循环）
- 键是唯一的，值不是
- 键必须是字符串，数字或符号
- 可以存储数据和“函数”（方法）

```javascript
const person = {
  name: 'LBjhui',
  age: 23,
  hobbies: ['NBA', 'Music'],
    greeting() {
    console.log('Hello, I am ' + this.name)
  }
}

console.log(person[0]) // undefined
person['name']
person.name

// 添加属性
person.sex = 'male'

// 删除属性
delete person.age

// 有方法，添加功能
person.greeting()
console.log(person)
```

## JavaScript 映射

- 有序的键值对数据
- 通过键访问元素
- 可遍历（使用 for 循环）
- 键是唯一的，值不是
- 键可是各种类型的值（包括对象、数组）
- 纯数据存储，针对数据访问进行了优化

```javascript
const resultData = new Map()

// 添加键值对
resultData.set('average', 1.6)
resultData.set('lastResult', null)

const person = {
  name: 'LBJhui',
  age: 18,
}
resultData.set(person, 1.24)

// for 循环遍历
for (const el of resultData) {
  console.log(el) // 数组 [key,value]
}

// key 相同情况
resultData.set('average', 23)

// 获取或访问值
resultData.get('lastResult')
resultData.lastResult // undefined

// 删除
resultData.delete('average')

// 删除 key 为对象的时候
resultData.delete(person) ✅
resultData.delete({
  name: 'LBJhui',
  age: 18,
})  ❎
```

## 对象 vs 映射

- 对象
  - 非常通用的构造和数据存储结构
  - 如果添加额外的功能则必须使用
- 映射
  - 专注于数据存储
  - 与对象相比，可以简化数据访问

## 弱集合 vs 弱映射

集合和映射的变体 ➡️ 值和键仅“弱引用” ➡️ 如果未在应用程序的其他任何地方使用，垃圾回收则可以删除值和键

# 自定义数据结构——链表

- 每一个元素都知道下一个元素
- 可以有效地调整大小并在列表的开头和结尾插入

```JavaScript
class LinkedList {
  constructor () {
    this.head = null // 链表中第一个节点
    this.tail = null // 链表中最后一个节点
  }

  // append 追加节点(末尾添加)
  append (value) {
    const newNode = { value: value, next: null }
    if (this.tail) {
      this.tail.next = newNode
    }
    this.tail = newNode
    if (!this.head) {
      this.head = newNode
    }
  }
}
const linkedList1 = new LinkedList()
```