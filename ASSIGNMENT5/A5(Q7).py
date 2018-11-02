class bank:
    def __init__(self):
        print "Enter 1 to work in account 1"
        print "Enter 2 to work in account 2"
        print "Enter 3 to work in account 3"
        print "Enter -1 to exit"
        self.s1=0
        self.s2=0
        self.s3=0
    def account1(self):
        print "Enter 1 to add in account 1"
        print "Enter 2 to withdraw in account 1"
        print "Enter 3 to check in account 1"
        self.va=int(input("Enter the number"))
        if self.va==1:
            self.amount1=int(input("Enter the amount"))
            self.s1=self.s1+self.amount1
        if self.va==2:
            self.withdraw1 = int(input("Enter the amount"))
            self.s1 = self.s1 - self.withdraw1
        if self.va==3:
            print "The amount in account 1 is ",self.s1

    def account2(self):
        print "Enter 1 to add in account 2"
        print "Enter 2 to withdraw in account 2"
        print "Enter 3 to check in account 2"
        self.va = int(input("Enter the number"))
        if self.va == 1:
            self.amount1 = int(input("Enter the amount"))
            self.s2 = self.s2 + self.amount1
        if self.va == 2:
            self.withdraw1 = int(input("Enter the amount"))
            self.s2 = self.s2 - self.withdraw1
        if self.va == 3:
            print "The amount in account 2 is ", self.s2

    def account3(self):
        print "Enter 1 to add in account 3"
        print "Enter 2 to withdraw in account 3"
        print "Enter 3 to check in account 3"
        self.va = int(input("Enter the number"))
        if self.va == 1:
            self.amount1 = int(input("Enter the amount"))
            self.s3 = self.s3 + self.amount1
        if self.va == 2:
            self.withdraw1 = int(input("Enter the amount"))
            self.s3 = self.s3 - self.withdraw1
        if self.va == 3:
            print "The amount in account 3 is ", self.s3
if __name__=="__main__":
    ab=bank()
    k=int(input("Enter the number to work"))
    while k!=-1:
        if k==1:
            ab.account1()
        elif k==2:
            ab.account2()
        elif k==3:
            ab.account3()
        k=int(input("Enter the number to work"))