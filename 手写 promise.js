Promise.myAll = function (proms) {
  let res, rej
  const p = new Promise((resolve, reject) => {
    res = resolve
    rej = reject
  })
  let i = 0
  // proms 为可迭代对象
  const result = []
  for (const item of proms) {
    const index = i
    i++
    Promise.resolve(item).then((data) => {
      // 1.把成功的结果保存到数组
      result[index] = data
      // 2. 判断是不是所偶的 promise 都已成功
      i--
      if (i === 0) {
        res(result)
      }
    }, rej)
  }
  if (i === 0) {
    res([])
  }
  return p
}

Promise.myAll([1, 2, 3, 4, Promise.reject(5)])
  .then((data) => {
    console.log(data)
  })
  .catch((err) => {
    console.log(err)
  })

class MyPromise {
  constructor() {}
  static resolve() {}
  static reject() {}
  static all() {
    console.log('all')
  }
  static race() {}
}
