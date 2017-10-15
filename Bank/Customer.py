from Account_class import Account

class Customer(Account):
    def __init__(self,firstName,lastName,balance):
        super().__init__(balance)
        self.__firstName = str(firstName)
        self.__lastName = str(lastName)
    def getfirstName(self):
        return self.__firstName
    def getlastName(self):
        return self.__lastName
    def getAccount(self):
        return self.getBalance()
    def getName(self):
        name = self.__firstName +' '+ self.__lastName
        return name
