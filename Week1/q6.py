#get mrp and discount rate to calculate the final price
mrp = int(input("Enter the mrp of the product: "))
disRate = float(input("Enter the discount rate: "))
finalPrice = mrp*(1-disRate/100)
print(f'The final price is {finalPrice}')