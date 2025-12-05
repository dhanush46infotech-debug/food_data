
# ==============================
#   PROGRAM BY DHANUSH KUMAR
# ==============================

from abc import ABC, abstractmethod

# -----------------------------------
# Abstract Base Class (DATA ABSTRACTION)
# -----------------------------------
class Account(ABC):
    def __init__(self, account_number, holder_name, balance=0.0):
        self._account_number = account_number
        self._holder_name = holder_name
        self._balance = float(balance)

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def apply_interest(self):
        pass

    def get_details(self):
        print(f"Account Number: {self._account_number}")
        print(f"Holder Name: {self._holder_name}")
        print(f"Balance: {int(self._balance)}")


# -----------------------------------
# Child Class (Concrete Implementation)
# -----------------------------------
class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance=0.0, interest_rate=0.01):
        super().__init__(account_number, holder_name, balance)
        self._interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposit of ${amount} successful.")
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawal of ${amount} successful.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def apply_interest(self):
        interest = self._balance * self._interest_rate
        self._balance += interest
        print(f"Interest of ${interest} applied.")


# -----------------------------------
# Demo / Main Program
# -----------------------------------
if __name__ == "__main__":

    # Creating a Savings Account
    sa = SavingsAccount("123456789", "Dhanush Kumar", balance=1000, interest_rate=0.01)

    # Showing initial details
    sa.get_details()

    # Deposit
    sa.deposit(500)
    print(f"Balance after deposit: {int(sa._balance)}")

    # Withdrawal
    sa.withdraw(200)
    print(f"Balance after withdrawal: {int(sa._balance)}")

    # Apply interest
    sa.apply_interest()
    print(f"Balance after applying interest: {sa._balance}")
