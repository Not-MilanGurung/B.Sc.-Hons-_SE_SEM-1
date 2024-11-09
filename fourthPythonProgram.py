'''
num = int(input('Enter an integer: '))

if num > 0:
    print(f'{num} is positive')
    if num % 2 == 0:
        print(f'{num} is even')
        if num < 10:
            print(f'{num} is smaller than 10')
        else:
            print(f'{num} is greater or equal to 10')
    else:
        print(f'{num} is odd')
else:
    print(f'{num} is negetive or zero')

age = int(input('Enter your age:'))
def vote(age):
	if 0 < age < 121:
		if age > 17:
			res = 'You can vote'
		else:
			res = 'You can not vote'
	else:
		res = 'Enter a valid age'
	return res

output = vote(age)
print(output)

b = int(input('Enter an number'))
def calculation(a):
	def sum(b):
		sum = a+b
		return sum
	def sub(b):
		sub = b - a
		return sub
	return sum(b), sub(b)

print(calculation(10))
'''
def sum():
	sum = num1 + num2
	print(sum)
num1 = 10
num2 = 20
sum()
