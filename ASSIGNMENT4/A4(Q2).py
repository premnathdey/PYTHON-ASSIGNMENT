N=int(input())
g=1
for i in range (N):
    for  k in range (i+1):
        if(k==0 or i==0):
            g=1
        else:
            g=g*(i-k+1)//k
        print g,
    print
