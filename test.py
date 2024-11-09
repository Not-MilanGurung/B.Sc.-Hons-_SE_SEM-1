dis_limit={
    10_000 : 5,
    15_000 : 10,
    25_000 : 15
}


prizes={
    1 : 'T-Shirt',
    2 : 'Bottle',
    3 : 'Rs 100 Coupon',
    4 : 'Phone',
    5 : 'Toblorone'
}

import random
def spin():
    key = random.randint(1,5)
    if key in prizes.keys():
            y = prizes[key]
            print(f'You win {y}')
    
def discount(cost):
    dis = 0
    spin = False
    if cost < 5_000:
        if cost > 1_000:
                spin = True
    else: 
        dis = dis_limit[10_000]
        if cost > 10_000:
            dis = dis_limit[15_000]
            if cost > 15_000:
                dis = dis_limit[25_000]
    discount = cost * dis/100
    bill = cost - discount
    return bill, discount, spin

cost = int(input('Enter the total cost of the goods: '))
bill, discount, spin1 = discount(cost)

print(f'The final bill with {discount} discount is {bill}')
if spin1:
    print('You are eligible for a spin!')
    spin()

