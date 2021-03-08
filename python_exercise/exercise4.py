# 条件语句
'''
if(<expr>):
    <statement>
    <statement>
elif(<expr>):
    <statement>
elif(<expr>):
    <statement>
else:
    <statement>
<following_statement>            
'''

# for循环语句
'''
for i in 'hello':
    print(i)
'''

# 可迭代对象
'''
都含有__iter__方法
'''
lst = [1,2,3,4]
for i in lst:
    print(i, i+10)

d = {'name':'Wayne', 'lang':'python', 'age':19}
for k in d:
    print(k, d[k])

dt = {}
for k in d:
    dt[d[k]] = k

for k, v in d.items():
    print(k, v)


