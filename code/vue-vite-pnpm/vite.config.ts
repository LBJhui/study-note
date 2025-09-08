import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import VueDevTools from 'vite-plugin-vue-devtools'
import AutoImport from 'unplugin-auto-import/vite' //模块自动导入
import { resolve } from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    VueDevTools(),
    AutoImport({
      imports: ['vue', 'vue-router'], // 第三方
      // dirs: ['./src/api'], // 本地
      dts: 'src/types/auto-imports.d.ts' // 生成 ts 声明文件
    })
  ]
})
