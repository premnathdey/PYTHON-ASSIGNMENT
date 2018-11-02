class x:
    def __init__(self):
        print "hello"
    def hlw(self):
        print"i m in class x"
    def show(self):
        self.hlw()
    def sum(self,a,b):
        c=a+b
        return c
if __name__=="__main__":
 a=x()
 a.hlw()
 a.show()
 print "enter number"
 k=input()
 l=input()
 r=a.sum(k,l)
 print r