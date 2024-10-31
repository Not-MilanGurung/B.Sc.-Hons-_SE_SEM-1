def Sum3(a, b, c):
    return a+b+c

def Both(s):
    print(float(s))
    print(int(s))

#! Doesn't account for two biggest numbers being equal 
def Biggest(a, b, c):
    if a > b:
        if a > c:
            res = a
        else:
            res = c
    else:
        if b > c:
            res = b
        else:
            res = c
    return res

def Smallest(a, b, c):
    if a < b:
        if a < c:
            res = a
        else:
            res = c
    else:
        if b < c:
            res = b
        else:
            res = c
    return res

def Mean(a, b, c, d, e):
    return (a+b+c+d+e)/5

def Squared(n):
    return n**2

def IsOdd(n):
    if n%2 != 0: print(n, "is odd")

def IsOddFruitful(n):
    if n%2 == 0: res = False
    else: res = True
    return res

def YourIntAsString(n):
    match n:
        case 0 : res = 'Zero'
        case 1 : res = 'One'
        case 2 : res = 'Two'
        case 3 : res = 'Three'
        case 4 : res = 'Four'
        case 5 : res = 'Five'
        case 6 : res = 'Six'
        case 7 : res = 'Seven'
        case 8 : res = 'Eight'
        case 9 : res = 'Nine'
        case 10: res = 'Ten'
        case _ : res = 'Out of Range'
    return res

def YourStringAsInt(n):
    match n:
        case 'Zero' : res = 0
        case 'One'  : res = 1
        case 'Two'  : res = 2
        case 'Three': res = 3
        case 'Four' : res = 4
        case 'Five' : res = 5
        case 'Six'  : res = 6
        case 'Seven': res = 7
        case 'Eight': res = 8
        case 'Nine' : res = 9
        case 'Ten'  : res = 10
        case _      : res = 0
    return res