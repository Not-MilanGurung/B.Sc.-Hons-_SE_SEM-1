#get name, addr, age, target year and current year, and show how old the person will be in target year
name = input('Enter your name: ')
addr = input('Enter your address: ')
age = int(input('Enter your age: '))
currentYear = int(input('Enter the current year: '))
targetYear = int(input('Enter the target year: '))

finalAge = age + targetYear - currentYear   #getting the difference between the years and adding to the age

print(f'Hello, my name is {name}, I live in {addr} and in year {targetYear} I will be {finalAge} years old')