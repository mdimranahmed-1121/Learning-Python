class Account:
    def __init__(self,balance,acc_no):
        self.balance=balance
        self.acc_no=acc_no
    
    def debit(self,amount):
        self.balance-=amount
        print("Tk",amount,"debited,from account no:",self.acc_no)
        print("Total balance:",self.get_balance())


    def credit(self,amount):
        self.balance+=amount
        print("Tk",amount,"Credited in account no:",self.acc_no)
        print("Total balance:",self.get_balance())
    
    def get_balance(self):
        return self.balance
    
acc1=Account(10000,1243)
acc1.debit(1000)
acc1.credit(500)


        