'''
a = '4.8'
b = 4
c = 4.8
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

num1 = 5
num2 = 10
num3 = 15
if num1 > num2 and num1 > num3:
    print('num1 is greatest')
elif num2 > num1 and num2 > num3:
    print('num2 is greatest') 
else:
    print('num3 is greatest')

num = int(input('Enter an integer: '))
if num == 0:
    print(f'{num} is zero')
elif num % 2 == 0:
    print(f'{num} is even')
else:
    print(f'{num} is odd')

name = input('Enter your name: ')
age = int(input('Enter your age: '))

if age <18:
    vote = 'can not'
else:
    vote = 'can'

if age >0 and age <120:
    print(f'Their name is {name} and since their age is {age}, they {vote} vote')
else:
    print('Invalid age')

def avg(n1,n2,n3):
    average = (n1+n2+n3)/3
    print(f'The average of {n1}, {n2}, {n3} is {average}')
avg(2,5,8)

import datetime
def agetoYear(age):
    year = datetime.date.today().year - age
    return year

def gen(dob):
    if 1964< dob < 1980:
        print('Gen X')
    elif 1979< dob < 1996:
        print('Millennial')
    elif 1994< dob < 2013:
        print('Gen Z')
    elif 2012< dob < 2025:
        print('Gen Alpha')
    else:
        print('Out of range')

name = input('Enter your name: ')
age = int(input('Enter your age: '))

print(f'Your name is {name} and you are ')
gen(agetoYear(age))


def sugg(temp):
    if 60 > temp > 29:
        print('Wear shorts and a t-shirt')
    elif 19 < temp:
        print('Wear a light jacket')
    elif 9 < temp :
        print('Wear a sweater')
    elif -60 < temp:
        print('Wear a heavy coat')
    else:
        print('Run for your life')

sugg(int(input('Enter the temperature in Celsius: ')))
  '''  