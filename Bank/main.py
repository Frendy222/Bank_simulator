from bank import *

print("Bank simulation")

customer_list = []
num = 0
while True:
    first = input('\nThe Customer First Name :').title()
    last = input('The Customer Last Name :').title()
    money = int(input('The initial Balance :'))

    custom = Customer(first,last,money)
    customer_list.append(custom)

    conti = input('Continue adding customer (y/n)?').lower()
    if conti == 'y':
        continue
    else : break


for i in customer_list:
    num = num + 1

bankName = input('The bank Name:').capitalize()

bank = Bank(customer_list,num,bankName)

while True:
    x = 0
    for cus in customer_list:
        print(x,'.',bankName,' Bank Account :',cus.getName())
        x = x + 1

    cus_used = int(input('Which customer id you used(input in number)?'))

    used = customer_list[cus_used]

    while True:
        print('\n1. Check Balance')
        print('2. Deposit')
        print('3. Withdraw')
        todo = int(input("What to do ?"))

        if todo == 1:
            print(used.getAccount())
        elif todo == 2:
            amt = int(input('How much do you want to deposit?'))
            print(used.deposit(amt))
        elif todo == 3:
            amt = int(input('How much do you want to Withdraw?'))
            print(used.withdraw(amt))
        else :
            print('error')
        conti = input('Continue(y/n)?').lower()
        if conti == 'y':
            continue
        else:
            break
    conti = input('Want To Change Account ?').lower()
    if conti == 'y':
        continue
    else:
        break
