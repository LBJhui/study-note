console.log('hello loader')
import './css/index.css'
const sum = (...args) => {
  return args.reduce((p, c) => p + c, 0)
}

console.log(sum(1, 2, 3, 4, 5))
