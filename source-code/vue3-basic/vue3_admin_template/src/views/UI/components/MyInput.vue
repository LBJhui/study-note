<template>
  <div class="my-input">
    <el-input ref="inp" v-bind="$attrs">
      <template v-for="(, name) in $slots" #[name]="slotData">
        <slot :name="name" v-bind="slotData || {}"></slot>
      </template>
    </el-input>
  </div>
</template>

<!-- https://juejin.cn/post/7262343902889197629 -->
<script setup lang="ts">
import type { FormInstance } from 'element-plus'
// 引入useAttrs方法:获取组件标签身上属性与事件
import { ref, useAttrs, useSlots, toRaw, defineExpose } from 'vue'
// 此方法执行会返回一个对象
let $attrs = useAttrs()

// 插槽
let $slots = useSlots()
let inp = ref<FormInstance>()

// 对外暴露方法，在父组件中，可通过 ref 调用
defineExpose(toRaw(inp))
</script>

<style scoped>
.my-input {
  transition: 0.3s;
}
.my-input:hover,
.my-input:focus-within {
  filter: drop-shadow(0 0 10px #409eff);
}
</style>
