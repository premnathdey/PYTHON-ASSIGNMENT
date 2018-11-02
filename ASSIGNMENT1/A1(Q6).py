#find gcd of two numbers
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(raw_input())
b=int(raw_input())
print(gcd(a,b))
