print(
    True and True,                      #True as expected
    True and False or True,             #True as it in both orders the answer is the same
    False or False and True,            #False as the answer for both cases is the same
    not False and True,                 #True as expected
    not(True or not(False and False)),  #False as expected
    (10>14) and (4==5),                 #False as both terms are false
    True and 5,                         #5, when terms are True or integer, and returns the value on the right
    False or 0,                         #0, when the result is false, the operater returns value on the right if it is also false otherwise it returns false
    7 and 5,                            #5, when the result is true and integers are involved, amd operater returns the value on the right
    (3*4) != (14-2) or ('C'>='D')       #False as both conditions are false
)