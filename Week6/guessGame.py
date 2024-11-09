import random

num = random.randint(1,100)
guess = int(input('Guess the number between 1 and 100: '))
while guess != num:
    if guess < num:
        guess = int(input('The number is higher\nTry again: '))
    else:
        guess = int(input('The number is lower\nTry again:'))
print('You guessed right')    
