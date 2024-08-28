class Stack {
  /**
   * 实现私有属性：
   *  1.使用下划线命名约定来标记一个属性为私有属性
   *    下划线命名约定就是在属性名称之前加上一个下划线（_）​。
   *    不过这种方式只是一种约定，并不能保护数据，而且只能依赖于使用我们代码的开发者所具备的常识。
   *    this._count = 0;
   *    this._items = {};
   *
   *  2.使用Symbol
   *    const _items = Symbol('stackItems');
   *    class Stack{
   *      constructor(){
   *         this[_items] = {};
   *      }
   *    }
   *      Object.getOwnProperty-Symbols方法能够取到类里面声明的所有Symbols属性
   *
   *  3.使用WeakMap
   *    采用这种方法，代码的可读性不强，而且在扩展该类时无法继承私有属性
   *    const items = new WeakMap();
   *    class Stack {
   *      constructor() {
   *        items.set(this, []);
   *      }
   *
   *      push(element) {
   *        items.get(this).push(element);
   *      }
   *
   *      pop() {
   *        const list = items.get(this);
   *        if (list.length === 0) return undefined;
   *        return list.pop();
   *      }
   *    }
   *  4.属性前添加井号（#）作为前缀来声明私有属性
   */
  constructor() {
    this.count = 0;
    this.items = {};
  }
  push(element) {
    this.items[this.count] = element;
    this.count++;
  }

  size() {
    return this.count;
  }

  isEmpty() {
    return this.count === 0;
  }

  pop() {
    if (this.isEmpty()) {
      return undefined;
    }
    this.count--;
    const result = this.items[this.count];
    delete this.items[this.count];
    return result;
  }

  peek() {
    if (this.isEmpty()) {
      return undefined;
    }
    return this.items[this.count - 1];
  }

  clear() {
    while (!this.isEmpty()) {
      this.pop();
    }

    /**
     * this.items = {}
     * this.count = 0
     */
  }

  toString() {
    if (this.isEmpty()) {
      return '';
    }
    let objString = `${this.items[0]}`;
    for (let i = 1; i < this.count; i++) {
      objString = `${objString},${this.items[i]}`;
    }
    return objString;
  }
}

/**
 * 将十进制数字转换为二进制字符串
 *
 * @param {number} decNumber - 输入的十进制数字
 * @returns {string} - 转换后的二进制字符串
 */
const decimalToBinary = (decNumber) => {
  // 创建一个栈来存储余数
  const remStack = new Stack();
  // 定义一个变量来存储当前处理的数字
  let number = decNumber;
  // 定义一个变量来存储除法运算的余数
  let rem;
  // 定义一个字符串变量来存储最终的二进制字符串
  let binaryString = '';

  // 当数字大于0时，继续进行除法和取余操作
  while (number > 0) {
    rem = Math.floor(number % 2);
    remStack.push(rem);
    number = Math.floor(number / 2);
  }

  // 当栈不为空时，从栈中弹出余数并拼接到字符串的最右边
  while (!remStack.isEmpty()) {
    binaryString += remStack.pop().toString();
  }
  // 返回最终形成的二进制字符串
  return binaryString;
};

/**
 * 将十进制数转换为指定进制的字符串
 * @param {number} decNumber - 待转换的十进制数
 * @param {number} base - 目标进制（必须在2到36之间）
 * @returns {string} - 转换后的字符串，如果目标进制无效则返回空字符串
 */
function baseConverter(decNumber, base) {
  // 使用栈来存储余数，以便逆序取出，构建目标进制的字符串表示
  const remStack = new Stack();
  // 可用于表示数字的字符，覆盖0-9和A-Z，共36个字符
  const digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'; // {6}
  let number = decNumber;
  let rem;
  let baseString = '';

  // 检查目标进制是否在有效范围内（2到36），如果无效则直接返回空字符串
  if (!(base >= 2 && base <= 36)) {
    return '';
  }

  // 循环直到十进制数被完全分解
  while (number > 0) {
    // 计算当前数字在指定进制下的余数
    rem = Math.floor(number % base);
    // 将余数压入栈中
    remStack.push(rem);
    // 更新十进制数为商，准备下一轮计算
    number = Math.floor(number / base);
  }

  // 从栈中弹出元素，构建目标进制的字符串
  while (!remStack.isEmpty()) {
    // 栈顶元素对应的字符添加到结果字符串中
    baseString += digits[remStack.pop()]; // {7}
  }

  return baseString;
}

export { decimalToBinary, baseConverter };
