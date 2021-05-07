# 产生异常
# 有两种可以产生异常的语法
"""
raise exception(args)
raise exception(args) from original_exception
raise
"""
# 使用第一种语法时，指定的异常应该或者是内置的异常，或者继承自Exception的自定义异常
# 如果给定一些文本作为该异常的参数，那么在捕获到该异常并打印时，这些文本应该为输出信息
# 使用第二种语法，也就是没有指定异常时，raise将重新产生当前活跃的异常——如果当前没有，就会产生一个TypeError。
# 自定义异常
# 1.用户自定义异常类型，只要该类继承了Exception类即可，至于类的主题内容用户自定义，可参考官方异常类
# class exceptionName(baseException): pass


class TooLongException(Exception):
    """this is user's Exception for check the length of name """
    def __init__(self, leng):
        self.leng = leng

    def __str__(self):
        print("姓名长度是"+str(self.leng)+"，超过长度了")
# 2.如何手动抛出异常：raise
# 系统的自带的异常只要触发会自动抛出，比如NameError，但用户自定义的异常需要用户自己决定什么时候抛出。
# raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。大多数的异常的名字都以"Error"结尾，
# 所以实际命名时尽量跟标准的异常命名一样。
# 2.手动抛出用户自定义类型异常


def name_test():
    name = input("enter your name:")
    if len(name) > 4:
        raise TooLongException(len(name))  # 抛出异常很简单，使用raise即可,但是没有处理，即捕捉
    else:
        print(name)


# 调用函数，执行
name_test()
"""
-----------------执行时满足条件后抛出一个用户定义的异常如下：--------------------------------------
enter
your
naem: 是打发斯蒂芬
Traceback(most
recent
call
last):
姓名长度是6，超过长度了
File
"D:/pythoyworkspace/file_demo/Class_Demo/extion_demo.py", line
21, in < module >
name_Test()
__main__.TooLongExceptin: < exception
str()
failed >
"""
# 3.捕捉用户手动抛出的异常


def name_test():
    try:
        name = input("enter your naem:")
        if len(name) > 4:
            raise TooLongException(len(name))
        else:
            print(name)
    except TooLongException as e_result:  # 这里异常类型是用户自定义的
        print("捕捉到异常了")
        print("打印异常信息：", e_result)


# 调用函数，执行
name_test()
# 注意，虽然所有类同时继承自 BaseException，但它是为系统退出异常而保留的，假如直接继承 BaseException，可能会导致自定义异常不会被捕获，而是直接
# 发送信号退出程序运行，脱离了我们自定义异常类的初衷。


class InputError(Exception):
    """当输出有误时，抛出此异常"""

    # 自定义异常类型的初始化
    def __init__(self, value): # __init__方法：无需直接调用，生成实例对象的时候自动调用
        self.value = value

    # 返回异常类对象的说明信息
    def __str__(self):
        return "{} is invalid input".format(repr(self.value))


try:
    raise InputError(1)  # 抛出 MyInputError 这个异常
except InputError as err:
    print('error: {}'.format(err))

