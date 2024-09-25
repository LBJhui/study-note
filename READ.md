```javascript
Number(undefined) // NaN
Number('   123    ') // 123
Number('12 3') // NaN (only whitespace from the start and end are removed)
NaN ** 0 // 1

typeof null // object

let numbers = {
  0: 0
}

console.log(numbers."0"); // error
console.log(numbers[0]); // 0
```

###### 12. What's the result?

```javascript
isNaN('this is a string not a NaN value')
Number.isNaN('this is a string not a NaN value')
```

<details><summary><b>Answer</b></summary>
<p>

true, false

isNaN tries to coerce the value into a Number before checking if it's a NaN value. This issue has been fixed in Number.isNaN().

</p>
</details>

###### 16. What's the result?

```javascript
let fruit = prompt('Which fruit to buy?', 'apple')

let bag = {
  [fruit]: 5,
}
```

<details><summary><b>Answer</b></summary>
<p>
  That’s called computed properties. The name of the property is taken from the variable fruit.
</p>
</details>

###### 23. What's the result?

```javascript
function BigUser() {
  this.name = 'John'

  return { name: 'Godzilla' }
}

function SmallUser() {
  this.name = 'John'

  return 'Rick'
}

console.log(new BigUser().name)
console.log(new SmallUser().name)
```

<details><summary><b>Answer</b></summary>
<p>

1. Godzilla, 2. Johm`

If return is called with an object, then the object is returned instead of this
If return is called with a primitive, it’s ignored.

</p>
</details>

###### 24. Is the constructor call valid?

```javascript
function User() {
  this.name = 'Admin'
}
let user = new User()
```

<details><summary><b>Answer</b></summary>
<p>
  We can omit parentheses after new, if it has no arguments. Omitting parentheses here is not considered a “good style”, but the syntax is permitted by specification.
</p>
</details>
