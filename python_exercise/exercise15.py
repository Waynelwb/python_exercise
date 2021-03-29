# 字典内涵
"""
字典内涵是一个表达式，同时也是一个循环，该循环有一个可选的条件(包含在方括号中)，与集合内涵非常类似。
"""
"""
{keyexpression: valueexpression for key, value in iterable}
{keyexpression: valueexpression for key, value in iterable if condition}
"""
import os
# 下面的实例展现如何用字典内涵创建字典，其中，，每个键是当前目录中文件的文件名。值则为以字节计数的文件大小
file_sizes = {name: os.path.getsize(name) for name in os.listdir(".")
              if os.path.isfile(name)}
# os.path.isfile()用于判断某一对象(需提供绝对路径)是否为文件
# os.listdir()方法，此方法返回一个列表，其中包含有指定路径下的目录和文件的名称
# 字典内涵也可以用于创建反转的目录：
inverted_d = {v: k for k, v in d.items()}
# 如果有任何值不是可哈希运算的，那么这种反转会失败，并产生TypeError异常
# 与列表内涵和集合内涵一样，字典内涵中的iterable也可以是一个内涵，因此，所有各种嵌套的内涵都是可能的

# 默认字典
import collections
words = collections.defaultdict(int)
x = words["xyz"]
# defaultdict类避免KeyError异常:
import collections
bag = ['apple', 'orange', 'cherry', 'apple','apple', 'cherry', 'blueberry']
count = collections.defaultdict(int)
for fruit in bag:
    count[fruit] += 1
"""
输出：
defaultdict(<class 'int'>, {'apple': 3, 'orange': 1, 'cherry': 2, 'blueberry': 1})
"""
# collections.defaultdict类使用：
# 类型名称作为初始化函数参数：这个就是上面的例子
# 可调用函数作为初始化函数参数：
import collections


def zero():
    return 0


dic = collections.defaultdict(zero)
dic['bbb']
print(dic)

# 有序字典
d = collections.OrderedDict([("z", -4), ("e", 19), ("k", 7)])
tasks = collections.OrderedDict()
tasks[8031] = "Backup"
tasks[4027] = "Scan Email"
tasks[5733] = "Build System"
"""
如果想要将某个数据项移到尾部，需要删除再添加
调用popitem()删除并返回最后一个键-值项
或者调用popitem(last = False)删除并返回第一个数据项。
给定字典d，可以用：
d = collections.OrderedDict(sorted(d.items()))
转化为排序字典。
值得注意的是，如果我们要插入任意额外的键，这些键将被插入在尾部，因此，在进行插入操作后，为了保持排序的顺序，我们必须重新创建该字典（重新执行前面创建
该字典的代码）。
"""

# 组合类型的复制
"""
对象引用将指向存放字面值的内存对象
"""
songs = ["because", "Boys", "Carol"]
beatles = songs
print(beatles, songs)
beatles[2] = "Cayenne"
print(beatles, songs)
# 会发现两者一起发生了变化
# 如果需要整个序列的副本，而不仅仅是一个对象引用，则可以通过下面方式实现：
songs = ["because", "Boys", "Carol"]
beatles = songs[:]
beatles[2] = "Cayenne"
print(beatles, songs)
# 对于字典和集合而言，这种复制操作可以使用dict.copy()与set.copy()来实现。此外，copy模块提供了copy.copy()函数，该函数返回给定对象的一个副本
# 对内置组合数据类型进行复制的另一种方法是使用类型名作为函数，将待复制的组合类型数据作为参数，实例如下：
copy_of_dict_d = dict(d)
copy_of_list_L = list(L)
copy_of_set_s = set(s)
# 值得注意的是，这些复制技术都是浅拷贝，也就是说复制的只是对象引用而非对象本身。对固定数据类型，比如字符串与数字，这与复制的效果是相同的，但对于可变数
# 据类型, 比如嵌套的组合类型，这意味着相关对象同时被原来的组合和复制得来的组合引用
# 这时候就需要深拷贝：
import copy
x = [53, 68, ["A", "B", "C"]]
y = copy.deepcopy(x)
y[1] = 40
x[2][0] = 'Q'
print(x, y)
