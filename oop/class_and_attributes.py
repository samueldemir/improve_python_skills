from abc import ABC, abstractmethod


class Account(ABC):
    acc = 1

    def __init__(self):
        Account.acc += 1
        self.__balance = 5000
        self.__acc_number = Account.acc
        self.__acc_name = input("Enter name: ")
        print(self.__acc_name)

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amt):
        self.__balance = amt

    def deposit(self):
        print("Deposit")
        amt = int(input("Enter the amount of deposit: "))
        self.balance += amt

    def acc_info(self):
        print("Account No : ", self.__acc_number)
        print("Account Name : ", self.__acc_name)
        print("Balance: ", self.balance)

    @abstractmethod
    def withdraw(self):  # AbstractMethod
        pass


class SavingsAccount(Account):
    """
    Sparbuch
    """
    def __init__(self):
        super().__init__()
        self.__min_balance = 5000
        print("SavingsAccount")

    def withdraw(self):
        amt = int(input("Enter the amount to withdraw: "))
        if self.balance - amt >= self.__min_balance:
            self.balance -= amt
        else:
            print("Minimum achieved. Cannot withdraw.")


class CurrentAccount(Account):
    """
    Girokonto
    """
    def __init__(self):
        super().__init__()
        self.__odlimit = 50000

    def withdraw(self):
        amt = int(input("Enter the amount to withdraw: "))
        if self.balance - amt >= self.balance:
            self.balance -= amt
        elif amt <= self.__odlimit:
            self.__odlimit -= amt
        else:
            print(
                "Cannot withdraw. "
                "Amount to withdraw is bigger than overdraft limit"
            )


sa = SavingsAccount()
sa.deposit()
sa.withdraw()
sa.acc_info()

ca = CurrentAccount()
ca.deposit()
ca.withdraw()
ca.acc_info()
