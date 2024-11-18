// 图片预加载 vite 插件
import type { Plugin } from 'vite'
import fg from 'fast-glob'

interface PreLoadImagesOptions {
  dir: string
  attrs?: {
    rel: 'prefetch' | 'preload'
  }
}

export const preLoadImages = (options: PreLoadImagesOptions): Plugin => {
  const { dir, attrs = {} } = options
  return {
    name: 'vite-plugin-image-prefetch',
    transformIndexHtml(html, ctx) {
      console.log('%c 🍋 html', 'font-size:16px;color:#42b983', html)
      const files = fg.sync(dir, {
        cwd: ctx.server?.config.publicDir,
      })
      const images = files.map((file) => ctx.server?.config.base + file)
      return images.map((item) => {
        return {
          tag: 'link',
          attrs: {
            rel: 'prefetch', // preload
            href: item,
            as: 'image',
            ...attrs,
          },
        }
      })
    },
  }
}
