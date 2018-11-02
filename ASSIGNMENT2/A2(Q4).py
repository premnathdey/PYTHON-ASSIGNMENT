#find the fibonnaci sequence of N
def fibonaciseries(N):
    if(N<=1):
        return N
    else:
        return (fibonaciseries(N-1)+fibonaciseries(N-2))
N=int(raw_input())
if(N<0):
    print("Negative Numbers")
else:
    for i in range(N):
        print(fibonaciseries(i))
        
