#Getting Input
print("A standard sized egg box holds 6 eggs")
eggs = int(input("How many eggs do you need to pack?: "))

#Calculating the boxes completely filled and extra eggs left
extraEggs = eggs % 6
boxes = eggs // 6
#Checking if extra box is needed, and if so how much of it is empty
if extraEggs != 0: 
    boxes+=1
    emptySpaces = 6 - extraEggs
else:
    emptySpaces = 0

#Printing the result
print(f"You will need {boxes}")
print(f"The last box will have {emptySpaces} empty spaces")