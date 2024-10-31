def Dont():
    print("Don't eat it")

def EatIt():
    print('EAT IT')

def Cat():
    inp = input('Did the cat lick it?: ')
    if inp == 'n':
        EatIt()
    elif inp == 'y':
        inp = input('Is your cat healthy?: ')
        if inp == 'y':
            EatIt()
        elif inp == 'n':
            print('Your call')

def ShouldIEatDroppedFood():
    print('Answer with y as Yes and n as No')
    inp = input('Did anyone see you?: ')
    if inp == 'y':
        inp = input('Was it a boss/lover/parent?: ')
        if inp == 'n':
            EatIt()
        elif inp == 'y':
            inp = input("Was it expensive?: ")
            if inp == 'y':
                inp = input('Can you cut off the part that touched the floor?: ')
                if inp == 'y':
                    EatIt()
                elif inp == 'n':
                    print('Your call')
            elif inp == 'n':
                inp = input('Is it bacon?: ')
                if inp == 'y':
                    EatIt()
                elif inp == 'n':
                    Dont()
    elif inp == 'n':
        inp = input('Was it sticky?: ')
        if inp == 'y':
            inp = input('Is it a raw steak?: ')
            if inp == 'y':
                inp = input('Are you a puma?: ')
                if inp == 'y':
                    EatIt()
                elif inp == 'n':
                    Dont()
            elif inp == 'n':
               Cat()
        elif inp == 'n':
            inp = input('Is it an Emausaurus?: ')
            if inp == 'n':
                Cat()
            elif inp == 'y':
                inp = input('Are you a Megalosaurus?: ')
                if inp =='y':
                    EatIt()
                elif inp == 'n':
                    Dont()

ShouldIEatDroppedFood()