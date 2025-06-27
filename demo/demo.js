const arr1 = [33, 22, 55, 33, 11, 33, 5]
const arr2 = [22, 55, 77, 88, 88, 99, 99]

console.log([...new Set(arr1).intersection(new Set(arr2))])
