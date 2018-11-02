#to find the number of digits in the number
count=0
def countdigits(N):
    global count
    if(N>0):
        count=count+1
        countdigits(N//10)
    return count
N=int(raw_input())
print(countdigits(N))
        
    
