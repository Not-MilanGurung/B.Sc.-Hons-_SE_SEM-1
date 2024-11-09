'''
fname = input('First Name :')
lname = input('Last Name :')
print('Welcome',fname, lname)

a=int(input("Num 1: "))
b=int(input("Num 2: "))
c=int(input("Num 3: "))
sum = a+b+c
print(f'Sum of {a},{b}&{c} is {sum}')
import math
n = int(input("Enter a number: "))
f = math.factorial(n)
print('Factorial of', n,'=',f)

import random
n1 = random.randint(1,int(1e2))
n2 = random.randint(1,int(1e2))
n3 = random.randint(1,int(1e2))
sum = n1+n2+n3
print(f'Sum of 3 random values {n2} + {n3} + {n1} is {sum}')

import datetime
name = input("Enter your name: ")
age = int(input("Enter your age: "))
addr= input("Enter your addres: ")
currentyear = datetime.date.today().year
targetyear = int(input('Enter the target year: '))
futrueage= age + (targetyear - currentyear)
print(f'Hello, my name is {name}. I live in {addr} and in year {targetyear} I will be {futrueage} years old.')

length = int(input('Enter the length: '))
breadth = int(input('Enter the breadth: '))
area = length * breadth
perimeter = 2*(length * breadth)
print(f'The area of the rectangle({length} & {breadth}) is {area}')
print(f'The perimeter of the rectangle({length} & {breadth}) is {perimeter}')

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius*9/5)+32
print(f'The temperature in Fahrenheit is {fahrenheit}')

npr = int(input("Enter amount in Nepali Rupee: "))
inrConver = 1.6
usdConver = 134.61
euroConver = 148.34
inr = round(npr/inrConver,2)
usd = round(npr/usdConver,2)
euro = round(npr/euroConver,2)
print(f'The equivalent in INR = {inr}, USD = ${usd} and EURO = {euro}')
'''

mrp = int(input("Enter the mrp of the product: "))
disRate = float(input("Enter the discount rate: "))
finalPrice = mrp*(1-disRate/100)
print(f'The final price is {finalPrice}')