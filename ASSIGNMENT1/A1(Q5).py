#write a fibonacci series of a given number using recurrsion
def fibser(n):
    if(n<=1):
        return n
    else:
        return (fibser(n-1)+fibser(n-2))
N=int(raw_input())
if(N<0):
    print("NEGATIVE NUMBER INVALID")
else:
    for i in range(N):
        print(fibser(i))
        
    
