"""
十进制数字：
decimal模块可以提供固定的十进制数，其精度由我们自己指定
设计decimal的计算比浮点数的计算要慢
"""
import decimal
a = decimal.Decimal(9876)
b = decimal.Decimal("7578.23232426536")
print(a + b)
# 十进制数使用decimal.Decimal()函数进行创建，可以接受整数或字符串作为参数——但不能接受浮点数作为参数
# 使用decimal.Deciamls from-float()函数将floats转换为十进制数，该函数以float作为参数
# 使用**或者pow()时，第二个参数必须为整数，且math模块和cmath模块不适用于decimal
