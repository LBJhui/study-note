## 检查 JavaScript 变量是否为数字的几种方式

JavaScript 是一种动态类型的语言，这意味着解释器是在运行时确定变量类型的。这允许我们可以用同一变量中存储不同类型的数据。但是如果没有文档和保持一致性，在使用代码时，我们很有可能并不知道变量究竟是哪种类型。

当我们打算对数字进行操作时，如果对字符串或数组进行操作会带来奇怪的结果。在本文中，我们将研究可以帮我们确定所用的变量是否为数字的各种函数。

字符串形式的数字例如 `"100"` 不应该被处理，同时在 JavaScript 中 `NaN`，`Infinity` 和 `-Infinity` 之类的特殊值也都是数字，不过我们将忽略这些值。

根据这些要求，最好使用 `Number` 对象内置 `isFinite()` 函数。但是有时候我们也会使用其他函数，例如 `Number.isNaN()` 和 `typeof()` 等。

首先创建一些测试变量：

```javascript
const intVar = 2
const floatVar = 10.5
const stringVar = '4'
const nanVar = NaN
const infinityVar = Infinity
const nullVar = null
let undefinedVar
```

## 使用 Number.isFinite()函数

`Number.isFinite()` 用来函数检查变量是否为数字，但也用来检查其是否为某些特殊值。它在遇到 `NaN`, `Infinity` 或者 `-Infinity` 时会返回 `false`。

接下来在上面定义的变量上进行测试：

```javascript
> Number.isFinite(intVar)
true
> Number.isFinite(floatVar)
true
> Number.isFinite(stringVar)
false
> Number.isFinite(nanVar)
false
> Number.isFinite(infinityVar)
false
> Number.isFinite(nullVar)
false
> Number.isFinite(undefined)
false
```

结果令人满意。特殊的数字值以及所有非数字类型的变量都将会被忽略。如果想要检查某个变量是否为数字， `Number.isFinite()` 函数是最好的选择。

## 使用 Number.isNaN()函数

标准的 `Number` 对象具有 `isNaN()` 方法。用来判断传入的参数值是否为 `NaN`。由于我们要检查变量是否为数字，所以需要在检查中要使用非运算符 `!`。

现在看看通过非运算符加 `Number.isNaN()` 函数能否只过滤数字：

```javascript
> !Number.isNaN(intVar)
true
> !Number.isNaN(floatVar)
true
> !Number.isNaN(stringVar)
true # 判断错误
> !Number.isNaN(nanVar)
false
> !Number.isNaN(infinityVar)
true # 判断错误
> !Number.isNaN(nullVar)
true # 判断错误
> !Number.isNaN(undefinedVar)
true # 判断错误
```

这种方法相当宽松，因为它接受的值根本不是数字。这种方法最适合在你知道自己的值是数字并且要检查它是否为 `NaN` 值的情况下，并不适合常规数字的。

## 使用 typeof()函数

`typeof()` 函数是一个全局函数，它的参数可以接受变量或值，并返回其类型的字符串表示形式。JavaScript 共有 9 种类型：

- `undefined`
- `boolean`
- `number`
- `string`
- `bigint`
- `symbol`
- `object`
- `null` (`typeof()` 显示为对象)
- `function` (对象的一种特殊类型)

为了验证变量是否为数字，我们只需要检查 `typeof()` 返回的值是否为 `"number"`。让我们尝试一下测试变量：

```javascript
> typeof(intVar) == 'number'
true
> typeof(floatVar) == 'number'
true
> typeof(stringVar) == 'number'
false
> typeof(nanVar) == 'number'
true # 判断错误
> typeof(infinityVar) == 'number'
true # 判断错误
> typeof(nullVar) == 'number'
false
> typeof(undefined) == 'number'
false
```

`typeof()` 函数比 `Number.isNaN()` 好得多。它可以正确的判断 `null` 和 `undefined` 不是数字。但如果是 `NaN` 和 `Infinity`，它会返回 true。

尽管从技术角度上来说这是正确的，但 `NaN` 和 `Infinity` 是特殊的数字值，我们在大多数情况下都会忽略它们。

## 总结

本文研究了如何检查 JavaScript 中的变量是否为数字。

- 只有在我们知道自己的变量是一个数字，并且需要验证它是否为 `NaN` 时，`Number.isNaN()` 函数才适用。
- 如果你的代码需要处理 `NaN`，`Infinity` 或 `-Infinity` 及其他数字时，则 `typeof()` 函数是适用的。
- `Number.isFinite()` 方法能够处理特殊数字，并且最适合我们的要求。
