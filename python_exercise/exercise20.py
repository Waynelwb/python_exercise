import math
import string


def heron(a, b, c):
    s = (a+b+c) / 2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))


print(heron(3, 4, 5))
# 传入的参数过多或者过少将会产生一个TypeError
# python中的每个函数都有一个返回值，忽略返回值也是可以的，返回值可以是单独的一个值也可以是一组值，还可以是组合类型的值，return None 或者没有return


def letter_count(text, letters=string.ascii_letters):  # string.ascii_letters返回的是所有字母
    letters = frozenset(letters)
    count = 0
    for char in text:
        if char in letters:
            count += 1
    return count


print(letter_count("hello world"))
# 这里letters被赋值为以默认形式给定的字符串
print(letter_count("hello", "aeiou"))
print(letter_count("hello", letters="aeiou"))
# 需要注意的是，参数语法不允许在没有默认值的参数后面跟随默认值，因此，def bad(a, b=1, c)不能生效


def append_if_even(x, lst=None):
    if lst is None:
        lst = []
    if x % 2 == 0:
        lst.append(x)
    return lst

# 文档字符串Docstrings


def function():
    """say something here!"""
    pass


print(function.__doc__)
# 参数和参数拆分
# 我们可以使用序列拆分操作符（*）来提供位置参数：heron(sides[0], sides[1], sides[2])或heron(*sides).如果列表（或其他序列）包含比函数参数更
# 多的项目，就可以分片提取出合适的参数
# 我们也可以在函数参数列表中使用序列拆分操作符，在创建使用可变数量的位置参数函数时，这种方法是有用的。下面给出了一个product()函数


def product(*args):
    result = 1
    for arg in args:
        result *= arg
    return result


print(product(1, 2, 3, 4))
print(product(5, 3, 8))
# 我们可以将关键字参数跟随在位置参数后面，如下面这个用于计算参数和的函数，其中每个参数被按给定的幂进行运算


def sum_of_powers(*args, power=1):
    result = 0
    for arg in args:
        result += arg ** power
    return result
