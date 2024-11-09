items = int(input('Enter the number of items: '))
rate = float(input('Enter the price per item: '))

def discount(items, rate):
    tcost = items * rate
    if tcost > 300:
        dis = 10
    else:
        dis = 0
    final = tcost * (1-dis/100)
    return final, tcost, dis

final, tcost, dis = discount(items, rate)
amount = final * 1.05
print(f'The total cost is {tcost}')
print(f'After {dis}% discount and 5% tax, the final amount is {amount}')