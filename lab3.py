# Exercise2 Write a Python program to sort  a tuple by its float element
x = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print("Sample data: ", x)
x.sort(key=lambda t: float(t[1]), reverse=True)
print('Expected output:', x)

# Exercise3 Write a Python program to sort a given matrix in ascending order according to the sum of its row
z = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
y = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
print('Original Matrix: ', z)
z.sort(key=lambda n: n[0]+n[1]+n[2], reverse=False)
print("Sorted: ", z)
print('Original Matrix: ', y)
y.sort(key=lambda n: n[0]+n[1]+n[2], reverse=False)
print('Sorted: ', y)

# Exercise1 Write a program that asks a string to the user, and counts the number of time each character occurs in the
# string
s = input("Please enter a string: ")
print([(n, s.count(n)) for n in sorted({x for x in s}, key=s.index)])

# Exercise2 Repeat exercise1, but in such a way that the program outputs a set
s = input("Please enter a string: ")
print({(n, s.count(n)) for n in sorted({x for x in s}, key=s.index)})

# Exercise3 Repeat exercise1, but in such a way that program outputs a dictionary
dic = dict()
d = {}
s = input("Please enter a string: ")
for x in s:
    d[x] = s.count(x)
print(d)

# Exercise4
student1 = ["number", "grade1", "grade2", "Avg"]
student2 = ["number", "grade1", "grade2", "Avg"]
student3 = ["number", "grade1", "grade2", "Avg"]
student4 = ["number", "grade1", "grade2", "Avg"]
for i in range(4):
    if i == 0:
        x = input("Student 1 number: ",)
        student1[0] = x
        y = input("Student {0} grade 1: ".format(student1[0]),)
        student1[1] = y
        z = input("Student {0} grade 2: ".format(student1[0]),)
        student1[2] = z
        student1[3] = float((int(y) + int(z)) / 2)
    elif i == 1:
        x = input("Student 2 number: ", )
        student2[0] = x
        y = input("Student {0} grade 1: ".format(student2[0]), )
        student2[1] = y
        z = input("Student {0} grade 2: ".format(student2[0]), )
        student2[2] = z
        student2[3] = float((int(y) + int(z)) / 2)
    elif i == 2:
        x = input("Student 3 number: ", )
        student3[0] = x
        y = input("Student {0} grade 1: ".format(student3[0]), )
        student3[1] = y
        z = input("Student {0} grade 2: ".format(student3[0]), )
        student3[2] = z
        student3[3] = float((int(y) + int(z)) / 2)
    else:
        x = input("Student 4 number: ", )
        student4[0] = x
        y = input("Student {0} grade 1: ".format(student4[0]), )
        student4[1] = y
        z = input("Student {0} grade 2: ".format(student4[0]), )
        student4[2] = z
        student4[3] = float((int(y) + int(z)) / 2)
print("{0} {1} {2} {3}".format('Number', 'Grade1', 'Grade2', 'Avg'))
print("{0:6} {1:6} {2:6} {3}".format(student1[0], student1[1], student1[2], student1[3]))
print("{0:6} {1:6} {2:6} {3}".format(student2[0], student2[1], student2[2], student2[3]))
print("{0:6} {1:6} {2:6} {3}".format(student3[0], student3[1], student3[2], student3[3]))
print("{0:6} {1:6} {2:6} {3}".format(student4[0], student4[1], student4[2], student4[3]))
