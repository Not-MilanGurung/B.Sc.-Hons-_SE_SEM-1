#get three random int (1,100) and print their sum 
#importing the library 
import random
#generating the random values
num1 = random.randint(1,100)
num2 = random.randint(1,100)
num3 = random.randint(1,100)
#storing their sum
sum = num1 + num2 + num3
#printing the output
print(f'The value of {num1}, {num2}, {num3} is {sum}')
