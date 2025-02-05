# JavaScrip 数组 API 的时间复杂度

## entries()

`entries()` 方法返回一个新的数组迭代器对象，该对象包含数组中每个索引的键/值对，时间复杂度为 O(1)。

```javascript
const array1 = ['a', 'b', 'c']

const iterator1 = array1.entries()

console.log(iterator1.next().value) // [ 0, 'a' ]

console.log(iterator1.next().value) // [ 1, 'b' ]
```

## values()

`values()` 方法返回一个新的数组迭代器对象，该对象迭代数组中每个元素的值，时间复杂度为 O(1)。

```javascript
const array1 = ['a', 'b', 'c']
const iterator = array1.values()

for (const value of iterator) {
  console.log(value) // 'a', 'b', 'c'
}
```

## isArray()

`Array.isArray()` 静态方法用于确定传递的值是否是一个数组，时间复杂度为 O(1)。

```javascript
console.log(Array.isArray([1, 3, 5])) // true
console.log(Array.isArray('[]')) // false
console.log(Array.isArray(new Array(5))) // true
console.log(Array.isArray(new Int16Array([15, 33]))) // false
```

## pop()

`pop()` 方法从数组中删除最后一个元素，并返回该元素的值。此方法会更改数组的长度。时间复杂度为 O(1)。

## push()

`push()` 方法将指定的元素添加到数组的末尾，并返回新的数组长度。时间复杂度为 O(1)。

## sort()

`sort()` 方法就地对数组的元素进行排序，并返回对相同数组的引用。默认排序是将元素转换为字符串，然后按照它们的 UTF-16 码元值升序排序。时间复杂度为 O(n log n)。通常使用经典的快速排序（quicksort）算法。

如果想要不改变原数组的排序方法，可以使用 `toSorted()`。

## join()

`join()` 时间复杂度为 O(n)。

## keys()

`keys()` 方法返回一个新的数组迭代器对象，其中包含数组中每个索引的键。时间复杂度为 O(n)。

```javascript
const array1 = ['a', 'b', 'c']
const iterator = array1.keys()

for (const key of iterator) {
  console.log(key) // 0, 1, 2
}
```

## concat()

`concat()` 方法用于合并两个或多个数组。此方法不会更改现有数组，而是返回一个新数组。时间复杂度 O(n)。

```javascript
const array1 = ['a', 'b', 'c']
const array2 = ['d', 'e', 'f']
const array3 = array1.concat(array2)

console.log(array3) // [ 'a', 'b', 'c', 'd', 'e', 'f' ]
```

## copyWithin()

`copyWithin()` 方法浅复制数组的一部分到同一数组中的另一个位置，并返回它，不会改变原数组的长度。时间复杂度为 O(n)。

```javascript
copyWithin(target)
copyWithin(target, start)
copyWithin(target, start, end)

const array1 = ['a', 'b', 'c', 'd', 'e']
// Copy to index 0 the element at index 3
console.log(array1.copyWithin(0, 3, 4)) // [ 'd', 'b', 'c', 'd', 'e' ]
// Copy to index 1 all elements from index 3 to the end
console.log(array1.copyWithin(1, 3)) // [ 'd', 'd', 'e', 'd', 'e' ]
```

**target**

序列开始替换的目标位置，以 0 为起始的下标表示，且将被转换为整数

- 负索引将从数组末尾开始计数——如果 target < 0，则实际是 target + array.length。
- 如果 target < -array.length，则使用 0。
- 如果 target >= array.length，则不会拷贝任何内容。
- 如果 target 位于 start 之后，则复制只会持续到 array.length 结束（换句话说，copyWithin() 永远不会扩展数组）。

**start** 可选

要复制的元素序列的起始位置，以 0 为起始的下标表示，且将被转换为整数

- 负索引将从数组末尾开始计数——如果 start < 0，则实际是 start + array.length。
- 如果省略 start 或 start < -array.length，则默认为 0。
- 如果 start >= array.length，则不会拷贝任何内容。

**end** 可选

