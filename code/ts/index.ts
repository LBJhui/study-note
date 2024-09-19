interface Person {
  name: string
  age: string
}

// keyof
function print(obj: Person) {
  let key: keyof Person
  for (key in obj) {
    // ✅
    console.log(key, obj[key].toUpperCase())
  }
}

// Object.keys()
function print(obj: Person) {
  Object.keys(obj).forEach((k) => {
    // ✅
    console.log(k, obj[k as keyof Person].toUpperCase())
  })
}
