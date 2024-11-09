assign = int(input('Enter the no. of assignment: '))
assignPer = float(input('Enter the avg percentage per assignment: '))
midGrade = float(input('Enter midterm grade in percentage: '))
finGrade = float(input('Enter final exam grade in percentage: '))

def grade(a,aP,mG,fG):
    if mG>100 or mG <0 or fG > 100 or mG < 0 or aP > 100 or aP < 0:
        print('Invalid input')
        exit()
    total = 25 *(mG/100 + fG/100) + 50 * assignPer/100
    return total
total = grade(assign, assignPer, midGrade, finGrade)
def letter(total):
    if total >= 90:
        res = 'A'
    elif total >=80:
        res = 'B'
    elif total >=70:
        res = 'C'
    else:
        res = 'D'
    return res

letter = letter(total)
print(f'The final grade is {total} which is {letter}')