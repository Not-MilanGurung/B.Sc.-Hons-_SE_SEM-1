#calculate the bmi from height and weight

kg = float(input('Enter your weight(kg): '))
h = float(input('Enter your height(m): '))

bmi = round(kg/(h*h),2)

print(f'For a weight of {kg}kg and height of {h}m, the BMI is {bmi}')