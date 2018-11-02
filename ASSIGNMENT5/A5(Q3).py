class abc:
    def __init__(self):
        self.a=int(input("Enter the number"))
        self.b=int(input("Enter its power"))
    def pow(self):
       self.c=self.a**self.b
       return self.c
if __name__=="__main__":
    ab=abc()
    k=ab.pow()
    print "Its power is"+str(k)