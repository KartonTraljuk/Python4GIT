"""
This is module of my homework 10
"""
# Task 1,2,3. Create ur version of calculator, use try/except blocks
# use ur customclass of exceptoins


result = 0

# 1st number
number_1 = input("Enter your 1 number: ")
if number_1.isdigit():
    number_1 = int(number_1)
    print(number_1)
else:
    print("You enter wrong type!!!")

# 2nd number
number_2 = input("Enter your 2 number: ")

if number_2.isdigit():
    number_2 = int(number_2)
    print(number_2)
else:
    print("You enter wrong type!!!")

# operation
from exception import MyError
# !!!!!!!!!!!!!!!
# mathematics
if oper == '+':
    result = number_1 + number_2
    print(f'Your result is: {number_1} + {number_2} = {result}')

elif oper == '-':
    result = number_1 - number_2
    print(f'Your result is: {number_1} - {number_2} = {result}')

elif oper == '*':
    result = number_1 * number_2
    print(f'Your result is: {number_1} * {number_2} = {result}')

elif oper == '/':
    if number_2 == 0:
        print("Devision by zero")
    else:
        rezult = number_1 / number_2
        print(f'Your result is: {number_1} / {number_2} = {result}')
else:

    print("You choose wrong operation!!!")

