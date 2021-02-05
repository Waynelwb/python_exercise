#coding:utf-8
'''
布尔类型
'''
True = 1
False = 0
bool(...) #可以是空，可以是空字符串，可以是只有空格的字符串，可以是列表，可以是空字典。得到不同的结果：False、False、True、False、False

'''
比较对象
'''
1 > 2
1 < 2
1 == 2 #判断是否相等
1 != 2 #判断是否不相等
1 >= 2 #大于等于
1 <= 2 #小于等于
lst_a = [1,2,[1,2]]
lst_b = lst_a.copy()
lst_a == lst_b #返回的值为True
lst_a is lst_b #返回的值为False

'''
逻辑运算(布尔运算)
'''
A = 1
B = 0
A and B #返回的值为False
#相当于 if：bool(A) == False 
#          返回A
#      else：
#          返回B
False and 3 #返回False
0 and 3 #返回0
3>2 and 4>3 #返回True
3>2 and 4 #返回4

A or B
3 or 0 #先判断A是否为真，如果A为真，则返回A，否则返回B

not B #返回相反的布尔值
not lst_a == lst_b #返回的为False

'''
import语句
'''
import math
import math as shuxue
from math import pi
from math import pi as pai
from math import *

'''
赋值语句
'''
#variable = object
a = 1,2,3
a,b,c = 1,2,3
a,_,c = 1,2,3
a, *b = 1,2,3 #这样的话得到的b为一个列表
a = b = 1
a = a + 1 # ==> a += 1
a -= 2
a *= 2
a /= 2