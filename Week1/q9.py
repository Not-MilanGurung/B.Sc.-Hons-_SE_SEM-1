#convert seconds into hh:mm:ss
inSec= int(input('Enter the seconds: '))

sec = inSec%60      #get the remaining seconds not converted into round minutes
temp = int(inSec/60)    #convert seconds into minute without remainder
min = temp%60       #get the remaining minutes not converted into round hours
hour = int(temp/60)

print(f'{inSec} seconds isequivalent to {hour} hour, {min} minute, and {sec} second')