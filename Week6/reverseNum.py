num = int(input('Enter an integer: '))
rev = 0
while num != 0:
    rev = rev*10 + num%10
    num = num//10
print(f'The reverse is {rev}')