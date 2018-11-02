#factorial of a given number using recurssion
def factorial(N):
    if(N==0):
        return 1
    else:
        return N*factorial(N-1)
N=int(raw_input())
if(N<0):
    print("NEGATIVE INPUT INVALID")
else:
    print(factorial(N))
