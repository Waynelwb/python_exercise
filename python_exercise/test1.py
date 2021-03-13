for _ in (0,1,2,3,4,5):
    print('hello world!')

"""
数据类型：标识符与关键字， Integral类型，整数， 布尔型， 浮点类型
"""
"""
浮点类型：float decimal.Decimal complex
"""
# decimal.Decimal 具有更高的精度
"""
int and float = float
float and complex = complex
decimal.Decimal can only use decimal.Decimal or int
"""
# 浮点数
# float数据类型可以作为函数调用——不指定参数时返回0.0
# 下列函数用于比较floats是否相等
import sys
def equal_float(a, b):
    return abs(a - b) <= sys.float_info.epsilon
print(equal_float(1, 2))

"""
round() math.floor() math.ceil() float.is_integer() float.as_integer_ratio()
使用float.hex()方法可以将浮点数以十六进制形式表示为字符串
使用float.fromhex()方法可以做相反的转换
"""
# math.hypot()用于计算原点到点的距离
"""
复数：Literal复数在书写上使用+或-符号将实数部分和虚数部分结合起来（虚数部分使用字母j）
"""
