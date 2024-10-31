cond={
    3 : 'Fizz',
    5 : 'Buzz'
}

list = range(1,101,1)

i = 0 #letting exec() access the variable in the loop

def calc():
    for i in list:
        out = ''
        for x,y in cond.items():
            if i % x == 0:
                out += y
        if out == '':
            out = i
        print(out)

calc()