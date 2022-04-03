"""
python重要基础语法学习
"""


import random
# 随机数的生成

# print(random.randint(1, 10))
# 连续数的生成
# for item in range(1, 4, 2):  # 开始，结束，间隔
#     print(item)
# for item in range(1, 4):  # 开始，结束
#     print(item)
# for item in range(4):  # 结束；默认从零开始，不包括结束
#     print(item)
# 将字符转换为ASCII码
# print(ord('a'))
# # 输出ASCII码对应的字符
# print(chr(97))
# 练习：循环输入字符直到输入的内容为空就停止输入，输出输入的内容
# while True:
#     str = input("请输入内容：")
#     if str == '':
#         print("你没有输入任何字符")
#         break
#     print(str)
# temp = '''
#             123
#             456
#             789
# '''
# print(temp)
# # 转义符与原始字符
# print('hello \'DedicationYu\'')  # \转义字符  hello 'DedicationYu'
# print(r"c:\a\b\c")  # r"字符串":可以输出原始字符串  c:\a\b\c
# # %d控制整数位数
# print('%.5d' % 123)  # 00123
# # %f控制小数精度
# print('%.2f' % 12.34567)  # 12.35
# # %%可以输出%，\%无法输出%
# print('汇率为%.2f%%' % 12.23434)  # 汇率为12.23%
# 打印正方形
# side = int(input('请输入矩形的边长：'))
# count = 1
# for __ in range(side):  # 对于不会用到的变量一般用__表示
#     # 第一种写法
#     # if count == 1 or count == side:
#     #     print('*' * side)
#     # else:
#     #     print('*%s*'%(' ' * (side-2)))
#     # count += 1
#     # 第二种写法
#     point = ('*' * side) if (count == 1 or count == side) else ('*%s*'%(' ' * (side-2)))
#     count += 1
#     print(point)

# list01 = [1, 2, 3]
# list01[1:1] = [4,5]  # [1:1]定位到下标为1到下标为1的元素，但不包括下标为1的元素，结果为定位到下标为0到下标为1之间，这里为在之间插入元素
# print(list01)  # [1, 4, 5, 2, 3]
# 删除列表中的固定元素
# list01 = ['张三', '李四', '王五']
# if '张三' in list01:
#     # list01.remove('三')  # 如果移除的元素不在列表中会报错  ValueError: list.remove(x): x not in list
#     list01.remove('张三')
# print(list01)
# 根据下标删除列表中的元素
# del list01[0:1]
# print(list01)  # ['李四', '王五']
# # 更改索引
# list01 = [1, [2, 3], 4]
# list02 = list01  # 这属于将list02的索引也指向原先List01的索引目标，修改List01索引目标的值则list02也发生改变(因为list02也指向该目标)
# list01[0] = 10 # 修改list01的值，list02的对应值也改变
# print(list02)  # [10, [2, 3], 4]
# 浅拷贝：只拷贝第一层
# list01 = [1, [2, 3], 4]
# list02 = list01[:]  # 切片属于浅拷贝
# list01 [0] = 10  # 第一层的修改
# list01 [1][0] = 20  # 第二层的修改
# print(list02)  # 浅拷贝修改第一层互不影响，单对深层的修改相互影响 [1, [20, 3], 4]
# 深拷贝
# import copy
# list01 = [1, [2, 3], 4]
# list02 = copy.deepcopy(list01)  # deepcopy表示深拷贝，拷贝全部数据，所有层都拷贝一遍
# list01[1][0] = 20  # 深拷贝不管第几层修改都互不影响
# print(list02)  # [1, [2, 3], 4]
# # 列表转化为字符串：result = '连接符'.join(列表)
# list01 = ['1', '2', '3']
# str01 = ''.join(list01)  # 将列表中的元素用空字符串拼接起来
# print(str01)  # 123
# 面试题：根据某个循环逻辑拼接字符串(核心思想：将不可变转换为可变)
# 循环拼接0-9
# 方案一(不推荐)
# result = ''  # 字符串是一个不可变类型
# for num in range(0, 10):
#     result += str(num)  # 不断修改一个不可变类型，且每次得到的值都会被丢弃，最后只保留最新的值，这样会产生垃圾，垃圾多了会清除内存从而影响其他程序的运行
# print(result)
# # 方案二(推荐)
# list01 = []  # 列表是一个可变类型
# for result in range(0, 10):
#     list01.append(str(result))
# result = ''.join(list01)  # 将列表转换为字符串
# print(result)
# # 将字符串转化内列表
# list01 = 'a-b-c-d'.split('-')  # split表示分割，将a-b-c-d按照-进行分割后放入列表中
# print(list01)  # ['a', 'b', 'c', 'd']
# # 列表推导式：变量 for 变量 in 可迭代对象 if 条件
# # 需求：将列表list01中所有大于5的数放入列表list02中
# list01 = [1, 3, 5, 7, 9]
# list02 = [num for num in list01 if (num > 5)]
# print(list02)  # [7, 9]
# # 拆包：*表示接收剩余的元素
# *str1, str2 = '1234'
# print(str1)  # ['1', '2', '3']
# list01, *list02, list03 = [1, 2, 3, 4]
# print(list02)  # [2, 3]
# dist01 = {
#     'name': 'KarrieTuu',
#     'age': 24,
#     'sex': 'man'
# }
# # 获取所有的Key
# for key in dist01:
#     print(key)
# # 获取所有的value
# for value in dist01.values():
#     print(value)
# # 获取所有的key和value
# for key, value in dist01.items():
#     print(key)
#     print(value)
# # 删除字典
# del dist01['age']
# print(dist01)

# # 字典推导式：推导式是遍历的简单写法
# # 需求：得到一个字典，key为0-5，value为key的平方
# result = {key: key ** 2 for key in range(0, 6)}
# print(result)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# # 将上述字典中键为偶数的键值对放入另一个字典中
# result01 = {key: value for key,value in result.items() if key % 2 == 0}
# print(result01)  # {0: 0, 2: 4, 4: 16}
# 集合的定义
# set01 = {'a', 'b', 'c'}
# # 说明：字典和集合都是无序的，但字典的输出表面看都是有序的，这是假象，而集合的输出就是无序的
# # 因为字典是按照键寻找数据输入顺序没有意义，而集合就是有键无值得键值对
# print(set01)
# # 集合无法定位(无序)
# # 应用：去重
# list01 = ['a', 'v', 'b', 'd', 'a']
# set02 = set(list01)
# print(set02)  # {'d', 'a', 'b', 'v'}
# # 删除
# set01.remove('a')  # 元素不存在会报错
# set01.discard('a')  # 元素不存在不会报错
# print(set01)
# set01 = {1, 2, 3}
# set02 = {2, 3, 4}
# print(set01 & set02)  # &和|表示交集和并集，-表示差集，^表示补集：返回不同的元素  {2, 3}
# dict01 = {
 #     'name':'KarrieTuu',
#     'age': 22,
#     'sex': 'man'
# }
# for key in list(dict01):
#     if dict01[key] == 22:
#         del dict01[key]
# print(dict01)
# print('a', end='')
# print('b')
