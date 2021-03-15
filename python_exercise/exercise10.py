x = "fhksfhks\
djfhfhk"
print(x)

t = "jffsjfs" +\
    "jfjskdfkj"
print(t)

s = ("kfskjhfkjf" 
     "sdjfhkfhefekj")
print(s)

# 以上三个可以达到相同的效果
# 前两个需要转义换行

"""
字符串支持通常的比较操作符，这些操作符在内存中逐个字节对字符串进行比较
"""

"""
字符串分片和步距：
从左向右从0递增，从右像左从-1递减
"""

"""
字符串索引的两个方法：
str.index(t, start, end) and str.find(t, start, end)
下面给出两个函数实例：
"""


def extract_from_tag1(tag, line):
    opener = "<" + tag + ">"
    closer = "</" + tag + ">"
    try:
        i = line.index(opener)
        start = i + len(opener)
        j = line.index(closer, start)
        return line[start:j]
    except ValueError:
        return None


def extract_from_tag2(tag, line):
    opener = "<" + tag + ">"
    closer = "</" + tag + ">"
    i = line.find(opener)
    if i != -1:
        start = i + len(opener)
        j = line.find(closer, start)
        if j != -1:
            return line[start:j]
    return None
