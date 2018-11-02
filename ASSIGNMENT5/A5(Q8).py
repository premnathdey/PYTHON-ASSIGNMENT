import math
a=int(input("Enter the number to check "))
d=int(math.sqrt(a))
j=0
for i in range(2,d+1,1):
    if a%i==0:
        j=1
        break
s=0
d=a
while d!=0:
    p=d%10
    s=s+p
    d=d/10
if j==1 or a<2:
    print "Number is not a prime number and its sum is "+str(s)
else:
        print "Number is a prime number and its sum is " + str(s)