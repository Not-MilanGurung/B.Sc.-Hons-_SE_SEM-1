'''
def sumof2nums(num1, num2):
    sum = num1 + num2
    return sum
n1 = int(input('Enter a number: '))
n2 = int(input('Enter another number: '))
result = sumof2nums(n1, n2)
print(result)

def largest3(num1,num2,num3):
    if num1>num2 and num1> num3:
        result = f'The largest is {num1}'
    elif num2>num1 and num2>num3:
        result = f'The largest is {num2}'
    elif num3>num1 and num3>num2:
        result = f'The largest is {num3}'
    else:
        result = 'Either two or more numbers are equal or an error occured'
    return result
output = largest3(7,7,6)
print(output)

def arthimatic(num1, num2, operation):
    if operation == '+':
        sum = num1 + num2
        result = f'{num1} + {num2} = {sum}'
    elif operation == '-':
        diff = num1 - num2
        result = f'{num1} - {num2} = {diff}'
    elif operation == '*':
        multi = num1 * num2
        result = f'{num1} * {num2} = {multi}'
    elif operation == '/':
        div = round(num1 / num2, 4)
        result = f'{num1} / {num2} = {div}'
    else:
        result = 'Error'
    return result
n1 = int(input('Enter a number: '))
n2 = int(input('Enter another number: '))
op = input('Enter the symbol corresponding to the operation(+,-,*,/): ')
output = arthimatic(n1, n2, op)
print(output)

def is_leap_year(year):
    if year%4==0 and (year%100!=0 or year%400==0):
        result = 'leap year'
    elif year%4!=0 or (year%100==0 and year%400!=0):
        result = 'not a leap year'
    else:
        result = 'error'
    return result

year = int(input('Enter the year: '))
output = is_leap_year(year)
print(output)

def calculate_grade(mark):
    if mark > 100:
        result = 'Invalid'
    elif mark >= 90:
        result = 'A'
    elif mark >= 80:
        result = 'B'
    elif mark >= 70:
        result = 'C'
    elif mark >= 60:
        result = 'D'
    elif mark >= 0:
        result = 'F'
    else:
        result = 'Invalid'
    return result

marks = int(input('Enter your marks(0-100): '))
output = calculate_grade(marks)
print(f'Your grade is {output}')

def cost(itemCost, quantity):
    return itemCost * quantity

def totalCost(cost1, cost2):
    return cost1 + cost2

def discount(tCost):
    if tCost > 1000:
        result = tCost * 0.9
        dis = tCost * 0.1
    elif tCost > 500:
        result = tCost * 0.95
        dis = tCost * 0.05
    else:
        result = tCost
        dis = 0
    return result, dis

print('First item: ')
name1 = input('Enter the name: ')
price1 = int(input('Enter the price: '))
quantity1 = int(input('Enter the quantity: '))

print('\nSecond Item: ')
name2 = input('Enter the name: ')
price2 = int(input('Enter the price: '))
quantity2 = int(input('Enter the quantity: '))

output1 = cost(price1, quantity1)
print(f'The total cost of {name1} is {output1}')
output2 = cost(price2, quantity2)
print(f'The total cost of {name2} is {output2}')
total = totalCost(output1, output2)
print(f'\nThe total cost of everything is {total}')

final, dis = discount(total)
print(f'\nThe final bill is {final} with {dis} discount ')
'''

hourlyWage = float(input('Enter the hourly wage: '))
regularHours = float(input('Enter the regular hours worked: '))
overTimeHours = float(input('Enter the over time hours worked(0 if none): '))
if regularHours < 0.0 or overTimeHours < 0.0 or (hourlyWage < 0
    or (regularHours + overTimeHours)> 80):
    print('Error')
    exit()
def salary(regularHours, overTimeHours):
    if regularHours > 40.0:
        extra = regularHours - 40
        regularHours -= extra
        overTimeHours += extra
    return regularHours* hourlyWage + overTimeHours * hourlyWage * 1.5

totalSalary = salary(regularHours, overTimeHours)
print(f'The salary this week is {totalSalary}')

def tax(totalSalary):
    if totalSalary > 5000.0:
        result = totalSalary * 0.8
    elif totalSalary > 3000.0:
        result = totalSalary * 0.9
    else:
        result = totalSalary
    return result

finalSalary = tax(totalSalary)
print(f'The final salary after tax is {finalSalary}')