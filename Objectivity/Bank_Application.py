class BankAccount:
    def __init__(self, owner, balance,):
        self.owner= owner
        self.balance= balance

    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self,value):
        self._owner= value
    @property
    def balance(self):
        return self.balance
    @balance.setter
    def balance(self,value):
        self._balance= value

    def check_balance(self):
        return f"Funds {self._owner} that: {self._balance}"

    def transfer(self, recipient, amount):
        try:
            if amount <= self._balance:
                self._balance -= amount
                recipient._balance += amount
                print(f"Transferred {amount} to {recipient.owner}")
            else:
                print("Transfer failed. Insufficient funds.")
        except Exception as e:
            print(f"The funds in Balance are unavailable {e}")




account_1= BankAccount("Tobiasz Fuczek", 1000)
account_2= BankAccount("Robert Lewandowski", 350)

print(account_1.check_balance())
print(account_2.check_balance())

account_1.transfer(account_2, 100)

print(account_1.check_balance())
print(account_2.check_balance())