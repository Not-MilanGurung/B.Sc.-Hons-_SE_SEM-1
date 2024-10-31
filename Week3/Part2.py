def MyNewFunction():            #Question 1: Defining the function
    print("I get functions!")   #Printing the required sentence

MyNewFunction()                 #Calling the funtion 

def PassAValue(a):                      #Question 2
    print(f'You passed the value: {a}')

PassAValue("Hello")                     #Test cases with function call
PassAValue(5)

def EitherSide(b):                      #Question 3
    print(f"You typed {b}, one less than {b} is {b-1}, one more than {b} is {b+1}")

EitherSide(11)                          #Calling function with test value

def DoubleIt(a):        #Question 4
    return a*2          #Returning the input value after doubling it

num = DoubleIt(12)      #Calling the funtion with test value and storing the output 
print(num)              #Printing the output

def TimesFour(a):       #Question 5
    a = DoubleIt(a)     #Doubling the value
    a = DoubleIt(a)     #Doubling again
    return a    

num = TimesFour(4)      #Call and store
print(num)              #Print output