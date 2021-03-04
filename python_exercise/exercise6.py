# coding: utf-8
"""
Python3 程序开发指南.第二版
"""
# 逻辑操作符
a = ["remember", 3, None]
b = ["remember", 3, None]
print(a is b)

b = a
print(a is b)

a = "something"
b = None
print(a is not b, b is None)

# 逻辑操作符
a = 2
b = 6
print(a == b)
print(a < b)
print(a <= b, a != b, a >= b, a > b)

# python中可以进行结链比较
a = 9
print(0 <= a <= 10)

"""
Python中可以容易的创建自定义数据类型，并且与已有数据类型进行很好的整合，比如，我们可以创建自定义的数值类型，并将其与内置的int类型进行比较，也可以与其
他内置的或自定义的数值类型进行比较，但不能与字符串或其他非数值类型进行比较。
"""

# 成员操作符
"""
列表[]
字典{}
元组()
集合 a = set() {}
"""

