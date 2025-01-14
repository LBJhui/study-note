class Deque {
  constructor() {
    this.queue = {}
    this.rear = 0
    this.head = 0
  }
  // 队首添加
  addFront(item) {
    this.queue[--this.head] = item
  }
  // 队尾添加
  addBack(item) {
    this.queue[this.rear++] = item
  }
  // 队首删除
  removeFront() {
    if (this.isEmpty()) {
      return
    }
    const headData = this.queue[this.head]
    delete this.queue[this.head++]
    return headData
  }
  // 队尾删除
  removeBack() {
    if (this.isEmpty()) {
      return
    }
    const backData = this.queue[this.rear - 1]
    delete this.queue[--this.rear]
    // this.rear-- 与 上一步 this.rear - 1 合并
    return backData
  }
  // 获取队首值
  frontTop() {
    if (this.isEmpty()) {
      return
    }
    return this.queue[this.head]
  }
  // 获取队尾值
  backTop() {
    if (this.isEmpty()) {
      return
    }
    return this.queue[this.rear - 1]
  }
  isEmpty() {
    return this.size() === 0
  }
  size() {
    return this.rear - this.head
  }
}

const deq = new Deque()
