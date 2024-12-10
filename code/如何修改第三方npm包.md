# 如何修改第三方 npm 包

稳定库，直接爬下来，node_modules，直接修改

patch 方案

fork package，自己来维护

## 背景

难言之隐，来自于设计、产品、老板 boss

## 方案

- 稳定库，node_modules 直接改
- patch 方案
  patch-package，自动化
  `pnpm i patch-package postinstall`

  npm hook

  - prepare
  - postinstall
  - publish

  ```json
  {
    "scripts": {
      "postinstall": "patch-package"
    }
  }
  ```

  创建补丁

  ```bash
  npx patch-package 'package-name'
  ```

- fork package，自己来维护

直接改源码，源码改完之后，构建，发布到 npm 私服
修改的一些内容，如果想贡献给社区，给原来的作者提 PR，code review，test，合并了，你的代码就贡献给社区，提升知名度
