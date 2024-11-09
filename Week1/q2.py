#get length and breadth, and print area and perimeter of rectangle

#taking input
l = float(input('Enter the length of rectangle: '))
b = float(input('Enter the breadth of rectangle: '))
#calculating values
area = l * b
perimeter = 2*(l+b)
#printing the output
print(f'The area of rectangle with length {l} & breadth {b} is {area}')
print(f'The perimeter of rectangle with length {l} & breadth {b} is {perimeter}')