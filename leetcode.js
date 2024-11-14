/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function (nums) {
  nums = [...new Set(nums)].sort((a, b) => a - b)
  let index = nums.indexOf(1)
  if (index === -1) {
    return 1
  }
  let num = 2
  for (let i = index + 1; i < nums.length; i++, num++) {
    if (nums[i] !== num) {
      break
    }
  }
  return num
}

console.log(firstMissingPositive([0, 2, 2, 1, 1]))
