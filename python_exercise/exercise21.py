# 模块
# 5.1模块与包
"""
import importable
import importable1, importable2, ..., importableN
import importable as preferred_name
"""
import os.path  # 导入一个包中的模块
# 导入模块一般放在文件的起始处
# 首先导入标准库模块，之后是第三方模块库，最后才是我们的自定义模块
from os import *  # 在实践中，这意味着导入模块中的每个对象（除了那些名称以下划线引导的对象），或者，如果模块有一个全局的__all__变量，其中存放一
# 个列表，就导入名称包含在__all__变量中的所有对象
# 如果我们调用了 from os import dirname，就可以调用dirname（）函数，但是如果我们又使用了dirname = ‘。’，此时函数将不能再使用，会产生TypeError的异常

# heapq模块-堆与二叉搜索树
# 堆的内存占用更少，搜索性能更慢，更新性能更快
