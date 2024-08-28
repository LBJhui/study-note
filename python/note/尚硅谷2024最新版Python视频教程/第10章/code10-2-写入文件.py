# _*_ coding: utf-8 _*_
# @Time: 2024/5/24 10:32
# @Author: LBJ辉
# @File: code10-2-写入文件
# @Project: nxops-01

# 打开文件
f = open('test.txt', mode='w', encoding='utf-8')  # 原有文件覆盖，文件不存在时，新建文件并写入
# 写入文件内容
f.write('你好，我是mia\n')
f.write('你是谁\n')
context = ['你好，我是mia', '你是谁\n']
f.writelines(context)
for i in context:
    f.write(i + '\n')
# 关闭文件
f.close()

# f = open('test.txt', mode='r', encoding='utf-8')  # 相对路径
# context = f.read()
# print(context)
# f.close()
