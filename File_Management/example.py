'''
file_name = 'example.txt'

file = open(file_name, 'w')
file.write('This is the first line of the file.\n')
file.write('This is the second line.\n')
file.close()
print('File created and initial information written.')
'''

import csv

data = [
    ['Name','Age','City'],
    ['Alice',30,'New York'],
    ['Bob',25,'Los Angeles'],
    ['Charlie',35,'Chicago'],
]

file=open('example.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerows(data)
file.close()

print('Data writtern to example.csv')