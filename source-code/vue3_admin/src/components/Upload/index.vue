<template>
  <div>
    <!-- <el-upload v-model:file-list="fileList" class="upload" action="" multiple :limit="3" :show-file-list="false">
      <div class="upload-btn">上传</div>
    </el-upload> -->
    <el-upload v-model:file-list="fileList" :="attrs" @change="handleChange" v-if="attrs.type === 'dashbutton'">
      <!-- <div class="upload-btn">上传</div> -->
      <el-button class="upload-btn" type="primary">
        <span class="iconfont icon-attachment"></span>
        上传
      </el-button>
    </el-upload>
  </div>
</template>

<script setup lang="ts">
import { ref, useAttrs } from 'vue'

let attrs = useAttrs()
console.log('%c 🍰 attrs', 'font-size:16px;color:#93c0a4', attrs)
const props = defineProps(['modelValue'])
const emit = defineEmits(['update:modelValue'])

const handleChange = (file: any) => {
  emit('update:modelValue', file.raw)
}

const fileList = ref([])
</script>

<style scoped lang="scss">
.upload-btn {
  background: #ffffff;
  border-radius: 2px;
  border: 1px dashed $primaryColor;
  color: $primaryColor;
  font-size: 14px;
  width: 90px;
}
</style>
