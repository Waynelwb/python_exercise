# 映射类型
"""
映射类型是一种支持成员关系操作符（in）和尺寸函数len()的数据类型，并且是可以迭代的。
三种映射类型：内置的dict类型， 标准库中的collections.defaultdict类型，以及有序的collections.OrderedDict类型
可哈希运算的对象可以作为字典的键，字典的值可以用任意类型的对象
字典类型可以用标准的比较操作符进行比较。但是对于字典而言， 真正有意义的比较操作符是==以及！=
"""
# 字典
# 字典是一种无序的对象类型，索引和分片，切片实际上是无意义的
# 可以通过调用dict()生成字典，无参数生成空字典
# 下面展示创建字典的几种方法
d1 = {}
d2 = {'spam': 1, 'egg': 2, 'bar': 3}
d3 = dict(spam=1, egg=2, bar=3)
# 二元组列表创建
lst = [('spam', 1), ('egg', 2), ('bar', 3)]
d4 = dict(lst)
d5 = dict(zip('abc', [1, 2, 3]))
d6 = {i: 2*i for i in range(3)}
d7 = dict.fromkeys(range(3), 'x')
# 对字典进行迭代的几种方法
for item in d2.items():
    print(item[0], item[1])

for key, value in d2.items():
    print(key, value)

for value in d2.values():
    print(value)

for key in d2.keys():
    print(key)

for key in d2:
    print(key)
# 这里如果我们要改变字典中的值，惯用的做法是在键上进行迭代，并使用方括号操作符来引用并改变其对应的对象。
for key in d2:
    d2[key] += 1

# item() keys() values()等方法都会返回字典视图。在实际作用上，字典视图是一个只读的iterable对象，看起来存放了字典的项、键、或值，具体依赖于我们
# 的实际需求
# 字典视图并不是简单的iterables：第一，如果该视图引用的字典发生变化，那么该视图将会发生变化。第二，键视图于项视图支持一些类似于集合的操作。给定字典
# 视图v与set（或字典视图）x，支持的操作包括：
v & x
v | x
v - x
v ^ x
# 我们可以使用成员关系操作符in来查看某个特定的键是否存在于字典中，比如：x in d。我们也可以使用联合操作符来查看来自给定集合的哪些键存在于字典中
d = {}.fromkeys("ABCD", 3)
s = set("ACX")
matches = d.keys() & s # 取交集
