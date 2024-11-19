/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function (n) {
  for (let i = 0; i < 32; i++) {
    if (2 ** i === n) {
      return true
    }
  }
  return false
}

console.log(isPowerOfTwo(4))
