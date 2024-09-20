<template>
  <input type="text" v-model="todoMsg">
  <button @click="add">添加</button>
  <button @click="clearHasDone">清理</button>
  <div v-if="lists.length">
    <div v-for="(item, index) in lists" :key="item.msg">
      <input type="checkbox" v-model="item.done">
      <span :class="{ done: item.done }">{{ item.msg }}</span>
      <span @click="deleteItem(index)">❎</span>
    </div>
    <div>
      <span>全选</span>
      <input type="checkbox" v-model="isAllDone">
      <span>{{ hasDown }} / {{ lists.length }}</span>
    </div>
  </div>
  <div v-else>暂无数据</div>
</template>

<script lang='ts' setup>
import { ref, computed } from 'vue';

interface TodoItem {     // 定义 todo 事项类型
  msg: string            // 要做的事
  done: boolean          // 是否完成
}

const todoMsg = ref<string>('')    // 用一个ref来定义 todo 事项，并双向绑定

const lists = ref<TodoItem[]>([   // 定义 todo 列表，初始化一些数据
  { msg: '吃饭', done: true },
  { msg: '睡觉', done: false },
  { msg: '打游戏', done: false }
])

const hasDown = computed(() => lists.value.filter(item => item.done).length)  // 已经做了的事项列表

const isAllDone = computed<boolean>({     // 所有的事项是否完成，双向绑定到全选按钮
  get() {  // isAllDone 的获取方法，用于双向绑定数据
    return hasDown.value === lists.value.length
  },
  set(value: boolean) {   // isAllDone 的更改方法，用于实现全选 和 取消全选功能
    lists.value.forEach(item => {
      item.done = value
    })
  }
})

const add = () => {      // 新增事项
  if (todoMsg.value) {   // 有值才新增
    lists.value.push({
      msg: todoMsg.value,
      done: false
    })
    todoMsg.value = ''    // 新增完了，输入框的值清空
  }
}

const deleteItem = (index: number) => {  // 删除事项
  lists.value.splice(index, 1)
}

const clearHasDone = () => {      // 清理所有已完成的事项
  lists.value = lists.value.filter(item => !item.done)
}
</script>

<style>
.done {
  text-decoration: line-through;
  color: gray;
}
</style>