# OOP Concept
# Class and Object
'''
class Car:
    # Constructor/Initilisation
    def __init__(self, model: str, colour: str, numofPassenger: int, amountofGas: float,
                 engineOn = False, speed = 0, topSpeed = 100) -> None:
        self.model = model
        self.colour = colour
        self.numofPassenger = numofPassenger
        self.amountofGas = amountofGas
        self.engineOn = engineOn
        self.speed = speed
        self.topSpeed = topSpeed
    
    def displayInfo(self):
        print(f"{self.model, self.colour, self.numofPassenger, self.amountofGas}")

    def startEngine(self):
        self.engineOn = True
        return f'The {self.model} engine is now on.'
    
    def stopEngine(self):
        self.engineOn = False
        return f'The {self.model} engine is now off.'
    
    def accelerate(self):
        if not(self.engineOn): return 'The car engine is off'
        if self.speed < self.topSpeed:
            self.speed += 10
        else:
            return f'{self.model} can not accerelate beyond {self.topSpeed}'
        

    def brake(self):
        if self.speed > 0:
            self.speed -=10
        else:
            return 'The car is stationery'
car1 = Car('Honda Civic', 'Blue', 5, 10.0)
car2 = Car('Hurrican', 'Red', 15, 25.0)

print(car1.startEngine(), car1.speed, car1.brake(), car1.accelerate(), car1.speed, car1.accelerate(),
      car1.speed, car1.brake(), car1.speed, car1.brake(), car1.speed)

for i in range(1, 12):
    print(car1.accelerate(), car1.speed)

car1.stopEngine()
print(car1.accelerate())
'''

'''
from datetime import date
class Employee:


    def __init__(self, name: str, salary: int, age: int, bonusPercentage = 0.1):
        self.name = name
        self.salary = salary
        self.age = age
        self.bonus = bonusPercentage

    def displayDetail(self):
        print(f"Name: {self.name}\n"
              f"Salary: {self.salary}\n"
              f"Age: {self.age}")
        
    def bonusSalary(self):
        bonus = self.bonus * self.salary
        print(f'The bonus of {self.name} is {bonus}')

    def dob(self):
        dob = date.today().year - self.age
        print(f'The dob of {self.name} is {dob}')

emp1 = Employee('Ram', 15_000, 39)
emp2 = Employee('Shyam', 20_000, 18)  

emp1.displayDetail()
emp1.bonusSalary()
emp1.dob()
print('')
emp2.displayDetail()
emp2.bonusSalary()
emp2.dob()
'''