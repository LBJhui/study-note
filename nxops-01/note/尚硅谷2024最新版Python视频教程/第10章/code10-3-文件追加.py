# _*_ coding: utf-8 _*_
# @Time: 2024/5/24 10:40
# @Author: LBJ辉
# @File: code10-3-文件追加
# @Project: nxops-01

# 打开文件
f = open('test.txt', mode='a', encoding='utf-8')
# 写入文件
f.write('hello\n')
a = ['a', 'vb\n', 'c\n']
f.writelines(a)
# 关闭文件
f.close()
