#print pascal triangle
def printpascal(N):
    for i in range (0,N):
        for j in range (0,i+1):
            print bincof(i,j),
        print 
def bincof(n,k):
    res=1
    if(k>n-k):
        k=n-k
    for i in range (0,k):
        res*=(n-i)
        res/=(i+1)
    return res
N=int(raw_input())
printpascal(N)
