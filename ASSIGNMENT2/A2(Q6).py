#to find the lcm of two numbers
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,b%a)
a=int(raw_input())
b=int(raw_input())
if(b>a):
        lcm=(a*b)//gcd(b,a)
else:
     lcm=(a*b)//gcd(a,b)
print(lcm)
