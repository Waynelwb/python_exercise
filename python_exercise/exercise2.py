#coding:utf-8
'''
Example1: Enter the radius of the circle to get the area of the circle.
'''
import math
r = float(input("Enter your radius: "))
area = math.pi * r * r
print("The area is: ", round(area, 2))


'''
Example2: The letter are encrypted using the scheme of the Caesar Code.
'''
letter = input("Please input an English letter: ")#One letter, not a word.
n = 3
pwd = ord(letter) + n
pwd_letter = chr(pwd)
print(letter, "==>", pwd_letter)

'''
Example3: Case conversion of words.
'''
word = input('Please input an English word: ')
new_lst = []
for i in word:
    if i.islower():
        new_lst.append(i.upper())
    else:
        new_lst.append(i.lower())
new_word = ''.join(new_lst)
print(word, '==>', new_word)

