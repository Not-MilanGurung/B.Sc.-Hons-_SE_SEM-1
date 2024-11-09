days = int(input('Enter the number of days rented: '))
rate = float(input('Enter the base daily rental rate: '))

def cost(days, rate):
    tcost = days * rate
    insu = days * 10
    if days > 7:
        dis = 15
    elif days > 3:
        dis = 10
    else:
        dis = 0
    final = (tcost + insu) * (1-dis/100)
    return final, tcost, insu, dis

final, tcost, insu, dis = cost(days, rate)
print(f'The total cost with rental cost {tcost}, insurance cost {insu} '
        f'and a discount of {dis}% is {final}')
if final > 500:
    tax = 3
else:
    tax = 0
finalAmount = final * (1+tax/100)
print(f'The final amount with {tax}% tax is {finalAmount}')
    
