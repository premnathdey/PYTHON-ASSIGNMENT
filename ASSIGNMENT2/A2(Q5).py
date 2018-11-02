#find the f(n)=3*n
sum=0
def func(N):
            global sum
            if(N>0):
                    if(N==0):
                              sum+=0
                    else:
                              sum=3+func(N-1)
            else:
                    if(N==0):
                              sum+=0
                    else:
                              sum=-3+func(N+1)   
            return sum
N=int(raw_input())
print(func(N))
    
