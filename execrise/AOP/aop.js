// function test1 () {
//   console.log('--------------')
//   console.log('1')
//   console.log('++++++++++++++')
// }

// function test2 () {
//   console.log('--------------')
//   console.log('2')
//   console.log('++++++++++++++')
// }

// function test3 () {
//   console.log('--------------')
//   console.log('3')
//   console.log('++++++++++++++')
// }

// test1()
// test2()
// test3()

Function.prototype.before = function (cb) {
  var __self__ = this

  return function () {
    cb.apply(__self__, arguments)
    return __self__.apply(__self__, arguments)
  }
}

Function.prototype.after = function (cb) {
  var __self__ = this

  return function () {
    var result = __self__.apply(__self__, arguments)
    cb.apply(__self__, arguments)

    return result
  }
}

function test1 () {
  console.log('--------------') // before
  console.log('1')
  console.log('++++++++++++++') // after
}

const res = test1.before(() => {
  console.log('--------------')
}).after(() => {
  // console.log('++++++++++++++')
  return 'AOP'
})()

console.log(res)