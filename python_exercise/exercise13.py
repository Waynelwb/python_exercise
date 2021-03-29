# 忽略我
l = [1, 2, 3, 4, 2]
for i in range(len(l)):
    l[i] += 1
print(l)

# 集合类型
"""
set是一种组合数据类型，支持成员关系操作符（in）、对象大小计算操作符（len（）），并且也是字面量。
具有set.isdisjoint()方法-用于比较两个集合是否含有相同的元素，支持比较，也支持位逻辑操作符
python提供两种集合数据类型：可变的set类型和固定的frozenset类型。
进行迭代时，集合类型以任意顺序提供其数据项
只有可哈希运算的对象可以添加到集合中，所有的内置固定数据类型都是可哈希运算的(float, frozenset, int, str, tuple)
而内置的可变数据类型都是不可哈希运算的(dict, list, set), 这些值不能添加到集合中
"""
# 非空集合可以不使用set函数创建，而空集合必须使用set函数创建，而不能使用空的圆括号创建
# 集合中的项是无序的，因此没有索引位置的概念，也不能分片或者按步距分片
s = {7, "veil", 0, -29, ("x", 11), "sun", frozenset({8, 4, 7}), 913}
# set数据类型可以作为函数进行调用，set()——不带参数进行调用时将返回一个空集合；带一个参数时返回该参数的浅拷贝；
# 对任意其他参数将尝试将给定的参数转换为集合
set("pecan") | set("pie")  # 并集
set("pecan") & set("pie")  # 交集
set("pecan") - set("pie")  # 差集
set("pecan") ^ set("pie")  # 补集
# 集合数据类型的一个常用场景时进行快速的成员关系测试。比如，如果用户没有输入任何命令行参数，或输入的参数是“-h”或者“-help”，就返回给用户一条使用帮助
# 消息
"""
import sys
if len(sys.argv) == 1 or sys.argv[1] in {"-h", "-help"}:
"""
# 另一个常用场景：确保没有重复处理的数据
# example1:
seen = set()
for ip in ips:
    if ip not in seen:
        seen.add(ip)
        process_ip(ip)

# example2:
for ip in set(ips):
    process_ip(ip)

# 集合内涵
"""
{expression for item in iterable}
{expression for item in iterable if condition}
"""
s = {i*2 for i in [4, 6, 7]}
n = {i*2 for i in [4, 6, 7] if i > 5}
# 可以使用集合内涵进行过滤，下面给出一个实例
files = ["a.htm", "b.jpeg", "c.pdf", "d.txt"]
html = {x for x in files if x.lower().endswith((".htm", ".html"))}
print(html)

# 固定集合
m = frozenset()
# 集合可以用于删除不需要的数据项
filenames = set(filenames) - {"MAKEFILE", "Makefile", "makefile"}
