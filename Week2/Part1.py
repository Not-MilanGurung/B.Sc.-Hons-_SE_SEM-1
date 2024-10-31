# // 1+6                // is invalid
myVal = "Hello world"   #does as expected
# in = 10 + 23          # can use in for variable name as it is is a reserved keyword; it is a membership operator
print(10**-2)           # Raises 10 to -2 power
print(46//6)            #Floor divison; result without decimal values

print(type((6+7)+(21.3+2.7)))   #float data type
print(chr(78))                  #Returns letter N
print(ord("X"))                 #UTF-8 value is 88
print(int(5*2.4))               #This first calculates 5*2.4 which is 12.0 and prints the integer part 12
print(int(5) * int(2.4))        #This first gets the integer parts i.e. 5 and 2 then calulates 5 * 2 giving us 10
print(1+2)                      #3 as expected
print(ord("1") + ord("2"))      #The result is 99
print(chr(ord("1") + ord("2") - (1+2))) #That is UTF-8: 96 which is `
