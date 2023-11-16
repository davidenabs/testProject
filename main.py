# # myVariable = "Hello Africa"
# #
# # print(myVariable)
# #
# # x = 10
# # y = 20
# # z = x + y
# #
# # print(type(myVariable))
#
# # x = str(6)
# # print(x)
#
# # Strings
#
# # myStr = "This is my single line string"
# #
# # multiLineStr = """This is a short story about myself.
# # I am David Enabs.
# # I love coding.
# # """
# #
# # print(myStr)
# # print(multiLineStr)
#
# # name = 'David'
#
# # print(name[0])
# # print(name[1])
# # print(name[2])
# # print(name[3])
# # print(name[4])
#
# # print(len(name))
# #
# # text = "This is the second python class we're having"
# # checker = 'David' not in text
# # print(checker)
#
# word = "Transformation "
# # print(word[2:5])
# # print(word[:5])
# # print(word[5:])
# # print(word[-1])
# # print(word[-5:-2])
# # print(word[-2:-5])
# #
# # print(word.upper())
# # print(word.lower())
# # print(word.strip())
#
#
# # print(word[2], word[5])
# # print(word[5])
#
# txt = "Hello world"
# result = txt.split(' ')
# print(result)
# print(result[0])
# print(result[1])

# a = "Hello, World!"
# print(a.replace("Hello", "Hi"))


# a = "Hello"
# b = "World"
# c = a + ' ' + b
# print(c)

# age = 19
# sen = 'Hello, I am ' + str(age) + ' years old'
# print(sen)
#
# sen1 = 'Hello, I am {} years old'
# print(sen1.format(age))
#
# apple = 2
# orange = 3
# watermelon = 1
# mylist = ['a', 'b', 'c']
# sen1 = 'i have {} apples and {} oranges including {} watermelon. {}'
# print(sen1.format(apple, orange, watermelon, mylist))
#
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))
#
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))
#
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = f"I want {quantity} pieces of item {itemno} for {price} dollars."
# print(myorder)


# msg = ' we\'re playing football '
# msg = "We are the so-called \"Vikings\" from the north."
# print(msg.upper())

# Boolean

# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# a = 200
# b = 33
#
# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")
#
# print(bool(""))
# print(bool(0))

# Operators
# a = 100
# b = 25
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a // b)
# print(a ** b)

# x = 10
# x += 3 # x = x + 3
# print(x)
# x -= 3  # x = x + 3
# print(x)
# x /= 3 # x = x + 3
# print(x)
# x *= 3 # x = x + 3
# print(x)
# x **= 3 # x = x + 3
# print(x)
# x %= 3 # x = x + 3
# print(x)

# List

# myList = [100,3,42,4,5,2,57,8,9]

# print(myList[2])
# print(myList[1:8:2])

# print(myList)

# changing values in a list
# using index number eg [0]

# myList[0:4] = [100,205,606,111]
# myList[5] = 0

# print(myList)

# using insert function
# myList.insert(0, 150)
# print(myList)

# Adding value to a list

# myList.append('Last element came in')
# myList.append(10)
# list2 = [10,2,23]
# myList.append(list2)
# print(myList + list2)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)
#
# thislist.remove('apple')
# thislist.pop(1)
# thislist.pop()
#
# del thislist[0]
#
# thislist.clear()
#
# print(thislist)




# lists = [
#     'David',
#     30,
#     {'name': 'Dan', 'age': 10},
#     True,
#     16.9,
#
# ]
#
# print(len(lists))

# myList = ["apple", "banana", "cherry"]
# print(myList[0])
# print(myList[1])
# print(myList[2])

# for kosi in myList:
#     print(kosi)

# for i in range(len(myList)):
#     # print(i)
#     print(myList[i])

# 

# def countdown(n):
#     print(n)
#     if n == 0:
#         return             # Terminate recursion
#     else:
#         countdown(n - 1)   # Recursive call
#
#
# countdown(5)

# File Handling
# r ,a , w, x
# openFile = open("C:\\Users\\USER\Documents\pythonTask4.txt", 'r')
# # print(openFile.readline())
# for line in openFile:
#     print(line)
# openFile.close()
# x = input()
# file = open('thisfiledoesnotexist.txt', 'a')
# file.write('\nJust wrote this now!')
# file.close()
#
# file = open('demo.txt', 'r')
# print(file.read())
# file = open('thisfiledoesnotexist.txt', 'x')
# import os
#
# # os.remove('thisfiledoesnotexist.txt')
#
# if os.path.exists("thisfiledoesnotexist.txt"):
#   os.remove("thisfiledoesnotexist.txt")
#   print('file removed')
# else:
#   print("The file does not exist")
#
#   os.rmdir('test')


# Error Handling

# print(x)
# try:
#   print(x)
# except IndentationError:
#   print("An exception occurred")

# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

# print(x)

# x = -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")














