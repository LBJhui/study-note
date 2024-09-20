# Vue 3 + TypeScript + Vite

This template should help get you started developing with Vue 3 and TypeScript in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

Learn more about the recommended Project Setup and IDE Support in the [Vue Docs TypeScript Guide](https://vuejs.org/guide/typescript/overview.html#project-setup).

新建项目： `pnpm create vite`

pnpm 是一个流行的 Node.js 包管理器，‌ 它提供了一系列命令来管理项目的依赖、‌ 运行脚本、‌ 查看信息等。‌

**查看版本和配置**

- pnpm -v：‌ 查看 pnpm 的版本。‌
- pnpm config get registry：‌ 查看当前使用的注册表地址。‌
- pnpm config set registry <淘宝源或其他源地址>：‌ 切换到指定的注册表地址。‌

**管理依赖**

- pnpm install：‌ 安装项目的所有依赖。‌
- pnpm add <pkg>：‌ 添加指定的包到项目中。‌
- pnpm remove <pkg>：‌ 从项目中移除指定的包。‌

**运行脚本和测试**

- pnpm run <script-name>：‌ 运行 package.json 文件中定义的脚本。‌
- pnpm test：‌ 运行测试脚本（‌ 如果存在）‌。‌
- pnpm start：‌ 启动项目（‌ 如果 package.json 中有定义 start 脚本）‌。‌

**查看信息**

- pnpm list 或 pnpm ls：‌ 查看项目依赖树。‌
- pnpm outdated：‌ 检查过期的依赖。‌
- pnpm publish：‌ 发布依赖包到注册表。‌

**环境管理**

- pnpm env use <node 版本号>：‌ 使用指定的 Node.js 版本。‌

修改缓存和状态文件位置：‌ 通过命令行设置 pnpm-cache 和 pnpm-state 的位置，‌ 以优化磁盘空间使用。‌
