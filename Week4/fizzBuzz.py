def main(list, cond):

    def multiple(i,x):
        if i % x == 0:
            res = True
        else:
            res = False
        return res
    for i in list:
        out = ''
        for x,y in cond.items():
            if y[1] == 0:
                if multiple(i, x):
                    if y[2] == 0:
                        out += y[0]
                    else:
                        out = y[0]
                        break
        if out == '':
            out = i
        print(out)



cond = {
    3 : ['Fizz', 0, 1],
    5 : ['Buzz', 0, 0]
} 

list = range(1,101)

main(list, cond)