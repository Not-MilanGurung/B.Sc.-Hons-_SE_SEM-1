#given nested list
result = [[70,86,76], [86,92,57], [59,65, 88]]

avg_terminal = []
mcct_avg = 0
os_avg = 0
se_avg = 0
termCount = 0

for i in result:
    sum = 0         #var used to store sum of all subjects of a term
    termCount += 1  
    #getting the values from the indices and getting the sums
    mcct_avg += i[0]
    os_avg += i[1]
    se_avg += i[2]
    #looping through individual value 
    for j in i:
        sum += j
    avg_terminal.append(round(sum/3, 2))

#finding the averages from their sums and rounding
mcct_avg =round(mcct_avg/termCount, 2)
os_avg = round(os_avg/termCount, 2)
se_avg = round(se_avg/termCount, 2)

print(f'The average of each terms are {avg_terminal}')
print(f'Average of MCCT: {mcct_avg}')
print(f'Average of OS: {os_avg}')
print(f'Average of SE: {se_avg}')    
