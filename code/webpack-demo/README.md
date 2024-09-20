**npm**

```shell
# 查看源
npm config get registry
# 切换淘宝源
npm config set registry https://registry.npmmirror.com/
```

**\*pnpm**

```shell
# 查看源
pnpm config get registry
# 切换淘宝源
pnpm config set registry https://registry.npmmirror.com/
```

**设置官方镜像源**

```shell
npm config set registry https://registry.npmjs.org
```

**查看镜像源**

```shell
npm config get registry
```

**安装**

```shell
mkdir webpack-demo
cd webpack-demo
npm init -y
npm i webpack webpack-cli --save-dev
```

查看版本：`npx webpack -v`

执行打包命令：`npx webpack-cli`

在文件根目录下创建：`touch webpack.config.js`

> touch : 无法将“touch”项识别为 cmdlet、函数、脚本文件或可运行程序的名称。请检查名称的拼写，如果包括路径，请确保路径正 确，然后再试一次。
> `npm install touch-cli -g`
