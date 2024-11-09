num = int(input('Enter an integer: '))
digit = 0

while num != 0:
    digit += 1
    num = num//10

print(f'The number has {digit} digits')