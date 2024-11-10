'''
n = int(input('Enter the end point: '))
sum = 0
i = 10
while i >= n:
    sum += i
    #print(i)
    i -=1
print(sum)

password = input('Please enter the password: ')
while password != 'secret':
    password = input('Incorrect password. Try again: ')
print('You have entered the correct password')

m = int(input('Enter a integer: '))
e = 10
i = 1

while i <= 10:
    print(f'{m} x {i} = {m*i}')
    i+=1


sum = 0
start = 1
stop = 100
for i in range(start ,stop+1):
    sum += i
print(sum)

sum = 0
stop = 100
i = 1
while i <= stop:
    sum += i
    i += 1
print(sum)

num = int(input('Enter a number: '))
sum = 0
for i in str(num):
    sum += int(i)
print(f'The sum of its digits is {sum}')

myList = [5, 7,12,9,4,6,8,9]
print(len(myList))
myList.append('lion')
print(myList)
myList.insert(3,'Cat')
print(myList)
del(myList[5])
print(myList)
myList.reverse()
print(myList)
'''

fruits = ['apple', 'banna', 'pear']
fruits[2] = 'coconut'
print(fruits)
del fruits[0]
print(fruits)
fruits.insert(2, 'pear')
print(fruits)
fruits.append('peach')
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)