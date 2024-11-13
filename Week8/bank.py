class Bank:
    def __init__(self, account_holder: str, balance: int) -> None:
        self.account_holder = account_holder
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, newBalance: int):
        self.__balance = newBalance

    def withdraw(self, amount: int) -> str:
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f'Withdrew {amount}. New balance is {self.__balance}'
        elif amount < 0:
            return 'Enter a positive value'
        else:
            return 'Insuffecient balance'
        
    def deposit(self, amount: int) -> str:
        if amount > 0:
            self.__balance += amount
            return f'Deposited {amount}. New balance is {self.__balance}'
        else:
            return 'Invalid deposit amount'
    
    def viewbalance(self) -> str:
        return f'{self.account_holder}, your balace is {self.__balance}'
    



class SavingAccount(Bank):
    
    def __init__(self, account_holder: str, balance:int, interest_rate: int):
        super().__init__(account_holder, balance)
        self.__interest_rate = interest_rate

    def interest(self):
        interest = self.get_balance() * self.__interest_rate/100
        self.set_balance(self.get_balance() + interest)
        return f'Interest aquired is {interest}, the new balance is {self.get_balance()}'
        


class FixedDepositAccount(Bank):
    def __init__(self, account_holder: str, balance: int, interest_rate: int, term_years: int) -> None:
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
        self.term_years = term_years

    def calculate_maturity_value(self):
        maturity_value = self.get_balance() * (1 + (self.interest_rate/100) * self.term_years)
        return f'At the end of {self.term_years} years, the maturity value will be {maturity_value}'
    
    def withdraw(self, amount: int) -> str:
        if self.term_years > 0:
            penalty = amount * 0.02
            amount_after_penalty = amount - penalty
            new_balance = self.get_balance() - amount_after_penalty
            return f'Withdrew {amount} with a 2% penalty. New balance is {new_balance}'
        else:
            return super().withdraw(amount)
        
fix = FixedDepositAccount('Jon', 10_000, 7, 10)

print(fix.deposit(1_000))
print(fix.withdraw(500))
print(fix.calculate_maturity_value())



