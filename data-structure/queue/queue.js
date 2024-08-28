class Queue {
  constructor() {
    this.count = 0;
    this.lowestCount = 0; // 队头元素索引
    this.items = {};
  }

  // 向队列尾部添加一个（或多个）新的项
  enqueue(element) {
    this.items[this.count] = element;
    this.count++;
  }

  // 移除队列的第一项（即排在队列最前面的项）并返回被移除的元素
  dequeue() {
    if (this.isEmpty()) {
      return undefined;
    }
    const result = this.items[this.lowestCount];
    delete this.items[this.lowestCount];
    this.lowestCount++;
    return result;
  }

  // 返回队列中第一个元素
  peek() {
    if (this.isEmpty()) {
      return undefined;
    }
    return this.items[this.lowestCount];
  }

  // 判断队列是否为空
  isEmpty() {
    return this.size() === 0;
  }

  // 队列的元素个数
  size() {
    return this.count - this.lowestCount;
  }

  // 清空队列
  clear() {
    this.items = {};
    this.count = 0;
    this.lowestCount = 0;
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

/**
 * 模拟“击鼓传花”游戏
 * @param {Array} elementsList - 游戏参与者的列表
 * @param {number} num - 每次传递后需要出列的数量
 * @returns {Object} - 包含被淘汰者列表和获胜者的对象
 */
const hotPotato = (elementsList, num) => {
  // 创建一个队列来模拟游戏中的传递过程
  const queue = new Queue();
  // 初始化一个数组来存放被淘汰的参与者
  const elimitatedList = [];

  // 将游戏参与者依次加入队列
  for (let i = 0; i < elementsList.length; i++) {
    queue.enqueue(elementsList[i]);
  }

  // 当队列中还有两个以上参与者时，继续游戏
  while (queue.size() > 1) {
    // 按指定次数传递“花”
    for (let i = 0; i < num; i++) {
      queue.enqueue(queue.dequeue());
    }
    // 出列一次，表示该参与者被淘汰
    elimitatedList.push(queue.dequeue());
  }

  // 返回游戏结果，包括被淘汰的参与者列表和最后的获胜者
  return {
    eliminated: elimitatedList,
    winner: queue.dequeue(),
  };
};

const queue = new Queue();
console.log(queue.isEmpty());
queue.enqueue('john');
queue.enqueue('jack');
console.log(queue.toString());
queue.enqueue('camila');
console.log(queue.toString()); // John, Jack, Camila
console.log(queue.size()); // 输出3
console.log(queue.isEmpty()); // 输出false
queue.dequeue(); // 移除John
queue.dequeue(); // 移除Jack
console.log(queue.toString()); // Camila
