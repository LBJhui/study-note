# python pip 更改国内源 及 取消源

注：此方法为永久改变源，如果你需要的库，国内源没有的话，请看到本文最后重置源为默认

清华源相关代码

```shell
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

其他源

```shell
豆瓣 https://pypi.doubanio.com/simple/
网易 https://mirrors.163.com/pypi/simple/
阿里云 https://mirrors.aliyun.com/pypi/simple/
腾讯云 https://mirrors.cloud.tencent.com/pypi/simple
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
```

取消所有源，替换为默认

```shell
pip config unset global.index-url
```