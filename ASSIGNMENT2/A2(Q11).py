#program for sum of a number
def sum(N):
    if(N==0):
        return 0
    else:
        return N+sum(N-1)
N=int(raw_input())
print(sum(N))
