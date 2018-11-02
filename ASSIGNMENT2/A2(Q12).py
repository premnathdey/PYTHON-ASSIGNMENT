#to find the sum of N natural numbers
def sumofnaturalnumbers(N):
    if(N!=0):
        return N+sumofnaturalnumbers(N-1)
    else:
        return N
N=int(raw_input())
print(sumofnaturalnumbers(N))
