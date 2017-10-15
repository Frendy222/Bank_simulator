from Customer import *

class Bank(object):
    def __init__(self,customers,numerOfCustomer,bankName):
        self.__customers = customers
        self.__numberOfCustomer = int(numerOfCustomer)
        self.__bankName = str(bankName)
    def addCustomer(self,firstName,lastName,balance):
        custo = Customer(firstName,lastName,balance)
        return custo

    def getNumOfCustomer(self):
        return self.__numberOfCustomer
    def getCustomer(self):
        return self.__customers