要复制的元素序列的结束位置，以 0 为起始的下标表示，且将被转换为整数。copyWithin 将会拷贝到该位置，但不包括 end 这个位置的元素。

- 负索引将从数组末尾开始计数——如果 end < 0，则实际是 end + array.length。
- 如果 end < -array.length，则使用 0。
- 如果省略 end 或 end >= array.length，则默认为 array.length，这将导致直到数组末尾的所有元素都被复制。
- 如果 end 位于 start 之前，则不会拷贝任何内容。

## every()

every() 方法测试一个数组内的所有元素是否都能通过指定函数的测试。它返回一个布尔值。时间复杂度为 O(n)。
fill() 时间复杂度为 O(n)
filter() 时间复杂度为 O(n)
find() 时间复杂度为 O(n)
findIndex() 时间复杂度为 O(n)
findLast() 时间复杂度为 O(n)
findLastIndex 时间复杂度为 O(n)
flat() 时间复杂度是 O(n)

## some()

`some()` 方法测试数组中是否至少有一个元素通过了由提供的函数实现的测试。如果在数组中找到一个元素使得提供的函数返回 true，则返回 true；否则返回 false。它不会修改数组。时间复杂度为 O(n)。

## forEach()

`forEach()` 方法对数组的每个元素执行一次给定的函数。时间复杂度是 O(n)。

```javascript
forEach(callbackFn)
forEach(callbackFn, thisArg)
```

**callbackFn**

为数组中每个元素执行的函数。并会丢弃它的返回值。该函数被调用时将传入以下参数：

> **element** 数组中正在处理的当前元素。
>
> **index** 数组中正在处理的当前元素的索引。
>
> **array** 调用了 forEach() 的数组本身。

**thisArg** 可选

执行 callbackFn 时用作 this 的值。

`forEach()` 不会改变其调用的数组，但是，作为 `callbackFn` 的函数可以更改数组。请注意，在第一次调用 `callbackFn` 之前，数组的长度已经被保存。因此：

- 当调用 `forEach()` 时，`callbackFn` 不会访问超出数组初始长度的任何元素。
- 已经访问过的索引的更改不会导致 `callbackFn` 再次调用它们。
- 如果 `callbackFn` 更改了数组中已经存在但尚未访问的元素，则传递给 `callbackFn` 的值将是在访问该元素时的值。已经被删除的元素不会被访问。

除非抛出异常，否则没有办法停止或中断 `forEach()` 循环。

## map()

`map()` 方法创建一个新数组，这个新数组由原数组中的每个元素都调用一次提供的函数后的返回值组成。时间复杂度为 O(n)。

```javascript
map(callbackFn)
map(callbackFn, thisArg)
```

**callbackFn**

为数组中的每个元素执行的函数。它的返回值作为一个元素被添加为新数组中。该函数被调用时将传入以下参数：

> **element** 数组中当前正在处理的元素。
>
> **index** 正在处理的元素在数组中的索引。
>
> **array** 调用了 map() 的数组本身。

**thisArg** 可选

执行 callbackFn 时用作 this 的值。

## reduce()

`reduce()` 时间复杂度为 O(n)。

## reduceRight()

`reduceRight()` 方法对累加器（accumulator）和数组的每个值（按从右到左的顺序）应用一个函数，并使其成为单个值。时间复杂度为 O(n)。

## shift()

`shift()` 方法从数组中删除第一个元素，并返回该元素的值。此方法更改数组的长度。时间复杂度为 O(n)。

**返回值** 从数组中删除的元素；如果数组为空则返回 undefined。

## unshift()

`unshift()` 方法将指定元素添加到数组的开头，并返回数组的新长度。时间复杂度为 O(n)。

## slice()

`slice()` 方法返回一个新的数组对象，这一对象是一个由 start 和 end 决定的原数组的浅拷贝（包括 start，不包括 end），其中 start 和 end 代表了数组元素的索引。原始数组不会被改变。时间复杂度为 O(n)。

**start** 可选

提取起始处的索引（从 0 开始），会转换为整数。

- 如果索引是负数，则从数组末尾开始计算——如果 start < 0，则使用 start + array.length。
- 如果 start < -array.length 或者省略了 start，则使用 0。
- 如果 start >= array.length，则不提取任何元素。

