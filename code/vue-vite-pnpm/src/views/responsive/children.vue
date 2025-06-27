<template>
  <div>得到传入的属性:{{ count }}</div>
  <div>doubled:{{ doubleCount }}</div>
</template>

<script setup lang="ts">
const props = defineProps<{
  count: number
}>()
/**
 *
 * vue响应式的本质
 * vue 的数据响应式：数据变化时，依赖数据的函数重新运行
 * 响应式：函数和数据进行关联
 *  函数：被监控的函数
 *    render
 *    computed
 *    watch
 *    watchEffect
 *  数据：函数中读取到的数据，该数据是响应式对象的某个属性
 *    响应式数据
 *    必须在函数中用到
 */
//

// 1 不是响应式
// const doubleCount = ref(props.count * 2)

// 2 响应式
// const doubleCount = ref(0)
// watchEffect(() => {
//   console.log('watchEffect')
//   doubleCount.value = props.count * 2
// })
// props.count(响应式数据) 变化 -> watchEffect -> doubleCount.value -> render

// 3
// 不是响应式
// function useDouble(count: number) {
//   const doubleCount = ref(count * 2)
//   watchEffect(() => {
//     console.log('watchEffect')
//     doubleCount.value = count * 2 // count 不是响应式数据，变化不会引起 watchEffect 执行
//   })
//   return doubleCount
// }
// const doubleCount = useDouble(props.count)

// 响应式
// function useDouble(props) {
//   const doubleCount = ref(props.count * 2)
//   watchEffect(() => {
//     console.log('watchEffect')
//     doubleCount.value = props.count * 2
//   })
//   return doubleCount
// }
// const doubleCount = useDouble(props)

// 4 响应式
// const doubleCount = computed(() => props.count * 2)

// 5 不是响应式
function useDouble(count: number) {
  const doubleCount = computed(() => count * 2)
  return doubleCount
}
const doubleCount = useDouble(props.count)
</script>

<style scoped lang=""></style>
