# Created with Python AI
# Exercise1
try:
    x = input("Please enter a two-digit positive integer number:")
    y = []
    y += x
    print(y[0])
    print(y[1])
except ValueError as err:
    print(err)

# Exercise2
try:
    x = int(input("Please enter the number of seconds:"))
    day = x // 86400
    y = x - day * 86400
    hours = y // 3600
    z = y - hours * 3600
    minutes = z // 60
    seconds = z - minutes * 60
    print(x, " seconds correspond to ", day, ' day, ', hours, " hours, ", minutes, " minutes, ", seconds, " seconds.")
except ValueError as err:
    print(err)

# Exercise3
import operator

try:
    x = input("Please enter a string:")
    z = []
    z += x
    y = list(reversed(z))
    if operator.eq(z, y):
        print(x, " is a palindrome")
    else:
        print(x, " is not palindrome")
except EOFError as err:
    print(err)

# Exercise4
x = input("Please enter a sentence: ")
y = x.split(" ")
z = len(y)
word = max(y, key=len, default='')
print("The sentence has ", z, ' words and the longest word is ', word)