**end** 可选

提取终止处的索引（从 0 开始），会转换为整数。slice() 会提取到但不包括 end 的位置。

- 如果索引是负数，则从数组末尾开始计算——如果 end < 0，则使用 end + array.length。
- 如果 end < -array.length，则使用 0。
- 如果 end >= array.length 或者省略了 end，则使用 array.length，提取所有元素直到末尾。
- 如果 end 在规范化后小于或等于 start，则不提取任何元素。

`slice()` 方法会保留空槽。如果被切片的部分是稀疏的，则返回的数组也是稀疏的。

## toString()

`toString()` 方法返回一个字符串，表示指定的数组及其元素。时间复杂度为 O(n)。

## splice()

`splice()` 方法就地移除或者替换已存在的元素和/或添加新的元素。时间复杂度为 O(n)。

要创建一个删除和/或替换部分内容而不改变原数组的新数组，请使用 `toSpliced()`。要访问数组的一部分而不修改它，参见 `slice()`。

```javascript
splice(start)
splice(start, deleteCount)
splice(start, deleteCount, item1)
splice(start, deleteCount, item1, item2)
splice(start, deleteCount, item1, item2, /* …, */ itemN)

const months = ['Jan', 'March', 'April', 'June']
months.splice(1, 0, 'Feb')
// Inserts at index 1
console.log(months) // [ 'Jan', 'Feb', 'March', 'April', 'June' ]

months.splice(4, 1, 'May')
// Replaces 1 element at index 4
console.log(months) // [ 'Jan', 'Feb', 'March', 'April', 'May' ]
```

**返回值**

一个包含了删除的元素的数组。如果只移除一个元素，则返回一个元素的数组。如果没有删除任何元素，则返回一个空数组。

## toLocaleString()

`toLocaleString()` 方法返回一个字符串，表示数组中的所有元素。每个元素通过调用它们自己的 toLocaleString 方法转换为字符串，并且使用特定于语言环境的字符串（例如逗号“,”）分隔开。时间复杂度为 O(n)。

```javascript
toLocaleString()
toLocaleString(locales)
toLocaleString(locales, options)

const array1 = [1, 'a', new Date('21 Dec 1997 14:12:00 UTC')]
const localeString = array1.toLocaleString('en', { timeZone: 'UTC' })

console.log(localeString) // '1,a,12/21/1997, 2:12:00 PM'
```

如果一个元素是 `undefined`、`null`，它会被转换为空字符串，而不是 "null" 或者 "undefined"。

当用于稀疏数组时，`toLocaleString()` 方法迭代时会把空槽当作 `undefined` 一样处理它。

`toLocaleString()` 方法是通用的。它只期望 `this` 值具有 `length` 属性和整数键属性。

## from()

`Array.from()` 静态方法从可迭代或类数组对象创建一个新的浅拷贝的数组实例。时间复杂度为 O(n)。

```javascript
Array.from(arrayLike)
Array.from(arrayLike, mapFn)
Array.from(arrayLike, mapFn, thisArg)
```

**mapFn** 可选

调用数组每个元素的函数。如果提供，每个将要添加到数组中的值首先会传递给该函数，然后将 mapFn 的返回值增加到数组中。使用以下参数调用该函数：

> **element** 数组当前正在处理的元素。
>
> **index** 数组当前正在处理的元素的索引。

**thisArg** 可选

执行 mapFn 时用作 this 的值。

`Array.from()` 绝不会创建稀疏数组。如果 `arrayLike` 对象缺少一些索引属性，那么这些属性在新数组中将是 `undefined`。

## includes()

`includes()` 方法用来判断一个数组是否包含一个指定的值，根据情况，如果包含则返回 true，否则返回 false。时间复杂度为 O(n)。

```javascript
includes(searchElement)
includes(searchElement, fromIndex)
```

**fromIndex** 可选

开始搜索的索引（从零开始），会转换为整数。

