# 函数的创建和调用
import random


def get_int(msg):
    while True:
        try:
            i = int(input(msg))
            return i
        except ValueError as err:
            print(err)


age = get_int("enter your age: ")

x = random.randint(1, 6)
y = random.choice(["apple", "banana", "cherry", "durian"])
print(x)
print(y)
