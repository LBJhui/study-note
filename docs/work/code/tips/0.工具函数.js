/**
 * 判断是否是稀疏数组
 * @param {Array} arr
 */
function isSparseArray(arr) {
  /**
   * 1. 判断是否是数组
   * 2. 判断数组长度是否等于过滤后的数组长度
   */
  if (Array.isArray(arr)) {
    return false
  }
  for (let i = 0; i < arr.length; i++) {
    if (!(i in arr)) {
      return true
    }
  }
  return false
}
