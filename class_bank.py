class Bank:
 
    def withdraw():
        amt=int(input('Enter a amt'))
        money=20000
        bal1=money-amt
        print("balance after withdraw =",bal1)
    withdraw()
    def deposit():
        amt= int(input('money deposited'))
        money=20000
        bal=money+amt

        print("bal after deposit",bal)
    deposit()
    
