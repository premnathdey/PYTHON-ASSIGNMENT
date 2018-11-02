N,M=map(int,raw_input().split())
arr=[]
for i in range (N):
    arr.append([])
    for j in range (M):
        s=int(input())
        arr[i].append(s)
print arr
brr=[]
J, K=map(int,raw_input().split())
for i in range (J):
    brr.append([])
    for j in range (K):
        p=int(input())
        brr[i].append(p)
print brr
if(M==J):
    result = [[sum(a * b for a, b in zip(arr_row, brr_col)) for brr_col in zip(*brr)] for arr_row in arr]
    for r in result:
        print(r)
else:
    print "Multiplication not possible"
