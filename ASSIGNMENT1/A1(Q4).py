#to find the corresponding fibonnaci number of a given number
def fib(N):
    fib=[0]*(N+1)
    fib[0]=0
    fib[1]=1
    for i in range(2, N + 1):
         fib[i] = fib[i - 1] + fib[i - 2]
    return fib[N]
N=int(raw_input())
print(fib(N))
