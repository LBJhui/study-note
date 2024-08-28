class Deque {
  constructor() {
    this.count = 0;
    this.lowestCount = 0;
    this.items = {};
  }

  addFront(element) {
    if (this.isEmpty()) {
      this.addBack(element);
    } else if (this.lowestCount > 0) {
      this.lowestCount--;
      this.items[this.lowestCount] = element;
    } else {
      for (let i = this.count; i > 0; i--) {
        this.items[i] = this.items[i - 1];
      }
      this.count++;
      this.items[0] = element;
    }
  }

  addBack(element) {
    this.items[this.count] = element;
    this.count++;
  }

  removeFront() {
    if (this.isEmpty()) {
      return undefined;
    }
    const result = this.items[this.lowestCount];
    delete this.items[this.lowestCount];
    this.lowestCount++;
    return result;
  }

  removeBack() {
    if (this.isEmpty()) {
      return undefined;
    }
    this.count--;
    const result = this.items[this.count];
    delete this.items[this.count];
    return result;
  }

  peekFront() {
    if (this.isEmpty()) {
      return undefined;
    }
    return this.items[this.lowestCount];
  }

  peekBack() {
    if (this.isEmpty()) {
      return undefined;
    }
    return this.items[this.count - 1];
  }

  isEmpty() {
    return this.size() === 0;
  }

  clear() {
    this.items = {};
    this.count = 0;
    this.lowestCount = 0;
  }

  size() {
    return this.count - this.lowestCount;
  }

  toString() {
    if (this.isEmpty()) {
      return '';
    }
    let objString = `${this.items[this.lowestCount]}`;
    for (let i = this.lowestCount + 1; i < this.count; i++) {
      objString = `${objString},${this.items[i]}`;
    }
    return objString;
  }
}

// 创建一个回文检查器函数
const palindromeChecker = (aString) => {
  // 检查输入字符串是否未定义、为空或长度为0
  if (aString === undefined || aString === null || (aString !== null && aString.length === 0)) {
    return false;
  }
  // 初始化一个双向队列
  const deque = new Deque();
  // 将字符串转换为小写并移除空格
  const lowerString = aString.toLocaleLowerCase().split(' ').join('');
  // 初始化一个布尔变量用于判断是否为回文
  let isEqual = true;
  // 定义用于存储首尾字符的变量
  let firstChar, lastChar;

  // 遍历字符串，将每个字符添加到双向队列尾部
  for (let i = 0; i < lowerString.length; i++) {
    deque.addBack(lowerString.charAt(i));
  }

  // 当双向队列大小大于1时，继续比较首尾字符
  while (deque.size() > 1 && isEqual) {
    // 从队列前端移除并获取第一个字符
    firstChar = deque.removeFront();
    // 从队列尾端移除并获取最后一个字符
    lastChar = deque.removeBack();
    // 如果首尾字符不相等，则设置isEqual为false并结束循环
    if (firstChar !== lastChar) {
      isEqual = false;
    }
  }

  // 返回是否为回文的布尔值
  return isEqual;
};

const deque = new Deque();
console.log(deque.isEmpty()); // 输出true
deque.addBack('John');
deque.addBack('Jack');
console.log(deque.toString()); // John, Jack
deque.addBack('Camila');
console.log(deque.toString()); // John, Jack, Camila
console.log(deque.size()); // 输出3
console.log(deque.isEmpty()); // 输出false
deque.removeFront(); // 移除John
console.log(deque.toString()); // Jack, Camila
deque.removeBack(); // Camila决定离开
console.log(deque.toString()); // Jack
deque.addFront('John'); // John回来询问一些信息
console.log(deque.toString()); // John, Jack
