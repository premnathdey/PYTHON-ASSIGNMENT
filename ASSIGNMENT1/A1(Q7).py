#A number palindrome or not
def palindrome(N):
    sum=0
    J=N
    while(N>0):
        r=N%10
        sum=sum*10+r
        N=N//10
    if(sum==J):
        print("YES")
    else:
        print("NO")
N=int(raw_input())
palindrome(N)
