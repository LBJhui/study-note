import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  css: {
    preprocessorOptions: {
      less: {
        // less文件路径
        additionalData: `@import "src/assets/css/index.less";`,
      },
    },
  },
})
