/**
 * 腾讯面试题
 * 异步执行一个函数
 * 如果可以，尽量将函数放入到微队列中
 * @params {Function} func 无参，无返回
 */

function asyncRun(func) {
  if (typeof Promise !== 'undefined') {
    Promise.resolve().then(func)
  } else if (typeof MutationObserver !== 'undefined') {
    const observer = new MutationObserver(func)
    const textNode = document.createTextNode(1)
    observer.observe(textNode, { characterData: true })
    textNode.data = 2
  } else {
    setTimeout(func, 0)
  }
}
