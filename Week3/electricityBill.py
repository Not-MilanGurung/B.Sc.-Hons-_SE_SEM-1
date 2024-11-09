unit = int(input('Enter the units consumed: '))
rate = float(input('Enter the cost per unit of electricity: '))

def bill(units, rate):
    if units < 0:
        print('Invalid units amount')
        exit()
    elif units<101:
        bill1 = units
        bill2 = 0
        bill3 = 0
    elif units < 201:
        bill1 = 100
        bill2 = units - 100
        bill3 = 0
    else:
        bill1 = 100
        bill2 = 100
        bill3 = units - 200
    result = rate* (bill1 + bill2 * 1.5 + bill3 *2 )
    return result

totalBill = bill(unit, rate)
print(f'The total bill is {totalBill}')

def final(totalBill):
    surcharge = 0
    if totalBill > 150:
        surcharge = totalBill * 0.05
    serviceCharge = totalBill * 0.05
    finalBill = totalBill + serviceCharge + surcharge
    return finalBill, serviceCharge, surcharge

f,sur,ser = final(totalBill)
print(f'The final bill with {ser} service charge and {sur} surcharge is {f}')

        
