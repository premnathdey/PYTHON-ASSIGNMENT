#program for factorial of a number
def factorial(N):
    if(N==0):
        return 1
    else:
        return N*factorial(N-1)
N=int(raw_input())
print(factorial(N))
