class Account(object):
    def __init__(self,balance):
        self.__balance = float(balance)
    def getBalance(self):
        return self.__balance
    def deposit(self,amt):
        self.__balance = self.__balance + amt
        return self.__balance
    def withdraw(self,amt):
        if amt < self.__balance:
            self.__balance = self.__balance-amt
            return self.__balance
        else :
            print('The amount exceed the balance.')
    def setAccount(self,acc):
        self.__balance = acc
