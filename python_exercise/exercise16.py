# Chapter4-控制结构与函数
# 4.1-控制结构
# 4.1.1-条件分支
# General Syntax
"""
if _boolean_expression_:
    suite1
elif expression2:
    suite2
...
else:
    suiteN
"""
# 可以有0个或者多个elif语句
# 如果我们需要考虑某个特殊情况，但在该情况出现时又不需要做什么，可以是同pass作为该分支的suite
# 在有些情况下可以将一条if...else语句缩减为单一的表达式：
# expression1 if boolean_expression else expression2
import sys
offset = 20
if not sys.platform.startswith("win"):
    offset = 10
# 上下两个是等价的
offset = 20 if sys.platform.startswith("win") else 10
# 下列演示了一种错误情况(不正确的使用圆括号)和解决方式：
margin = True
width = 100 + 10 if margin else 0  # wrong!
width = 100 + (10 if margin else 0)  # true!
count = 1
print("{0} file{1}".format((count if count != 0 else "no"),
                           ("s" if count != 1 else "")))


# 4.1.2-循环
# General Syntax（while）
"""
while boolean_expression:
    suite
else:
    suite
"""
# else分支是可选的，只要expression为真，while的suite就会执行。如果为假，则就会执行else的suite
# 在while块的suite中如果执行continue，就会跳到循环起始处，并对expression重新评估。
# 如果循环不能正常终止，就会跳过所有可选的else分支
# 只要循环是正常终止的else分支的suite就总会正常执行，如果遇到break语句或者由于返回语句或者发生异常跳出循环，else中suite就不会执行。
# 发生异常时，python会跳过else分支并寻找适当的异常处理部分
lst = [1, 2, 3, 4, 5, 6]
target = 7


def list_find(x, y):
    index = 0
    while index < len(x):
        if x[index] == y:
            break
        index += 1
    else:
        index = -1
    return index


print(list_find(lst, target))
# 这一函数在给定的列表中搜索目标。如果找到目标就终止循环，并返回适当的索引位置。如果找不到目标，就会循环完毕并正常终止，之后执行else中的suite
# str.index() and list.index()方法可以返回给定字符串或数据项的索引位置，并在找不到时产生ValueError的异常，使用str.find()的功能找不到时不会
# 产生异常，而是返回索引值-1
# 对于列表没有等价的find（）方法

# for loop
# General Syntax
"""
for expression in iterable:
    suite
else:
    suite
"""
# 如果在suite中执行了continue语句，那么控制流立即跳转到循环起始处，并开始下一次迭代。
# 循环正常终止，执行else suite语句，如果循环跳出（执行了break或者return语句），控制流会立即跳转到循环后的语句，所有的else都会被跳过
# 如果发生异常，python会跳过else分支并寻找适当的异常处理程序


def lst_find(x, y):
    for index, t in enumerate(x):
        if t == y:
            break
    else:
        index = -1
    return index


print(lst_find(lst, target))
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
# 上述程序和while实现的程序功能相同
