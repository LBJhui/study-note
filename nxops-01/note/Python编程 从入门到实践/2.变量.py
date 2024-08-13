# _*_ coding: utf-8 _*_
# @Time: 2024/5/8 11:12
# @Author: LBJ辉
# @File: 2.变量
# @Project: nxops-01

message = "Hello Python world!"
print(message)

'''
变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头，例如，可将变量命名为message_1，但不能将其命名为1_message。
变量名不能包含空格，但可使用下划线来分隔其中的单词。例如，变量名greeting_message可行，但变量名greeting message会引发错误。
不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，如print。
变量名应既简短又具有描述性。例如，name比n好，student_name比s_n好，name_length比length_of_persons_name好。
慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0。
'''

name = 'aDa lovelace'
# title()以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写。
print(name.title())  # Ada Lovelace
print(name.upper())  # ADA LOVELACE
print(name.lower())  # ada lovelace

# 合并(拼接)字符串
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name
print(full_name)  # ada lovelace

# 使用制表符或换行符来添加空白
print('Python')
print('\tPython')
print('Languages:\nPython\nC\nJavaScript')
print('Languages:\n\tPython\n\tC\n\tJavaScript')

# 删除空白
favorite_language = ' Python '
# 删除字符串末尾空白，不会改变原字符串
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
print(favorite_language)

# 使用函数str()避免类型错误
age = 23
message = 'Happy ' + str(age) + 'rd Birthday!'
print(message)
'''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
