class Bank:
    def __init__(self,accno,name,typ,bal):
        self.acc=accno
        self.name=name
        self.typ=typ
        self.bal=bal
        
    def deposit(self,amt1):
        self.bal+=amt1
        print("balance:",self.bal)
        
    def withdraw(self,amt2):
        if self.bal<amt2:
            print("insufficient balance")
        else:
            self.bal-=amt2
            print("balance:",self.bal)
            
    def display(self):
        print('\naccno',self.acc,'\naccount holder name:',self.name,'\nacc type:',self.typ,'\nbalance:',self.bal)
        print("--MENU--")
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Display")
        print("4.Exit")
        
b1=Bank(1002,"rami","savings",0)
b1.display()
while True:
    choice=int(input("\enter your choice(1-4):"))
    if choice==1:
        d=int(input("enter amount to be deposited:"))
        b1.deposit(d)
    elif choice==2:
        w=int(input("enter amount to withdraw:"))
        b1.withdraw(w)
    elif choice==3:
        b1.display()
    elif choice>3:
        print("enter a valid choice")
    else:
        break
        
