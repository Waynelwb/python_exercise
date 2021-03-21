# 字符串的format()方法可以使用映射拆分
# 当前还在作用范围内的局部变量可以通过内置的locals()函数访问，该函数会返回一个字典，字典的键是局部变量名
element = 'silver'
number = 47
print("Element {number} is {element}".format(**locals()))

# 转换
# decimal.Deccimal有两种展现形式，一种是表象形式，一种是字符串形式

# 格式规约

# 命名的元组
"""
collections模块提供的namedtuple()函数，用于创建自定义元组类型
"""
import collections
Sale = collections.namedtuple("Sale", "productid customerid date quantity price")
sales = []
sales.append(Sale(432, 921, "2008-09-14", 3, 7.99))
sales.append(Sale(419, 874, "2008-09-15", 1, 18.49))
total = 0
for sale in sales:
    total += sale.quantity*sale.price
print("Total ${0:.2f}".format(total))

"""
命名的元组有几个私有方法，例如：namedtuple._asdict()返回的是键-值对的映射
"""
"{manufacturer}{model}".format(**aircraft_asdict())