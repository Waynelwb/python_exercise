leaps = []
for year in range(1900, 1940):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leaps.append(year)
print(leaps)
# 排序
lst = [1, 2, 342, 5345, 33,  2345, 3]
lst.sort()
print(lst)
# 列表内涵
"""
最简单形式：[item for item in iterable]， 返回一个列表其中包含iterable的每个数据项，在语义上与list(iterable)是一致的
两种受欢迎格式：
[expression for item in iterable]
[expression for item in iterable if condition]-->等价于上面第二段表达
"""
leaps = [y for y in range(1900, 1940)]
leaps = list(range(1900, 1940))
leaps = [y for y in range(1900, 1940) if y % 4 ==0]
leaps = [y for y in range(1900, 1940)
         if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)]

# 列表内涵进行嵌套
codes = []
for sex in "MF":
    for size in "SMLX":
        if sex == "F" and size == "X":
            continue
        for color in "BGW":
            codes .append(sex + size + color)
print(codes)
# 上述代码使用列表内涵只需要两行代码就可以实现
codes = [s + z + c for s in "MF" for z in "SMLX" for c in "BGW"
         if not (s == "F" and z == "X")]
print(codes)