- 负索引从数组末尾开始计数——如果 fromIndex < 0，那么实际使用的是 fromIndex + array.length。然而在这种情况下，数组仍然从前往后进行搜索。
- 如果 fromIndex < -array.length 或者省略 fromIndex，则使用 0，这将导致整个数组被搜索。
- 如果 fromIndex >= array.length，则不会搜索数组并返回 false。

**描述**

`includes()` 方法使用零值相等(零值相等与严格相等的区别在于其将 `NaN` 视作是相等的，与同值相等的区别在于其将 -0 和 0 视作相等的。)算法将 `searchElement` 与数组中的元素进行比较。0 值都被认为是相等的，不管符号是什么。（即 -0 等于 0），但 false 不被认为与 0 相同。`NaN` 可以被正确搜索到。

当在稀疏数组上使用时，`includes()` 方法迭代空槽，就像它们的值是 `undefined` 一样。

`includes()` 方法是通用的。它只期望 this 值具有 length 属性和整数键属性。

## indexOf()

`indexOf()` 方法返回数组中第一次出现给定元素的下标，如果不存在则返回 -1。时间复杂度为 O(n)。

```javascript
indexOf(searchElement)
indexOf(searchElement, fromIndex)

const beasts = ['ant', 'bison', 'camel', 'duck', 'bison']

console.log(beasts.indexOf('bison')) // 1
// Start from index 2
console.log(beasts.indexOf('bison', 2)) // 4
console.log(beasts.indexOf('giraffe')) // -1
```

**fromIndex** 可选

开始搜索的索引（从零开始），会转换为整数。

- 负索引从数组末尾开始计数——如果 frommindex < 0，使用 frommindex + array.length。注意，在这种情况下，仍然从前到后搜索数组。
- 如果 fromIndex < -array.length 或者省略了 fromIndex ，将使用 0，而导致整个数组被搜索。
- 如果 fromIndex >= array.length，数组不会继续搜索并返回 -1。

**描述**

`indexOf()` 使用严格相等（与 === 运算符使用的算法相同）将 `searchElement` 与数组中的元素进行比较。`NaN` 值永远不会被比较为相等，因此当 `searchElement` 为 `NaN` 时 `indexOf()` 总是返回 -1。

`indexOf()` 方法会跳过稀疏数组中的空槽。

`indexOf()` 方法是通用的。它只期望 this 值具有 length 属性和整数键属性。

## lastIndexOf()

`lastIndexOf()` 方法返回数组中给定元素最后一次出现的索引，如果不存在则返回 -1。该方法从 fromIndex 开始向前搜索数组。 时间复杂度为 O(n)。

```javascript
lastIndexOf(searchElement)
lastIndexOf(searchElement, fromIndex)

const animals = ['Dodo', 'Tiger', 'Penguin', 'Dodo']

console.log(animals.lastIndexOf('Dodo')) // 3
console.log(animals.lastIndexOf('Tiger')) // 1
```

**fromIndex** 可选

以 0 起始的索引，表明反向搜索的起始位置，会被转换为整数。

- 如果 fromIndex < 0，则从数组末尾开始倒数计数——即使用 fromIndex + array.length 的值。
- 如果 fromIndex < -array.length，则不搜索数组并返回 -1。从概念上讲，你可以把它想象成从数组开始之前不存在的位置开始反向搜索，这条路径上没有任何数组元素，因此 searchElement 永远不会被找到。
- 如果 fromIndex >= array.length 或者省略了 fromIndex，则使用 array.length - 1，这会导致搜索整个数组。可以将其理解为从数组尾部之后不存在的位置开始向前搜索。最终会访问到数组最后一个元素，并继续向前开始实际搜索数组元素。

**描述**

`lastIndexOf` 使用严格相等（与 === 运算符使用的算法相同）比较 `searchElement` 和数组中的元素。`NaN` 值永远不会被比较为相等，因此当 `searchElement` 为 `NaN` 时 `lastIndexOf()` 总是返回 -1。

`lastIndexOf()` 方法会跳过稀疏数组中的空槽。

`lastIndexOf()` 方法是通用的。它只期望 this 值具有 length 属性和整数键属性。
