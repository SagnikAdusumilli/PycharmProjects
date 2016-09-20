class Account:
    def __init__(self, accntNum, balance):
        self.accntNum = accntNum
        self.balance = balance

    def __str__(self):
        return "Account number: " + str(self.accntNum) + "\n" \
               + "Balance: " + str(self.balance)

    def deposit(self, amount):
        """

        :param amount:
        :type amount:
        """
        self.balance += amount


class Checking(Account):
    def __init__(self, accntNum, balance, fees):
        Account.__init__(self, accntNum, balance)
        self.fees = fees

    def __str__(self):
        return "Account type: Checking\n" \
               + Account.__str__(self)

    def getFee(self):
        return self.fees

    def withdraw(self, amnt):
        if amnt > self.balance:
            print("insufficent funds")
        else:
            self.balance -= (amnt + self.fees)


class Savings(Account):
    def __init__(self, accntNum, balance):
        Account.__init__(self, accntNum, balance)

    def __str__(self):
        return "Account type: Savings\n" + Account.__str__(self)

    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient funds")
        else:
            self.balance -= amount


ca = Checking("123", 500, .50)
print(ca)
ca.withdraw(100)
print(ca)
ca.deposit(10 ** 5)
print(ca)

sa = Savings("456", 1000)
print(sa)
sa.withdraw(100)
print(sa)
sa.deposit(10 ** 10)
print(sa)

accounts = [ca, sa]
print("Displaying all accounts: ")
# for i in range(0, len(accounts)):
#	print(accounts[i])
for i in accounts:
    print(i)
