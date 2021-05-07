# 4.2异常处理
# 4.2.1异常捕获：通常使用try...except块实现的，其通常语法格式如下：
"""
try:
    try_suite
except exception_group1 as variable1:
    except_suite1
...
except exception_groupN as variableN:
    except_suiteN
else:
    else_suite
finally:
    finally_suite
"""
# 其中至少要包括一个except块，但else与finally块都是可选的。在try块的suite正常执行完毕时，会执行else块的suite——如果发生异常，就不会执行。如果
# 存在一个finally块，则总会最后执行
d = dict()
try:
    x = d[5]
except LookupError:
    print("Lookup error occured")
except KeyError:
    print("Invalid key used")
# 在上述代码中我们无法看到KeyError的执行：因为KeyError是LookupError的子类
# 因此在使用多个except块时，我们必须坚持对其排序，从最具针对性的异常到最通常的异常
try:
    x = d[k / n]
except Exception:  # 捕获所有异常
    print("Something happened")
# 直接写成except：也是可能的，将捕获所有异常，包括来自BaseException的异常
# 如果没有except块匹配该异常，python会沿着调用栈回溯，并寻找适当的异常处理程序。如果找不到，程序将终止
# 如果没有异常产生，那么任意可选的else块都将执行。在所有情况下，finally中的suite块总会执行


def list_find(lst, target):
    try:
        index = lst.index(target)
    except ValueError:
        index = -1
    return index
# 在上面的代码中，有效使用了try...except块，将异常转换为错误值。也可以使用同样的方法捕获某一种异常并产生另一种异常
# python还提供了简单的try...finally块


"""
try:
    try_suite
finally:
    finally_suite
"""
# 将with语句与上下文管理器一起使用，也可以达到try...finally块的效果
# 下列程序从命令行读取一个文件名列表，对其中每个文件，生成一个同名文件，但是后缀名改为.nb,内容上去除原有文件中的空白行
import os
import sys


def read_data(filename):
    lines = []
    fh = None
    try:
        fh = open(filename, encoding="utf8")
        for line in fh:
            if line.strip():  # 用于移除头尾的字符，默认为空格和换行符
                lines.append(line)
    except (IOError, OSError) as err:  # IOError主要指要打开的文件不存在的错误提示
        print(err)
        return []
    finally:
        if fh is not None:
            fh.close()
    return lines


def write_data(lines, filename):
    fh = None
    try:
        fh = open(filename, "w", encoding="utf8")
        for line in lines:
            fh.write(line)
    except EnvironmentError as err:
        print(err)
    finally:
        if fh is not None:
            fh.close()


if len(sys.argv) < 2:
    print("usage: noblanks.py infile1 [infile2 [... infileN]]")
    sys.exit()

for filename in sys.argv[1:]:
    lines = read_data(filename)
    if lines:
        write_data(lines, os.path.splitext(filename)[0] + ".nb")
