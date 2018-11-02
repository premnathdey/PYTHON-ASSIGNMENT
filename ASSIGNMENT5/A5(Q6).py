global s
s=0
class bank:
    def __init__(self):
        pass

    def deposit(self,x,s):
        s=s+x
        return s
    def withdraw(self,x,s):
        s=s-x
        return s
    def check(self,s):
        return s
if __name__=="__main__":
    a=bank()
    print "Enter 1 to exit"
    print "Enter 5 to deposit"
    print "Enter 6 to withdraw money"
    print "Enter 7 to check amount"
    b=int(input("Enter the number: "))
    while 1:
     if b==1:
         break
     elif b==5:
         k=int(input("Enter amount to enter"))
         s=a.deposit(k,s)
     elif b==6:
         k=int(input("Enter amount to withdraw"))
         s=a.withdraw(k,s)
     elif b==7:
         k=a.check(s)
         print "Your net amount is ",k
     b=int(input("Enter the number"))




