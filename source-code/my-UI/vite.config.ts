import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [ vue() ],
  build: {
    rollupOptions: {
      external: [ 'vue' ],
      output: {
        globals: {
          vue: 'Vue'
        }
      }
    },
    lib: {
      entry: './packages/index.ts',
      name: 'lbjhui-ui',
    },
  },
})
